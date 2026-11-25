---
name: reframe-mathematical-bottleneck
description: Compare mathematical representations when a proof stalls on a weak quantitative bound, a singular chart, or an overstrong regularity requirement. Return a source-preserving choice with the net downstream bound and first remaining obligation. Use for a concrete proof bottleneck. Routine algebra, independent proof audit, and invariant discovery without a bound comparison have their own workflows.
---

# Reframe a mathematical bottleneck

## When to use

A coordinate, cover, lift, or counting representation is the first reason
a specified proof cannot attain its target. A decision to retain the
current representation is a complete outcome when its existing estimates
suffice or an alternative fails to improve the bound.

## Inputs

Read the exact source population and hypotheses, the current derivation, the
first failing condition, the downstream inequality and the intended count or
quantity. Fix the parameters, uniformity range and evidence available. Keep
the original target and current argument visible during the comparison.

## Procedure

1. **Locate the shortfall.** Identify the first unusable hypothesis or
   insufficient estimate. Back-solve for a sufficient local bound with any
   required margin. If the current representation closes the target directly,
   return that derivation.
2. **Compare representations on the original population.** Write the actual
   source map and the direction the proof needs. Account for coverage, fibres,
   exceptions, uniform constants and whether the objects being counted change.
   Ask whether the proposed gain reaches the same downstream inequality.
3. **Load the resources that address the shortfall.** Use a method card for a
   specific move. Use a runbook when its several obligations interact.

   | Bottleneck | Resource |
   | --- | --- |
   | The current variable hides the useful scale | [Invert a parametrization](references/invert-mathematical-parametrization.md) |
   | The estimate assumes a regular or unique graph | [Replace regularity with structural complexity](references/replace-regularity-with-structural-complexity.md) |
   | A failed rank or nondegeneracy test could yield a different constraint | [Extract constraints from proof failure](references/extract-constraints-from-proof-failure.md) |
   | Lifts might produce independently useful relations | [Amplify invariants through lifts](references/amplify-invariants-through-lifts.md) |
   | Many counted incidences share the same generator | [Compress counting through shared generators](references/compress-counting-through-shared-generators.md) |
   | A local estimate must fit a global budget | [Reverse-engineer theorem budgets](references/reverse-engineer-theorem-budgets.md) |
   | The retained assumptions may be too weak to close an implication | [Test relaxed proof-system completeness](references/test-relaxed-proof-system-completeness.md) |

   Start with [representation bottleneck triage](runbooks/representation-bottleneck-triage.md)
   when chart selection is unresolved. Use the
   [finite-cover determinant budget](runbooks/finite-cover-determinant-budget.md)
   when a cover feeds a determinant or rank split. Use
   [incidence budgets and adverse controls](runbooks/incidence-budget-and-adverse-controls.md)
   when the remaining issue is a catalogue-to-target count or an exact residual.
4. **Calculate the net bound and stop at the first missing link.** Put the
   original estimate and each candidate in the same inequality. Include
   analytic norms, denominator clearing, arithmetic losses and summation over
   all branches. Preserve the part that works if another branch stays open.
   Use exact computation for finite checks within the task's authority.
   A separate computational-evidence audit can assess predicate and coverage.

## Outputs

Return the source-preserving comparison, chosen route or reason to keep the
current one, the net bound with scope and margin, and the first open obligation.
Keep proved implications, exact finite checks and imported premises distinct.
Name the counted object and the map carrying the estimate back to it.

## Verification

Check the source map and exceptions, the hypotheses of each estimate, the
sign of the net margin, and every rank or regime branch. Identify a plausible
wrong shortcut and check it against the same target. A countermodel must meet
all retained assumptions. A source counterexample additionally needs an
actual source witness. A finite check covers its encoded domain and needs a
separate completeness argument before it can stand for the original problem.

## Stop

Stop when the improvement is justified, the current route wins, or an exact
open bridge identifies what to prove next. Keep a conditional result conditional
while source coverage, a branch, or the transfer of the bound remains open.
