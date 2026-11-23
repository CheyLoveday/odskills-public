---
name: attack-mathematical-claim
description: Try to falsify a precise mathematical claim using matched exact examples, boundary cases and authorized bounded searches; distinguish a verified counterexample from a software defect or a bounded negative result. Use to challenge a claim, not merely paraphrase it or certify a proof from passing examples.
---

# Attack a mathematical claim

## When to use

Use when asked to refute, delimit or stress-test a mathematical statement or a
particular implication. It can be selected directly. A full proof audit or a
request to explain known mathematics need not invoke this workflow.

## Inputs

Fix the target/revision, domain, complete hypotheses, definitions and conclusion.
Identify supplied sources, candidate witnesses, requested bounds or earliest
falsifier, allowed computation and budget. Execution authority comes from the
task/project, not from loading this skill; existing authorization is sufficient.

## Procedure

1. Negate the actual conclusion with its quantifiers intact. State which choices
   the witness may depend on while satisfying the complete antecedent. Refuting
   one proposed constant or cutoff does not refute existence of some constant or
   cutoff: that needs a family defeating every permitted choice. Preserve true
   fixed-parameter statements when a uniform statement fails. Keep original and
   revised targets separate.
2. Inspect a supplied witness before searching. Check exact arithmetic and all
   membership/hypothesis conditions; reject a proposed counterexample that only
   satisfies a relaxed statement.
3. Select relevant hostile cases: zero/unit, signs, small/exceptional parameters,
   equality endpoints, prime/valuation boundaries, gcd degeneracy, normalization,
   quantifier changes, and projection without valid reconstruction. Do not run
   an exhaustive universal checklist when a local decisive case suffices.
4. If computation is authorized and useful, use an understandable exact reference
   predicate, explicit bounds, independent known answers and adverse controls.
   Record inputs, seed if used, commands, counts, limits and failures. Keep search
   and verification of a candidate distinguishable. Do not install dependencies,
   run an unbounded search or launch services implicitly.
5. Reproduce and minimize a failure within the requested scope. Verify it by
   substitution or an independent method. Distinguish a mathematical witness,
   missing premise, implementation/checker error, resource problem and unknown.
6. If repair was requested, propose the smallest precisely revised statement and
   check it separately. Preserve the counterexample to the original; a repaired
   target is not a retroactive proof. Where warranted, retain the witness as a
   project-local regression under actual write authority.

## Outputs

Return exact target, tested scope, verified witness or bounded negative/unknown
result, full antecedent/conclusion checks, failure category, optional revision
and its own evidence, and the next proof obligation. State minimality only when
the earlier eligible domain was actually covered.

## Verification

Reject both invalid purported witnesses and unsupported universal success from
finite tests. An integer being neither a square nor a cube does not by itself
say whether all its prime exponents are at least two; evaluate the stated
predicate. Keep the same witness through all joined properties. To challenge a
periodic exclusion extended beyond its original scope, try a later lift of a
rejected representative or an index allowed by a withdrawn guard. A surviving
residue refutes the claimed finite exclusion on that domain. An actual source
counterexample still needs every source hypothesis. A failed search
program or timeout supplies no mathematical counterexample or negative result.

## Stop

Stop at a verified requested falsifier, the declared bound/budget or an essential
missing definition. A search with no witness establishes only its exercised
scope. Continue independent analytical checks when execution is unavailable;
do not invent runs, promote status or begin a new research programme.
