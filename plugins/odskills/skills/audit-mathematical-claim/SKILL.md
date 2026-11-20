---
name: audit-mathematical-claim
description: Audit a proposed mathematical argument against its exact claim, dependencies and evidence; independently check load-bearing steps and report supported scope, counterexamples or gaps. Use for proof or cross-evidence review, not merely summarizing a proof, discovering a new theorem or granting project acceptance.
---

# Audit a mathematical claim

## When to use

Use for a proposed proof, theorem application or claim supported by human,
formal and/or computational evidence. A narrow counterexample, certificate or
Lean-correspondence question can go directly to its specialist; this skill is
not a prerequisite. Ordinary explanation or copyediting needs no audit.

## Inputs

Identify the exact target and revision, definitions, domains, quantifiers,
assumptions, proof/evidence and requested review depth. Read the consuming
project's applicable rules and selected sources. Record permitted effects,
budget and output; a review request does not itself authorize builds, computational searches,
edits or status promotion. State authorship and actual review independence.

## Procedure

1. Preserve the submitted target. Separate a revision or proposed repair from
   the original. Resolve material ambiguity from sources; leave unsupported
   interpretations explicit rather than silently changing the claim.
2. Map the load-bearing implications to their exact premises, witnesses and
   sources. Separate written proof, Lean statement/proof evidence, bounded
   computation, literature and claims that an alternative method is impossible.
   Prioritize steps whose failure would invalidate the conclusion; a dependency
   map is not proof that its edges are valid.
3. Reconstruct those steps independently of the author's asserted conclusion.
   Check inference direction, quantifier order, hidden/circular assumptions,
   exhaustive cases and projection versus reconstruction. When these are
   delicate, read [inference boundaries](references/inference-boundaries.md).
4. Test the weakest implications against matched exact examples, boundaries
   and plausible countercontrols. Use `attack-mathematical-claim` if a deeper
   falsification task is needed and available; ordinary local reasoning does
   not require another skill. Finite survival does not prove a universal claim.
5. For a material computational or Lean bridge, select
   `audit-computational-evidence` or `audit-lean-correspondence` only when useful
   and available. Inspect suitable existing evidence directly when sufficient.
   For actual multi-source handoffs, read [handoff checks](references/handoffs.md).
   Missing tools block dependent verification, not independently reviewable work.
6. Locate and classify each finding: false mathematical implication, missing
   premise, scope/reconstruction gap, implementation defect, representation or
   documentation error, missing evidence, or unresolved question. A defective
   witness/checker does not refute the target. Conversely, clean code or axiom
   output cannot repair a false mathematical implication.
7. Return the strongest supported conclusion for each target/evidence layer,
   a minimal gap or failure reproduction, and the smallest warranted correction.
   Apply repairs only within actual edit authority; preserve unrelated correct
   code when the defect is confined to prose, a comment or a checker.

## Outputs

Return target/source identities, dependency/argument trace, authorship and
independence, findings with locations and evidence, checks actually performed,
unverified obligations, bounded verdict and next action. Distinguish a valid
argument under stated premises, a refuted claim, a defective proof, an incomplete
review and unavailable evidence. An audit recommendation does not change a
project's canonical mathematical or release status.

## Verification

Check that every conclusion uses the original domain and matched premises.
Explain material steps rather than accepting their labels. Validate alleged
counterexamples against the complete antecedent and original conclusion;
accept legitimate alternative proofs/normalizations with justified bridges.
Record failed attempts, limits and affected rechecks after revisions. Do not
describe self-review, simulated notes or a tool quorum as independent review.

## Stop

Stop at the requested review outcome or declared budget. Report indispensable
missing premises and unresolved layers without manufacturing acceptance.
Do not auto-launch solvers, remote reviewers, formal builds, publications or
consumer changes. Reuse existing authorization for checks already permitted.
