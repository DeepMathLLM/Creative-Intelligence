"""Deterministic integration tests against the real Moonshine runtime.

These tests intentionally fake only provider responses. Session persistence,
tool registration/dispatch, tool-event storage, material staging, resume, and
archive publication all use the real Moonshine implementation.
"""

from __future__ import annotations

import copy
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

import run_archive
from moonshine.app import MoonshineApp
from moonshine.providers import ProviderResponse, ProviderStreamEvent, ProviderToolCall


ARCHIVE_TEXT = """# Mathematical Object Origin Archive | Integration Test Object

## 1. Archive Information

- Standard Name: Integration Test Object
- Mathematical Field: Test Mathematics
- Abstract: A deterministic fixture used to exercise the archive runtime.

## 2. Core Record

### Precise Description

This object is a deterministic integration-test fixture.

### Background

The fixture exists only to test the research-agent runtime boundary [1].

### Essential Role

It verifies session, tool, persistence, recovery, and publication behavior.

## 3. Notes

No mathematical claim beyond the fixture contract is intended.

## 4. Sources

[1] Creative-Intelligence deterministic integration fixture.
"""

HISTORICAL_EVIDENCE = "[1] The archive is an explicit deterministic test fixture; no external historical claim is asserted."

PASS_REVIEW = {
    "mathematical": {
        "verdict": "pass",
        "issues": [],
        "rationale": "The fixture is internally consistent.",
    },
    "historical": {
        "verdict": "pass",
        "issues": [],
        "rationale": "The fixture makes no unsupported external historical claim.",
    },
    "format": {
        "verdict": "pass",
        "issues": [],
        "rationale": "The archive follows the supplied fixture format.",
    },
    "repair_targets": [],
    "summary": "All deterministic fixture checks passed.",
}


class ScriptedArchiveProvider(object):
    """Issue the verifier tool call once, then return a normal final answer."""

    def __init__(self, archive=ARCHIVE_TEXT, evidence=HISTORICAL_EVIDENCE):
        self.archive = archive
        self.evidence = evidence
        self.calls = []
        self.tool_call_issued = False

    def stream_generate(self, *, system_prompt, messages, tool_schemas=None):
        self.calls.append(
            {
                "system_prompt": system_prompt,
                "messages": copy.deepcopy(list(messages)),
                "tool_schema_names": [item.get("name") for item in list(tool_schemas or [])],
            }
        )
        if not self.tool_call_issued:
            self.tool_call_issued = True
            response = ProviderResponse(
                content="",
                tool_calls=[
                    ProviderToolCall(
                        name=run_archive.VERIFICATION_TOOL,
                        arguments={
                            "archive": self.archive,
                            "historical_evidence": self.evidence,
                        },
                        call_id="verify-archive-1",
                    )
                ],
            )
            yield ProviderStreamEvent(type="response", response=response)
            return

        response = ProviderResponse(content="The archive verification was submitted.")
        yield ProviderStreamEvent(type="text_delta", text=response.content)
        yield ProviderStreamEvent(type="response", response=response)


class PassingVerificationProvider(object):
    """Return a fixed fail-closed review payload accepted by the runner."""

    def __init__(self):
        self.calls = []

    def generate_structured(self, *, system_prompt, messages, response_schema, schema_name):
        self.calls.append(
            {
                "system_prompt": system_prompt,
                "messages": copy.deepcopy(list(messages)),
                "response_schema": copy.deepcopy(dict(response_schema)),
                "schema_name": schema_name,
            }
        )
        return copy.deepcopy(PASS_REVIEW)


class MoonshineRunnerIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        self.format_specification = run_archive.FORMAT_FILE.read_text(encoding="utf-8").strip()

    def _job(self):
        input_path = self.root / "queue.json"
        material_path = self.root / "material.md"
        material_path.write_text("Deterministic local material for the integration fixture.\n", encoding="utf-8")
        input_path.write_text(
            json.dumps(
                {
                    "format": run_archive.FORMAT_ID,
                    "objects": [
                        {
                            "name": "Integration Test Object",
                            "materials": [str(material_path)],
                        }
                    ],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        object_job = run_archive.ObjectJob(
            index=1,
            name="Integration Test Object",
            materials=(material_path.resolve(),),
            project_slug=run_archive._project_slug("Integration Test Object"),
            archive_path=self.root / "archives" / "001-Integration Test Object.md",
        )
        job = run_archive.JobFile(
            path=input_path.resolve(),
            sha256=run_archive._sha256_file(input_path),
            key="queue",
            format_id=run_archive.FORMAT_ID,
            language="en",
            objects=(object_job,),
            state_path=self.root / "runs" / "queue.state.json",
        )
        state = run_archive._new_state(job)
        run_archive.save_state(job, state)
        return job, state, object_job, state["objects"][0]

    def _configured_app(self, home, main_provider=None):
        home = Path(home)
        run_archive.sync_skills(home)
        app = MoonshineApp(home=str(home))
        main_provider = main_provider or ScriptedArchiveProvider()
        verification_provider = PassingVerificationProvider()
        app.provider = main_provider
        app.verification_provider = verification_provider
        app.agent.provider = main_provider
        app.agent.verification_provider = verification_provider
        app.context_manager.provider = main_provider
        app.memory.set_provider(main_provider)
        app.research_project_resolver.provider = main_provider
        run_archive.configure_task_exposure(app)
        return app, main_provider, verification_provider

    def _process(self, app, job, state, object_job, item_state):
        with redirect_stdout(io.StringIO()):
            run_archive.process_object(
                app,
                job=job,
                state=state,
                object_job=object_job,
                item_state=item_state,
                format_specification=self.format_specification,
                max_turns=1,
                verbose=False,
            )

    def test_verified_run_persists_tool_event_stages_material_and_publishes(self):
        job, state, object_job, item_state = self._job()
        app, main_provider, verification_provider = self._configured_app(self.root / "moonshine-home")

        self._process(app, job, state, object_job, item_state)

        self.assertEqual(item_state["status"], "verified")
        self.assertTrue(object_job.archive_path.exists())
        self.assertEqual(object_job.archive_path.read_text(encoding="utf-8").strip(), ARCHIVE_TEXT.strip())
        self.assertEqual(item_state["archive_sha256"], run_archive._sha256_text(ARCHIVE_TEXT.strip()))
        self.assertTrue(item_state["session_id"])
        self.assertGreaterEqual(len(main_provider.calls), 2)
        self.assertEqual(len(verification_provider.calls), 1)
        self.assertIn(run_archive.VERIFICATION_TOOL, main_provider.calls[0]["tool_schema_names"])
        for slug in run_archive.EXPOSED_SKILLS:
            self.assertIsNotNone(app.skill_manager.get_skill(slug))

        tool_events = run_archive._verification_events(app, item_state["session_id"])
        self.assertEqual(len(tool_events), 1)
        self.assertTrue(tool_events[0]["output"]["passed"])
        self.assertEqual(tool_events[0]["output"]["session_id"], item_state["session_id"])
        self.assertEqual(tool_events[0]["output"]["project_slug"], object_job.project_slug)

        meta = app.session_store.get_session_meta(item_state["session_id"])
        self.assertEqual(meta.get("status"), "closed")
        archive_task = dict(meta.get("archive_task") or {})
        self.assertEqual(archive_task.get("status"), "verified")
        runtime_materials = list(archive_task.get("runtime_materials") or [])
        self.assertEqual(len(runtime_materials), 1)
        self.assertTrue(Path(runtime_materials[0]).exists())
        self.assertTrue(str(Path(runtime_materials[0]).resolve()).startswith(str(app.paths.home.resolve())))

    def test_retry_recovers_persisted_verification_without_another_model_turn(self):
        job, state, object_job, item_state = self._job()
        home = self.root / "moonshine-home"
        first_app, _, _ = self._configured_app(home)

        with mock.patch.object(
            run_archive,
            "_publish_archive",
            side_effect=run_archive.RunnerError("simulated crash after verification persistence"),
        ):
            with self.assertRaisesRegex(run_archive.RunnerError, "simulated crash"):
                self._process(first_app, job, state, object_job, item_state)

        session_id = item_state["session_id"]
        self.assertTrue(session_id)
        self.assertEqual(item_state["status"], "running")
        self.assertFalse(object_job.archive_path.exists())
        persisted_events = run_archive._verification_events(first_app, session_id)
        self.assertEqual(len(persisted_events), 1)
        self.assertTrue(persisted_events[0]["output"]["passed"])

        resumed_provider = ScriptedArchiveProvider()
        resumed_app, resumed_provider, _ = self._configured_app(home, main_provider=resumed_provider)
        self._process(resumed_app, job, state, object_job, item_state)

        self.assertEqual(item_state["session_id"], session_id)
        self.assertEqual(item_state["status"], "verified")
        self.assertTrue(object_job.archive_path.exists())
        self.assertEqual(object_job.archive_path.read_text(encoding="utf-8").strip(), ARCHIVE_TEXT.strip())
        self.assertEqual(resumed_provider.calls, [])
        recovered_events = run_archive._verification_events(resumed_app, session_id)
        self.assertEqual(len(recovered_events), 1)

    def test_resume_rejects_session_owned_by_another_project(self):
        job, state, object_job, item_state = self._job()
        app = MoonshineApp(home=str(self.root / "moonshine-home"))
        wrong_state = app.start_shell_state(
            mode="chat",
            project_slug="different-project",
            agent_slug=run_archive.AGENT_SLUG,
        )
        item_state["session_id"] = wrong_state.session_id
        run_archive.save_state(job, state)

        with self.assertRaisesRegex(run_archive.RunnerError, "belongs to project"):
            self._process(app, job, state, object_job, item_state)

        meta = app.session_store.get_session_meta(wrong_state.session_id)
        self.assertEqual(meta.get("project_slug"), "different-project")
        self.assertFalse(object_job.archive_path.exists())

    def test_resume_rejects_same_project_session_with_wrong_mode(self):
        _, _, object_job, item_state = self._job()
        app = MoonshineApp(home=str(self.root / "moonshine-home"))
        wrong_state = app.start_shell_state(
            mode="research",
            project_slug=object_job.project_slug,
            agent_slug="research-control-loop",
        )
        item_state["session_id"] = wrong_state.session_id

        with self.assertRaisesRegex(run_archive.RunnerError, "mode=research, not chat"):
            run_archive._open_or_create_session(app, object_job, item_state)

        meta = app.session_store.get_session_meta(wrong_state.session_id)
        self.assertEqual(meta.get("mode"), "research")
        self.assertEqual(meta.get("project_slug"), object_job.project_slug)

    def test_resume_rejects_same_project_session_with_wrong_agent(self):
        _, _, object_job, item_state = self._job()
        app = MoonshineApp(home=str(self.root / "moonshine-home"))
        wrong_state = app.start_shell_state(
            mode="chat",
            project_slug=object_job.project_slug,
            agent_slug="research-control-loop",
        )
        item_state["session_id"] = wrong_state.session_id

        with self.assertRaisesRegex(run_archive.RunnerError, "agent=research-control-loop, not %s" % run_archive.AGENT_SLUG):
            run_archive._open_or_create_session(app, object_job, item_state)

        meta = app.session_store.get_session_meta(wrong_state.session_id)
        self.assertEqual(meta.get("mode"), "chat")
        self.assertEqual(meta.get("agent_slug"), "research-control-loop")
        self.assertEqual(meta.get("project_slug"), object_job.project_slug)


if __name__ == "__main__":
    unittest.main()
