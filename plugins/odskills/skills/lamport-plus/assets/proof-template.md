# Proof blueprint

```text
THEOREM [claim ID and revision]. [Exact statement]
ASSUME [hypotheses and sources]
PROVE [goal]

Governing idea: [the decisive reduction and why it helps]

⟨1⟩1. [Reduction, with its hypotheses]
       Justification: [definition, identity or prior theorem]
⟨1⟩2. [Intermediate claim]
  ⟨2⟩1. [Scoped witness or precise local obligation]
         Justification: [construction and supporting facts]
  ⟨2⟩2. QED. By [supporting steps and discharged assumptions].
⟨1⟩3. QED. By [the dependencies that establish the exact goal].
```

Replace a closure with `OPEN` where evidence is missing. Give the precise
obligation, active assumptions and blocked proof paths. Keep exploratory
records and any formal crosswalk next to the blueprint where applicable.
