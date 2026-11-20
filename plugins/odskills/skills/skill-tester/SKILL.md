---
name: skill-tester
description: Test a selected skill against realistic tasks, negative controls, scope boundaries and observable artifacts. Use for skill evaluation, regression checks or a read-only review; distinguish static validity, helper behavior and fresh-agent behavior. Do not redesign or execute an untrusted skill's scripts without the selected authority.
---

# Test a skill

## When to use

Use for a selected skill's evaluation, regression checks or read-only review.
`chey-skill-creator` owns authoring; assessment does not automatically authorise
repairs or execution of candidate scripts.

## Inputs

Read the actual skill, used resources and governing instructions. Bind its
version or relevant dirty bytes, requested outcome and selected lane: read-only
review, trusted helper testing or authorised fresh-agent trial. Use the
[case template](assets/test-case.md) for retained cases. Select expected outcomes
before execution, separately from implementation; include success and adverse
controls, plus a nearby non-trigger when routing is assessed.

## Procedure

1. Run the bundled static checker in an existing environment with the pinned
   [requirements](requirements.txt), or install them only in an authorised
   selected development environment:

   ```sh
   python /path/to/skill-tester/scripts/check_skill.py --json /path/to/selected-skill
   ```

   This reads required frontmatter, field types, duplicate keys, name/folder
   consistency and a nonempty body, recording the entrypoint hash. It never
   imports or executes target code. Its scope is entrypoint structure only;
   `behavior: NOT_RUN` remains explicit, and other resources are not all hashed.
2. Inspect referenced resources/commands. Use available `link-management` with an
   explicit root enclosing the selected surface for paths and anchors; otherwise
   inspect available references and disclose the missing automated lane. Preserve
   frozen sources, user edits and one editable authority. A link pass does not
   establish that a command or dependency works.
3. For helper behavior, inspect and explicitly select the trusted helper first.
   Run its actual public entrypoint on owned disposable positive/adverse fixtures.
   Check artifacts and unauthorised changes as well as status. An always-passing
   or always-rejecting tool, empty input, skipped dependency or fabricated receipt
   cannot qualify acceptance. Reuse relevant existing tests/normal checks.
4. For instruction/routing behavior, use a fresh evaluator only when available
   and authorised. Supply the task, skill and minimum raw artifacts, keeping the
   expected result and suspected failure with the assessor. Observe actual
   artifacts/actions; a claim of following the skill is insufficient. If this
   lane is unavailable, report NOT_RUN and complete the other selected checks.
5. Preserve failures until diagnosed. Return the smallest supported correction
   or regression recommendation; apply it only when the assignment includes
   repairs. Do not create a generic evaluation framework for a narrow check.

## Outputs

Report findings first with concrete locations, then separate structure/references,
trusted helper behavior and fresh-agent behavior. Record input/source identities,
commands, actual outcomes, independence and limitations. Missing evidence stays
unavailable or NOT_RUN; do not combine lanes into a confidence percentage.

## Verification

Use independently selected expected results and known-wrong controls. Verify that
required cases ran and that a failed required case remains failed. Static/helper
checks and self-review do not establish fresh-agent behavior or universal coverage.

## Stop

Stop at the selected evidence/recommendation. No untrusted target execution,
provider call, remote submission, credential access, deployment, publication or
spending follows from testing. Preserve the reviewed artifact unless repairs
were requested.
