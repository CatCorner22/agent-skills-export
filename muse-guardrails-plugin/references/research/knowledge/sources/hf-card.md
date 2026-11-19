# Muse Spark Open 816B-A42B — Meta model card

## Source

- **Title:** Muse Spark Open 816B-A42B — Meta model card
- **Author/origin:** Meta (hosted on Hugging Face)
- **Date:** Publication unknown; accessed 2026-11-10 (evidence heading date not validated as publication)
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `hf-card.txt`.
- **Source URL / scope:** https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B — Muse Spark Open 816B-A42B — Meta model card; Publication unknown; accessed 2026-11-10 (evidence heading date not validated as publication)

## Grade

**A** — First-party statements/specifications about Meta’s own product; not independent validation.

## Product/version covered

Muse Spark Open 816B-A42B

## Summary

Architecture, benchmark labels and limitations are primary specifications; serialized templates are not bug reports. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Model overview: 1M context, MoE; weights BF16/NVFP4, text output from text/image/video/audio input. `"816B total / 42B active"` (hf-card.txt L283).
- Meta model-card limitation. `"The model may produce inaccurate, biased, or objectionable responses to user prompts."` (hf-card.txt L542).
- Not an independently measured failure rate. `"While optimized for agentic tasks, the model may still make errors in multi-step reasoning, particularly in novel scenarios not well represented in training data."` (hf-card.txt L543).
- Meta acknowledges occasional input-processing failure. `"When using very short or low-resolution videos (a few seconds at around 100 px), the model may sometimes reply that it can't view the video."` (hf-card.txt L547).
- Video mitigation from Meta. `"Use longer clips or higher resolution (448 px or more on the short side) for reliable results."` (hf-card.txt L547).
- Meta API-model evaluation, no system safeguards; benchmark-specific refusal, not a production agent security guarantee. `"The model refused 99.2% of jailbreaks on our internal benchmark and 94.8% when aggregating across PolyGuard (cyber subset), RedCode, and CyberBench 2024."` (hf-card.txt L535).
- Tested checkpoint only; zero measured misbehavior is not universal proof. `"with a 98.1% honesty rate on the MASK benchmark and a 0% misbehavior rate on the Agentic Misalignment benchmark."` (hf-card.txt L537).
- Explicit scope limitation; modifications may degrade safety. `"These evaluations characterized the released checkpoint under the tested conditions and do not cover every downstream configuration or use case."` (hf-card.txt L538).

## Data/numbers

- `"When using very short or low-resolution videos (a few seconds at around 100 px), the model may sometimes reply that it can't view the video."` Meta acknowledges occasional input-processing failure. (hf-card.txt L547).
- `"Use longer clips or higher resolution (448 px or more on the short side) for reliable results."` Video mitigation from Meta. (hf-card.txt L547).
- `"The model refused 99.2% of jailbreaks on our internal benchmark and 94.8% when aggregating across PolyGuard (cyber subset), RedCode, and CyberBench 2024."` Meta API-model evaluation, no system safeguards; benchmark-specific refusal, not a production agent security guarantee. (hf-card.txt L535).
- `"refusing over 98% of harmful requests on SecureBio's BioTIER refusal benchmark and over 99% on our internal single-turn chemistry refusal benchmark."` Vendor-reported bio/chem refusal. (hf-card.txt L536).
- `"with a 98.1% honesty rate on the MASK benchmark and a 0% misbehavior rate on the Agentic Misalignment benchmark."` Tested checkpoint only; zero measured misbehavior is not universal proof. (hf-card.txt L537).
- `"'low': 8, 'medium': 32, 'high': 256, 'xhigh': 512} -%}\n{%- if not"` Serialized chat-template mapping, not an independent bug report. (hf-card.txt L35).
- `"Unsupported reasoning_effort: ' ~ reasoning_effort ~ '. Expected one of: low, medium, high, xhigh.') -}}\n{%- endif -%}\n{%- set"` Template rejects unsupported effort values; preserve Spark Open versus hosted Spark 1.3 distinction. (hf-card.txt L35).
- `"816B total / 42B active"` Model overview: 1M context, MoE; weights BF16/NVFP4, text output from text/image/video/audio input. (hf-card.txt L283).
- `"at least 700GB of VRAM for NVFP4 and 2TB for BF16"` Meta recommended GPU deployment footprint; quantized Apple/HF demos use different precision/overhead. (hf-card.txt L304).
- `"The default is xhigh."` low/medium/high/xhigh only; other values error. Not hosted Spark 1.3 max effort vocabulary. (hf-card.txt L308).
- `"For Muse Spark Open we use xhigh reasoning effort, temperature = 1.0, top_p=1.0, top_k=disabled across benchmarks."` All following model-card score rows use these settings; methodology mixes internal, official leaderboard and self-report sources. (hf-card.txt L313).
- `"JobBench"` Table value for quoted label: 61.8. Meta comparison table; MCP-Atlas 89.2, OSWorld Verified 80.4, Toolathlon Verified 72.8; benchmark-specific, see methodology provenance. (hf-card.txt L334).
- `"HLE-Diamond (no tools)"` Table value for quoted label: 26.1. HLE with tools 61.0, GPQA Diamond 89.0; no-tools versus tool-assisted results not interchangeable. (hf-card.txt L380).
- `"DeepSWE 1.1 Preferred harness"` Table value for quoted label: 60. Model-card comparison: Kimi K3 68, GLM 5.3 67; different preferred harnesses, not an apples-to-apples base-model test. (hf-card.txt L426).
- `"Terminal-Bench 2.1 Terminus 2 agent"` Table value for quoted label: 76.4. Kimi K3 85.0 and GLM 5.3 83.9; shared Terminus 2 methodology except self-report exceptions in method PDF. (hf-card.txt L444).
- `"VideoMMEv2"` Table value for quoted label: 61.5. Model-card multimodal row; tools/settings differ across evaluation types. (hf-card.txt L499).
- `"StrongREJECT v2 (adaptive) lower is better"` Table value for quoted label: 0.5. Vendor table versus Kimi K3 66.6; benchmark adaptive jailbreak score, not a general 0.5% app compromise rate. (hf-card.txt L518).

## How it relates to other sources

- **Extends:** [Muse Spark Open evaluation methodology — Meta](open-evalmethod.md) — Methodology supplies harness, judge, subset and exclusion caveats for the vendor table.
- **Qualified implementation comparison:** [Muse Spark Open — Hugging Face technical analysis](hf-open.md) — HF local/training observations concern specific runtimes; effort mappings and deployment precision need reconciliation.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- First-party capabilities, privacy/approval promises and benchmark claims are not independently validated by being quoted here.
- The evidence heading’s 2026-01-04 is not validated as publication metadata. Embedded JSON/Jinja is serialized template content, not a separate observed bug. StrongREJECT v2 is explicitly lower-is-better.
