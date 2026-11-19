---
name: restraint-pass
description: "Strip over-claiming from a draft before delivery: absolutes, intensifiers, superlatives, numbers the brief does not support, certainty beyond the evidence. Works on any model's output. Use after drafting reports, memos, marketing copy, summaries or recommendations, and whenever a fact sheet or evidence grade exists."
---

# Restraint pass

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
A draft is done and someone will act on it.

## Steps
1. Gather the fact sheet or evidence table the draft should rest on.
2. Run `python3 scripts/restraint_check.py draft.md --facts factsheet.md`. It flags absolutes (always, proven), intensifiers (clearly, revolutionary), superlatives (best, leading) and any number missing from the fact sheet. Without a fact sheet it flags numbers with no source cue in the sentence.
3. For each flag choose one: cut, soften to the evidence grade ("in one test", "vendor-reported", "probable"), or add the source inline.
4. Check that each recommendation has a stated condition ("if retries are cheap"). Unconditional advice is a claim too.
5. Add one sentence of the strongest counter-view where the draft argues a position.
6. Deliver with a short list of what was softened. Keep the energy; cut the adjectives.

## Evidence
- Product-copy and essay tests of frontier models found unsupported claims and over-certain tone as the main defects, independent of model. Kimi K3.1 Pro: 12 unsupported claims on a sales brief, 0 on a factual brief (SpringPrompt). Single-source. https://springprompt.com/blog/kimi-k3-1-pro-review
- Claim-evidence grading practice from research methodology; the flags are heuristics, not judgments.
- Full research notes: [references/evidence.md](references/evidence.md)
