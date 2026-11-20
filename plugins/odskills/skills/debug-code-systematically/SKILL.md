---
name: debug-code-systematically
description: Diagnose unclear, recurring or cross-component software failures through reproductions and discriminating checks, then verify a bounded repair. Use when a cause is uncertain or an attempted repair failed; not for every understood typo, expected negative test, performance study or mathematical proof gap.
---

# Diagnose and repair a software failure

## When to use

Use when an observed failure needs investigation rather than an already
understood local correction. Session-wide failure capture can exist independently
of this skill; starting an investigation does not require a new logging system.
An observed mismatch may come from code, a test, a fixture, an environment or an
ambiguous contract. Do not decide the faulty layer from the error category alone.

## Inputs

Collect the triggering action and relevant sanitized diagnostic, expected versus
actual behavior, affected revision/working state, public entrypoint, inputs and
environment needed to reproduce, recent changes and previous attempts. Reuse the
existing session record/logs. Avoid unrestricted environment, private data or
credential dumps. Identify which local checks and repairs are authorised.

## Procedure

1. Preserve the original observation and failure status before changing inputs
   or code. Establish the intended contract from callers, documentation and
   tests; a green suite or a colleague's explanation does not settle it. If an
   essential requirement is unresolved, separate that question from facts you
   can already test.
2. Reproduce through the real failing entrypoint when feasible. Reduce the case
   while retaining the triggering state, order, data shape and boundary behavior.
   For intermittent failures, record conditions and frequencies rather than
   repeatedly rerunning until a success replaces the failure.
3. Form plausible competing explanations, including an invalid oracle or missing
   prerequisite when relevant. Choose a cheap observation that distinguishes
   them: compare working/failing inputs, inspect a boundary value before and after
   conversion, bypass one layer in a disposable probe, or use a known valid and
   known invalid control. Trace where the first relevant divergence occurs.
4. Change one causal factor where practical; retain what the check rules out and
   what remains suspected. Instrument only the necessary boundary and sanitize
   observations. Consult the current official documentation/source for an
   uncertain runtime or service contract before changing its behavior. A timeout
   without timing evidence is not proof of its cause.
5. Once evidence supports a bounded repair, implement it at the responsible
   boundary if authorised. Preserve unaffected behavior and failure semantics.
   A mitigation can be appropriate when the cause remains uncertain, but label
   it as such. Do not swallow failures, invent default success, or add retries
   unless repeat safety and the retryable condition are established.
   When changing cache/state identity, revisit retained-state growth and lifetime:
   a more complete key can turn a previously bounded key space into unbounded
   retention. Preserve an applicable capacity bound or make the unresolved
   capacity decision explicit.
6. Verify the original reproduction and affected neighboring cases through the
   public path. Add regression protection where useful and confirm it rejects
   the demonstrated old/wrong behavior. Keep expected negative-test failures
   distinguishable from unexpected failures. If the repair fails, revise the
   explanation using that evidence instead of stacking speculative patches.
   For exact numeric work, check public representation separately from arithmetic:
   small valid inputs can produce much larger integer outputs. Declare unsupported
   resource/serialization limits rather than claiming all valid inputs succeed;
   avoid process-global relaxations to accommodate one output path.
7. Return the observation, supported cause or remaining uncertainty, repair or
   mitigation, actual verification and unresolved failures. Promote only a
   reusable mechanism or check; not every incident needs a permanent entry.

## Outputs

A bounded diagnosis/repair with the reproducing action, relevant evidence,
causal status, alternatives ruled out, affected files, genuine check outcomes
and residual limitations. A diagnosis-only request yields findings and a repair
recommendation; it does not authorise source changes.

## Verification

Retest the original condition, a legitimate positive case and a nearby adverse
case. Check returned status and actual output as well as diagnostic text. A mock
or local substitute does not establish provider compatibility. If reproducing
is blocked, report what was inspected and the smallest missing observation;
do not claim a verified cause or fix from an unexecuted hypothesis.

## Stop

Stop when the selected failure is explained and the authorised repair is verified,
or when necessary evidence/effects are unavailable. Preserve blocked evidence and
continue independent checks. Do not impose a fixed retry count, force an
architecture rewrite after several failures, or broaden a local repair into a
cleanup, deployment or credential change.
