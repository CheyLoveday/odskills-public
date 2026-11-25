# Proof hierarchy and reader reconstruction

## Write the argument

Begin with the exact theorem. Use `ASSUME` and `PROVE` when they clarify
scope. The top level should state the strategy, why the decisive intermediate
claim helps, and how the steps reach the goal. Use labels such as `⟨1⟩1`
and `⟨1⟩2` with deeper levels for subproofs. Cite the enclosing path when
local labels repeat, or give reusable facts stable names.

Use `TAKE` for an arbitrary object, `ASSUME` for a scoped premise,
`CHOOSE` for a witness, `CASE` for a branch, `SUFFICES` for a reduction,
and `QED` for closure. Give the object a type where it enters scope. Explain
why a witness exists, how it is constructed and why it has the required
properties. Discharge local assumptions, verify exhaustive cases, and keep
witnesses in scope. Check both directions of each equivalence. Split steps
that introduce independent obligations. Justify every substantive leaf with
a definition, identity, prior step or identified theorem and its applicable
hypotheses. Check for circular dependencies.

For `OPEN`, name the missing assertion under the assumptions available at
that leaf and identify the dependents. Keep supplied premises visible at
their point of use. An abstract conditional proof can be complete while an
application remains open. Review terminology and the exact statement against
the proof, claim registry and any formal target.

## Help a reader reconstruct it

Present the objective and governing idea before technical details. Explain
how backward and forward reasoning led to the useful intermediate lemma,
where the load-bearing hypotheses enter and which steps still work without
them. Show how choices of representatives and witnesses are justified.
Label intuition and follow it with the exact implication or equality it
suggests. Keep the same domains, hypotheses and conclusion at each level.

Show the top-level route first and put leaves where the reader can expand
them as needed. Ask the reader to recover the decisive reduction, justify
a witness and locate the first step lost if a hypothesis is removed. Offer
a new problem with a similar mechanism and an explicit change in assumptions.
When assessing transfer, give the new statement and necessary inputs first,
withhold the solution, and score the argument independently of fluency.
Treat a question set as a proposed assessment until a reader actually
attempts it.
