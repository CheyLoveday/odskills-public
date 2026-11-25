---
name: lamport-plus
description: Discover and refine mathematical lemmas, write structured proofs, or help a reader reconstruct a proof and transfer its method to a new problem. Use for a human-readable argument, proof blueprint, or research record. Use the corresponding specialist for Lean-only work, an independent audit alone, or routine copyediting.
---

# Lamport-Plus

## When to use

| Mode | When | Return |
| --- | --- | --- |
| Light | Routine lemma | Exact statement and a short proof with explicit justifications and only useful hierarchy |
| Full research | Difficult, reusable or contested claim | Research record, candidate lemmas and falsifiers, evidence and coverage, hierarchical proof or open obligations, and claim ledger entries |
| Learning | A reader wants to reconstruct or transfer the argument | Governing idea, top-level proof, expandable leaves, reconstruction questions and a transfer exercise |

Use the requested mode. If unspecified, use learning for reconstruction, full
research for substantial discovery or evidence-dependent work, and light for a
routine proof. Combine full research and learning outputs when both are requested.

## Inputs

Read the target or existing proof, its definitions, source assumptions and the
reader's objective. Identify available evidence and any existing claim registry.
Ask for an indispensable missing premise or mark the corresponding obligation
open. Keep the target invariant across modes.

## Procedure

1. **Freeze the claim.** State types, quantifier order, hypotheses, boundary
   cases and conclusion, including strictness and witness or uniqueness
   requirements. Keep an existing claim ID. Assign an ID under the project's
   convention when a reusable claim needs tracking. Give a material statement
   change a new ID or explicit version and reassess inherited evidence.
2. **Find and challenge the bridge.** Work backward to a sufficient lemma and
   forward from the supplied hypotheses. In full research, record why the
   bridge helps, try falsifiers, and plan exact checks with an adverse control
   before execution. Read the [research and evidence guide](references/research-and-evidence.md)
   for discovery, tests and ledger decisions. Record actual checks and coverage
   or mark them `NOT_RUN`.
3. **Expose the mathematical dependency chain.** Lead with the governing idea.
   Write a top-level route that shows what drives the conclusion. Expand
   load-bearing steps into precise assertions, scoped witnesses and
   independently checkable justifications. Use the
   [proof and learning guide](references/proof-and-learning.md) for hierarchy,
   open leaves and reader reconstruction. Keep research trials in the research
   record and explain a failed route in the proof only when it clarifies a step.
4. **Check the result and hand off.** Review the unchanged target, leaf
   dependencies, witness scope, imported premises and outstanding source
   bridges. In learning mode, let the reader attempt reconstruction before
   revealing transfer answers. Record observed reader evidence separately.
   If formalization is requested, supply the exact blueprint and
   [optional Lean crosswalk](assets/lean-crosswalk.md) with claim IDs, proof
   paths, candidate targets and the actual verification status. Review
   [evidence fields](references/research-and-evidence.md#claim-and-evidence-record)
   before assigning any completion status.

## Optional specialists

Use a specialist when its outcome is needed and it is available. Give it the
exact claim, its source assumptions and the scoped question. Use
`derive-structural-invariants` for an exact representation or transport,
`attack-mathematical-claim` for falsification,
`audit-mathematical-claim` for independent proof review, and
`audit-computational-evidence` for certificate and coverage review.
`write-lean-proofs` implements the formal target and
`audit-lean-correspondence` independently checks its meaning and assurance.
Retain the returned artifacts and limitations against the same claim ID.
All guidance needed for the three modes is inside this package.

## Outputs

Return the artifacts for the selected mode with the narrowest justified status.
Use the [proof template](assets/proof-template.md) for a reusable blueprint.
See the [integer parity proof](examples/elementary-proof.md) for a light
worked proof or the [vector-space quotient](examples/residual-quotient.md)
for a proof with a falsifier and transfer exercise.

## Verification

Check the exact claim and the status of each dependency. For a missing
resource, name it and continue with the available evidence. Keep any outcome
that needs the missing input open.

## Stop

Label an unresolved leaf `OPEN` with its exact obligation, assumptions and
dependents. Close only the goals whose dependencies are discharged.
Use project records and run tests or builds within the task's authority.
