---
name: profile-hotspot
description: Diagnose measured runtime or memory bottlenecks in Python and scientific code and select a correctness-preserving improvement, including whether vectorization, JIT, an existing native library or C++ is justified. Use for a concrete performance problem; not speculative refactoring, test selection or an abstract language comparison.
---

# Profile and optimize an actual hotspot

## When to use

Use when a real application, algorithm or numerical workload is too slow, memory-heavy or resource-intensive and the user requests diagnosis, a performance plan or a bounded optimization. Do not create an acceleration project on the basis of code style, language preference or an unmeasured impression. The smallest justified outcome may be to keep the implementation unchanged.

## Inputs

Fix the supported public interface and correct reference results; representative input shapes, values and bit sizes; performance target, resource budget, platform and runtime; source revision, dependencies and compiler options where relevant; effects and permitted tools. Treat the source program, mathematical semantics and user-facing success/failure contract as separate constraints.

## Procedure

1. When execution is authorised, reproduce the workload and establish a baseline on the actual public path, separating cold startup/import/compile, warm steady state, CPU, memory, I/O and external service time. Otherwise use available evidence or describe the proposed baseline and mark it NOT_RUN. Read [benchmark evidence](references/benchmark-evidence.md) when choosing repetitions and measurement conditions.
2. Locate the dominant observed cost, including unnecessary work, algorithmic complexity, allocations/copies, batching, serialization, Python dispatch or native-library calls. A microbenchmark alone does not establish end-to-end benefit.
3. Compare minimal options in order of relevance, not as a compulsory ladder: do nothing; reduce work or change algorithm/representation; batch or cache within semantics; vectorize; use an existing optimized library; JIT; or implement a narrow native kernel. Avoid optimization whose expected gain is below the evaluation or maintenance cost.
4. Before proposing fixed-width, JIT, C++ or other native paths, read [native and exactness decisions](references/native-decisions.md). Declare admissible types, ranges, accumulator bounds, memory ownership, error mapping, compiler/platform support, precision and exact fallback or failure semantics. Do not silently convert unbounded Python integers to machine integers.
5. Implement only the smallest explicitly authorised change. Retain an understandable reference path and independently verify candidate outputs and failure behaviour on matched examples, boundaries and adversarial inputs.
6. When a candidate exists and benchmarking is authorised, compare reference and candidate on **identical workloads**, with repetitions, cold/warm effects and memory observations relevant to the user-facing objective. Otherwise record the comparison as NOT_RUN. If no measured gain survives the full public path, report that and stop rather than continuing to a different language.
7. Return the observed bottleneck, tested alternatives, performance and parity evidence, unsupported environments, added maintenance cost and the retained/remaining work.

## Outputs

A baseline with workload identity and limits, hotspot evidence, ranked minimal alternatives, selected keep-Python/vectorize/JIT/native/C++/no-change decision, results of authorised code changes if any, actual comparative timings and memory when measured, correctness/overflow controls and unresolved dependencies.

## Verification

Separate **measured result**, analytical estimate and hypothesis. Report revisions, OS/CPU, interpreter/compiler, input geometry and bit widths, warm-up/repetitions, statistic and variability, cold/warm performance, peak memory, errors, and independent result parity. A faster finite computation does not establish mathematical completeness or statistical calibration.

## Stop

Do not invent a C++ threshold, move a whole package to native code by default, install libraries, launch remote jobs, or change API/numeric semantics without authorisation. A missing benchmark, unsupported input type, unverified native result or failed parity check blocks the dependent performance claim, not unrelated correct work.
