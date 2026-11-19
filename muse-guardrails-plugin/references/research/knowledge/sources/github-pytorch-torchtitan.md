# pytorch/torchtitan — Muse integration findings

## Source

- **Title:** pytorch/torchtitan — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-11-07
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh/pytorch_torchtitan_issues_5915.txt`.
- **Source URL / scope:** https://github.com/pytorch/torchtitan/issues/5915 — Muse Spark token embedding gets no gradient under TP (2026-11-07); 2026-11-07

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark (version unspecified)

## Summary

Token embeddings reportedly receive no gradient under tensor parallelism; training infrastructure, not hosted inference, is at issue. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. ``"On main (`9f70e5597`), `muse_spark_debugmodel` at TP2+EP2 (seed 42) gives `tok_embeddings.embedding.weight.grad is None` at every step; every other parameter gets a gradient."`` (pytorch/torchtitan#5915, 2026-11-07; attribution: harness/router-side (distributed-training/runtime); gh/pytorch_torchtitan_issues_5915.txt L2).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"#5802 makes the embedding's reduction explicit and synchronous, which restores the gradient (grad norm 0.0590 at step 1; TP1 reference 0.0564), and #5807 removes the async boundary path."` (pytorch/torchtitan#5915, 2026-11-07; attribution: harness/router-side (distributed-training/runtime); gh/pytorch_torchtitan_issues_5915.txt L4).
- **Evidence scope:** The retained statement supports the limited takeaway above, not an additional independent observation. ``"On main (`9f70e5597`), `muse_spark_debugmodel` at TP2+EP2 (seed 42) gives `tok_embeddings.embedding.weight.grad is None` at every step; every other parameter gets a gradient."`` (gh/pytorch_torchtitan_issues_5915.txt).

## Data/numbers

- ``"On main (`9f70e5597`), `muse_spark_debugmodel` at TP2+EP2 (seed 42) gives `tok_embeddings.embedding.weight.grad is None` at every step; every other parameter gets a gradient."``  (pytorch/torchtitan#5915, 2026-11-07; attribution: harness/router-side (distributed-training/runtime); gh/pytorch_torchtitan_issues_5915.txt L2).
- `"#5802 makes the embedding's reduction explicit and synchronous, which restores the gradient (grad norm 0.0590 at step 1; TP1 reference 0.0564), and #5807 removes the async boundary path."`  (pytorch/torchtitan#5915, 2026-11-07; attribution: harness/router-side (distributed-training/runtime); gh/pytorch_torchtitan_issues_5915.txt L4).

## How it relates to other sources

- **Related training boundary:** [Muse Spark Open — Hugging Face technical analysis](hf-open.md) — Gradient and sharding/resume failures concern training frameworks, not production API behavior.
- **Architecture anchor:** [Muse Spark Open 816B-A42B — Meta model card](hf-card.md) — The vendor architecture table does not independently test tensor-parallel gradients.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- Sparse source: only 2 substantive retained claim(s). Scope/ceiling bullets explain that limitation rather than inventing additional findings.
