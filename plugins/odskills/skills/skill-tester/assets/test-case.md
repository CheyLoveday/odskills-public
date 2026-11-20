# Skill test case

- Target skill and exact version/dirty snapshot:
- Lane: static/reference, executable helper, or agent behavior:
- Realistic user request:
- Raw input artifacts and identities:
- Expected observable output, selected before execution:
- Permitted effects and protected inputs:
- Positive control and adverse/regression control:
- Nearby task outside scope, when testing routing:
- Command or fresh-evaluator prompt and actual environment:
- Observed artifacts, actions, exit and result:
- Finding, limitation or missing check:
- Actual evaluator independence:

Keep golden outcomes and suspected defects separate from a fresh evaluator's task.
For a helper-only test, mark agent behavior `NOT_RUN`; for a structural check,
mark executable behavior `NOT_RUN`. Do not manufacture filled-in observations.
