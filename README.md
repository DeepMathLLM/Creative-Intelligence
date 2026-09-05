# Creative-Intelligence

This project explores mathematical creativity in AI—whether it can move beyond solving existing problems to originate new ideas and expand the frontiers of mathematics alongside humans.

## Current Focus

1. **Tracing the Origins of Mathematical Concepts**
   Study how important mathematical concepts emerged, including their historical context, the problems they addressed, the limitations they overcame, and their influence on mathematics and related fields.

2. **Exploring Mathematical Creativity in AI**
   Use frontier AI models to investigate whether they can move beyond solving existing problems and demonstrate genuine mathematical creativity, including the ability to generate new concepts, perspectives, and approaches.

## Mathematical Object Origin Archive Runner

This runner supports the first research direction by generating and verifying origin archives for mathematical concepts and objects. It processes an ordered collection serially, gives each object its own Moonshine project and session, and writes the final Markdown archive only after verification passes.

## Moonshine dependency

This is a Moonshine runtime extension, not a standalone application. Install, initialize, and configure Moonshine by following the [Moonshine repository](https://github.com/DeepMathLLM/Moonshine/tree/main).

Place this repository directly inside the initialized Moonshine runtime home, not inside the Moonshine source-code package. With the default Moonshine setup, the runtime home is `~/.moonshine`. If Moonshine was initialized with `--home`, use that directory instead.

```text
<MOONSHINE_HOME>/
├── config.yaml
├── config/
├── projects/                              # Moonshine projects created for individual objects
├── sessions/                              # Moonshine session records
├── skills/
│   └── installed/                         # Runtime copies installed automatically by the runner
└── Creative-Intelligence/                 # This GitHub repository
    ├── README.md
    ├── run_archive.py
    ├── archive-format-specification.md
    ├── tests/
    │   └── test_run_archive_offline.py
    ├── skills/
    │   ├── math-object-origin-archive/
    │   │   └── SKILL.md
    │   └── verify-math-object-origin-archive/
    │       └── SKILL.md
```

`config.yaml` and the other runtime directories are created by `python -m moonshine init`. The runner treats its parent directory as `MOONSHINE_HOME` and automatically installs the two included skills into that runtime when it starts.

## Input

Create a UTF-8 JSON file containing an ordered list of objects. The JSON file may be stored anywhere:

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

`materials` is optional and accepts local UTF-8 text or Markdown files. Relative material paths are resolved from the directory containing the input JSON file, not from the repository or runtime home.

## Run

Run commands from the initialized Moonshine runtime home. Replace `<MOONSHINE_HOME>` with the runtime directory used during Moonshine initialization:

```bash
cd <MOONSHINE_HOME>
```

This must be the same directory previously passed to `python -m moonshine --home <MOONSHINE_HOME> init`, or the runtime directory created by the default initialization.

Process every object serially:

```bash
python Creative-Intelligence/run_archive.py path/to/concepts.json
```

Optionally validate the input without starting Moonshine sessions:

```bash
python Creative-Intelligence/run_archive.py path/to/concepts.json --validate-only
```

Start from a specific 1-based index:

```bash
python Creative-Intelligence/run_archive.py path/to/concepts.json --start-index 5
```

Retry objects previously marked as failed:

```bash
python Creative-Intelligence/run_archive.py path/to/concepts.json --retry-failed
```

Optional flags include `--max-turns N` and `--verbose`. Run the same command again to resume the saved Moonshine sessions. After a run has started, keep its input JSON unchanged; use a new, uniquely named JSON file for another queue.

## Generated files

The following directories are created automatically when the runner is used and are not part of the initial repository structure:

- Final archives: `Creative-Intelligence/archives/<input-name>/`
- Queue state and project/session associations: `Creative-Intelligence/runs/<input-name>.state.json`

## Offline regression tests

The deterministic runner contracts can be tested from a standalone checkout without an initialized Moonshine runtime, provider credentials, network access, or model calls. The test harness uses only the Python standard library and provides import-time stubs for the narrow Moonshine symbols required to load `run_archive.py`.

Run from the `Creative-Intelligence` repository root:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

These tests cover runner-owned deterministic behavior such as queue validation, immutable queue state, format-placeholder checks, verifier-output integrity, archive overwrite protection, and provider preflight logic. They do **not** simulate Moonshine agent execution, session storage, MCP tools, or real verification-provider behavior; those remain runtime integration concerns.

## Reference verification

`tools/verify_references.py` adds a deterministic layer underneath the model-based acceptance gate: it checks every numbered source in an archive's `Sources` section before any model review is involved. The goal is to catch fabricated or miscopied references — the failure mode a model reviewer cannot reliably detect, because a hallucinated citation still *looks* plausible.

Checks performed, per archive:

- **Structure (offline):** contiguous `[n]` numbering, and every in-text citation `[n]` resolving to a listed source (uncited entries are warnings, not failures).
- **Existence:** each source is resolved against external bibliographic indexes — Crossref (by DOI or scored bibliographic query), OpenAlex, zbMATH Open, the Internet Archive, and Open Library. A confident match requires title similarity **and** surname overlap **and** a publication year within ±2, so a real paper with fabricated authors (or vice versa) does not pass. zbMATH Open and the Internet Archive extend coverage to the 19th-century literature that origin archives frequently cite.
- **Link liveness:** DOIs and URLs must resolve (warnings by default; `--strict` escalates).
- **Consistency:** bibliographic details claimed in the entry (year, volume, pages) are compared with the matched records. Claims contradicted by every matched record are failures; disagreement between the indexes themselves (e.g., first-page variants) is reported as a warning.

The tool is deterministic and offline-testable: all network access goes through a JSON cache (`--cache-file`, default `.reference-cache.json`), and `--offline` restricts it to that cache, which is how the regression tests in `tests/test_verify_references.py` run — their fixtures are recorded responses from the five indexes.

```bash
python tools/verify_references.py path/to/archive.md            # human-readable report
python tools/verify_references.py path/to/archive.md --json     # machine-readable report
python tools/verify_references.py a.md b.md --offline           # CI-friendly, cache-only
```

Exit codes: `0` = all sources verified, `1` = at least one failure, `2` = usage or file error.

The tool never judges whether a source *supports* a historical claim — claim-level support remains the responsibility of the model review in `verify_math_object_origin_archive`.
