---
name: chey-skill-creator
description: Create or improve Chey's user-owned reusable skills from real tasks and observed failures, with concise instructions, runnable helpers where useful and explicit behavioral acceptance cases. Use for authoring a skill; use skill-tester for a read-only assessment of an existing skill.
---

# Create a user-owned skill

## When to use

Use for an actual skill addition or improvement grounded in a requested operation
or observed failure. Inspect existing skills first and prefer a narrow update
when one already owns the outcome. Use `skill-tester` directly for assessment.

## Inputs

Identify the requested inputs, outputs, effects and completion condition, selected
source location and governing instructions. Inspect the existing package and
invocation/dependency fields before an update. For new decision guidance, specify
observable success, a meaningful adverse/regression case and a nearby request
outside scope before drafting; keep assessor outcomes separate from raw fixtures.

## Procedure

1. Choose a distinct name and discriminating description, preserving the user's
   product and scope. Reserve a new package with an operation that refuses an
   existing destination. Update an existing package in place rather than
   reinitializing it or erasing unrelated resources and invocation policy.
2. Write only the non-obvious decisions, actual constraints and useful routing
   another capable agent needs. Keep the entrypoint short; route conditional
   detail to a referenced resource. Avoid scaffolding, duplicated controllers
   and instructions that merely say to be careful.
3. Add a deterministic helper when repeated mechanics justify it. Specify inputs,
   effects, dependencies and failure behavior; keep it inert on import. Research
   current official documentation and the selected version before adding
   platform/API behavior. A missing validator, empty surface or interrupted check
   must not become success. Treat candidate code as data until execution is
   explicitly selected and trusted.
4. Use available `skill-tester` guidance proportionately: validate structure and
   references, exercise changed trusted helpers on independently selected
   positive/adverse cases, and inspect task/authority boundaries. Wire maintained
   checks into the existing normal test command where useful. If that specialist
   is unavailable, perform the available concrete checks and report the missing
   lane; do not install a dependency or build a new evaluation service by default.
5. For complex decision changes, use a fresh evaluator when available and
   authorised. Supply the task, target skill and minimum raw artifacts, excluding
   suspected bugs and golden outcomes. Inspect actual artifacts/actions. Keep
   self-exercised checks distinct from fresh-agent evidence; retain failures and
   correct the smallest demonstrated weakness.
6. Keep one editable source. Honor the selected repository destination; otherwise
   default to a user-owned installation without modifying bundled/system skills.
   A consumer installation/refresh requires its applicable authority. After an
   authorised refresh, compare complete file lists and bytes against the source
   pin rather than treating deployed copies as separately maintained versions.

## Outputs

Deliver the actual skill and used resources, source/installed paths, exact checks
and outcomes, remaining limits and local/committed/pushed status. Preserve existing
name, metadata and invocation policy unless the request needs a change.

## Verification

Check observable behavior and meaningful invariants, not preferred wording.
Independent expectations must not be manufactured by the implementation. A
frontmatter/link pass is not behavioral qualification. Retain a regression at the
enforcing boundary for recurring failures; routine edits need no new framework.

## Stop

Stop after the requested package and proportionate verification. Do not infer
push, publishing, credentials, spending, deployment or unrelated project authority
from skill creation. Preserve user work and report blocked or unrun lanes.
