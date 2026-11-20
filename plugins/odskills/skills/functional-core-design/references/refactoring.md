# Small behavioural refactors

Load when changing existing code rather than designing a new component.

- Freeze the public entry points, selected semantics and externally observable behaviour before moving code.
- Identify the smallest extraction: one pure selector/validator/decision function, then a shell call that supplies facts and performs effects.
- Reuse existing discriminating tests; add missing positive or adverse cases from expectations independent of the implementation where the change warrants them. For bugs, preserve the failing reproduction first.
- Refactor incrementally, keeping identity/provenance, error semantics, resource limits, output format and user-visible status unchanged unless explicitly requested.
- Avoid introducing a new package, generic service layer or type hierarchy when ordinary functions are sufficient.
- Inspect transitive dependencies and import-time effects; keep old runtime packages and unwanted global state out of the new path.
- Re-run affected unit and actual entry-point tests. If no real backend is available, say so; do not treat a synthetic path as equivalent.
- Report precise changed functions, preserved contracts, test outcomes and remaining gaps. Stop at the selected scope.
