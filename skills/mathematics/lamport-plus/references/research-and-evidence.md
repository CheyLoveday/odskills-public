# Mathematical discovery and evidence

## Find a decisive lemma

State the exact target and the downstream step that needs a bridge. Work
backward to a sufficient statement and forward to the strongest useful fact
available from the hypotheses. State the gap as a candidate lemma. Record
which hypotheses the proposed bridge consumes and how it would close the goal.

Try a small case or a change of representation. For analogy, identify the
structure that transfers and where transport needs proof. For abduction,
record the candidate mechanism and a prediction that could disconfirm it.
Generalize when a proof or a separate research question needs it.

## Refine under falsification

Try equality, zero, sign changes, degenerate objects and extreme legal
parameters. Remove hypotheses one at a time, test a converse separately and
change the order of quantifiers when dependence is suspect. For sharpness,
look for equality or a family approaching the bound. Verify a counterexample
against the exact hypotheses and identify whether it breaks the theorem, an
intermediate lemma, or a proposed proof step. Preserve the witness, the old
statement and the reason for any revision.

## Run exact controls when warranted

1. Freeze the predicate, domain, expected output and coverage before testing.
   Select ordinary and boundary cases, a known falsifier for a nearby false
   claim, and cases withheld from discovery or tuning.
2. Use exact arithmetic for exact claims. Compute the checked quantities from
   their inputs independently of the proposed conclusion. Feed the checker an
   intentionally false variant that should fail and confirm the failure reaches
   the intended test. A checker that gives the same answer on good and bad
   inputs supplies no discriminating evidence.
3. Retain the command, relevant revision or hashes, runtime, inputs, range and
   seed where applicable, result, skips and failure witnesses. Diagnose failures
   as statement, implementation, or checker problems. Keep exploratory and
   held-out results distinct and use `NOT_RUN` for work still planned.
4. State the general proof obligation. A finite search establishes its covered
   domain. When exhaustive computation is a proof step, justify how all
   theorem cases reduce to that domain and what validates the certificate.

## Claim and evidence record

Use the existing project registry. For reusable work without a registry, the
[ledger CSV](../assets/claim-ledger.csv) provides a starting schema. Keep routine
proofs in their natural output unless the project needs registration. Record
immutable statement revisions or stable IDs with explicit versions. Treat a
claim's kind (candidate, conjecture, theorem target, or local obligation)
separately from its current evidence.

Each evidence field links to its own artifact or records its actual status.
Use the [research record](../assets/research-record.md) to retain discovery and
dependencies, with one record per claim or linked records for revisions.

| Field | Minimum evidence |
| --- | --- |
| Exact statement | Stable ID, reference and revision with domains, quantifiers, hypotheses and conclusion |
| Counterexample | Explicit witness checked against the frozen target |
| Computation | Executed check and receipt with coverage, controls and boundaries |
| Ordinary proof | Complete hierarchy with justified leaves, or exact open obligations |
| Independent review | Reviewer, checked source revision and scoped verdict |
| Correspondence | Explicit comparison of the elaborated formal target with the mathematical statement |
| Lean declaration | Planned name in its own field. Record a verified name only against inspected declaration evidence |
| Lean build | Executed command, source revision, toolchain, inputs and result |
| Axiom inspection | Actual placeholder and target-dependency inspection and its result |
| Independent replay | Checker or kernel replay receipt and its scope |
| Understanding | Observed reconstruction or transfer result, with the reader and task scope recorded at the appropriate privacy level |

A claim can carry evidence in multiple fields. For example, a complete
abstract proof can coexist with a missing source bridge to an application.
A reserved identifier, a compiling weaker statement, and a planned replay
leave their relevant checks open.
