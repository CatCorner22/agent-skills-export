# Introducing Muse Code and Muse Spark 1.2 — Meta

## Source

- **Title:** Introducing Muse Code and Muse Spark 1.2 — Meta
- **Author/origin:** Meta
- **Date:** August 5, 2026
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `musecode-blog.txt`.
- **Source URL / scope:** https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2 — Introducing Muse Code and Muse Spark 1.2 — Meta; August 5, 2026

## Grade

**A** — First-party statements/specifications about Meta’s own product; not independent validation.

## Product/version covered

Muse Spark 1.1; Muse Spark 1.2; Muse Code

## Summary

Model and harness are co-trained for coding, compaction and subagents; training claims are not failure reports. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Meta statement; not an independent measurement. `"It can coordinate multiple persistent subagents for each task, solving difficult problems faster, more accurately, and with less intervention."` (musecode-blog.txt L10).
- Meta statement; not an independent measurement. `"These specialized background agents remain active throughout each session, rather than being spawned for individual tasks, helping avoid redundant information gathering."` (musecode-blog.txt L13).
- Meta statement; not an independent measurement. `"Their persistence reduces latency and the need for steering on difficult, multi-step tasks."` (musecode-blog.txt L13).
- Meta statement; not an independent measurement. `"The training included rejection sampled harness trajectories and recipe optimizations for goals, compaction, and subagents, alongside the integration of the Muse Code toolset to maximize harness compatibility."` (musecode-blog.txt L32).
- Meta statement; not an independent measurement. `"This single source of truth makes the runtime replay-exact and restart-safe: after a crash, the agent can resume precisely where it stopped."` (musecode-blog.txt L18).
- Meta statement; not an independent measurement. `"Muse Spark 1.2 was extensively trained on long-horizon coding tasks, including whole-repository generation, large end-to-end projects, and auto-research."` (musecode-blog.txt L34).
- Meta statement; not an independent measurement. `"It leverages planning to sequence work, goal conditioning to maintain direction, and context compaction to retain the knowledge needed to sustain progress."` (musecode-blog.txt L34).
- Meta statement; not an independent measurement. `"We also used Muse Spark 1.1 to generate challenging coding environments and instruction-following templates."` (musecode-blog.txt L36).

## Data/numbers

- `"Muse Spark 1.2 was extensively trained on long-horizon coding tasks, including whole-repository generation, large end-to-end projects, and auto-research."` Meta statement; not an independent measurement. (musecode-blog.txt L34).
- `"We also used Muse Spark 1.1 to generate challenging coding environments and instruction-following templates."` Meta statement; not an independent measurement. (musecode-blog.txt L36).
- `"We tested the model's ability to iteratively optimize GPU kernels over 1,000+ tool calls (up to 24 hours)."` Meta statement; not an independent measurement. (musecode-blog.txt L38).

## How it relates to other sources

- **Independent qualification, version dependent:** [Muse Spark 1.2 — Artificial Analysis](aa-12.md) — Check independent accuracy, cost and benchmark settings; do not project a later model’s results onto the launch version.
- **Contrasts with user experience:** [HN: Muse Code and Spark 1.2 discussion](hn-49187575.md) — Reports show harness/access/task differences, not a controlled refutation of all vendor claims.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- First-party capabilities, privacy/approval promises and benchmark claims are not independently validated by being quoted here.
