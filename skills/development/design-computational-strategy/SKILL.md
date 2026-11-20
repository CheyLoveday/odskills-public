---
name: design-computational-strategy
description: Design algorithms and representations for a concrete computational task by identifying structure, comparing costs and choosing a discriminating prototype. Use before committing to an approach or when unnecessary work dominates; not for a measured profiling investigation, proof certification or routine implementation of an already chosen algorithm.
---

# Design a computational strategy

## When to use

Use when the required answer is clear enough to compare ways of computing it,
but the algorithm or representation is still a meaningful decision. A short
recommendation or keeping the existing approach can be the complete outcome.
This is software computation design; it does not impose a scientific campaign
process or require a profiler before considering an algorithm.

## Inputs

Establish the required output: decision, count, witness, list, distribution,
approximation or certificate. Identify admissible inputs, exactness/accuracy,
duplicates and ordering, boundaries, typical and extreme sizes, repeated queries,
latency/memory constraints, available code and permitted experiments. Keep
mathematical, floating-point and statistical guarantees distinct. An unknown
workload property calls for a conditional choice or small measurement.

## Procedure

1. Write the smallest output contract that distinguishes correct alternatives.
   Trace how the result is consumed: a count may avoid listing objects, whereas
   a witness or reconstruction requirement may make that compression invalid.
   Preserve original identity, multiplicity and shared constraints when needed.
2. Keep an understandable reference computation or independently justified
   small oracle. Identify repeated work, sparsity, bounded support, monotonicity,
   algebraic structure and parameters invariant across queries. Do not assume
   that an integer input fits a machine word or that a large range is dense.
3. Compare a few relevant alternatives, including the current/simple method.
   For each serious candidate state what work disappears, what new work/state
   appears, setup and per-query cost, peak memory, applicable regimes and the
   condition under which it loses. Include bit size or precision where it
   changes the cost model. Analytical operation counts are estimates, not timings.
4. When choosing a structural transformation, load only the relevant section of
   [strategy mechanisms](references/strategy-mechanisms.md). Retain the argument
   that the transformation preserves the requested answer: coverage and duplicate
   handling for enumeration; sufficient information for summaries; error bounds
   for approximation; intermediate bounds for packing or narrowing. Reject a
   heuristic as an exact exclusion rule without the missing justification.
5. Choose the smallest experiment that could change the recommendation. Contrast
   independent reference and candidate results on tiny adversarial cases, then
   vary the workload dimension that separates their costs. Include setup and
   reuse where relevant. Run only authorised bounded probes; mark larger or
   unavailable comparisons NOT_RUN. A prototype need not become production code.
6. Return a preferred approach or explicit conditional decision, its validity
   argument, expected trade-offs, prototype observations and remaining checks.
   If a concrete measured bottleneck remains, a profiling handoff can consume
   the workload and parity oracle; it is not a mandatory next step.

## Outputs

A concise decision with alternatives and applicability conditions; output and
numeric contract; cost/memory estimates; a discriminating check or actual bounded
prototype if requested; and a precise implementation or measurement handoff.
Distinguish implemented, measured, estimated and still hypothetical results.

## Verification

Check the proposed transformation against an independently specified oracle and
boundary examples, including a plausible wrong shortcut. A legitimate alternative
may satisfy the same contract. Test public conversion/serialization if its limits
matter to the result. A finite comparison checks those inputs; an exactness or
coverage claim still needs its general argument. Faster operation counts do not
establish runtime benefit, calibration or a theorem.

## Stop

Stop at the requested decision or prototype. Missing evidence blocks only the
dependent recommendation. Do not launch a search campaign, add a cache/service,
install a backend, migrate languages or change consumer interfaces merely because
an option was discussed. Project execution, spend and acceptance remain local.
