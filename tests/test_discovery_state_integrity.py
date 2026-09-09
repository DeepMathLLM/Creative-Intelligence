"""Regression coverage for branch-discovery lifecycle integrity.

These tests pin fail-closed contracts for resumable discovery state, verified
artifact integrity, and duplicate-safe exact-name selection without requiring a
real Moonshine runtime or model provider.
"""

from __future__ import annotations

import tempfile
import types
import unittest
from pathlib import Path

from tests.test_run_archive_offline import _load_runner_module, _stub_write_json


PASS_REVIEW = {
    "mathematical": {"verdict": "pass", "issues": [], "rationale": "fixture"},
    "historical": {"verdict": "pass", "issues": [], "rationale": "fixture"},
    "format": {"verdict": "pass", "issues": [], "rationale": "fixture"},
    "repair_targets": [],
    "summary": "fixture passed",
}


class _VerificationProvider:
    def __init__(self):
        self.calls = 0

    def generate_structured(self, **_kwargs):
        self.calls += 1
        return PASS_REVIEW


class _Registry:
    def __init__(self):
        self.definition = None

    def register(self, definition):
        self.definition = definition


class DiscoveryStateIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner, cls._module_patcher = _load_runner_module()

    @classmethod
    def tearDownClass(cls):
        cls._module_patcher.stop()

    def setUp(self):
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self._temporary_directory.cleanup)
        self.temp_root = Path(self._temporary_directory.name)
        self.task_dir = self.temp_root / "Creative-Intelligence"
        self.task_dir.mkdir()
        self._original_task_dir = self.runner.TASK_DIR
        self.runner.TASK_DIR = self.task_dir
        self.addCleanup(setattr, self.runner, "TASK_DIR", self._original_task_dir)

    def _job(self, target_archives=2):
        return self.runner.build_discovery_job(
            ["Category Theory"],
            target_archives=target_archives,
            run_name="discovery-integrity",
        )

    def _row(self, job, index, name, status="verified"):
        return {
            "index": index,
            "name": name,
            "branch": "Category Theory",
            "source_urls": [],
            "status": status,
            "project_slug": self.runner._discovery_project_slug(job, index),
            "session_id": "session-%s" % index,
            "archive": str(
                self.task_dir
                / "archives"
                / job.key
                / ("%03d-%s.md" % (index, self.runner._safe_filename(name, "object")))
            ),
            "archive_sha256": self.runner._sha256_text("fixture-%s" % index),
            "verification_submissions": 1,
            "failure_stage": "",
            "last_verification": {},
            "last_error": "",
        }

    def _persist_state(self, job, rows):
        state = self.runner.load_or_create_state(job)
        state["objects"] = rows
        _stub_write_json(job.state_path, state)
        return state

    def _register_verifier(self, *, discovery=True):
        registry = _Registry()
        app = types.SimpleNamespace(tool_registry=registry)
        shell_state = self.runner.ShellState(
            mode="chat",
            project_slug="discovery-project",
            session_id="discovery-session",
            agent_slug=self.runner.AGENT_SLUG,
        )
        object_job = self.runner.ObjectJob(
            index=1,
            name="" if discovery else "Yoneda lemma",
            materials=(),
            project_slug=shell_state.project_slug,
            archive_path=self.task_dir / "pending.md",
            branch="" if discovery else "Category Theory",
        )
        self.runner.register_verification_tool(
            app,
            object_job=object_job,
            shell_state=shell_state,
            format_specification="No fenced placeholders.",
            material_context="(none)",
            discovery_branches=["Category Theory"] if discovery else (),
        )
        self.assertIsNotNone(registry.definition)
        return registry.definition.handler, shell_state

    def _write_attempt_history(self, name, status):
        path = self.task_dir / "runs" / ("history-%s.state.json" % status)
        _stub_write_json(
            path,
            {
                "schema_version": self.runner.STATE_SCHEMA_VERSION,
                "objects": [{"name": name, "status": status}],
            },
        )

    def test_discovery_state_rejects_unknown_row_status(self):
        job = self._job(target_archives=1)
        self._persist_state(job, [self._row(job, 1, "Yoneda lemma", status="corrupted")])

        with self.assertRaisesRegex(self.runner.RunnerError, "unknown.*status|invalid.*status"):
            self.runner.load_or_create_state(job)

    def test_discovery_state_rejects_case_insensitive_duplicate_object_names(self):
        job = self._job(target_archives=2)
        self._persist_state(
            job,
            [
                self._row(job, 1, "Yoneda lemma", status="failed"),
                self._row(job, 2, "yoneda LEMMA", status="verified"),
            ],
        )

        with self.assertRaisesRegex(self.runner.RunnerError, "duplicate.*object|duplicate.*name"):
            self.runner.load_or_create_state(job)

    def test_discovery_state_rejects_missing_verified_archive(self):
        job = self._job(target_archives=1)
        self._persist_state(job, [self._row(job, 1, "Yoneda lemma", status="verified")])

        with self.assertRaisesRegex(self.runner.RunnerError, "verified.*archive|archive.*missing|intact"):
            self.runner.load_or_create_state(job)

    def test_discovery_state_rejects_tampered_verified_archive(self):
        job = self._job(target_archives=1)
        row = self._row(job, 1, "Yoneda lemma", status="verified")
        archive = Path(row["archive"])
        archive.parent.mkdir(parents=True, exist_ok=True)
        archive.write_text("tampered\n", encoding="utf-8")
        self._persist_state(job, [row])

        with self.assertRaisesRegex(self.runner.RunnerError, "verified.*changed|hash|integrity"):
            self.runner.load_or_create_state(job)

    def test_discovery_state_accepts_intact_verified_archive(self):
        job = self._job(target_archives=1)
        row = self._row(job, 1, "Yoneda lemma", status="verified")
        archive = Path(row["archive"])
        archive.parent.mkdir(parents=True, exist_ok=True)
        archive.write_text("fixture-1\n", encoding="utf-8")
        self._persist_state(job, [row])

        loaded = self.runner.load_or_create_state(job)
        self.assertEqual(loaded["objects"][0]["status"], "verified")

    def test_discovery_verifier_rejects_previously_attempted_exact_name(self):
        for prior_status in ("verified", "failed"):
            with self.subTest(prior_status=prior_status):
                self._write_attempt_history("Yoneda lemma", prior_status)
                handler, shell_state = self._register_verifier(discovery=True)
                provider = _VerificationProvider()
                runtime = {
                    "project_slug": shell_state.project_slug,
                    "session_id": shell_state.session_id,
                    "verification_provider": provider,
                }
                with self.assertRaisesRegex(
                    self.runner.RunnerError,
                    "already attempted|duplicate|previously attempted",
                ):
                    handler(
                        runtime,
                        archive="# Archive | yoneda LEMMA\n\nfixture",
                        object_name="yoneda LEMMA",
                        branch="Category Theory",
                    )
                self.assertEqual(provider.calls, 0)

    def test_discovery_verifier_allows_unattempted_name(self):
        self._write_attempt_history("Yoneda lemma", "verified")
        handler, shell_state = self._register_verifier(discovery=True)
        provider = _VerificationProvider()
        runtime = {
            "project_slug": shell_state.project_slug,
            "session_id": shell_state.session_id,
            "verification_provider": provider,
        }

        result = handler(
            runtime,
            archive="# Archive | Kan extension\n\nfixture",
            object_name="Kan extension",
            branch="Category Theory",
        )

        self.assertTrue(result["passed"])
        self.assertEqual(provider.calls, 1)

    def test_non_discovery_verifier_keeps_existing_failed_repair_path_available(self):
        self._write_attempt_history("Yoneda lemma", "failed")
        handler, shell_state = self._register_verifier(discovery=False)
        provider = _VerificationProvider()
        runtime = {
            "project_slug": shell_state.project_slug,
            "session_id": shell_state.session_id,
            "verification_provider": provider,
        }

        result = handler(runtime, archive="# Archive | Yoneda lemma\n\nfixture")

        self.assertTrue(result["passed"])
        self.assertEqual(provider.calls, 1)


if __name__ == "__main__":
    unittest.main()
