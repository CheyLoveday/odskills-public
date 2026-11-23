---
name: audit-computational-evidence
description: Audit whether an exact computation or finite certificate supports its stated mathematical claim, checking specification, coverage, independent controls, replay and provenance. Use for mathematical evidence review, not generic test selection, performance tuning or treating a successful run as proof of a broader theorem.
---

# Audit computational mathematical evidence

## When to use

Use for exact experiments, sieves, enumerations, certificates or computation-to-
theorem bridges. A source-only review or replay plan is valid when execution is
unavailable. A narrow ordinary software test or benchmark needs its own workflow.

## Inputs

Identify the exact target/revision, mathematical reduction, domain/bounds,
inputs, implementation, checker and reported output; versions, hashes and
existing logs when available; allowed effects, budget and requested outcome.
Inspect supplied project runbooks and sources without importing another
project's directories, lifecycle gates or acceptance authority.

## Procedure

1. Derive the predicate actually needed from the mathematical statement. Compare
   it independently with the implemented predicate, source comments and report.
   Decide whether a test is necessary, sufficient or equivalent; record the
   proof or remaining obligation for that relation.
2. Map the claimed domain to actual coverage: endpoints, signs, exceptional
   cases, input classes, partitions, stopping rules and skipped/failed work.
   A larger bound or general theorem needs its own reduction, not extrapolation
   from an observed count. For periodic exclusions, symmetry reductions,
   delicate filters or numeric contracts read
   [predicate and coverage checks](references/predicate-and-coverage.md).
3. Inspect provenance and actual completion separately from mathematical scope.
   Match source/input/checker identities, versions, commands, outputs, return
   codes and logs. A supplied historical receipt is not a fresh execution.
   Missing or incompatible evidence remains unverified for the dependent claim.
4. When permitted, replay the selected public entrypoint on controlled disposable
   inputs. Challenge the checker with known valid and invalid results, boundary
   examples and a deliberately wrong implementation/certificate. Use independent
   literal results, distinct algorithms or justified invariants; agreeing copies
   of the same bug are not independent verification.
5. For a suspected local arithmetic or implementation defect, reproduce the
   smallest case and compare it directly with the defining equation. Report
   which layer failed. Correct only authorized artifacts; retain original
   diagnostics and recheck affected downstream outputs after a repair.
6. Return the exact claim the evidence supports, failed or missing obligations,
   and the smallest next check. Separate algorithm validity, implementation
   correctness, completed finite coverage, provenance and mathematical conclusion.

## Outputs

Return target/artifact identities, predicate/reduction map, coverage and
completion assessment, controls and actual results, layer-specific findings,
scoped verdict and unresolved obligations. A certificate audit recommends a
result; it does not admit a theorem or change canonical project status.

## Verification

Ensure an invalid result is rejected and a legitimate valid alternative is
accepted. Preserve nonzero/error/timeout status and missing results; an empty
selection is not successful coverage. Use exact arithmetic where required and
check precision, integer narrowing and intermediate bounds for optimized paths.
Do not describe model arithmetic, fixture checks or stored logs as a new real
tool/platform execution. A correct bounded computation can remain insufficient
for a universal theorem.

## Stop

Stop at the selected audit/repair and budget. Fail the dependent evidence claim
on a demonstrated checker/replay/coverage defect; unavailable evidence is
incomplete rather than a refutation of the mathematical theorem. Do not run
untrusted code without appropriate isolation, change runtimes, install tools,
spend remotely or overwrite historical evidence implicitly.
