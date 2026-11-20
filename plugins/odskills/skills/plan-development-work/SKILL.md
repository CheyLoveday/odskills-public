---
name: plan-development-work
description: Turn a development objective into scoped tasks, dependency-ordered waves, acceptance checks and requested PR or review briefs. Use for actionable development planning or evidence-backed closeout writing; not for implementing the change, reviewing an actual diff or preparing a current-state handover alone.
---

# Plan bounded development work

## When to use

Use to organise an actual development outcome or write its task, wave, PR or
review contract. A small change may need one task and a short PR; do not expand
it into a programme. Select `review-code-change` directly for an actual review,
or `prepare-development-handover` for resuming work from its current state.

## Inputs

Identify the requested outcome/documents, existing issue/plan and acceptance
requirements, current source or supplied snapshot, relevant interfaces/callers,
project instructions, preserved work and permissions already granted. Read
primary artifacts before repeating a summary. Missing essential source makes
its implementation/test details conditional, not invented. Ask only for inputs
that block the requested outcome; retain useful independent planning work.
Treat an existing request/issue document as context: a broader or older brief
does not expand the current user's requested outputs. Resolve that scope before
choosing assets, even when the document itself asks for additional deliverables.

## Procedure

1. State the observable result, scope and exclusions. Search existing owners,
   tasks and implementation before proposing new work. Distinguish an observed
   defect, missing evidence and a proposed improvement. Keep project-specific
   tools, release gates, budgets and mathematical claims in the project context;
   another project's template or historical approval supplies none of them.
2. Split work by deliverable and real dependency. For each task record inputs,
   owned paths/interface, expected output, acceptance and stop condition using
   the [task template](assets/task.md) when a task brief is requested. Give a
   prerequisite only when its result is needed; reject cycles, missing producers
   and duplicated ownership. Already valid inputs can satisfy a dependency.
3. For a multi-task plan load the [wave template](assets/waves.md). Group ready
   tasks into small useful increments with explicit exits. Separate discovery,
   a discriminating check, implementation and integration when uncertainty
   warrants it; combine them for simple work. Parallel work needs compatible
   inputs and disjoint writes. This describes opportunities, not an instruction
   to spawn agents, create worktrees or invent a scheduler. Do not require fixed
   W0–W6 stages, a benchmark, external deployment or independent review everywhere.
4. Choose checks that demonstrate the required behaviour and reject a plausible
   failure while preserving a legitimate positive case. Include the actual
   public/caller boundary when it matters. Use `select-code-tests` only when
   verification choice needs that specialist; existing valid checks suffice.
   Name planned commands and unknown environments honestly. Planning is not
   test execution; absent or skipped required evidence cannot count as PASS.
5. For a PR draft load only the [PR template](assets/pr.md) and relevant evidence.
   Lead with problem and resulting behaviour, then requirements addressed,
   actual checks and material limits. A planning-only PR describes documents,
   not implemented capability. Distinguish observed results from future gates;
   refresh changed evidence bindings rather than carrying an old sign-off.
6. For a review request/receipt load the [review template](assets/review.md).
   Bind its contract and actual snapshot, highlight relevant failure questions,
   and separate author reports from reviewer checks. `review-code-change` owns
   the actual review procedure. A prepared brief is NOT_RUN, not approval;
   same-author second pass is not automatically independent. An existing review
   can be linked without rerunning it if its source and scope still apply.
7. Check that the requested artifacts agree on task IDs, dependency direction,
   requirements, source state and outstanding gates. Preserve old evidence;
   use a fresh output or an explicitly selected document update, never overwrite
   a template or unrelated brief. Return Markdown unless another form is asked.
   Load only assets needed for the current outputs; do not append unrequested
   PRs, review briefs or other deliverables inside a requested task/wave document.

## Outputs

Only the requested actionable documents, scaled to the change: clear outcomes,
acyclic dependencies, appropriate tests, status/evidence and next permitted step.
Templates are optional writing aids, not validators, issue creators or new
project policy. Related skill IDs identify optional workflows, not prerequisites
or proof that a skill is installed. Source links in templates are navigation.

## Verification

Walk each dependency backwards to an available input or an explicitly open task;
check each acceptance condition against a concrete observable and adverse case.
A different valid task grouping is acceptable. Inspect the actual diff/evidence
before claiming implementation, testing, review, merge or release. Keep unknown,
blocked, unrun and not-applicable distinct; explain an inapplicable required gate.

## Stop

Stop at the requested planning/closeout documents. Do not implement, run proposed
checks, create remote issues/PRs, merge, deploy or spend merely because the plan
contains those steps. Reuse existing authority without requesting it again.
If work is being transferred, pass these documents and current primary evidence
to `prepare-development-handover`; writing a plan does not require a handover.
