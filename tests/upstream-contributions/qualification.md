# Qualification fixture

This supplied task contract and all receipts are synthetic. IDs below are
fixture revision identifiers. Assess the two snapshots independently. The user
asks for a local readiness assessment only. The target `northstar/atlas-lean`
guide makes these items mandatory for public-theorem behavior changes:

- a pinned-toolchain `lake build` from a clean checkout,
- a theorem statement comparison and exact declaration axiom audit,
- a diff review from someone who did not author the change, explicitly tied to
  the candidate revision,
- a public regression check demonstrating that the new intended behavior
  distinguishes the old faulty behavior.

The task is to repair `Atlas.fold_map` while preserving the public theorem
statement. Maintainer acceptance and remote mergeability are outside this task.

| Snapshot | Receipt |
| --- | --- |
| Q1 head `head-17`, base `base-23`, clean, Lean `toolchain-4` | Build success on `head-17/base-23/toolchain-4`; theorem type unchanged and the exact declaration has the permitted axioms on that same snapshot; independent review of that same diff found no blocking issue; the public regression fails with the expected assertion on the old implementation and passes on `head-17`. |
| Q2 head `head-18`, base `base-24`, dirty with a changed Lean file, Lean `toolchain-5` | Dashboard is green from `head-17/base-23/toolchain-4`; a local build of the dirty tree reported success; the only current regression run selected zero tests; the remaining review and theorem receipts are still for `head-17/base-23/toolchain-4`. |
