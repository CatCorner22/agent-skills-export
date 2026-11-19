# huggingface/trl — Muse integration findings

## Source

- **Title:** huggingface/trl — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-11-10
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh/huggingface_trl_pull_8225.txt`.
- **Source URL / scope:** https://github.com/huggingface/trl/pull/8225 — Map the Muse Spark Open chat template to its training template (2026-11-10); 2026-11-10

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark Open 816B-A42B

## Summary

Inference and training templates differ; assistant-only loss needs the appropriate training template/mask. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. ``"This PR stops `SFTTrainer` with `assistant_only_loss=True` from training the `<|start|>assistant` that opens each Muse Spark Open assistant turn: the generation markers the template ships also cover it, while the generation"`` (huggingface/trl#8225, 2026-11-10; attribution: harness/router-side (training template assistant-loss mask); gh/huggingface_trl_pull_8225.txt L2).
- Maps the product or interface rather than measuring success. ``"Add a training template with the same markers moved after the turn's leading `<|start|>assistant`: the same change as the Hub PRs on the Muse Spark Open repos"`` (huggingface/trl#8225, 2026-11-10; attribution: harness/router-side (training template assistant-loss mask); gh/huggingface_trl_pull_8225.txt L10).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"The rendered text is unchanged: only the assistant mask changes."` (huggingface/trl#8225, 2026-11-10; attribution: harness/router-side (training template assistant-loss mask); gh/huggingface_trl_pull_8225.txt L10).

## Data/numbers

- ``"Add a training template with the same markers moved after the turn's leading `<|start|>assistant`: the same change as the Hub PRs on the Muse Spark Open repos"``  (huggingface/trl#8225, 2026-11-10; attribution: harness/router-side (training template assistant-loss mask); gh/huggingface_trl_pull_8225.txt L10).

## How it relates to other sources

- **Implements template semantics:** [Muse Spark Open 816B-A42B — Meta model card](hf-card.md) — Serialized inference templates are not themselves reports of model bugs.
- **Related training constraints:** [Muse Spark Open — Hugging Face technical analysis](hf-open.md) — Template/mask fixes and sharded-resume limitations are separate implementation problems.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
