import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


MODULE_PATH = Path(__file__).resolve().parents[1] / "agent.py"
SPEC = importlib.util.spec_from_file_location("math_concept_agent_checkpoint", str(MODULE_PATH))
AGENT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AGENT)


class CrashSafeCheckpointTests(unittest.TestCase):
    def _seed_run(
        self,
        root,
        *,
        status="paused",
        turn=3,
        session_id="session-old",
        summary="Accepted research checkpoint",
        next_step="Prove the next lemma",
    ):
        run_dir = root / "runs" / "sample"
        run_dir.mkdir(parents=True)
        (run_dir / "problem.md").write_text("Research problem\n", encoding="utf-8")
        AGENT.atomic_write_json(
            run_dir / "state.json",
            {
                "run_id": "sample",
                "status": status,
                "turn": turn,
                "session_id": session_id,
                "runner_pid": None,
                "codex_pid": None,
                "source_problem": "<inline prompt>",
                "summary": summary,
                "next_step": next_step,
                "skills_used": ["construct-mathematical-concept"],
                "created_at": AGENT.utc_now(),
                "updated_at": AGENT.utc_now(),
            },
        )
        return run_dir

    @staticmethod
    def _run_args(*, once=False):
        return SimpleNamespace(
            run_id="sample",
            problem=None,
            prompt=None,
            keep_stop=False,
            once=once,
        )

    def test_failed_attempt_does_not_advance_or_overwrite_committed_checkpoint(self):
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(
            AGENT, "ROOT", Path(directory)
        ), mock.patch.object(
            AGENT, "build_codex_command", return_value=["codex"]
        ), mock.patch.object(
            AGENT,
            "execute_turn",
            return_value=(17, None, "session-old", None),
        ):
            self._seed_run(Path(directory))
            result = AGENT.command_run(self._run_args())

            self.assertEqual(result, 17)
            state = AGENT.read_json(AGENT.state_path_for("sample"), {})
            self.assertEqual(state["status"], "error")
            self.assertEqual(state["turn"], 3)
            self.assertEqual(state["summary"], "Accepted research checkpoint")
            self.assertEqual(state["next_step"], "Prove the next lemma")
            self.assertEqual(state["checkpoint"]["turn"], 3)
            self.assertEqual(state["checkpoint"]["summary"], "Accepted research checkpoint")
            self.assertEqual(state["attempt"]["turn"], 4)
            self.assertEqual(state["attempt"]["status"], "failed")
            self.assertIn("17", state["attempt"]["error"])

    def test_restart_retries_uncommitted_turn_and_reuses_observed_session(self):
        calls = []

        def build_command(session_id, prompt, config=None):
            calls.append(session_id)
            return ["codex"]

        def crash_turn(command, stop_path, on_session_id=None, on_started=None):
            if on_started:
                on_started(4321)
            if on_session_id:
                on_session_id("session-new")
            raise OSError("simulated controller crash window")

        completed = json.dumps(
            {
                "status": "complete",
                "summary": "Committed after restart",
                "skills_used": ["verify-mathematical-concept"],
                "next_step": "",
            }
        )

        with tempfile.TemporaryDirectory() as directory, mock.patch.object(
            AGENT, "ROOT", Path(directory)
        ), mock.patch.object(
            AGENT, "build_codex_command", side_effect=build_command
        ), mock.patch.object(
            AGENT, "execute_turn", side_effect=crash_turn
        ):
            self._seed_run(Path(directory), session_id=None)
            self.assertEqual(AGENT.command_run(self._run_args()), 1)

            # Re-open the same durable state as a fresh controller process would.
            state_after_crash = AGENT.read_json(AGENT.state_path_for("sample"), {})
            self.assertEqual(state_after_crash["turn"], 3)
            self.assertEqual(state_after_crash["session_id"], "session-new")
            self.assertEqual(state_after_crash["checkpoint"]["turn"], 3)

            with mock.patch.object(
                AGENT,
                "execute_turn",
                return_value=(0, None, "session-new", completed),
            ):
                self.assertEqual(AGENT.command_run(self._run_args()), 0)

            final_state = AGENT.read_json(AGENT.state_path_for("sample"), {})
            self.assertEqual(calls, [None, "session-new"])
            self.assertEqual(final_state["turn"], 4)
            self.assertEqual(final_state["checkpoint"]["turn"], 4)
            self.assertEqual(final_state["checkpoint"]["status"], "complete")
            self.assertEqual(final_state["summary"], "Committed after restart")
            self.assertIsNone(final_state["attempt"])

    def test_stale_reconciliation_preserves_checkpoint_and_marks_attempt_interrupted(self):
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(
            AGENT, "ROOT", Path(directory)
        ):
            root = Path(directory)
            self._seed_run(root, status="running")
            state = AGENT.read_json(AGENT.state_path_for("sample"), {})
            state["runner_pid"] = 999999
            state["codex_pid"] = 888888
            state["attempt"] = {
                "turn": 4,
                "status": "running",
                "runner_pid": 999999,
                "codex_pid": 888888,
                "started_at": AGENT.utc_now(),
            }
            AGENT.atomic_write_json(AGENT.state_path_for("sample"), state)

            repaired = AGENT.reconcile_state("sample", state, 999999, False)

            self.assertEqual(repaired["status"], "error")
            self.assertEqual(repaired["turn"], 3)
            self.assertEqual(repaired["summary"], "Accepted research checkpoint")
            self.assertEqual(repaired["checkpoint"]["turn"], 3)
            self.assertEqual(repaired["checkpoint"]["summary"], "Accepted research checkpoint")
            self.assertEqual(repaired["attempt"]["turn"], 4)
            self.assertEqual(repaired["attempt"]["status"], "interrupted")
            self.assertIn("no longer running", repaired["attempt"]["error"])

    def test_successful_result_is_the_only_operation_that_advances_checkpoint(self):
        completed = json.dumps(
            {
                "status": "continue",
                "summary": "New accepted result",
                "skills_used": ["construct-mathematical-concept"],
                "next_step": "Verify the candidate",
            }
        )
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(
            AGENT, "ROOT", Path(directory)
        ), mock.patch.object(
            AGENT, "build_codex_command", return_value=["codex"]
        ), mock.patch.object(
            AGENT,
            "execute_turn",
            return_value=(0, None, "session-old", completed),
        ):
            self._seed_run(Path(directory))
            self.assertEqual(AGENT.command_run(self._run_args(once=True)), 0)

            state = AGENT.read_json(AGENT.state_path_for("sample"), {})
            self.assertEqual(state["status"], "paused")
            self.assertEqual(state["turn"], 4)
            self.assertEqual(state["summary"], "New accepted result")
            self.assertEqual(state["checkpoint"]["turn"], 4)
            self.assertEqual(state["checkpoint"]["status"], "continue")
            self.assertEqual(state["checkpoint"]["summary"], "New accepted result")
            self.assertEqual(state["checkpoint"]["next_step"], "Verify the candidate")
            self.assertIsNone(state["attempt"])


if __name__ == "__main__":
    unittest.main()
