---
name: derive-structural-invariants
description: Discover source-coupled invariants, exact representations and reusable lemmas for mathematical research or formalization. Use when transferring mathematical structures across problems; not for routine Lean tactic repair, performance profiling or claiming a conjecture is solved.
---

# Derive structural mathematical invariants

## When to use

Use when a proof needs a better mathematical representation or a theorem family, including transfers between dynamical systems, Diophantine problems and formal methods. A finite experiment is not a universal theorem.

## Inputs

Pin the source population, hypotheses, observables, exact target, proved dependencies, counterexamples and source-to-consumer identity. Distinguish arbitrary source objects from finite samples, formal states or independently chosen witnesses.

## Procedure

1. Start from the target's source objects. When several observations must come from **one common witness**, write their joint image explicitly. For `a : S → A` and `b : S → B`, the joint image of `s ↦ (a s, b s)` is contained in the Cartesian product of marginal images. Prove the reverse inclusion separately if the target needs it.
2. Search exact invariants: shared factors and kernels, valuations, congruences, symmetries, induced actions, recurrences, conserved forms and canonical decompositions. Eliminate variables only after retaining constraints that link observations.
3. For compression `q : X → Y` and dynamics `F`, state the exact soundness law `q (F x) = G (q x)`, its invariant/reachable source domain and any required reverse lifting. Forward soundness does not imply recoverability.
4. Write a small mathematical ladder: source characterization → representation → invariant transport → joint compatibility → consumer theorem. Prove each direction and inspect edge cases. Locate a countermodel to the tempting stronger claim.
5. Keep proved algebra, exact finite controls, conditional arithmetic adapters and conjecture closure distinct. Check that local-to-global applications use the **same original witness** at every stage.
6. Supply the statements and hypotheses to a Lean proof writer; send actual measured cost problems to a kernel profiler rather than optimizing an unproved idea.

## Outputs

Return quantified lemma statements, proof dependencies, source-to-invariant map, invalid relaxations with counterexamples, and exact remaining application bridges. An elegant invariant is not by itself a proof of an unrestricted mathematical problem.

## Verification

Check zero/degenerate and adversarial cases, source recovery where required and independent exact toy examples. Read [source and quotient contracts](references/source-quotient-contracts.md) when a joint image, predictive quotient, factorization or local-global projection is central.

## Stop

Stop at a sound theorem programme or a falsifying counterexample. Do not turn a finite exhaustion, separate marginal facts or conditional source model into a universal closure theorem.
