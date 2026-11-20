---
name: audit-lean-correspondence
description: Check whether a Lean declaration and its proof evidence establish the intended mathematical statement, separating semantic correspondence, axioms and kernel/replay status. Use for paper-to-Lean audits or suspicious formal claims, not routine tactic completion or automatic release certification.
---

# Audit Lean correspondence

## When to use

Use for the connection between an intended statement and a selected Lean
declaration, including domain/definition bridges and the proof evidence relied
on. This specialist can be used directly; a full mathematical audit is optional.
A routine tactic edit or release campaign does not follow automatically.

## Inputs

Identify the intended claim/specification, exact declarations and relevant
definitions/imports, source/toolchain/dependency revisions, available elaborated
statements and logs, permitted checks and the consuming project's assurance
requirements. Do not substitute a donor project's target files or gate IDs.

## Procedure

1. Freeze the intended mathematical target independently of the submitted proof
   when trust matters. Record domains, quantifiers, definitions, boundary cases,
   conclusion and non-claims. Keep source text, elaborated statement and supplied
   descriptions distinguishable.
2. Compare actual meanings: types/coercions, binder order, implicit hypotheses,
   notation/typeclasses, changed definitions, vacuity and implication direction.
   Inspect transitive load-bearing definitions rather than only theorem names.
   Accept alternate syntax or a different formal domain when a valid explicit
   bridge establishes the required claim. Read [semantic checks](references/semantic-checks.md)
   for delicate translations.
3. Assess separately whether this exact declaration was elaborated/built,
   whether its transitive axioms meet the declared policy, whether it corresponds
   to the target, and whether required replay/external/independent checks were
   performed. Clean axioms do not establish semantic fidelity. A semantic mismatch
   does not by itself refute the intended mathematics.
4. If execution is authorized, inspect current official documentation for the
   pinned Lean/checker versions, then use supported project commands and exact
   declaration coverage. `#print axioms` reports transitive axiom dependencies;
   inspect real output and failures. Do not turn an empty output or failed
   command into a clean audit. `sorryAx`, unexplained custom axioms and native
   evaluation require explicit disposition under the selected contract.
5. Keep trusted comparison inputs outside untrusted proof control. Builds and
   metaprograms can execute effects; use appropriate supported isolation before
   running untrusted source. Missing tools allow a conditional source/evidence
   review, not an invented kernel or comparator pass. Do not upgrade the
   toolchain, install checkers or expand an assurance profile implicitly.
6. Report the precise bridge, mismatch or unresolved layer, evidence identity
   and whether it was observed now, supplied or historical. Preserve findings
   and re-evaluate dependent results after source/specification changes.

## Outputs

Return a claim-to-declaration crosswalk with explicit bridges/gaps; separate
semantic, axiom, build/replay and independent-review outcomes; actual commands
and scope when run; missing evidence and the smallest warranted correction.
This is not permission to promote a theorem, release or consumer artifact.

## Verification

Check both semantic countercontrols and legitimate alternate representations.
Match every log to the same target, snapshot and environment, including dirty
source. Clearly label source-text or supplied-log review when no live Lean
check occurred. A comparator can check a trusted formal challenge while that
challenge still misstates the paper; multiple checkers do not remove this gap.

## Stop

Stop after the requested correspondence review. Leave missing required evidence
incomplete, preserve failed checks, and continue independently reviewable layers.
Do not fabricate independence, accept a weaker theorem under the original name,
run unapproved builds or change project acceptance/status records.
