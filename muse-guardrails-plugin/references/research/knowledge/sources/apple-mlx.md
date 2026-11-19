# Muse Spark Open on Mac Studio — Apple ML Research

## Source

- **Title:** Muse Spark Open on Mac Studio — Apple ML Research
- **Author/origin:** Apple Machine Learning Research; individual authors not retained
- **Date:** October 15, 2026
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `apple-mlx.txt`.
- **Source URL / scope:** https://machinelearning.apple.com/research/mlx-distributed-inference — Muse Spark Open on Mac Studio — Apple ML Research; October 15, 2026

## Grade

**B** — Independent benchmark or deployment measurement; vendor facts repeated in the article retain vendor provenance.

## Product/version covered

Muse Spark Open 816B-A42B

## Summary

Measured multi-Mac MLX throughput depends on parallelism and a short 8,192-token test context. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. `"On a cluster of four Mac Studios, Muse Spark Open generates over 36 tokens per second (see Figure 1 ), well above average human reading speed."` (apple-mlx.txt L12).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"While both the Qwen and Mistral models fit on a single Mac Studio with 512GB of RAM, Muse Spark Open would require more than 1.6TB of RAM in its native precision (BF16) for the model parameters alone."` (apple-mlx.txt L43).
- Table 3 at 8,192 context / 128 generated tokens: two-Mac pipeline, two-Mac tensor, four-Mac tensor respectively; not a full-1M-context throughput claim. `"Muse Spark Open — — 15.74 24.99 36.73"` (apple-mlx.txt L88).

## Data/numbers

- `"On a cluster of four Mac Studios, Muse Spark Open generates over 36 tokens per second (see Figure 1 ), well above average human reading speed."`  (apple-mlx.txt L12).
- `"While both the Qwen and Mistral models fit on a single Mac Studio with 512GB of RAM, Muse Spark Open would require more than 1.6TB of RAM in its native precision (BF16) for the model parameters alone."`  (apple-mlx.txt L43).
- `"Muse Spark Open — — 15.74 24.99 36.73"` Table 3 at 8,192 context / 128 generated tokens: two-Mac pipeline, two-Mac tensor, four-Mac tensor respectively; not a full-1M-context throughput claim. (apple-mlx.txt L88).

## How it relates to other sources

- **Complementary measurement:** [Muse Spark Open — Hugging Face technical analysis](hf-open.md) — Both measure local deployment, but precision, parallelism, hardware and context differ.
- **Implements, not independently validates:** [Muse Spark Open 816B-A42B — Meta model card](hf-card.md) — Meta architecture/memory specifications frame the workload; short-context throughput is not 1M-context throughput.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- Versions, benchmark revisions, precision, context length, effort and runtime must match before comparing numbers. Vendor restatements inside an independent article remain vendor claims.
