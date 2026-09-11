"""Offline regression tests for deterministic ``run_archive.py`` contracts.

The production runner is a Moonshine runtime extension, but most of its safety
contracts are deterministic.  These tests install a deliberately tiny import
surface for Moonshine so the runner can be loaded from a standalone checkout
without an initialized runtime, provider credentials, network access, or model
calls.

The stubs are only an import harness.  They do not simulate Moonshine agent,
storage, verification-provider, or MCP behavior.
"""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import os
import re
import sys
import tempfile
import types
import unicodedata
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime
from pathlib import Path
from unittest import mock


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = REPOSITORY_ROOT / "run_archive.py"
RUNNER_MODULE_NAME = "creative_intelligence_run_archive_offline_test_target"


def _stub_slugify(text: str, prefix: str = "item") -> str:
    """Mirror Moonshine's deterministic slug algorithm for runner tests."""
    normalized = unicodedata.normalize("NFKD", text or "")
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    if slug:
        return slug[:64].strip("-")
    digest = hashlib.sha1((text or prefix).encode("utf-8")).hexdigest()[:10]
    return "%s-%s" % (prefix, digest)


def _stub_atomic_write(path: Path, text: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(str(temporary), str(path))


def _stub_read_json(path: Path, default=None):
    path = Path(path)
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _stub_write_json(path: Path, payload) -> None:
    _stub_atomic_write(Path(path), json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def _stub_trim_text_to_token_budget(text: str, token_budget: int, **_kwargs) -> str:
    source = str(text or "")
    if token_budget <= 0:
        return ""
    return source


def _moonshine_stub_modules():
    modules = {}

    moonshine = types.ModuleType("moonshine")
    moonshine.__path__ = []
    modules["moonshine"] = moonshine

    app = types.ModuleType("moonshine.app")

    class MoonshineApp:
        pass

    class ShellState:
        def __init__(self, mode="chat", project_slug="", session_id="", agent_slug=""):
            self.mode = mode
            self.project_slug = project_slug
            self.session_id = session_id
            self.agent_slug = agent_slug

    app.MoonshineApp = MoonshineApp
    app.ShellState = ShellState
    modules["moonshine.app"] = app

    json_schema = types.ModuleType("moonshine.json_schema")
    json_schema.validate_json_schema = lambda _value, _schema: None
    modules["moonshine.json_schema"] = json_schema

    providers = types.ModuleType("moonshine.providers")

    class OfflineProvider:
        pass

    providers.OfflineProvider = OfflineProvider
    modules["moonshine.providers"] = providers

    skills = types.ModuleType("moonshine.skills")
    skills.__path__ = []
    modules["moonshine.skills"] = skills

    skill_document = types.ModuleType("moonshine.skills.skill_document")
    skill_document.parse_skill_document = lambda raw: ({}, str(raw))
    skill_document.validate_skill_document = lambda *_args, **_kwargs: []
    modules["moonshine.skills.skill_document"] = skill_document

    tools = types.ModuleType("moonshine.tools")
    tools.__path__ = []
    modules["moonshine.tools"] = tools

    registry = types.ModuleType("moonshine.tools.registry")

    class ToolDefinition:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    registry.ToolDefinition = ToolDefinition
    modules["moonshine.tools.registry"] = registry

    utils = types.ModuleType("moonshine.utils")
    utils.atomic_write = _stub_atomic_write
    utils.read_json = _stub_read_json
    utils.slugify = _stub_slugify
    utils.trim_text_to_token_budget = _stub_trim_text_to_token_budget
    utils.utc_now = lambda: datetime(2026, 1, 1).isoformat() + "Z"
    utils.write_json = _stub_write_json
    modules["moonshine.utils"] = utils

    return modules


def _load_runner_module():
    stub_modules = _moonshine_stub_modules()
    patcher = mock.patch.dict(sys.modules, stub_modules, clear=False)
    patcher.start()
    try:
        spec = importlib.util.spec_from_file_location(RUNNER_MODULE_NAME, RUNNER_PATH)
        if spec is None or spec.loader is None:
            raise RuntimeError("could not load run_archive.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[RUNNER_MODULE_NAME] = module
        spec.loader.exec_module(module)
    except Exception:
        patcher.stop()
        sys.modules.pop(RUNNER_MODULE_NAME, None)
        raise
    return module, patcher


class OfflineRunnerRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner, cls._module_patcher = _load_runner_module()

    @classmethod
    def tearDownClass(cls):
        sys.modules.pop(RUNNER_MODULE_NAME, None)
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

    def _write_queue(self, payload, *, filename="queue.json") -> Path:
        queue_path = self.temp_root / "inputs" / filename
        queue_path.parent.mkdir(parents=True, exist_ok=True)
        queue_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return queue_path

    def _minimal_payload(self, *, name="Bochner formula", materials=None):
        return {
            "format": self.runner.FORMAT_ID,
            "language": "en",
            "objects": [
                {
                    "name": name,
                    "materials": list(materials or []),
                }
            ],
        }

    def test_load_job_resolves_relative_materials_and_derives_stable_paths(self):
        material = self.temp_root / "inputs" / "materials" / "notes.md"
        material.parent.mkdir(parents=True)
        material.write_text("source material\n", encoding="utf-8")
        queue_path = self._write_queue(self._minimal_payload(materials=["materials/notes.md"]))

        job = self.runner.load_job(queue_path)

        self.assertEqual(job.path, queue_path.resolve())
        self.assertEqual(job.language, "en")
        self.assertEqual(job.state_path, self.task_dir / "runs" / "queue.state.json")
        self.assertEqual(len(job.objects), 1)
        object_job = job.objects[0]
        self.assertEqual(object_job.materials, (material.resolve(),))
        self.assertEqual(object_job.project_slug, "math-object-archive-bochner-formula")
        self.assertEqual(
            object_job.archive_path,
            self.task_dir / "archives" / "queue" / "001-Bochner formula.md",
        )

    def test_load_job_rejects_case_insensitive_duplicate_names(self):
        payload = self._minimal_payload(name="Bochner formula")
        payload["objects"].append({"name": "bochner FORMULA", "materials": []})
        queue_path = self._write_queue(payload)

        with self.assertRaisesRegex(self.runner.RunnerError, "duplicate object name"):
            self.runner.load_job(queue_path)

    def test_load_job_rejects_duplicate_material_paths(self):
        material = self.temp_root / "inputs" / "source.md"
        material.parent.mkdir(parents=True)
        material.write_text("source\n", encoding="utf-8")
        queue_path = self._write_queue(
            self._minimal_payload(materials=["source.md", "./source.md"])
        )

        with self.assertRaisesRegex(self.runner.RunnerError, "duplicate material path"):
            self.runner.load_job(queue_path)

    def test_load_job_rejects_identifier_collisions_after_normalization(self):
        payload = {
            "format": self.runner.FORMAT_ID,
            "objects": [
                {"name": "A/B", "materials": []},
                {"name": "A B", "materials": []},
            ],
        }
        queue_path = self._write_queue(payload)

        with self.assertRaisesRegex(self.runner.RunnerError, "identifiers collide after normalization"):
            self.runner.load_job(queue_path)

    def test_load_job_rejects_non_utf8_materials(self):
        material = self.temp_root / "inputs" / "binary.dat"
        material.parent.mkdir(parents=True)
        material.write_bytes(b"\xff\xfe\x00")
        queue_path = self._write_queue(self._minimal_payload(materials=["binary.dat"]))

        with self.assertRaisesRegex(self.runner.RunnerError, "material is not UTF-8 text"):
            self.runner.load_job(queue_path)

    def test_concept_references_allow_optional_sources(self):
        reference_path = self.temp_root / "references.json"
        reference_path.write_text(
            json.dumps(
                [
                    {"name": "Yoneda lemma", "source": "https://example.org/yoneda"},
                    {"name": "Optimal transport"},
                ],
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        references = self.runner.load_concept_references(reference_path)

        self.assertEqual(
            references,
            (
                ("Yoneda lemma", "https://example.org/yoneda"),
                ("Optimal transport", ""),
            ),
        )

    def test_candidate_pool_is_part_of_discovery_run_identity(self):
        reference_path = self.temp_root / "references.json"
        reference_path.write_text(
            json.dumps([{"name": "Yoneda lemma"}]),
            encoding="utf-8",
        )
        plain = self.runner.build_discovery_job(
            ["Category Theory"],
            target_archives=1,
            run_name="plain",
        )
        candidate = self.runner.build_discovery_job(
            ["Category Theory"],
            target_archives=1,
            run_name="candidate",
            concept_reference_path=reference_path,
        )

        legacy_identity = json.dumps(
            {"branches": ["Category Theory"], "target_archives": 1},
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        self.assertEqual(plain.sha256, self.runner._sha256_text(legacy_identity))
        self.assertNotEqual(candidate.sha256, plain.sha256)
        self.assertEqual(candidate.concept_references, (("Yoneda lemma", ""),))

    def test_state_rejects_input_mutation_after_run_started(self):
        queue_path = self._write_queue(self._minimal_payload())
        first_job = self.runner.load_job(queue_path)
        state = self.runner.load_or_create_state(first_job)
        self.assertEqual(state["status"], "pending")
        self.assertTrue(first_job.state_path.exists())

        changed_payload = self._minimal_payload()
        changed_payload["language"] = "zh"
        queue_path.write_text(
            json.dumps(changed_payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        changed_job = self.runner.load_job(queue_path)

        with self.assertRaisesRegex(self.runner.RunnerError, "input JSON changed after this run started"):
            self.runner.load_or_create_state(changed_job)

    def test_state_rejects_tampered_project_association(self):
        queue_path = self._write_queue(self._minimal_payload())
        job = self.runner.load_job(queue_path)
        state = self.runner.load_or_create_state(job)
        state["objects"][0]["project_slug"] = "wrong-project"
        _stub_write_json(job.state_path, state)

        with self.assertRaisesRegex(self.runner.RunnerError, "state project association is inconsistent"):
            self.runner.load_or_create_state(job)

    def test_overall_status_aggregation_is_deterministic(self):
        cases = [
            (["verified", "verified"], "completed"),
            (["failed", "failed"], "failed"),
            (["verified", "failed"], "partially_failed"),
            (["pending", "running"], "running"),
            (["pending", "failed"], "pending"),
            ([], "pending"),
        ]
        for statuses, expected in cases:
            with self.subTest(statuses=statuses):
                state = {"objects": [{"status": status} for status in statuses]}
                self.runner._refresh_overall_status(state)
                self.assertEqual(state["status"], expected)
                self.assertIn("updated_at", state)

    def test_format_checker_only_uses_placeholders_from_fenced_templates(self):
        specification = """\
Outside prose may contain {Not A Template Placeholder}.

```markdown
# Archive | {Object Name}

{Content}
```
"""
        markdown = "# Archive | {Object Name}\n\n{Not A Template Placeholder}\n"

        issues = self.runner.deterministic_format_issues(markdown, specification)

        self.assertEqual(
            issues,
            [
                "Unresolved template placeholder from the active format specification: {Object Name}"
            ],
        )
        self.assertEqual(
            self.runner.deterministic_format_issues("   ", specification),
            ["The archive is empty."],
        )

    def test_normalized_check_fails_closed_when_extra_issues_exist(self):
        raw = {"verdict": "pass", "issues": [], "rationale": "looks good"}

        result = self.runner._normalized_check(raw, ["deterministic issue"])

        self.assertFalse(result["passed"])
        self.assertEqual(result["verdict"], "pass")
        self.assertEqual(result["issues"], ["deterministic issue"])

    def test_accepted_output_requires_bound_session_project_and_matching_hash(self):
        archive = "verified archive"
        shell_state = types.SimpleNamespace(session_id="session-1", project_slug="project-1")
        output = {
            "passed": True,
            "session_id": shell_state.session_id,
            "project_slug": shell_state.project_slug,
            "verified_archive": archive,
            "archive_sha256": self.runner._sha256_text(archive),
        }
        event = {"error": "", "output": output}

        accepted = self.runner._accepted_output([event], shell_state)
        self.assertEqual(accepted, output)

        for field, bad_value in [
            ("session_id", "other-session"),
            ("project_slug", "other-project"),
            ("archive_sha256", "0" * 64),
        ]:
            with self.subTest(field=field):
                bad_output = dict(output)
                bad_output[field] = bad_value
                self.assertIsNone(
                    self.runner._accepted_output(
                        [{"error": "", "output": bad_output}], shell_state
                    )
                )

        self.assertIsNone(
            self.runner._accepted_output([{"error": "tool failed", "output": output}], shell_state)
        )

    def test_publish_archive_is_idempotent_but_refuses_different_existing_content(self):
        archive = "accepted archive"
        digest = self.runner._sha256_text(archive)
        verification = {"verified_archive": archive, "archive_sha256": digest}
        output_path = self.temp_root / "archives" / "accepted.md"

        self.assertEqual(self.runner._publish_archive(output_path, verification), digest)
        self.assertEqual(output_path.read_text(encoding="utf-8"), archive + "\n")
        self.assertEqual(self.runner._publish_archive(output_path, verification), digest)

        output_path.write_text("tampered archive\n", encoding="utf-8")
        with self.assertRaisesRegex(self.runner.RunnerError, "refusing to overwrite"):
            self.runner._publish_archive(output_path, verification)

    def test_provider_preflight_is_fail_closed_without_credentials_or_capability(self):
        self.assertIn(
            "offline or unavailable",
            self.runner._provider_problem(self.runner.OfflineProvider(), "main"),
        )

        class MainProvider:
            api_key_env = "CREATIVE_INTELLIGENCE_TEST_KEY"

            def generate(self):
                return None

        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertIn(
                "requires environment variable CREATIVE_INTELLIGENCE_TEST_KEY",
                self.runner._provider_problem(MainProvider(), "main"),
            )

        with mock.patch.dict(
            os.environ,
            {"CREATIVE_INTELLIGENCE_TEST_KEY": "configured"},
            clear=True,
        ):
            self.assertEqual(self.runner._provider_problem(MainProvider(), "main"), "")
            self.assertIn(
                "does not support generate_structured",
                self.runner._provider_problem(MainProvider(), "verification", structured=True),
            )

    def test_validate_only_does_not_create_runtime_state(self):
        queue_path = self._write_queue(self._minimal_payload())
        expected_state = self.task_dir / "runs" / "queue.state.json"
        stdout = io.StringIO()
        stderr = io.StringIO()

        with redirect_stdout(stdout), redirect_stderr(stderr):
            exit_code = self.runner.main([str(queue_path), "--validate-only"])

        self.assertEqual(exit_code, 0)
        self.assertFalse(expected_state.exists())
        self.assertIn("Valid input:", stdout.getvalue())
        self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
