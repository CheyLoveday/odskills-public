---
name: functional-core-design
description: Design or refactor Python and scientific software into a functional core and imperative shell (FCIS) when domain logic is tangled with I/O or hidden state. Use for software boundary design; exclude conceptual explanations, tests of already-pure functions, and operations runbooks.
---

# Functional core, imperative shell (FCIS)

## When to use

Use when designing or refactoring software so domain rules are explicit, composable and testable independently of external effects. Inspect the task and implementation first: if existing separation is adequate, preserve it and complete the requested work without an unnecessary refactor. Prefer a small targeted boundary over reorganising an entire project. Do not activate for a conceptual explanation, tests of an already-pure function, unrelated writing, mathematical proof review or operations/deployment questions that require no software design change.

## Inputs

Identify existing modules, entry points, domain inputs/outputs, external effects, tests, behavioural invariants and authorised scope. Resolve an unclear contract from existing code, callers and tests where possible. If a consequential ambiguity remains, ask a targeted question or report the blocked portion before introducing a breaking change; continue independent work within the known contract.

## Procedure

1. Trace the *actual* data flow through the public entry point; mark pure transformations, decisions, mutable state and effects. Observe current tests and relevant failure cases.
2. Distinguish behaviour to preserve from a defect the task explicitly asks to fix. If a boundary change is needed, choose the smallest useful extraction and identify its inputs, outputs, decisions, excluded effects and compatibility requirements. Preserve the entry point and other observable behaviour. Do not add a framework for hypothetical uses. If the existing boundary suffices, skip the extraction steps below and proceed to the requested work and verification.
3. Reuse or define appropriate explicit types for inputs, outputs, configuration and state. Preserve arrays/tables for scientific workloads, rather than splitting every element into objects. For structural decisions load [data modelling](references/data-modelling.md).
4. Implement pure domain transformations and decision functions; pass dependencies/parameters explicitly instead of reading global state. If an iterable can perform external effects when consumed, keep that iteration in the shell or explicitly treat the consuming function as effectful; passing an iterator alone does not make the boundary pure.
5. Keep file, network, database, subprocess, clock, randomness and LLM interactions in a narrow imperative shell. For effect ownership, failure handling, retries or concurrency load [effect boundaries](references/effect-boundaries.md).
6. Make the smallest safe change in behavioural increments. If changing an established codebase load [incremental refactoring](references/refactoring.md).
7. Verify pure behaviour with independent oracles, and exercise the *actual* public workflow with effects controlled. For test design load [testing](references/testing.md).
8. Report altered boundaries, API compatibility, actual tests, untested effects and remaining limitations. Stop when the selected outcome is delivered.

## Outputs

The requested change with preserved authorised interfaces and focused tests; where separation is needed, working code/design with an explicit pure core and narrow effect shell. A design-only assignment yields a mapped boundary and precise implementation requirements, not unrequested code.

## Verification

Compare before/after observable behaviour and public entry points. Test core edge cases, effect failures and at least one end-to-end path when execution is authorised. Never report synthetic tests as real platform, scientific or proof verification.

## Stop

Stop before an unsupported effect, action outside the user's authority or breaking change based on an unresolved assumption. Resolve contract questions from available evidence first; otherwise identify the blocked portion and ask a focused question while continuing useful independent work. Stop when the selected outcome is delivered. Do not auto-start other changes, dependency migrations or deployments.
