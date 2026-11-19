# /debug — Fix the root cause

Goal: find the actual root cause of an issue and fix it there — not paper over the symptom. Screenshots, error messages, and pasted output are first-class input: let the evidence lead.

## Steps

1. **Capture the symptom precisely.**
   - What happened, what was expected instead, and how to reproduce it.
   - Collect the evidence: exact error text, screenshot, logs, the input that triggered it.
   - If it cannot be reproduced, instrument first (logging, smaller test case) before theorizing.
2. **Form ranked hypotheses.** List the 2–4 most plausible causes based on the evidence, most likely first. Say what observation would confirm or eliminate each.
3. **Test hypotheses cheapest-first.** Read the relevant code/config, add a targeted check, or reproduce in isolation. Change one variable at a time; a fix you cannot explain is a coincidence, not a fix.
4. **Fix at the root.** Patch where the cause lives, not where the symptom appeared. If a workaround is genuinely needed now, label it as such and record the real fix as follow-up.
5. **Verify the fix** by re-running the original reproduction — the exact failing case, not a happy-path neighbor. Check that nothing adjacent broke.
6. **Compound the learning.** If this class of bug could recur (or this is the second time), hand it to the `improve-system` skill so the prevention becomes part of the system.

## Output format

```markdown
## Debug: <symptom in one line>

- **Reproduction:** <steps / input that triggers it>
- **Root cause:** <what was actually wrong and why it produced this symptom>
- **Fix:** <what changed, and why there>
- **Verified:** <the re-run of the failing case and its result>
- **Prevention:** <what stops this class of bug from recurring, or "one-off">
```

## Anti-patterns

- Shotgun-fixing: changing five things and hoping.
- Declaring the first plausible theory to be the cause without confirming it.
- Fixing the symptom ("catch and ignore the error") and calling it resolved.
