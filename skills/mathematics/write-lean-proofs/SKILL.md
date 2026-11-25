---
name: write-lean-proofs
description: Construct or repair a Lean theorem and its exact semantic bridge using composable lemmas, structural induction and explicit proof obligations. Use for actual Lean proof writing; not independent correspondence audit, open-ended mathematical discovery or performance profiling alone.
---

# Write source-faithful Lean proofs

## When to use

Use when the goal is an exact Lean theorem or a precisely defined formalization step. If its mathematical witness, statement or bridge is not known, return that missing obligation instead of proving a convenient weaker surrogate.

## Inputs

Read the literal target, mathematical source, selected modules and imports, pinned Lean/Mathlib versions, existing lemmas, allowed axioms, known counterexamples and consumer requirements.

## Procedure

1. Freeze the theorem's exact binders, hypotheses, implicit typeclass assumptions, coercions, ranges and zero/nonunit cases. Keep the intended claim independent of tactic and source formatting.
2. Decompose into small reusable lemmas: exact representation, arithmetic or cochain identity, source-witness compatibility, induction/recursive transport and final consumer bridge. Keep statement strengths explicit and do not silently replace a real arithmetic object with an abstract placeholder.
   When translating a Lamport blueprint or restructuring a nontrivial proof
   for human review, read the [Lamport proof style guide](references/lamport-proof-style.md).
   For a Lamport-Plus blueprint, keep its claim IDs, exact statements, proof
   paths and substantive steps in the implementation handoff. Record any
   missing source bridge and its blocked dependents as open.
3. For a dynamical system, prove the step and transport it over arbitrary iterations, for example by induction or a library iteration lemma. Inspect the elaborated goal of any `decide` or `rfl` proof. A check at selected inputs leaves the general statement open, while definitional equality can establish a claim with arbitrary parameters.
4. Rewrite through **proved enclosing map/structure equalities** before projecting deeply nested function values. Avoid unnecessary unfolding of large definitions under casts, `DFunLike.coe`, quotient representatives and recursors. Read [proof-form choices](references/proof-form-choices.md) when choosing a costly equivalence representation.
5. No `sorry`, `admit`, new axioms, unsafe shortcuts, input-keyed answers or silent target edits. Separate a pure algebraic criterion from its application to actual source-derived classes, local traces or determinant bases.
6. Run exact compilation, statement/axiom inspection and the required independent checker/export gates when tools permit. If Lean is unavailable, mark the complete candidate `UNCOMPILED` and record executable commands; never describe it as kernel-proved.

## Outputs

A complete Lean patch and exact theorem statement, proof dependency graph, required imports, actually executed checks and remaining consumer-specific hypotheses.

## Verification

Compare elaborated targets against the frozen claim, preserve original proof source, inspect `#print axioms` and independent replay where required. For representation changes, prove transport both ways when the consumer needs equivalence and check actual downstream use.

## Stop

Stop at an exact compiled theorem or a precise blocking goal. Proof byte count, short tactic scripts and successful elaboration do not establish checker efficiency or manuscript completeness.
