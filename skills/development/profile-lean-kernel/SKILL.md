---
name: profile-lean-kernel
description: Isolate and improve a measured Lean elaboration, export or independent kernel-checker bottleneck using same-source controls and proof-form ablations. Use for Lean memory, time or reduction explosions; not routine theorem completion or weakening mathematics to force a pass.
---

# Profile Lean proof-checker reductions

## When to use

Use when a named Lean declaration, export or checker is unexpectedly expensive, stuck or resource-limited. Avoid broad refactors and unbounded reruns based only on speculation.

## Inputs

Pin source, theorem roots and dependency closure, Lean/Mathlib/checker hashes, `module` import/transparency mode, exact export, memory/time caps, previous logs and real failing stage.

## Procedure

1. Distinguish elaboration, compilation, proof export, parsing and independent kernel reduction. A successful `lake build` does not establish an inexpensive private-export replay.
2. Attribute costs to the smallest demonstrable declaration or term. Match start and completion events when available and consult the platform's CPU and memory measurements. Flush or verify live logs before attributing a stall to the last visible declaration. Record uncertainty when the checker exposes too little to localize the cost.
3. Compare proof representations: rewrite an equality at the enclosing map/structure boundary before projections, factor repeated normalization, minimize unnecessary unfolding and test symbolic representation changes. Do not change unapproved axioms or weaken the goal.
4. Change one proof representation at a time. Hold the theorem roots, checker binary, export procedure, runtime limits and workload fixed. Record separate source and export hashes for A and B, and explain any dependency changes. Use unchanged repeats to gauge noise and an invalid-term or wrong-output control to check the acceptance path. Retain adverse outcomes and report the measured metric with its units.
5. Recheck the exact source with required compilation, statement/axiom audit and all checker gates. A synthetic fixture or target-sharded diagnostic does not replace dependency-complete consumer verification.
6. Report the **removed expensive reduction**, new proof/import cost and bounded measurements or precise reason the result remains `INCOMPLETE`. Stop before changing memory limits, trust boundaries or checker semantics without authorization.

## Outputs

An evidence-bound culprit, proof-form alternatives, real A/B measurements where run, rejected candidates, checker-specific outcomes and a smallest reviewable patch or blocked obligation.

## Verification

Read [checker boundaries](references/checker-boundaries.md) when module opacity, exports, projection reduction or monitoring is implicated. Report `NOT_RUN` rather than inventing scores.

## Stop

Never hide incomplete checks, switch to opaque exported axioms to sidestep strict verification, remove transitive dependencies without a contract, or treat a compiler `bad_alloc` as the same incident as a kernel OOM.
