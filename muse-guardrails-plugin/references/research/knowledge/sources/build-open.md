# Build with Muse Spark Open — Meta developer guide

## Source

- **Title:** Build with Muse Spark Open — Meta developer guide
- **Author/origin:** Meta
- **Date:** publication date not captured; accessed 2026-11-10
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `build-open.txt`.
- **Source URL / scope:** https://dev.meta.ai/resources/blog/build-with-muse-spark-open — Build with Muse Spark Open — Meta developer guide; publication date not captured; accessed 2026-11-10

## Grade

**A** — First-party statements/specifications about Meta’s own product; not independent validation.

## Product/version covered

Muse Spark Open 816B-A42B

## Summary

Developer-facing deployment and agentic capabilities are vendor specifications, not independent reliability results. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Meta statement; not an independent measurement. `"Served in NVFP4 with a custom-trained DSpark drafter for faster decoding with 1M context window."` (build-open.txt L159).
- Meta statement; not an independent measurement. `"An 816B-parameter open-weight model from Meta Superintelligence Labs, trained for long-horizon agentic work such as coding and customer service agents."` (build-open.txt L42).
- Meta statement; not an independent measurement. `"It activates 42B parameters per token, takes text, image, video and audio input, and holds a 1M-token context window."` (build-open.txt L42).
- Meta statement; not an independent measurement. `"Serve the model on either two Mac Studios, with M5 Ultra and 512GB of unified memory; or four Mac Studios with 256GB of unified memory, for a total of 1TB of unified memory, enough to hold a NVFP4 quantized version of Muse Spark"` (build-open.txt L105).
- Meta statement; not an independent measurement. `"Connect your Mac Studios directly using the built-in support for Thunderbolt 5 and RDMA to ensure high-bandwidth, low-latency communication."` (build-open.txt L105).
- Meta statement; not an independent measurement. `"Unsloth's Dynamic GGUFs compress the model to as little as 2-bit, so the smallest version fits in about 300 GB of combined system RAM and VRAM, or unified memory on Apple silicon."` (build-open.txt L150).
- Meta statement; not an independent measurement. `"Unsloth Desktop runs on macOS, Windows and Linux, uses llama.cpp for CPU and GPU inference, and offloads layers to system RAM when VRAM runs short."` (build-open.txt L150).
- Meta statement; not an independent measurement. `"Download and chat with the model in the app, or serve it through OpenAI and Anthropic compatible endpoints for your applications and coding agents."` (build-open.txt L150).

## Data/numbers

- `"An 816B-parameter open-weight model from Meta Superintelligence Labs, trained for long-horizon agentic work such as coding and customer service agents."` Meta statement; not an independent measurement. (build-open.txt L42).
- `"It activates 42B parameters per token, takes text, image, video and audio input, and holds a 1M-token context window."` Meta statement; not an independent measurement. (build-open.txt L42).
- `"Serve the model on either two Mac Studios, with M5 Ultra and 512GB of unified memory; or four Mac Studios with 256GB of unified memory, for a total of 1TB of unified memory, enough to hold a NVFP4 quantized version of Muse Spark"` Meta statement; not an independent measurement. (build-open.txt L105).
- `"Connect your Mac Studios directly using the built-in support for Thunderbolt 5 and RDMA to ensure high-bandwidth, low-latency communication."` Meta statement; not an independent measurement. (build-open.txt L105).
- `"Unsloth's Dynamic GGUFs compress the model to as little as 2-bit, so the smallest version fits in about 300 GB of combined system RAM and VRAM, or unified memory on Apple silicon."` Meta statement; not an independent measurement. (build-open.txt L150).
- `"Served in NVFP4 with a custom-trained DSpark drafter for faster decoding with 1M context window."` Meta statement; not an independent measurement. (build-open.txt L159).
- `"Fireworks AI — Run serverless LoRA training on the NVFP4 checkpoint, with no GPUs to provision."` Meta statement; not an independent measurement. (build-open.txt L234).

## How it relates to other sources

- **Primary anchor / same-origin restatement:** [Muse Spark Open 816B-A42B — Meta model card](hf-card.md) — Use Meta’s model card for architecture, benchmark direction and limitations; secondary summaries are not fresh validation.
- **Different evidence class:** [Muse Spark Open on Mac Studio — Apple ML Research](apple-mlx.md) — Apple supplies deployment measurements under a specific precision/context, not a blanket confirmation of vendor benchmarks.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- First-party capabilities, privacy/approval promises and benchmark claims are not independently validated by being quoted here.
