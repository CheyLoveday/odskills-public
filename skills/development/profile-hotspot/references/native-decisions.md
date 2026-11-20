# Choosing Python, vectorization, JIT and native kernels

Load when a measured hot path raises a genuine language/runtime decision. This is a **decision contract**, not a command to rewrite.

| Observation | First candidate | Important adverse case |
|---|---|---|
| Workload performs unnecessary calculations | Better algorithm, filtering, memoization with validated keys | Semantic changes to what is searched or counted |
| Large homogeneous bulk numeric operations | Appropriate vectorized/native library | Overflow, dtype conversion, copies, masked missing values |
| Stable repeatedly called scalar numerical kernel | JIT or existing compiled dependency | Compilation startup, unsupported types, fallback and reproducibility |
| Large stable CPU-bound hot loop after simpler options | Small C++/native kernel behind stable Python interface | FFI/batch overhead, ABI, wheels, memory, exceptions, precision |
| Time dominated by disk/network/external library | Reduce effects/copies/batching or leave Python unchanged | A language port only accelerates a non-dominant fraction |
| Small or rare calls | Stay in Python absent contrary evidence | Fixed native overhead outweighs saved CPU |

For a fixed unaffected fraction `f` and a speedup `s` of the remaining work,
the analytical overall factor is `1 / (f + (1-f)/s)`. If `f > 0`, even unlimited
acceleration cannot exceed `1/f`: 95% unchanged I/O bounds the factor by
`20/19`, about 1.053. Check the arithmetic independently. This assumes fixed
work and unchanged costs; changed overlap, I/O or algorithms require a new
model and measurement. The bound is not an observed benchmark.

## Exact numerical obligations

- Specify arbitrary-precision, fixed-width or mixed mode. Python `int` is unbounded; C++ machine integers are not. Determine **intermediate and accumulator bounds**, not just input bounds.
- For signed 64-bit products, `3037000499²` fits while `3037000500²` does not. A mathematically valid modular multiplication may overflow before the modulus is taken.
- For mixed exact arithmetic, test the support predicate **before narrowing** and retain a correct arbitrary-precision fallback or explicit failure; no silent float approximation.
- Preserve integer division/sign conventions, rounding, ordering, error types, API outputs, reproducible seeds and deterministic enumeration when they form part of the contract.
- For C++ extensions, budget interface/ABI ownership, thread-safety, compiler/linking, supported Python and OS wheels, and full installed-artifact tests. A local microbenchmark cannot certify shipped interfaces.
- Test both sides of every numeric support boundary, including corrupt/invalid inputs and rejected fallback cases. A speedup is relevant only for the supported population.

Keep exact numeric support and reference-path parity explicit. Project-specific
execution commands and acceptance rules belong to the consuming project.
