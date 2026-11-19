# /work — Execute the plan

Goal: complete the plan phase by phase, and verify that it works before saying it's done. Being asked to verify forces thinking about the verification approach up front — which makes the work itself better.

## Steps

1. **Load the plan.** If there is no plan with a definition of done, stop and run `/plan` first.
2. **Work one phase at a time.**
   - Announce the phase being started.
   - Implement the steps, biasing toward the simplest thing that satisfies the phase's deliverable.
   - Run the phase's verification exactly as written in the plan. Show the evidence (output, screenshot, test result).
   - Only then mark the phase complete and move on.
3. **Handle surprises honestly.**
   - Small deviation: note it and continue.
   - Scope-changing discovery: pause, update the plan with the user, then continue.
   - A failure you cannot explain: switch to `/debug` rather than patching blind.
4. **Finish against the definition of done.** Walk through every acceptance criterion and check it explicitly. Anything unmet means the work is not done — say so plainly.

## Status reporting

After each phase, report in this shape:

```markdown
### Phase <n>: <name> — <complete | blocked>
- What was done: <summary>
- Verification: <the check that was run and its actual result>
- Deviations from plan: <none, or what and why>
```

## Anti-patterns

- Declaring done without running the verification ("it should work").
- Silently expanding scope mid-phase because something looked easy.
- Bundling three phases into one giant unreviewable change.
