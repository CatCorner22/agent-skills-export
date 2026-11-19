---
name: source-freshness-check
description: "Date every source and flag anything older than the topic's half-life or undated before relying on it. Use when writing research, comparisons, pricing or legal summaries, when reusing a knowledge base, or when a claim depends on something that changes often such as model prices, APIs, rankings, regulations or product features."
---

# Source freshness check

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
A deliverable rests on sources, and the topic moves.

## Steps
1. Set the half-life for the topic, in days. Suggested: model prices and rankings 30; API behavior and docs 90; software versions 180; regulations 365; history and settled science 3650.
2. Put the publish or retrieval date on every source line in your notes or bibliography.
3. Run `python3 scripts/source_freshness.py sources.md --half-life-days 90 --as-of 2026-11-12`. It flags stale and undated source lines.
4. For each stale line: re-check the primary source, update the date and the claim, or label the claim "as of <date>".
5. For each undated line: find the date in the page header, metadata or archive; otherwise label it "undated" in the deliverable and lower its weight.
6. State the as-of date at the top of the deliverable.

## Evidence
- In this research, Artificial Analysis index values for the same Kimi model ranged from 44 to 57 across index versions within four months, and Kimi API prices fell 33% between K3 and K3.1 Pro. Stale numbers change conclusions. https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks
- Half-life values are working defaults, not measured constants.
- Full research notes: [references/evidence.md](references/evidence.md)
