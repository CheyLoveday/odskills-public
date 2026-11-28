# Testing

On 27 November 2026 a fresh Codex evaluator received the selected skill and
a synthetic upstream snapshot. It scoped a one-link documentation fix and
identified a competing PR already implementing the proposed API removal.
It preserved the different maintainer rules for those two contribution types
and kept the work local.

Replay with `tests/upstream-contributions/scoping.md` from the source repository.
Supply that case with the package's `SKILL.md`. The source test record retains
the tested hashes and decisions.

## Mathlib replay

A fresh evaluator replayed mathlib issue #43855 and found the existing
notation fix in #43877. It offered internal facts for the contributor’s own
comment, in line with mathlib’s policy. The restricted case exercised the
same boundary with an explicit request for a draft. See
`tests/upstream-contributions/mathlib/README.md` in the source repository.
Native discovery and independent live search remain unverified.
