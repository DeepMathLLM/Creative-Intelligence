# Creative-Intelligence

This project explores mathematical creativity in AI—whether it can move beyond solving existing problems to originate new ideas and expand the frontiers of mathematics alongside humans.

## Current Focus

1. **Tracing the Origins of Mathematical Concepts**
   Study how important mathematical concepts emerged, including their historical context, the problems they addressed, the limitations they overcame, and their influence on mathematics and related fields.

2. **Exploring Mathematical Creativity in AI**
   Use frontier AI models to investigate whether they can move beyond solving existing problems and demonstrate genuine mathematical creativity, including the ability to generate new concepts, perspectives, and approaches.

## Mathematical Object Origin Archive Runner

This runner supports the first research direction by creating verified origin archives for mathematical concepts, objects, and methods. Each archive focuses on the mathematical problem that motivated the object, the difficulty that had to be overcome, the ideas that led to its formation, and the essential role of its defining structure.

Objects are processed serially. Each object receives its own Moonshine project and session, and the final Markdown archive is published only after verification passes.

## What Changed in v2

The original runner accepted a predefined JSON queue. Version 2 retains that workflow and adds branch-driven archive discovery.

- Select objects directly from supplied mathematical branches; no object list is required in advance.
- Choose objects that arose in response to a concrete mathematical problem or a well-defined problem class.
- Select, write, and verify one object within one Moonshine task.
- Continue until the requested number of verified archives has been published.
- Pass previously attempted object names into later tasks to reduce repetition.
- Record failed attempts without counting them toward the requested total.
- Resume interrupted projects and sessions from persistent runner state.
- Show normal Moonshine output in the terminal with `--stream-output`.
- Preserve the predefined JSON queue mode for collections assembled manually.

The archive specification and verification criteria now emphasize precise mathematical context rather than a chronology of people, publications, and dates.

The previous queue-focused implementation is preserved on the [`archive-runner-v1`](https://github.com/DeepMathLLM/Creative-Intelligence/tree/archive-runner-v1) branch.

## Moonshine Dependency

This is a Moonshine runtime extension, not a standalone application. Install, initialize, and configure Moonshine by following the [Moonshine repository](https://github.com/DeepMathLLM/Moonshine/tree/main).

Place this repository directly inside the initialized Moonshine runtime home, not inside the Moonshine source-code package:

```text
<MOONSHINE_HOME>/
└── Creative-Intelligence/
    ├── README.md
    ├── run_archive.py
    ├── archive-format-specification.md
    ├── tests/
    └── skills/
        ├── math-object-origin-archive/
        │   └── SKILL.md
        └── verify-math-object-origin-archive/
            └── SKILL.md
```

The runner treats the parent of `Creative-Intelligence` as `MOONSHINE_HOME` and automatically installs its two task-specific skills into that runtime when it starts.

Run all commands from the initialized Moonshine runtime home:

```bash
cd <MOONSHINE_HOME>
```

## Branch-Driven Discovery

This is the primary v2 workflow. Supply one or more mathematical branches, the number of verified archives to produce, and a stable run name:

```bash
python Creative-Intelligence/run_archive.py --branches "Differential Geometry" "Algebraic Topology" "Functional Analysis" --target-archives 10 --run-name graduate-math-v2 --stream-output
```

The runner repeatedly performs one complete object task:

1. Select a distinct object from the supplied branches.
2. Create its archive according to `archive-format-specification.md`.
3. Submit the archive to the verification tool.
4. Publish it only if verification passes.

Only successfully verified archives count toward `--target-archives`. Failed attempts remain in the run state and their names are treated as previously attempted objects.

### Resume a Discovery Run

Run the same command again with the same:

- `--run-name`;
- branches in the same order;
- `--target-archives` value.

These values define the identity of the run. Changing them while reusing the same run name is rejected to prevent an interrupted run from being resumed with different inputs.

To retry recorded verification failures before discovering additional objects, add:

```bash
--retry-failed
```

## Predefined JSON Queue

Use this mode when the mathematical objects have already been selected or local materials have been collected. Create a UTF-8 JSON file:

```json
{
  "format": "math-object-origin-archive-v1",
  "objects": [
    {
      "name": "Bochner formula",
      "materials": [
        "materials/bochner-notes.md"
      ]
    },
    {
      "name": "Riemann curvature tensor",
      "materials": []
    }
  ]
}
```

`materials` is optional and accepts local UTF-8 text or Markdown files. Relative paths are resolved from the directory containing the input JSON file. PDF, Word, and other binary files must first be converted to UTF-8 text or Markdown.

Process every object serially:

```bash
python Creative-Intelligence/run_archive.py path/to/concepts.json
```

Validate the input without creating runtime state:

```bash
python Creative-Intelligence/run_archive.py path/to/concepts.json --validate-only
```

Start at a specific 1-based index:

```bash
python Creative-Intelligence/run_archive.py path/to/concepts.json --start-index 5
```

Retry objects previously marked as failed:

```bash
python Creative-Intelligence/run_archive.py path/to/concepts.json --retry-failed
```

Useful options include:

- `--max-turns N`: set the maximum repair turns for queued or retried objects;
- `--verbose`: print Moonshine status events;
- `--stream-output`: show reasoning, text, tool summaries, and candidate archives in the terminal.

Run the same command again to resume. After a queue has started, do not modify its JSON file or referenced material files. Use a new JSON filename for a different queue.

## Verification and Publication

The runner exposes a session-bound verification tool that checks:

- mathematical correctness;
- accuracy and specificity of the mathematical context and formation;
- whether the archive identifies the concrete problem, obstacle, structural mechanism, and resulting change;
- compliance with the active format specification.

Accepted verifier output is bound to the expected project, session, and archive hash. The runner refuses to publish unverified content or overwrite a different existing archive.

Resumed sessions must also match the expected Moonshine mode, project, and agent identity. Local materials are bound to their resolved paths and SHA-256 hashes, so changed material cannot silently enter an existing run.

## Generated Files

These directories are created by the runner and are not part of the initial repository:

- Final Markdown archives: `Creative-Intelligence/archives/<run-name>/`
- Run state and project/session associations: `Creative-Intelligence/runs/<run-name>.state.json`

For JSON queue mode, `<run-name>` is derived from the input filename. Moonshine stores the associated projects and sessions in its own runtime directories.

## Tests

Run the deterministic offline regression suite from the repository root:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

These tests require no configured provider, credentials, network access, or live Moonshine session.

The separate integration suite exercises the real Moonshine runtime with deterministic provider substitutes:

```bash
python -m unittest -v tests.integration_run_archive_moonshine
```

It covers session persistence, skill and tool registration, material staging, verification-event storage, recovery, identity rejection, and archive publication. It does not evaluate live model quality, live provider availability, or web/MCP behavior.
