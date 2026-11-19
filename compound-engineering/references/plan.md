# /plan — Turn the idea into a delivery plan

Goal: a plan concrete enough that "done" is unambiguous and the work can be delivered in verifiable phases. Bias toward the simplest solution that meets the goal.

## Steps

1. **Restate scope** from the brainstorm: what is being built, for whom, and — just as important — what is explicitly out of scope for now (e.g. "assume I will be the only user to start").
2. **Define done.** Write acceptance criteria as observable checks, not vibes: "I can log a workout from my phone and see it in a list after refresh," not "the app works."
3. **Break into delivery phases.** Each phase must end in something demonstrable and verifiable on its own. Order phases so the riskiest assumption is tested first. 2–5 phases for most projects.
4. **Define verification per phase.** For each phase, state exactly how it will be checked: which command to run, which flow to click through, what output proves it.
5. **List open questions and risks** that could invalidate the plan, with what to do if they hit.
6. **Confirm the plan with the user** before `/work` begins.

## Output format

```markdown
## Plan: <project name>

**Goal:** <one sentence>
**Out of scope (for now):** <list>

### Definition of done
- [ ] <observable acceptance criterion>
- [ ] <...>

### Phases
#### Phase 1 — <name>
- Deliverable: <what exists at the end>
- Steps: <short list>
- Verify: <exact check that proves this phase works>

#### Phase 2 — <name>
...

### Risks & open questions
- <risk> → <mitigation>
```

## Anti-patterns

- Phases that end in invisible progress ("set up architecture") with nothing verifiable.
- A definition of done that no one could objectively check.
- Planning for scale, users, or features the user explicitly deferred.
