# Muse Spark Open — Hugging Face technical analysis

## Source

- **Title:** Muse Spark Open — Hugging Face technical analysis
- **Author/origin:** Hugging Face technical article; individual byline not retained
- **Date:** October 15, 2026
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `hf-open.txt`.
- **Source URL / scope:** https://huggingface.co/blog/meta-muse-spark-open — Muse Spark Open — Hugging Face technical analysis; October 15, 2026

## Grade

**B** — Independent benchmark or deployment measurement; vendor facts repeated in the article retain vendor provenance.

## Product/version covered

Muse Spark Open 816B-A42B

## Summary

Local quantized runs and training constraints complement, but do not independently validate, Meta’s benchmark table. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Maps the product or interface rather than measuring success. `"Only 8 experts run per token, so the model computes each token with about 42B parameters."` (hf-open.txt L91).
- Bounds supported capabilities or reliability; it does not establish universal failure. `"The mixture of experts model brings text, images, audio, and video into a model with approximately 816 billion parameters, around 42 billion active per token, and a context window of up to one million tokens."` (hf-open.txt L67).
- HF restates Meta’s training claim; not an independent observed coding failure or measurement. `"Meta describes Muse Spark Open as a coding-optimized model trained on real developer workflows such as multi-file refactors and long debugging sessions."` (hf-open.txt L71).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. `"An imatrix-calibrated 2-bit quant runs at 18 tokens/s, with plenty of room free for the KV cache (304 GB used by the model)."` (hf-open.txt L356).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"You can deploy Muse Spark Open on Inference Endpoints with a pre-validated SGLang recipe for the NVFP4 variant which runs on either 8 × NVIDIA RTX Pro 6000 98 GB with 131072 context length, or with 8 x NVIDIA H200 141GB if you"` (hf-open.txt L452).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. `"The endpoint exposes an OpenAI-compatible API with both Chat Completions API at /v1/chat/completions and Responses API at /v1/responses ."` (hf-open.txt L456).
- KV-cache memory at full 1M context; weights-only fit does not imply full context fits. `"266 GB for a full 1M-token context."` (hf-open.txt L100).
- Specific sharded training recipe caveat, not general Muse training inability. `"cannot resume a model that was sharded at load time. LoraConfig targets the four attention projections and the 256 experts of each layer stay frozen."` (hf-open.txt L503).

## Data/numbers

- `"The mixture of experts model brings text, images, audio, and video into a model with approximately 816 billion parameters, around 42 billion active per token, and a context window of up to one million tokens."`  (hf-open.txt L67).
- `"Only 8 experts run per token, so the model computes each token with about 42B parameters."`  (hf-open.txt L91).
- `"All 256 experts stay in memory, so deployment needs the memory of an 816B-parameter model, but runs at the much faster speed of a 42B model."`  (hf-open.txt L91).
- `"The processor expects mono audio at 24 kHz and pads the waveform to a multiple of 1,920 samples, corresponding to one audio embedding per 80 milliseconds."`  (hf-open.txt L227).
- `"An imatrix-calibrated 2-bit quant runs at 18 tokens/s, with plenty of room free for the KV cache (304 GB used by the model)."`  (hf-open.txt L356).
- `"The model takes about 344 GB, leaving room for the KV cache, and runs at about 225 tok/s prefill and 21 tok/s generation with a 1024-token prompt and 128 generated tokens."`  (hf-open.txt L443).
- `"You can deploy Muse Spark Open on Inference Endpoints with a pre-validated SGLang recipe for the NVFP4 variant which runs on either 8 × NVIDIA RTX Pro 6000 98 GB with 131072 context length, or with 8 x NVIDIA H200 141GB if you"`  (hf-open.txt L452).
- `"The endpoint exposes an OpenAI-compatible API with both Chat Completions API at /v1/chat/completions and Responses API at /v1/responses ."`  (hf-open.txt L456).
- `"We trained for 500 steps, which took about 2 hours on 64 H100s, at about 8,000 tokens per second."`  (hf-open.txt L506).
- `"266 GB for a full 1M-token context."` KV-cache memory at full 1M context; weights-only fit does not imply full context fits. (hf-open.txt L100).
- `"cannot resume a model that was sharded at load time. LoraConfig targets the four attention projections and the 256 experts of each layer stay frozen."` Specific sharded training recipe caveat, not general Muse training inability. (hf-open.txt L503).
- `"(16, 64, 256, 512)"` CONFLICT: explanatory symbolic mapping differs from model-card serialized template (8,32,256,512); high/xhigh agree, low/medium differ. (hf-open.txt L132).

## How it relates to other sources

- **Complementary measurement:** [Muse Spark Open on Mac Studio — Apple ML Research](apple-mlx.md) — Single-machine quantized demos and multi-Mac MLX tests are not interchangeable.
- **Related implementation constraint:** [huggingface/trl — Muse integration findings](github-huggingface-trl.md) — Training-template/loss-mask handling matters in addition to load-time sharding and resume limits.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- Versions, benchmark revisions, precision, context length, effort and runtime must match before comparing numbers. Vendor restatements inside an independent article remain vendor claims.
- hf-open.txt: Hugging Face technical article: grade B for its own measured demos, C for explanation, A-provenance for Meta claims quoted within it; runtime recipes have different context/modality support.
