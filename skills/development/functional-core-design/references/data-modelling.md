# Data modelling for FCIS

Load when selecting domain record types, configuring a computation or preserving structured scientific data.

## Rules

- Use explicit types where they clarify valid states and function contracts: `dataclass(frozen=True)` for compact records with frozen attributes, `TypedDict` for wire-style mappings, `Enum` or `Literal` for closed states, `Protocol` only when an actual interface has multiple implementations. Freezing is shallow: contained arrays, lists and other mutable objects can still change. Choose copying, immutable containers or an ownership convention only when the contract needs them; do not copy large scientific data by default.
- Prefer functions with explicit arguments and explicit result records to mutable global configuration. Preserve units, provenance, error conditions and missingness.
- Keep NumPy arrays, pandas DataFrames/Series, Arrow tables, sparse matrices and batched datasets as data structures. Avoid per-row object construction unless domain semantics justify it.
- Separate representations: external parsed data → validated domain values → pure outputs → encoded external result. Avoid types that falsely confer trusted provenance just because an object was constructed.
- Distinguish Boolean from integer where semantics require exact types; make invalid combinations unrepresentable where proportionate.
- Do not create an inheritance hierarchy, DTO for every local variable, or an all-purpose context object solely for “clean architecture”.

## Practical boundary example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Selection:
    selected: tuple[str, ...]
    missing: tuple[str, ...]

def select_paths(requested: tuple[str, ...], available: frozenset[str]) -> Selection:
    return Selection(
        selected=tuple(path for path in requested if path in available),
        missing=tuple(path for path in requested if path not in available),
    )
```

The function operates on supplied names. The shell obtains `available` from the filesystem or another input source and decides how missing paths affect the task. This example selects from supplied membership; it does not discover transitive dependencies.
