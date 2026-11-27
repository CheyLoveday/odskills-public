---
name: read-contribution-requirements
description: Read a receiving repository's rules before starting an external contribution. Use to check the claim or overlap, submission route and scope, assign checks to stages and owners, and choose the smallest verification run that meets the current requirement. Use existing intake evidence when the rules are already settled.
---

# Read the receiving repository’s contribution requirements

## When to use

Start with the [contribution requirements intake](assets/contribution-requirements.md)
before planning work or choosing verification for an outside repository. Use an existing
intake if its base, route, scope and live observations still apply. For a settled
intake, select planning, test selection, diff review, proof work or handover directly as
needed.

## Inputs

Identify the receiving repository, proposed target and contribution route, requested
result, and current user authorization. Use a receiving-project intake template when it
captures these requirements. Keep a small change to a short record.

## Procedure

1. Pin the receiving branch and full base commit. Read the applicable root and
   path-level instructions, contributor guide, task and maintainer instructions,
   relevant PR template, workflows and invoked scripts, and build configuration and
   dependency pins. Check CI triggers, paths and targets before treating a job as
   evidence. Record exact source locations and revisions. Date live observations and
   mark inaccessible sources or unresolved conflicts.
2. Check the route, claim rules and overlap in the relevant issue or board and open
   contributions. Record current ownership or the limits of the search, prescribed claim
   wording and venue, exact requested behavior or theorem type, and accepted paths and
   PR target. Reuse a valid claim. Record any required external action and proceed only
   within the user's authorization.
3. Record each actionable requirement with its source, force and trigger, stage, owner,
   pass evidence and current status. Keep intake, the first check, submission, CI and
   maintainer acceptance distinct where the repository does. If requirements appear to
   conflict, identify which decision depends on resolving them and continue independent
   work.
4. Choose the smallest check that produces the evidence due now. Specify requirement
   IDs, exact files, declarations or entry points, pinned inputs, toolchain, allowed
   runner and cache prerequisites, and the evidence to retain. Choose the runner after
   establishing the evidence. Keep conditional or later gates visible with their
   triggers and owners. For Lean, distinguish a focused module build, exact statement
   and axiom checks, and any project-wide discharge or integration report. Derive their
   timing from the receiving route. Keep the repository’s recorded due stage even when
   the user asks for an earlier diagnostic. Check whether the later gate can reuse that
   evidence.
5. Record the next permitted action. Recheck affected rows before submission if the
   base, changed paths, claim, workflow or route has changed. Pass requirement IDs and
   evidence due at the current stage to any plan, check request or handover.

## Outputs

Return the completed intake or its concise equivalent, including the first check, later
gates and any blocker that changes the next action.

## Verification

Trace each obligation to its source and confirm the proposed check covers the exact
target at the stated stage. Preserve distinctions among met, unrun, blocked, unknown and
inapplicable. Confirm ownership and authorization separately for each external action.

## Stop

Stop at the intake when that is the requested deliverable. A contribution rule can
require a claim, upload, run, push or PR. Carry it forward as pending until the
necessary user authorization is available.
