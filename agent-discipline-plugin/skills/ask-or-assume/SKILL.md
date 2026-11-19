---
name: ask-or-assume
description: "Classify every gap in a task as goal / input / constraint / context; ask goal gaps up front in one batch, proceed on labeled assumptions for reversible input/constraint gaps, ask only when a wrong guess is expensive, never interrupt past the midpoint unless blocked, ≤1 interruption per phase. Use at task start, before irreversible steps, and whenever you feel the urge to ask. Scope boundary: permissions already given → `autonomy-ledger`; verifying the user's stated facts → `premise-check`."
metadata:
  priority: 8
---
# Ask or assume

Studies agree: clarifying questions improve outcomes *and* poorly timed interruptions cost more than wrong reversible guesses. The skill is in timing and classification, not in asking less.

## Classify the gap
| Gap | Example | Policy |
|---|---|---|
| **Goal** | "Make export faster" — faster for whom, what number? | Ask **now**, before any work, batched with other goal gaps |
| **Input** | Which of two config files is canonical | Check it yourself; if truly undecidable and expensive to redo → ask |
| **Constraint** | Can I add a dependency? | Reversible → assume + label; confirm-first list → ask |
| **Context** | How the module is used elsewhere | Never ask — read the code |

## Mechanics
- **Batch** all goal questions into one block at the start. One question per turn is a violation.
- **Label assumptions** inline and in the checkpoint: `Assumed: CSV export is the hot path (90% of the logs). Say so and I'll switch.`
- **Midpoint rule:** after half the task, no questions unless blocked; finish on labeled assumptions and list them.
- **Budget:** ≤ 1 interruption per phase (plan → build → verify). Save the rest for the final report.
- **Irreversible** step → `scope-and-blast-radius-check` (one-word go-ahead, fully staged).
- Ask with options and a recommendation, not an open prompt: `A (recommended): …  B: …`.
