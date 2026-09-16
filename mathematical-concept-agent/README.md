# Mathematical Concept Agent (Stage 2)

This directory contains the second-stage exploratory agent for the
[Creative-Intelligence](https://github.com/DeepMathLLM/Creative-Intelligence)
project. It uses the local Codex CLI as its execution engine and keeps the
mathematical construction and verification policy in the two bundled Skills.

The controller is intentionally thin. It saves a research problem, starts or
resumes one Codex session, records the structured research state, and supports
foreground, background, status, and stop commands. Mathematical research files
are created inside a local run directory and are not part of this source
package.

## Included in the repository

```text
mathematical-concept-agent/
├── agent.py
├── AGENTS.md
├── config.toml
├── .gitignore
├── schemas/turn-result.schema.json
├── tests/test_agent.py
└── .agents/skills/
    ├── construct-mathematical-concept/SKILL.md
    └── verify-mathematical-concept/SKILL.md
```

Generated runs, logs, research branches, papers, PDFs, and other experiment
outputs are deliberately excluded. Local run state is written under
`runs/<run-id>/`, which is ignored by Git.

## Requirements

- Windows PowerShell or another environment that can run Python 3.10+;
- the Codex CLI installed and available as `codex`, or an explicit
  `CODEX_EXECUTABLE` environment variable;
- a configured Codex provider for live research turns.

The `validate` command checks the local framework files and the Codex
executable. It may report a missing executable on machines that have not yet
installed Codex; the offline unit tests do not require a provider or network.

## Usage

Run these commands from this directory:

```powershell
py -3.10 agent.py validate
py -3.10 agent.py run experiment-001 --prompt "State the mathematical problem or structure to investigate"
```

To start in the background:

```powershell
py -3.10 agent.py start experiment-001 --prompt "State the mathematical problem or structure to investigate"
```

Resume an existing run without replacing its original problem:

```powershell
py -3.10 agent.py run experiment-001
py -3.10 agent.py run experiment-001 --prompt "Continue by checking boundary cases" --once
```

Inspect or stop a run:

```powershell
py -3.10 agent.py status experiment-001
py -3.10 agent.py stop experiment-001
```

Run the deterministic controller tests:

```powershell
py -3.10 -m unittest discover -s tests -p "test_*.py" -v
```

The repository also runs the Stage 2 controller regression suite in GitHub
Actions. The Windows lane exercises the complete controller suite, while a
Linux lane independently pins the crash/recovery checkpoint contract.

## Crash-safe research checkpoints

`state.json` separates accepted research progress from an in-flight Codex
attempt. The nested `checkpoint` object is the durable record of the last
accepted structured research result; `attempt` records temporary lifecycle
state for the next turn.

Starting a Codex turn therefore does not advance the committed turn number or
overwrite the accepted summary. A failed or interrupted attempt is recorded
separately. On restart, the controller can reuse an already observed Codex
session while retrying the still-uncommitted turn. Only a valid structured
research result advances `checkpoint`.

This is a controller-level recovery guarantee, not exactly-once execution of a
Codex turn or of external side effects performed by tools inside that turn.

## Configuration and research contract

`config.toml` contains invocation-only Codex overrides. `agent.py` translates
them into temporary `codex -c key=value` arguments; it does not modify the
user's Codex configuration.

The controller accepts the structured result below for research turns:

```json
{
  "status": "continue | complete | blocked",
  "summary": "Current progress",
  "skills_used": [],
  "next_step": "Next research step"
}
```

The two Skills define when to construct or verify a mathematical concept and
how to distinguish proved results, evidence, conjectures, and open obligations.
