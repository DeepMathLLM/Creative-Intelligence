---
name: verify-math-object-origin-archive
description: Verify a complete mathematical-object origin archive for mathematical correctness, a concrete motivating problem, the exact difficulty addressed, content accuracy, and compliance with the runner-defined format. Use as the acceptance gate for origin archives, not for proof-only verification.
compatibility: Requires the verify_math_object_origin_archive tool dynamically registered by the origin-archive runner.
metadata:
  title: Verify Mathematical Object Origin Archive
  category: verification
  tags: mathematics, concepts, archive, verification
  skill-standard: agentskills.io/v1
---

# Verify Mathematical Object Origin Archive

## Summary

- Apply one fail-closed acceptance gate across mathematical accuracy, the motivating problem and difficulty addressed, the object's essential role, content accuracy, and format compliance.
- Accept the archive only when the verification tool returns `passed=true`.

## Execution Steps

1. Assemble the complete candidate archive.
2. Call `verify_math_object_origin_archive` with the complete archive and, when requested by the tool, the selected object's canonical name and supplied branch.
3. Require Mathematical Context and Formation to identify a concrete mathematical problem or well-defined problem class, locate the exact mathematical difficulty, explain why available concepts or methods were inadequate, and connect the relevant insight to the object's formation. Reject disconnected facts or a historical story.
4. Require Essential Role to state which part of the problem became tractable, which difficulties were overcome, bypassed, or reformulated, and how specific features of the object's definition or structure produced that change. Reject generic claims of importance, broad lists of applications, or later uses presented as the original role.
5. Reject an archive that remains at the level of broad conclusions or evaluative language without enough concrete mathematical detail to identify the problem, the obstacle, the relevant structural mechanism, and the resulting change. General claims must be explained rather than merely asserted.
6. Judge the accuracy of the archive's mathematical, contextual, and interpretive claims directly. Require no material error and compliance with the format specification supplied by the runner; citations or a separate evidence note are not acceptance requirements.
7. If any dimension fails or is inconclusive, revise the affected content and submit the complete archive again. If verification passes, end with only `ARCHIVE_COMPLETE`; otherwise, end with one short line reporting the current task status.

## Tool Calls

- `verify_math_object_origin_archive`: Run the mathematical, content-accuracy, and format checks and return the acceptance result.
- `read_runtime_file`: Recheck the format requirements or supplied materials when resolving an issue.

## File References

- `math-object-origin-archive/archive-format-specification.md`: Canonical format source used by the runner and format reviewer.

## Output Contract

- Only `passed=true` represents an accepted archive; a failing result must retain its repair targets.

## Notes

- Any change to the archive invalidates the earlier accepted text and requires verification of the complete revised version.
