---
name: select-code-tests
description: Select proportionate unit, integration, CLI, installed-package and end-to-end verification for a concrete software change, distinguishing iteration checks from acceptance gates. Use when asked what to test or whether checks are sufficient; not for writing one already-specified test, mathematical proof verification or deployment.
---

# Select sufficient code tests

## When to use

Use to select or assess evidence for a particular software change or public-behaviour claim. Start from the consuming project's actual contracts and validation runbook; do not replace its gates. A narrow unit-test-writing request does not require this planning skill. A mathematical theorem, clinical inference or release decision needs its own evidence.

## Inputs

For external contributions with unsettled receiving requirements, use
`read-contribution-requirements` before choosing checks. Use a current intake to
bind each check to its stage and owner.

Identify the exact change and immutable revision or working state; public interfaces and consumers; risk and supported environments; existing tests and independent expected outcomes; permitted effects, test cost and required project gates. Distinguish local iteration from a candidate acceptance or release check. If the source or target is unavailable, report the missing evidence instead of inventing a check result.

## Procedure

1. Trace the actual changed behaviour and its dependencies, including callers, storage/wire contracts, installation and failure paths. For a change-to-test map, inspect the maintained map and its fallback rather than guessing coverage from filenames.
2. Select the **smallest discriminating tests**: pure logic and edge cases at unit level; real interactions at integration level; subprocess/exit status/stdout/stderr for CLIs; whole user workflow or installed artifact for end-to-end claims. For examples and escalation choices, read [test boundaries](references/test-boundaries.md).
3. Use independent expected results, counterexamples, reconstruction identities or controlled negative paths where applicable. Do not use the implementation under test as its only oracle.
4. Separate focused iteration diagnostics from the project's required exact-head, full, platform or release qualification. Preserve tests with nonzero collection and disclose inherited filters, skips, unexecuted lanes and unavailable environments.
5. If a suite is slow, first inspect measured costs and simpler selection/slow-lane options; when actual sharding is proposed, read [long-running and shard controls](references/long-running-tests.md). Do not treat a test-ID shard as mathematical source coverage.
6. Run only tests permitted by the task and available tools. Retain original failure logs and independently observable outputs; do not automatically install dependencies, launch remote jobs, mutate evidence, merge or release.
7. Return the chosen evidence and its scope, missing checks, negative outcomes and exact handoff. Stop after the requested test strategy or authorised verification.

## Outputs

Return the affected contract, test-level rationale, selected commands or planned checks, independent oracles, expected adverse cases, actual result counts and identities when executed, untested boundaries and what the results do **not** establish. Distinguish NOT_RUN, BLOCKED and FAIL from PASS.

## Verification

For a real execution, inspect command, environment, revision, nonzero selected collection, success/failure/skip counts and genuine public-path observations. Mocks establish controlled calling behaviour, not external-provider guarantees. A green suite does not prove mathematical truth, statistical validity or permission to merge. Compare any selected reduced suite with its project-required fallback.

## Stop

Do not run broad or expensive checks merely because they appear in this skill. Missing prerequisites block only dependent checks. Never claim broader coverage from an empty selection, an unaccounted filter, missing required shards or skipped required gates. A deliberately focused selection can complete a task whose requested scope is itself focused. Preserve the consuming project's authority and stop at the approved deliverable.
