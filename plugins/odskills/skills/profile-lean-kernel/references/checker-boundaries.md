# Lean compiler/export/checker boundaries

- Compilation against `OLeanLevel.exported` can see opaque symbols; strict flat checking via `OLeanLevel.private` may expose their definitions and trigger extensive normalization.
- Switching strict export to opaque declarations can misclassify internal definitions as axioms and violate dependency-complete assurance. It is **not** a valid shortcut.
- Replaying just one target still includes its actual transitive logical dependencies.
- Use equivalent start/completion events when the checker exposes them. In the instrumented odProof run they were `kernel_enter` and `kernel_complete`. Buffered stderr can misidentify the declaration being checked.
- Given a proved `f = g` for complex maps, try rewriting at that wrapper level **before** `DFunLike.coe` or structure projections force weak-head normalization.
- Every run must bind exact source, export, binary, checker scope, axiom assumptions and memory limits. Keep the distinction between a two-module mechanism control and full consumer acceptance.
