---
name: math-object-origin-archive
description: Select when needed and generate an origin archive for one mathematical concept or object that arose in response to a concrete mathematical problem. Use when the deliverable must follow the archive format supplied by the runner; do not use for ordinary definitions or proof-only tasks.
compatibility: Works with Moonshine runtimes that provide local file reading and skill loading.
metadata:
  title: Mathematical Object Origin Archive
  category: research
  tags: mathematics, concepts, archive
  skill-standard: agentskills.io/v1
---

# Mathematical Object Origin Archive

## Summary

- Select one suitable target when mathematical branches are supplied, then produce one professional Markdown archive that follows the active format requirements.

## Execution Steps

1. Use a named target when one is supplied. When a candidate pool is supplied, choose only a suitable object from that pool; otherwise choose from the supplied branches. Never select a previously attempted object or an evident alias of one. The object must have a stable mathematical identity and must have arisen as a direct response to a concrete mathematical problem rather than merely acquiring a later application. Keep this selection internal and continue directly with the archive.
2. Use live search only when necessary to resolve an uncertainty that materially affects object selection or archive accuracy; avoid broad or repeated searches.
3. Read the active format requirements and the materials supplied in the task context.
4. In Mathematical Context and Formation, identify the concrete mathematical problem or well-defined problem class that motivated the object. Explain exactly where the difficulty lay, why the available concepts or methods were inadequate, and which ideas or insights led to the object's formation. Connect these points through their mathematical logic rather than listing facts, and keep the account about mathematical meaning rather than a historical story.
5. In Essential Role, explain precisely which part of the problem became tractable, which difficulties were overcome, bypassed, or reformulated, and how specific features of the object's definition or structure produced that change. Distinguish this direct contribution from generic importance or later applications, and include any deeper understanding or structural viewpoint the object introduced.
6. Draft the archive according to the active format specification. Distinguish established mathematical facts from interpretation, and qualify incomplete or disputed claims. If the archive refers to any material, list it in Sources.
7. Load `$verify-math-object-origin-archive` and submit the complete draft together with the selected object name and branch when requested by the verification tool.

## Tool Calls

- `read_runtime_file`: Read the format specification and all supplied local materials.
- `load_skill_definition` and `verify_math_object_origin_archive`: Load the verification skill and submit the complete archive.

## File References

- `math-object-origin-archive/archive-format-specification.md`: Canonical archive format and writing requirements.

## Output Contract

- Submit one complete Markdown archive for verification. If verification passes, end with only `ARCHIVE_COMPLETE`; otherwise, end with one short line reporting the current task status.
- If selection is required but no suitable distinct object can be identified, return only `ARCHIVE_DISCOVERY_STOP: {"reason":"Brief reason"}`.
