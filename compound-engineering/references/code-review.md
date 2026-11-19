# /code-review — Review like a senior engineer

Goal: review the output and the solution as a senior employee would — catching real issues, explaining them so the user can understand, and separating "must fix" from "nice to have." Works for code, but also documents, plans, and other deliverables.

## Steps

1. **Re-read the definition of done** from the plan; the review is against the goal, not against taste.
2. **Review in passes:**
   - **Correctness** — does it actually do what was promised? Edge cases, error paths, wrong assumptions.
   - **Safety** — anything that could lose data, leak secrets, or break existing behavior.
   - **Simplicity** — unnecessary complexity, dead code, abstractions with one caller, features nobody asked for.
   - **Maintainability** — will the next person (or next session) understand this? Naming, structure, surprising choices left uncommented.
3. **Classify every finding** as one of:
   - **Blocker** — must fix before shipping.
   - **Should fix** — real issue, ship-blocking only if trivial to fix now.
   - **Nit / future** — worth knowing, fine to defer.
4. **Explain in plain language.** The user may not be a specialist. For each finding: what it is, why it matters, and what could go wrong if ignored — no unexplained jargon.
5. **Offer the fixes.** For blockers, propose the concrete fix; apply approved fixes and re-verify.

## Output format

```markdown
## Review: <what was reviewed>

**Overall:** <ship it / fix blockers first / needs rework> — <one-sentence reason>

### Blockers
1. <finding> — <why it matters, in plain language> — <proposed fix>

### Should fix
...

### Nits & future improvements
...
```

## Anti-patterns

- A wall of nitpicks with no severity ranking.
- Approving without checking the definition of done.
- Explaining findings in jargon the user has to decode.
