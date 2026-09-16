#!/usr/bin/env python3
"""Thin Codex CLI controller for long-running mathematical research."""

import argparse
import ctypes
import datetime as dt
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.toml"
AGENTS_PATH = ROOT / "AGENTS.md"
SCHEMA_PATH = ROOT / "schemas" / "turn-result.schema.json"
RUN_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
ACTIVE_STATUSES = {"starting", "running", "stopping"}
STARTUP_TIMEOUT_SECONDS = 15
LONG_TOOL_SECONDS = 2.0
TURN_STATUS_LABELS = {
    "continue": "RESEARCH CONTINUES",
    "complete": "RESEARCH COMPLETE",
    "blocked": "RESEARCH BLOCKED",
}


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def validate_run_id(run_id):
    if not RUN_ID_PATTERN.fullmatch(run_id):
        raise ValueError(
            "Run id must start with a letter or digit and contain only letters, digits, '.', '_' or '-'"
        )
    return run_id


def run_dir_for(run_id):
    validate_run_id(run_id)
    return ROOT / "runs" / run_id


def runtime_dir_for(run_id):
    return run_dir_for(run_id) / ".runtime"


def state_path_for(run_id):
    return run_dir_for(run_id) / "state.json"


def stop_path_for(run_id):
    return runtime_dir_for(run_id) / "STOP"


def lock_path_for(run_id):
    return runtime_dir_for(run_id) / "runner.lock"


def atomic_write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(str(temporary), str(path))


def atomic_write_text(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(value)
        if not value.endswith("\n"):
            handle.write("\n")
    os.replace(str(temporary), str(path))


def read_json(path, default=None):
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        return default


def parse_config_value(text, line_number):
    if text == "true":
        return True
    if text == "false":
        return False
    if text.startswith('"') and text.endswith('"'):
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "Invalid string in config.toml line {}: {}".format(line_number, exc)
            )
    if text.startswith("'") and text.endswith("'"):
        return text[1:-1]
    if text.startswith("[") and text.endswith("]"):
        try:
            value = json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "Invalid array in config.toml line {}: {}".format(line_number, exc)
            )
        if isinstance(value, list):
            return value
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            raise RuntimeError(
                "Unsupported value in config.toml line {}".format(line_number)
            )


def load_runtime_config():
    """Read the small TOML subset used by this framework, with no dependency."""
    result = {}
    current = result
    for line_number, raw_line in enumerate(
        CONFIG_PATH.read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1].strip()
            if not section:
                raise RuntimeError(
                    "Empty table name in config.toml line {}".format(line_number)
                )
            current = result
            for part in section.split("."):
                if not part:
                    raise RuntimeError(
                        "Invalid table name in config.toml line {}".format(line_number)
                    )
                current = current.setdefault(part, {})
                if not isinstance(current, dict):
                    raise RuntimeError(
                        "Conflicting table in config.toml line {}".format(line_number)
                    )
            continue
        if "=" not in line:
            raise RuntimeError(
                "Expected key=value in config.toml line {}".format(line_number)
            )
        key, text = (part.strip() for part in line.split("=", 1))
        if not key or not text:
            raise RuntimeError("Invalid config.toml line {}".format(line_number))
        if key in current:
            raise RuntimeError(
                "Duplicate key '{}' in config.toml line {}".format(key, line_number)
            )
        current[key] = parse_config_value(text, line_number)
    return result


def flatten_config(value, prefix=""):
    result = []
    for key, item in value.items():
        full_key = "{}.{}".format(prefix, key) if prefix else key
        if isinstance(item, dict):
            result.extend(flatten_config(item, full_key))
        else:
            result.append((full_key, item))
    return result


def format_config_override(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (str, int, float)) and not isinstance(value, bool):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    raise RuntimeError("Unsupported temporary config value: {!r}".format(value))


def temporary_config_args(config=None):
    """Convert config.toml into invocation-scoped Codex `-c` overrides."""
    config = load_runtime_config() if config is None else config
    args = []
    for key, value in flatten_config(config):
        args.extend(["-c", "{}={}".format(key, format_config_override(value))])
    return args


def build_codex_command(session_id, prompt, config=None):
    command = [codex_executable(), *temporary_config_args(config), "-C", str(ROOT), "exec"]
    if session_id:
        command.append("resume")
    command.extend(
        [
            "--skip-git-repo-check",
            "--json",
            "--strict-config",
        ]
    )
    if session_id:
        command.append(session_id)
    command.append(prompt)
    return command


def render_prompt(run_id, continuation_prompt=None):
    run_dir = run_dir_for(run_id)
    problem_file = run_dir / "problem.md"
    context = (
        "Current research run: `{}`.\n"
        "Run directory: `{}`\n"
        "Problem file: `{}`\n"
    ).format(
        run_id,
        run_dir.relative_to(ROOT),
        problem_file.relative_to(ROOT),
    )
    if continuation_prompt:
        return context + (
            "\nFollow this additional user instruction for the current request:\n"
            "--- CONTINUATION INSTRUCTION BEGIN ---\n"
            + continuation_prompt.strip()
            + "\n--- CONTINUATION INSTRUCTION END ---\n"
            "Do not replace the run's original problem.\n"
        )
    return context + "\nAdvance this research autonomously by one substantial unit.\n"


def pid_alive(pid):
    if not isinstance(pid, int) or pid <= 0:
        return False
    if os.name == "nt":
        process_query_limited_information = 0x1000
        handle = ctypes.windll.kernel32.OpenProcess(
            process_query_limited_information, False, pid
        )
        if not handle:
            return False
        ctypes.windll.kernel32.CloseHandle(handle)
        return True
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def read_lock_pid(run_id):
    try:
        return int(lock_path_for(run_id).read_text(encoding="utf-8").strip())
    except (FileNotFoundError, ValueError):
        return None


def acquire_lock(run_id):
    path = lock_path_for(run_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    for _ in range(2):
        try:
            descriptor = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL)
        except FileExistsError:
            old_pid = read_lock_pid(run_id)
            if pid_alive(old_pid):
                raise RuntimeError(
                    "Run '{}' is already controlled by PID {}".format(run_id, old_pid)
                )
            path.unlink()
            continue
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(str(os.getpid()))
        return path
    raise RuntimeError("Could not acquire runner lock")


def release_lock(path):
    try:
        owner = int(path.read_text(encoding="utf-8").strip())
    except (FileNotFoundError, ValueError):
        return
    if owner == os.getpid():
        path.unlink()


def update_state(run_id, **changes):
    path = state_path_for(run_id)
    state = read_json(path, {})
    state.update(changes)
    state["updated_at"] = utc_now()
    atomic_write_json(path, state)
    return state


def _checkpoint_from_state(state):
    """Return the last accepted research checkpoint, including legacy state."""
    checkpoint = state.get("checkpoint")
    if isinstance(checkpoint, dict):
        turn = int(checkpoint.get("turn", 0))
        status = checkpoint.get("status", "initialized")
        if status not in {"initialized", "continue", "complete", "blocked"}:
            status = "continue" if turn > 0 else "initialized"
        skills = checkpoint.get("skills_used", [])
        if not isinstance(skills, list):
            skills = []
        return {
            "turn": turn,
            "status": status,
            "summary": str(checkpoint.get("summary", "")),
            "next_step": str(checkpoint.get("next_step", "")),
            "skills_used": [item for item in skills if isinstance(item, str)],
            "committed_at": checkpoint.get("committed_at")
            or state.get("updated_at")
            or state.get("created_at")
            or utc_now(),
        }

    raw_turn = int(state.get("turn", 0))
    # Legacy active states persisted the in-flight turn before it was accepted.
    # Recover the previous committed turn when upgrading such a state.
    if state.get("status") in ACTIVE_STATUSES and not state.get("attempt") and raw_turn > 0:
        turn = raw_turn - 1
    else:
        turn = raw_turn

    raw_status = state.get("status", "initialized")
    if raw_status in {"initialized", "continue", "complete", "blocked"}:
        status = raw_status
    elif raw_status == "paused":
        status = "continue"
    else:
        status = "continue" if turn > 0 else "initialized"
    skills = state.get("skills_used", [])
    if not isinstance(skills, list):
        skills = []
    return {
        "turn": turn,
        "status": status,
        "summary": str(state.get("summary", "")),
        "next_step": str(state.get("next_step", "")),
        "skills_used": [item for item in skills if isinstance(item, str)],
        "committed_at": state.get("updated_at") or state.get("created_at") or utc_now(),
    }


def _checkpoint_fields(checkpoint):
    """Mirror one committed checkpoint onto the public state fields."""
    return {
        "turn": int(checkpoint["turn"]),
        "summary": checkpoint.get("summary", ""),
        "next_step": checkpoint.get("next_step", ""),
        "skills_used": list(checkpoint.get("skills_used", [])),
    }


def _finish_attempt(attempt, status, error=None):
    value = dict(attempt or {})
    value["status"] = status
    value["runner_pid"] = None
    value["codex_pid"] = None
    value["finished_at"] = utc_now()
    if error is not None:
        value["error"] = str(error)
    return value

def ensure_initialized(run_id):
    run_dir = run_dir_for(run_id)
    if not (run_dir / "problem.md").is_file() or not state_path_for(run_id).is_file():
        raise RuntimeError(
            "Run '{}' does not exist. Start it with --prompt <text> or --problem <path>.".format(
                run_id
            )
        )


def terminate_process(process):
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def parse_codex_event(line):
    try:
        event = json.loads(line)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Codex emitted invalid JSONL: {}".format(exc))
    if not isinstance(event, dict):
        raise RuntimeError("Codex emitted a non-object JSONL event")

    session_id = None
    final_text = None
    if event.get("type") == "thread.started":
        value = event.get("thread_id")
        if isinstance(value, str) and value:
            session_id = value
    elif event.get("type") == "item.completed":
        item = event.get("item")
        if isinstance(item, dict) and item.get("type") == "agent_message":
            value = item.get("text")
            if isinstance(value, str):
                final_text = value
    return session_id, final_text


def normalize_progress_text(value):
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        # Codex may report a process invocation as argv.  JSON-encoding argv
        # adds wrapper quotes and escapes that look like path arguments to the
        # display parser, so join the already-separated arguments instead.
        value = " ".join(str(part) for part in value)
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return " ".join(value.split())


def _valid_progress_target(value):
    """Return a safe display target, never shell punctuation or wrapper quotes."""
    if not isinstance(value, str):
        return None
    value = value.strip().rstrip(",")
    if len(value) >= 2 and value[:2] == '\\"' and value[-2:] == '\\"':
        value = value[2:-2]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        value = value[1:-1]
    value = value.strip()
    if not value or value.strip("\\'\"") == "":
        return None
    if value[0] in "{[(" or value.startswith("-"):
        return None
    return value


def _resolve_simple_path_variable(raw_command, command_start, target):
    """Resolve only transparent same-command PowerShell path assignments."""
    if not target.startswith("$"):
        return target
    variable = re.escape(target)
    prefix = raw_command[:command_start]
    assignment_patterns = (
        variable + r"\s*=\s*['\"]([^'\"]+)['\"]",
        variable
        + r"\s*=\s*\(?\s*Resolve-Path\s+(?:-LiteralPath\s+|-Path\s+)?['\"]([^'\"]+)['\"]",
    )
    for pattern in assignment_patterns:
        assignment = re.search(pattern, prefix, flags=re.IGNORECASE)
        if assignment:
            return _valid_progress_target(assignment.group(1))
    return None


def powershell_command_target(raw_command, command_name, file_fallback=False):
    """Extract one trustworthy path argument from a PowerShell cmdlet."""
    command_match = re.search(
        r"\b{}\b".format(re.escape(command_name)), raw_command, flags=re.IGNORECASE
    )
    if command_match is None:
        return None
    command_tail = raw_command[command_match.start() :]
    path_match = re.search(
        r"(?:-LiteralPath|-Path)\s+(?:'([^']+)'|\"([^\"]+)\"|([^\s|;,)\]}]+))",
        command_tail,
        flags=re.IGNORECASE,
    )
    target = (
        next((value for value in path_match.groups() if value), None)
        if path_match is not None
        else None
    )
    target = _valid_progress_target(target)

    if target is None and file_fallback:
        path_match = re.search(
            r"(?:'([^']+\.[A-Za-z0-9]+)'|\"([^\"]+\.[A-Za-z0-9]+)\"|([^\s|;]+(?:\.[A-Za-z0-9]+|\$)))",
            command_tail,
        )
        target = _valid_progress_target(
            next((value for value in path_match.groups() if value), None)
            if path_match is not None
            else None
        )
    if not target:
        return None
    return _resolve_simple_path_variable(raw_command, command_match.start(), target)


def powershell_read_target(raw_command):
    """Extract a readable Get-Content target, resolving simple variables."""
    return powershell_command_target(raw_command, "Get-Content", file_fallback=True)


def _summary_with_target(action, target):
    return "{} | {}".format(action, target) if target else action


def command_progress_summary(item):
    """Return a short description of a shell command."""
    raw_command = normalize_progress_text(item.get("command"))
    command = raw_command.lower()
    if "get-childitem" in command:
        return _summary_with_target(
            "List files", powershell_command_target(raw_command, "Get-ChildItem")
        )
    if "rg --files" in command:
        return "List files"
    if "get-content" in command:
        return _summary_with_target("Read file", powershell_read_target(raw_command))
    if "select-string" in command:
        return _summary_with_target(
            "Search content",
            powershell_command_target(raw_command, "Select-String", file_fallback=True),
        )
    if re.search(r"(^|[ ;|])rg\s", command):
        return "Search content"
    if "test-path" in command:
        return _summary_with_target(
            "Check path", powershell_command_target(raw_command, "Test-Path")
        )
    if "unittest" in command or "pytest" in command:
        return "Run tests"
    for cmdlet in (
        "Set-Content",
        "Add-Content",
        "Out-File",
        "New-Item",
        "Copy-Item",
        "Move-Item",
        "Remove-Item",
    ):
        if cmdlet.lower() in command:
            return _summary_with_target(
                "Modify files", powershell_command_target(raw_command, cmdlet)
            )
    return "Execute command"


def full_event_text(value):
    """Preserve model-visible text exactly; format non-text values readably."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, indent=2)


def tool_display_name(item):
    item_type = str(item.get("type") or "tool")
    if item_type == "command_execution":
        command = normalize_progress_text(item.get("command")).lower()
        shell = (
            "PowerShell"
            if os.name == "nt" or "powershell" in command or "pwsh" in command
            else "Shell"
        )
        return "{} | {}".format(shell, command_progress_summary(item))
    if item_type == "file_change":
        changes = item.get("changes")
        paths = []
        if isinstance(changes, list):
            for change in changes:
                if isinstance(change, dict) and isinstance(change.get("path"), str):
                    paths.append(change["path"])
        return "File change{}".format(" | " + ", ".join(paths) if paths else "")
    if item_type == "web_search":
        query = item.get("query")
        return "Web search{}".format(" | " + full_event_text(query) if query else "")
    if item_type in {"collab_agent_tool_call", "mcp_tool_call"}:
        name = item.get("tool") or item.get("name") or item_type
        return "Agent tool | {}".format(name)
    name = item.get("tool") or item.get("name") or item_type
    return str(name).replace("_", " ").strip().title()


def event_result_suffix(item):
    status = item.get("status")
    if not isinstance(status, str) or status in {"in_progress", "completed"}:
        return ""
    return " | {}".format(status.upper())


def format_usage(usage):
    if not isinstance(usage, dict):
        return full_event_text(usage)
    labels = (
        ("input_tokens", "input"),
        ("cached_input_tokens", "cached"),
        ("output_tokens", "output"),
        ("reasoning_output_tokens", "reasoning"),
    )
    parts = ["{} {}".format(label, usage[key]) for key, label in labels if key in usage]
    return ", ".join(parts) if parts else full_event_text(usage)


def is_turn_result_message(value):
    """Identify the controller's final structured result so it is printed once."""
    if not isinstance(value, str):
        return False
    try:
        payload = json.loads(value)
    except json.JSONDecodeError:
        return False
    return (
        isinstance(payload, dict)
        and payload.get("status") in TURN_STATUS_LABELS
        and isinstance(payload.get("summary"), str)
        and isinstance(payload.get("next_step"), str)
        and isinstance(payload.get("skills_used"), list)
    )


def codex_progress_message(event):
    """Render one Codex event with full reasoning/messages and clear tool activity."""
    event_type = event.get("type")
    if event_type == "thread.started":
        return "SESSION | {}".format(event.get("thread_id", "started"))
    if event_type == "turn.started":
        return "REQUEST | STARTED"
    if event_type == "turn.completed":
        usage = event.get("usage")
        return "REQUEST | COMPLETED{}".format(
            " | " + format_usage(usage) if usage else ""
        )
    if event_type in {"turn.failed", "error"}:
        detail = event.get("error") or event.get("message") or event
        return "ERROR | {}".format(full_event_text(detail))
    if event_type == "token_count":
        return None
    if event_type not in {"item.started", "item.updated", "item.completed"}:
        return "EVENT | {}".format(event_type or "unknown")

    item = event.get("item")
    if not isinstance(item, dict):
        return "EVENT | {}".format(event_type)
    item_type = str(item.get("type") or "item")
    phase = event_type.split(".", 1)[1]

    if item_type == "agent_message":
        raw_text = item.get("text")
        if phase == "completed" and is_turn_result_message(raw_text):
            return None
        text = full_event_text(raw_text)
        return "MESSAGE | {}{}".format(phase.upper(), "\n" + text if text else "")

    if item_type == "reasoning":
        text = full_event_text(item.get("text") or item.get("summary"))
        return "REASONING | {}{}".format(
            phase.upper(), "\n" + text if text else ""
        )

    return "TOOL | {} | {}{}".format(
        phase.upper(), tool_display_name(item), event_result_suffix(item)
    )


def print_codex_progress(event):
    message = codex_progress_message(event)
    if message:
        timestamp = dt.datetime.now().astimezone().strftime("%H:%M:%S")
        print("[{}] {}".format(timestamp, message), flush=True)


class ProgressRenderer:
    """Coalesce short tool events while streaming all model-visible text."""

    def __init__(self, long_tool_seconds=LONG_TOOL_SECONDS, clock=None):
        self.long_tool_seconds = long_tool_seconds
        self.clock = clock or time.monotonic
        self.pending_tools = {}

    @staticmethod
    def _is_tool_event(event):
        if event.get("type") not in {"item.started", "item.updated", "item.completed"}:
            return False
        item = event.get("item")
        return isinstance(item, dict) and item.get("type") not in {
            "agent_message",
            "reasoning",
        }

    @staticmethod
    def _tool_key(item):
        item_id = item.get("id")
        if item_id:
            return ("id", str(item_id))
        return (
            str(item.get("type") or "tool"),
            normalize_progress_text(
                item.get("command") or item.get("tool") or item.get("name")
            ),
        )

    @staticmethod
    def _print(message):
        timestamp = dt.datetime.now().astimezone().strftime("%H:%M:%S")
        print("[{}] {}".format(timestamp, message), flush=True)

    @staticmethod
    def _with_duration(message, elapsed):
        return "{} | {:.1f}s".format(message, max(0.0, elapsed))

    def flush_long_running(self):
        now = self.clock()
        for pending in self.pending_tools.values():
            if pending["displayed"]:
                continue
            elapsed = now - pending["started_at"]
            if elapsed >= self.long_tool_seconds:
                item = pending["event"].get("item", {})
                self._print("TOOL | RUNNING | {}".format(tool_display_name(item)))
                pending["displayed"] = True

    def handle(self, event):
        if not self._is_tool_event(event):
            print_codex_progress(event)
            return

        item = event["item"]
        key = self._tool_key(item)
        phase = event["type"].split(".", 1)[1]
        if phase == "started":
            self.pending_tools[key] = {
                "event": event,
                "started_at": self.clock(),
                "displayed": False,
            }
            return

        pending = self.pending_tools.get(key)
        if phase == "updated":
            if pending is not None:
                pending["event"] = event
                self.flush_long_running()
            else:
                print_codex_progress(event)
            return


        if pending is None:
            print_codex_progress(event)
            return
        self.pending_tools.pop(key, None)
        elapsed = self.clock() - pending["started_at"]
        message = codex_progress_message(event)
        if message:
            self._print(self._with_duration(message, elapsed))

    def finish(self):
        now = self.clock()
        for pending in self.pending_tools.values():
            item = pending["event"].get("item", {})
            message = "TOOL | INTERRUPTED | {}".format(tool_display_name(item))
            self._print(self._with_duration(message, now - pending["started_at"]))
        self.pending_tools.clear()


def execute_turn(command, stop_path, on_session_id=None, on_started=None):
    diagnostics_path = stop_path.parent / "codex-stderr.log"
    diagnostics_path.parent.mkdir(parents=True, exist_ok=True)
    diagnostics_handle = diagnostics_path.open("ab")
    try:
        process = subprocess.Popen(
            command,
            cwd=str(ROOT),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=diagnostics_handle,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except Exception:
        diagnostics_handle.close()
        raise
    if on_started:
        on_started(process.pid)
    events = queue.Queue()
    end_of_stream = object()

    def read_events():
        try:
            for line in process.stdout:
                events.put(line)
        finally:
            events.put(end_of_stream)

    reader = threading.Thread(target=read_events, daemon=True)
    reader.start()
    observed_session_id = None
    final_text = None
    stream_ended = False
    stop_reason = None
    renderer = ProgressRenderer()

    try:
        while True:
            if stop_path.exists() and process.poll() is None:
                stop_reason = "command"
                terminate_process(process)

            try:
                item = events.get(timeout=0.25)
            except queue.Empty:
                renderer.flush_long_running()
                if process.poll() is not None and stream_ended:
                    break
                continue

            if item is end_of_stream:
                stream_ended = True
            else:
                try:
                    event_session_id, event_final_text = parse_codex_event(item)
                    event = json.loads(item)
                except RuntimeError:
                    if stop_reason:
                        continue
                    raise
                renderer.handle(event)
                if event_session_id:
                    observed_session_id = event_session_id
                    if on_session_id:
                        on_session_id(event_session_id)
                if event_final_text is not None:
                    final_text = event_final_text

            if process.poll() is not None and stream_ended and events.empty():
                break
    except KeyboardInterrupt:
        stop_reason = "keyboard"
        stop_path.parent.mkdir(parents=True, exist_ok=True)
        stop_path.touch()
        terminate_process(process)
    except Exception:
        terminate_process(process)
        raise
    finally:
        renderer.finish()
        reader.join(timeout=2)
        if process.stdout is not None:
            process.stdout.close()
        diagnostics_handle.close()

    return process.returncode, stop_reason, observed_session_id, final_text


def parse_turn_result(text):
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Codex returned invalid JSON: {}".format(exc))
    if not isinstance(value, dict):
        raise RuntimeError("Codex did not produce a JSON object")
    if value.get("status") not in {"continue", "complete", "blocked"}:
        raise RuntimeError("Codex returned an unknown status")
    for key in ("summary", "next_step"):
        if not isinstance(value.get(key), str):
            raise RuntimeError("Codex result is missing string field '{}'".format(key))
    if not isinstance(value.get("skills_used"), list) or not all(
        isinstance(item, str) for item in value["skills_used"]
    ):
        raise RuntimeError("Codex result has an invalid skills_used field")
    return value


def parse_optional_turn_result(text):
    """Return a research-state result, or None for an ordinary model response."""
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        return None
    if not isinstance(value, dict):
        return None
    controller_fields = {"status", "summary", "skills_used", "next_step"}
    if not controller_fields.intersection(value):
        return None
    return parse_turn_result(text)


def initialize_run(run_id, problem=None, prompt=None):
    run_id = validate_run_id(run_id)
    source = None
    problem_text = None
    if problem is not None:
        source = Path(problem).expanduser().resolve()
        if not source.is_file():
            raise RuntimeError("Problem file does not exist: {}".format(source))
    else:
        problem_text = prompt.strip()
        if not problem_text:
            raise RuntimeError("Inline problem prompt must not be empty")
    run_dir = run_dir_for(run_id)
    if run_dir.exists() and any(run_dir.iterdir()):
        raise RuntimeError("Run directory already exists and is not empty: {}".format(run_dir))
    run_dir.mkdir(parents=True, exist_ok=True)
    if source is not None:
        shutil.copy2(str(source), str(run_dir / "problem.md"))
        source_problem = str(source)
    else:
        atomic_write_text(run_dir / "problem.md", problem_text)
        source_problem = "<inline prompt>"
    created_at = utc_now()
    checkpoint = {
        "turn": 0,
        "status": "initialized",
        "summary": "",
        "next_step": "",
        "skills_used": [],
        "committed_at": created_at,
    }
    atomic_write_json(
        state_path_for(run_id),
        {
            "run_id": run_id,
            "status": "initialized",
            "turn": 0,
            "session_id": None,
            "runner_pid": None,
            "codex_pid": None,
            "source_problem": source_problem,
            "summary": "",
            "next_step": "",
            "skills_used": [],
            "checkpoint": checkpoint,
            "attempt": None,
            "created_at": created_at,
            "updated_at": created_at,
        },
    )
    print("Initialized run '{}' at {}".format(run_id, run_dir))

def prepare_run(args):
    run_id = validate_run_id(args.run_id)
    run_dir = run_dir_for(run_id)
    initialized = (run_dir / "problem.md").is_file() and state_path_for(run_id).is_file()
    problem = getattr(args, "problem", None)
    prompt = getattr(args, "prompt", None)
    supplied_problem = problem is not None or prompt is not None

    if initialized:
        # The original problem is immutable. A prompt on an existing run is a
        # one-turn continuation instruction and does not replace problem.md.
        if problem is not None:
            raise RuntimeError(
                "Run '{}' already exists; --problem can only be used when creating a new run.".format(
                    run_id
                )
            )
        if prompt is not None:
            continuation_prompt = prompt.strip()
            if not continuation_prompt:
                raise RuntimeError("Continuation prompt must not be empty")
            args._continuation_prompt = continuation_prompt
        else:
            args._continuation_prompt = None
        return run_id

    if not supplied_problem:
        raise RuntimeError(
            "Run '{}' does not exist; provide --prompt <text> or --problem <path>.".format(
                run_id
            )
        )
    initialize_run(run_id, problem=problem, prompt=prompt)
    args._continuation_prompt = None
    return run_id


def command_run(args):
    run_id = prepare_run(args)
    continuation_prompt = getattr(args, "_continuation_prompt", None)
    stop_path = stop_path_for(run_id)
    if not args.keep_stop and stop_path.exists():
        stop_path.unlink()
    lock = acquire_lock(run_id)
    try:
        state = read_json(state_path_for(run_id), {})
        checkpoint = _checkpoint_from_state(state)
        session_id = state.get("session_id")
        previous_public_status = state.get("status", checkpoint["status"])

        # Upgrade legacy state lazily. Runtime status may change while the
        # checkpoint fields stay pinned to the last accepted research result.
        state = update_state(
            run_id,
            checkpoint=checkpoint,
            attempt=state.get("attempt"),
            **_checkpoint_fields(checkpoint)
        )

        while True:
            if stop_path.exists():
                update_state(
                    run_id,
                    status="stopped",
                    runner_pid=None,
                    codex_pid=None,
                    checkpoint=checkpoint,
                    **_checkpoint_fields(checkpoint)
                )
                print("Stop requested; run ended.")
                return 0

            previous_public_status = state.get("status", checkpoint["status"])
            attempt_turn = int(checkpoint["turn"]) + 1
            prompt = render_prompt(run_id, continuation_prompt=continuation_prompt)
            continuation_prompt = None
            command = build_codex_command(session_id, prompt)
            attempt = {
                "turn": attempt_turn,
                "status": "starting",
                "runner_pid": os.getpid(),
                "codex_pid": None,
                "started_at": utc_now(),
            }
            state = update_state(
                run_id,
                status="starting",
                runner_pid=os.getpid(),
                codex_pid=None,
                checkpoint=checkpoint,
                attempt=attempt,
                **_checkpoint_fields(checkpoint)
            )
            print("Starting Codex request for '{}'...".format(run_id), flush=True)

            active_session_id = session_id

            def remember_session_id(observed_session_id):
                nonlocal active_session_id, attempt
                if active_session_id and observed_session_id != active_session_id:
                    raise RuntimeError(
                        "Codex resumed an unexpected session: {}".format(observed_session_id)
                    )
                active_session_id = observed_session_id
                attempt = dict(attempt)
                attempt["session_id"] = observed_session_id
                update_state(
                    run_id,
                    session_id=observed_session_id,
                    attempt=attempt,
                )

            def remember_process(codex_pid):
                nonlocal attempt
                attempt = dict(attempt)
                attempt.update(
                    status="running",
                    runner_pid=os.getpid(),
                    codex_pid=codex_pid,
                )
                update_state(
                    run_id,
                    status="running",
                    runner_pid=os.getpid(),
                    codex_pid=codex_pid,
                    attempt=attempt,
                )

            try:
                return_code, stop_reason, observed_session_id, final_text = execute_turn(
                    command, stop_path, remember_session_id, remember_process
                )
                session_id = observed_session_id or active_session_id
                if stop_reason:
                    finished_attempt = _finish_attempt(
                        attempt, "stopped", "Stopped by {}".format(stop_reason)
                    )
                    update_state(
                        run_id,
                        status="stopped",
                        runner_pid=None,
                        codex_pid=None,
                        session_id=session_id,
                        checkpoint=checkpoint,
                        attempt=finished_attempt,
                        **_checkpoint_fields(checkpoint)
                    )
                    print("Run stopped by {}.".format(stop_reason))
                    return 0
                if return_code != 0:
                    message = "codex exec exited with code {}".format(return_code)
                    update_state(
                        run_id,
                        status="error",
                        runner_pid=None,
                        codex_pid=None,
                        session_id=session_id,
                        checkpoint=checkpoint,
                        attempt=_finish_attempt(attempt, "failed", message),
                        **_checkpoint_fields(checkpoint)
                    )
                    print(
                        "Codex failed with exit code {}. No automatic retry. "
                        "See {}.".format(
                            return_code, runtime_dir_for(run_id) / "codex-stderr.log"
                        )
                    )
                    return return_code or 1
                if not session_id:
                    raise RuntimeError("Codex did not report a session id")
                if final_text is None:
                    raise RuntimeError("Codex did not emit a final agent message")
                result = parse_optional_turn_result(final_text)
            except (RuntimeError, OSError) as exc:
                session_id = active_session_id
                update_state(
                    run_id,
                    status="error",
                    runner_pid=None,
                    codex_pid=None,
                    session_id=session_id,
                    checkpoint=checkpoint,
                    attempt=_finish_attempt(attempt, "failed", exc),
                    **_checkpoint_fields(checkpoint)
                )
                print("Codex run error: {}".format(exc), file=sys.stderr)
                return 1

            if result is None:
                state = update_state(
                    run_id,
                    status=previous_public_status,
                    runner_pid=None,
                    codex_pid=None,
                    session_id=session_id,
                    checkpoint=checkpoint,
                    attempt=None,
                    **_checkpoint_fields(checkpoint)
                )
                return 0

            checkpoint = {
                "turn": attempt_turn,
                "status": result["status"],
                "summary": result["summary"],
                "next_step": result["next_step"],
                "skills_used": list(result["skills_used"]),
                "committed_at": utc_now(),
            }
            state = update_state(
                run_id,
                status=result["status"],
                runner_pid=os.getpid() if result["status"] == "continue" else None,
                codex_pid=None,
                session_id=session_id,
                checkpoint=checkpoint,
                attempt=None,
                **_checkpoint_fields(checkpoint)
            )
            print("\n=== {} ===".format(TURN_STATUS_LABELS[result["status"]]), flush=True)
            print("Progress:", flush=True)
            print(result["summary"], flush=True)
            if result["skills_used"]:
                print("Skills: {}".format(", ".join(result["skills_used"])), flush=True)
            if result["next_step"]:
                print("Next step:", flush=True)
                print(result["next_step"], flush=True)

            if result["status"] != "continue":
                return 0
            if args.once:
                state = update_state(
                    run_id,
                    status="paused",
                    runner_pid=None,
                    codex_pid=None,
                    checkpoint=checkpoint,
                    attempt=None,
                    **_checkpoint_fields(checkpoint)
                )
                print("Paused after one turn (--once).")
                return 0
    finally:
        release_lock(lock)

def command_start(args):
    run_id = prepare_run(args)
    continuation_prompt = getattr(args, "_continuation_prompt", None)
    existing_pid = read_lock_pid(run_id)
    if pid_alive(existing_pid):
        raise RuntimeError("Run '{}' is already active as PID {}".format(run_id, existing_pid))
    stop_path = stop_path_for(run_id)
    if stop_path.exists():
        stop_path.unlink()

    log_path = runtime_dir_for(run_id) / "background.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    child_command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "run",
        run_id,
        "--keep-stop",
    ]
    if continuation_prompt is not None:
        child_command.extend(["--prompt", continuation_prompt])
    popen_kwargs = {"cwd": str(ROOT), "stdin": subprocess.DEVNULL, "close_fds": True}
    if os.name == "nt":
        popen_kwargs["creationflags"] = (
            getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
            | getattr(subprocess, "CREATE_NO_WINDOW", 0)
        )
    else:
        popen_kwargs["start_new_session"] = True

    with log_path.open("ab") as log_handle:
        process = subprocess.Popen(
            child_command,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            **popen_kwargs
        )

    deadline = time.monotonic() + STARTUP_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        return_code = process.poll()
        state = read_json(state_path_for(run_id), {})
        lock_pid = read_lock_pid(run_id)
        if (
            lock_pid == process.pid
            and state.get("runner_pid") == process.pid
            and state.get("status") == "running"
        ):
            print("Started '{}' in background as PID {}.".format(run_id, process.pid))
            print("Log: {}".format(log_path))
            return 0
        if return_code is not None:
            detail = state.get("summary") or "see background log"
            raise RuntimeError(
                "Background runner exited during startup (code {}): {}".format(
                    return_code, detail
                )
            )
        time.sleep(0.1)

    stop_path.touch()
    raise RuntimeError(
        "Background runner did not reach running state within {} seconds; stop requested. "
        "See {}".format(STARTUP_TIMEOUT_SECONDS, log_path)
    )


def command_stop(args):
    run_id = validate_run_id(args.run_id)
    ensure_initialized(run_id)
    lock_pid = read_lock_pid(run_id)
    if not pid_alive(lock_pid):
        raise RuntimeError("Run '{}' is not currently active".format(run_id))
    stop_path = stop_path_for(run_id)
    stop_path.touch()
    print("Immediate stop requested for '{}'.".format(run_id))
    return 0


def reconcile_state(run_id, state, lock_pid, runner_alive):
    if state.get("status") not in ACTIVE_STATUSES or runner_alive:
        return state
    previous = state.get("status")
    stale_pid = state.get("runner_pid") or lock_pid
    lock_path = lock_path_for(run_id)
    if lock_path.exists() and not pid_alive(lock_pid):
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass

    checkpoint = _checkpoint_from_state(state)
    message = "Controller PID {} is no longer running; reconciled stale '{}' state.".format(
        stale_pid, previous
    )
    attempt = state.get("attempt")
    if not isinstance(attempt, dict):
        attempt = {
            "turn": int(checkpoint["turn"]) + 1,
            "status": previous,
            "runner_pid": state.get("runner_pid"),
            "codex_pid": state.get("codex_pid"),
            "started_at": state.get("updated_at") or utc_now(),
        }
    attempt = _finish_attempt(attempt, "interrupted", message)
    return update_state(
        run_id,
        status="error",
        runner_pid=None,
        codex_pid=None,
        checkpoint=checkpoint,
        attempt=attempt,
        **_checkpoint_fields(checkpoint)
    )

def command_status(args):
    run_id = validate_run_id(args.run_id)
    ensure_initialized(run_id)
    state = read_json(state_path_for(run_id), {})
    lock_pid = read_lock_pid(run_id)
    runner_alive = pid_alive(lock_pid)
    state = reconcile_state(run_id, state, lock_pid, runner_alive)
    state["runner_alive"] = runner_alive
    state["lock_pid"] = lock_pid if runner_alive else None
    state["stop_requested"] = stop_path_for(run_id).exists()
    print(json.dumps(state, ensure_ascii=False, indent=2))
    return 0


def resolve_command(command):
    candidate = Path(command)
    if candidate.is_file():
        return str(candidate.resolve())
    return shutil.which(command)


def codex_executable():
    """Find Codex on PATH or in the standard Windows desktop-app bundle."""
    override = os.environ.get("CODEX_EXECUTABLE")
    if override:
        resolved = resolve_command(override)
        if resolved:
            return resolved
        raise RuntimeError("CODEX_EXECUTABLE does not point to a command or file")

    resolved = resolve_command("codex")
    if resolved:
        return resolved

    if os.name == "nt":
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            bundle_root = Path(local_app_data) / "OpenAI" / "Codex" / "bin"
            candidates = [path for path in bundle_root.glob("*/codex.exe") if path.is_file()]
            if candidates:
                return str(max(candidates, key=lambda path: path.stat().st_mtime).resolve())

    raise RuntimeError(
        "Codex command was not found. Install it, add it to PATH, or set CODEX_EXECUTABLE"
    )


def command_validate():
    errors = []
    notes = []
    for path in (CONFIG_PATH, AGENTS_PATH, SCHEMA_PATH):
        if not path.is_file():
            errors.append("Missing framework file: {}".format(path))
    if CONFIG_PATH.is_file():
        try:
            overrides = temporary_config_args()
            notes.append(
                "Loaded {} invocation-only config values from {}".format(
                    len(overrides) // 2, CONFIG_PATH
                )
            )
        except (OSError, RuntimeError) as exc:
            errors.append("Invalid temporary config: {}".format(exc))
    try:
        resolved = codex_executable()
    except RuntimeError as exc:
        errors.append(str(exc))
    else:
        try:
            check = subprocess.run(
                [resolved, "--version"],
                cwd=str(ROOT),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10,
            )
            if check.returncode:
                errors.append("Codex version check failed: {}".format(check.stderr.strip()))
            else:
                notes.append(check.stdout.strip())
        except (OSError, subprocess.TimeoutExpired) as exc:
            errors.append("Codex version check failed: {}".format(exc))

    skill_dirs = [
        ROOT / ".agents" / "skills" / "construct-mathematical-concept",
        ROOT / ".agents" / "skills" / "verify-mathematical-concept",
    ]
    for skill_dir in skill_dirs:
        if not skill_dir.is_dir():
            errors.append("Missing Skill directory: {}".format(skill_dir))
        elif not (skill_dir / "SKILL.md").is_file():
            notes.append("Skill intentionally not implemented yet: {}".format(skill_dir.name))

    report = {
        "valid": not errors,
        "framework_root": str(ROOT),
        "notes": notes,
        "errors": errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


def build_parser():
    parser = argparse.ArgumentParser(
        description="Run a Skill-directed mathematical research agent with Codex CLI."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run continuously in the foreground")
    run_parser.add_argument("run_id")
    run_source = run_parser.add_mutually_exclusive_group()
    run_source.add_argument("--problem", help="Problem file for a new run")
    run_source.add_argument(
        "--prompt",
        "--problem-text",
        dest="prompt",
        help="Problem text for a new run, or a one-turn continuation instruction for an existing run",
    )
    run_parser.add_argument("--once", action="store_true", help="Run one Codex turn only")
    run_parser.add_argument("--keep-stop", action="store_true", help=argparse.SUPPRESS)

    start_parser = subparsers.add_parser("start", help="Run continuously in the background")
    start_parser.add_argument("run_id")
    start_source = start_parser.add_mutually_exclusive_group()
    start_source.add_argument("--problem", help="Problem file for a new run")
    start_source.add_argument(
        "--prompt",
        "--problem-text",
        dest="prompt",
        help="Problem text for a new run, or a one-turn continuation instruction for an existing run",
    )

    stop_parser = subparsers.add_parser("stop", help="Immediately stop an active run")
    stop_parser.add_argument("run_id")

    status_parser = subparsers.add_parser("status", help="Show saved and live run status")
    status_parser.add_argument("run_id")

    subparsers.add_parser("validate", help="Validate config, Codex, and framework files")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "run":
            return command_run(args)
        if args.command == "start":
            return command_start(args)
        if args.command == "stop":
            return command_stop(args)
        if args.command == "status":
            return command_status(args)
        if args.command == "validate":
            return command_validate()
    except (ValueError, RuntimeError, OSError) as exc:
        print("error: {}".format(exc), file=sys.stderr)
        return 2
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    sys.exit(main())
