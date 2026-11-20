# Lamport-style proof writing in Lean

Use this guide to translate a structured proof blueprint or make a
nontrivial Lean proof easier to review. The outer proof should show the
witnesses, decisive facts, cases and conclusion.

## Start from the exact claim

Fix the statement, assumptions, domains and conclusion. Identify the
obligations that carry the argument and the earlier facts each one uses.
If formalisation exposes a missing hypothesis or unproved bridge, record
it in the blueprint. Preserve the intended theorem while resolving it.

## Make the outer proof readable

| Blueprint move | Lean form | When to use it |
| --- | --- | --- |
| Pick a witness | `obtain … := …` | Extract the witness and the facts that justify using it. Name the existential fact separately if the proof reuses it. |
| Assert an intermediate result | `have h_fact : … := by …` | State a fact the argument relies on. Give it a name that describes its content. |
| Reduce the target | `suffices h_bridge : … by …` | State a useful subgoal and show how it implies the original target. |
| Split the argument | `rcases`, `cases` or explicit `induction` branches | Show the branches when they have distinct witnesses or reasoning. |
| Chain equalities or bounds | `calc` | Show the intermediate expressions that explain the argument. |
| Justify a step from named facts | An explicit lemma application, rewrite or small local proof | Show the inputs that justify the step. Use automation to close routine goals once the obligation is visible. |

Keep a one-off obligation local with `have`. Extract a lemma when its
statement is self-contained and the extraction clarifies the main proof.
Expose it publicly when a consumer needs it.

## Connect back to the blueprint

Use the blueprint's existing step IDs on substantive blocks. A short
map from step to block or declaration can make the correspondence clear.
Use explicit arguments or a small lemma when a reader needs to see the
inputs. Verify declaration dependencies separately when assurance calls for it.

## Review the result

Skim the theorem and outer proof before reading the tactic blocks. Check
where the witnesses come from, which fact drives the argument and how
the cases close. Keep names and comments that help a reader answer those
questions. Compile on the pinned toolchain. When restructuring a theorem,
preserve its statement and assumptions and check affected consumers.

## Example

```lean
import Mathlib

theorem sq_mod_three_of_not_dvd (n : ℤ) (h_ndvd : ¬ (3 ∣ n)) :
    ∃ k : ℤ, n ^ 2 = 3 * k + 1 := by
  -- LP1: Choose a quotient and a bounded remainder.
  obtain ⟨q, r, h_div, h_nonneg, h_lt⟩ :
      ∃ q r : ℤ, n = 3 * q + r ∧ 0 ≤ r ∧ r < 3 := by
    refine ⟨n / 3, n % 3, ?_, ?_, ?_⟩
    · omega
    · omega
    · omega

  -- LP2: Exclude zero remainder using nondivisibility.
  have h_remainder_ne_zero : r ≠ 0 := by
    intro h_zero
    apply h_ndvd
    refine ⟨q, ?_⟩
    simpa [h_zero] using h_div
  have h_cases : r = 1 ∨ r = 2 := by
    omega

  -- LP3: Give the witness in each remaining case.
  rcases h_cases with h_one | h_two
  · refine ⟨3 * q ^ 2 + 2 * q, ?_⟩
    rw [h_div, h_one]
    ring
  · refine ⟨3 * q ^ 2 + 4 * q + 1, ?_⟩
    rw [h_div, h_two]
    ring
```

| Blueprint step | Lean block | What a reader should see |
| --- | --- | --- |
| LP1 | Typed `obtain` | The chosen quotient and remainder, the division identity and the remainder bounds. |
| LP2 | `h_remainder_ne_zero`, then `h_cases` | Zero would give `q` as a divisibility witness. The bounds leave `1` and `2`. |
| LP3 | `rcases h_cases` | Each branch gives a witness. `ring` checks the identity for that witness. |

Checked with Lean 4.35.0 and Mathlib at
`56a005855ea17e0b0958f73ec801ae140b0a1679` using `lake env lean`.
