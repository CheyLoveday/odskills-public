# Reproducible performance evidence

Load when constructing, comparing or interpreting performance measurements.

- Identify the **actual operation**: a public API call, installed distribution, worker batch or whole pipeline. Distinguish those from a small inner-loop timing.
- Freeze revision, environment, package versions, OS/CPU, optional accelerator, seed where relevant, exact input bit lengths/shapes/sparsity, and correctness oracle. Use a range covering ordinary, small, boundary and worst-supported cases when warranted.
- Measure cold import/JIT/compilation, warm execution, I/O, serialization, memory peak and output verification as applicable. Report number of trials, a robust summary, variability and resource/timeouts.
- Separate complexity analysis, empirical trend and an extrapolation. Do not convert a single fitted curve into an all-input guarantee.
- Compare at **the same correctness contract**; refuse an apparent speedup obtained by dropping precision, source coverage, input classes, error checks or full completion.
- For caching, bind the key and lifetime to every result-affecting input and configuration. Object identity, shape or a filename alone does not establish unchanged contents. Exercise legitimate state changes, validation after a warm hit, and ownership of returned mutable results. Use a valid immutable snapshot, invalidation or no cache as appropriate; do not copy large scientific inputs by default. Separate reuse-eligible measurements from fresh-work workloads.
- A required parity or acceptance gate must execute in every supported runtime mode. Python can remove `assert` statements under optimization; use explicit failure checks for a measurement receipt's required conditions. Keep benchmark execution behind an explicit command, with no workload launch on module import.
- When a helper writes persistent measurements, preserve earlier receipts and profiles. Preflight occupied output paths before running the workload and create new evidence without replacing existing files, including linked paths. A label such as `baseline` does not select a source version: bind each run to its actual source, workload and parameters, and validate those identities before comparing runs. A failed or partial publication remains distinguishable from a completed receipt; do not claim a multi-file transaction from individual file writes.
- Stop when no expected meaningful improvement or when the target has been reached. An unexecuted suggestion is a hypothesis, not a measured speedup.

## Example interpretation

A sub-millisecond over-cap refusal measures rejection, not completion of the
unsupported calculation. Report it as a refusal. An operation whose historical
cost was not measured remains unmeasured. Check public installed behavior outside
the source tree, and compare exact kernels against a transparent reference with
intermediate integer-width and overflow controls.
