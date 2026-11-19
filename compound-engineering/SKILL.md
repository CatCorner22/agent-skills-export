---
name: compound-engineering
description: Ship work like an engineer instead of yoloing prompts. Use when the user runs /brainstorm, /plan, /work, /code-review, or /debug, or wants to build, deliver, or fix something non-trivial (an app, a proposal, a launch, a document). Walks a disciplined loop - brainstorm ideas, plan with a definition of done, execute in phases with verification, review like a senior engineer, and debug to root cause.
---

# Compound Engineering

The other skills load your system and pressure-test the work. This one actually turns it into something shipped. It applies the same engineering process to everything — code, proposals, product launches:

1. **Plan** what you are doing.
2. **Define done** explicitly.
3. Work through clear **delivery phases**.
4. **Review** the work and troubleshoot if needed.
5. **Mark it done** and move to the next thing.

Why this beats yoloing:

- AI defaults to solving the immediate thing in front of it as efficiently as possible; it does not care about the big picture unless the process forces it to.
- Reviewing bad output takes more time than a proper plan would have taken.
- Working this way builds the muscle to deliver progressively more complex things.

## The five phases

Each phase has a detailed playbook in `references/`. Read the playbook for the phase you are entering; do not load all five at once.

| Command | Phase | Playbook |
|---|---|---|
| `/brainstorm` | Explore solutions before committing to one | [references/brainstorm.md](references/brainstorm.md) |
| `/plan` | Turn the chosen idea into a phased delivery plan with a definition of done | [references/plan.md](references/plan.md) |
| `/work` | Execute the plan phase by phase, verifying as you go | [references/work.md](references/work.md) |
| `/code-review` | Review the output like a senior engineer, in plain language | [references/code-review.md](references/code-review.md) |
| `/debug` | Find and fix the root cause of an issue | [references/debug.md](references/debug.md) |

## How the phases connect

- Do not skip brainstorm: your first idea is rarely the best solution.
- Do not start `/work` without a plan that names the definition of done — "verify it works before saying it's done" only means something if "works" was defined.
- After `/work`, always offer `/code-review`. After review or real usage surfaces an issue, go to `/debug`, and feed the root cause back into the plan if it changes scope.
- When the same class of problem appears twice, hand it to the `improve-system` skill so the fix becomes permanent.

## Worked example (proof-of-concept web app)

1. `/brainstorm` — "I want to build a proof-of-concept web app that lets me log my workouts from my phone. Interview me to come up with ideas for features."
2. `/plan` — "Based on what we discussed, create a delivery plan that biases toward the simplest solution. Assume I'll be the only user to start."
3. `/work` — "Complete the plan outlined here. Make sure to verify the app works before saying it's done."
4. `/code-review` — "Review the code and flag any issues. Simplify the explanation so I can understand it."
5. `/debug` — "Fix this issue" + a screenshot of the error.

## Rules

- One phase at a time; announce which phase you are in.
- Bias toward the simplest solution that meets the definition of done.
- Never claim done without having run the verification defined in the plan.
