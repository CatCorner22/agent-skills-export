# /brainstorm — Explore before committing

Goal: generate and compare real alternatives so the chosen approach is a decision, not a default. Never assume the initial idea is the best solution.

## Steps

1. **Interview the user.** Ask focused questions (a few at a time) to surface:
   - The underlying problem — not the requested feature. "Why do you want this?" often changes the answer.
   - Who it is for and how success will be judged.
   - Constraints: time, budget, tools, what already exists, what must not change.
2. **Generate 3–5 genuinely different approaches.** Vary along real axes: simplest-possible vs. full-featured, build vs. reuse, manual vs. automated. Include at least one "do much less than you think" option.
3. **Evaluate each option** briefly: what it delivers, effort, key risk, and what it forecloses later.
4. **Recommend one** with reasoning, and say what evidence would change the recommendation.
5. **Get explicit agreement** on the chosen direction before moving to `/plan`.

## Output format

```markdown
## Brainstorm: <problem statement in one sentence>

### What I learned from the interview
- <key facts and constraints>

### Options
1. **<Option name>** — <what it is>. Effort: <low/med/high>. Risk: <the main one>.
2. ...

### Recommendation
<Which option and why, in plain language.>
```

## Anti-patterns

- Jumping to the user's first framing without asking why.
- Listing five variations of the same idea and calling it a brainstorm.
- Starting to build during brainstorm.
