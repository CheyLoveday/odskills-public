---
name: review-code-change
description: Review an actual code change against its intended behavior for correctness, regressions, failure paths and discriminating tests, returning evidence-backed findings. Use for a separate review pass on a diff or snapshot; not an implementation summary, automatic repair, dedicated security audit or mathematical proof review.
---

# Review an actual code change

## When to use

Use when asked to assess a concrete implementation change. A review can be a
separate reasoning pass by the same developer; it need not require a PR, team,
second model or immutable clean checkout. Do not call a second pass independent
unless its context actually supports that claim. No findings is a valid outcome.

## Inputs

Identify the actual reviewed snapshot or working-state diff, comparison basis,
requested behavior and non-goals, governing project instructions, public callers
and relevant verification evidence. Record dirty files in scope rather than
discarding or committing them. Without a base or source, state which comparison
cannot be made and review only the available material.

## Procedure

1. Read the actual diff and enough surrounding code, callers and tests to
   reconstruct the contract. Use the implementer's summary as context, not as
   the review oracle. Locate the consumer that makes each changed value or
   failure observable.
2. Follow changed behavior across its real boundaries. Select the relevant risks:
   compatibility, state/cache identity, resource ownership and early exit,
   partial writes, overwrite/retry behavior, validation and error propagation,
   packaging or numeric conversion. Keep optional improvements distinct from
   contract violations; a new abstraction or stricter rule is not inherently a fix.
3. For numeric/scientific changes inspect applicable domains, units, endpoint
   conventions, intermediate bounds, conditioning and claimed accuracy. A
   passing software test does not establish the mathematical/statistical
   conclusion drawn from the result. Limit such claims to inspected evidence.
4. Challenge important assertions with a small concrete failure route. Reuse
   independently justified expected results and safe disposable probes when
   authorised. Inspect whether tests reach production code and reject the
   plausible defect, rather than only a mock or copied replacement. Prefer a
   targeted counterexample to a catalogue of hypothetical concerns.
5. Inspect relevant checks, counts, skips and environment/source identities.
   Run permitted focused checks if useful; otherwise mark them NOT_RUN. Historical
   results apply only to their recorded snapshot and conditions. A new change
   requires rechecking dependent findings, while unrelated evidence can remain.
6. Return actionable findings first, ordered by consequence. For each give a
   precise location, triggering condition, observed or reasoned mechanism,
   affected behavior and a discriminating reproduction/check. Separate confirmed
   defects, evidence-backed concerns, unresolved questions and preferences. If
   none are supported, say so and state coverage limits without inventing work.

## Outputs

A review bound to its actual snapshot and contract: findings and their evidence,
checks performed, missing evidence and the smallest necessary repair suggestions.
Use a project-required verdict if one exists; do not create a new approval process.
Keep the implementer's checks distinct from checks performed during this review.

## Verification

Verify locations and inspect each proposed failure against a legitimate positive
case and the intended contract. A plausible exploit or race outside the selected
contract can be reported as a scoped concern, not a demonstrated regression.
Reviewing tests is distinct from executing them, and passing tests do not erase
a demonstrated defect. Report review independence and unexercised environments.

## Stop

Review is read-only on the artifact unless repairs were also requested. Use
disposable outputs for probes and preserve unrelated work. Loading this skill
does not grant merge, installation, publication, spend or consumer authority.
Stop after the selected review; do not automatically start repairs or chain other
skills. A specialist can be used directly when only its narrower outcome is needed.
