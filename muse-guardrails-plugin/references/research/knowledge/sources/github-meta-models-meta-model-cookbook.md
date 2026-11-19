# meta-models/meta-model-cookbook — Muse integration findings

## Source

- **Title:** meta-models/meta-model-cookbook — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-05
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/meta-models_meta-model-cookbook_issues_57.txt`.
- **Source URL / scope:** https://github.com/meta-models/meta-model-cookbook/issues/57 — Model API: token logprobs for classification and judging (allow logprobs on the answer with minimal reasoning, or a non-reasoning mode) (2026-10-05); 2026-10-05

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark (version unspecified); Meta Model API

## Summary

Requested logprobs/non-reasoning support is a first-party API capability gap, distinct from latency and client retry behavior. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"- `logprobs: true` is refused whenever reasoning is on, and reasoning can't be turned off:"`` (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L8).
- Describes a mitigation or verification practice, not a guaranteed universal fix. `"- The only workaround is sampling the answer k times and counting."` (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L14).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. ``"That is slow and costly on Muse Spark: one call with an 87-token prompt and a one-word answer used **128 reasoning tokens** and took **8.8 s** at `minimal`."`` (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L14).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``""`logprobs` cannot be true when `reasoning_effort` is `minimal`. logprobs is not supported with reasoning.""`` (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L11).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"In our probe (2026-10-04), OpenAI, Together, Fireworks, DeepSeek, OpenRouter and Hugging Face routes returned token logprobs for the same request shape, so judge features built that way don't work on the Meta Model API."` (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L16).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. `"This overlaps with #56, which asks for a non-reasoning, low-latency path for inline suggestions; one mode could serve both."` (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L21).

## Data/numbers

- ``"That is slow and costly on Muse Spark: one call with an 87-token prompt and a one-word answer used **128 reasoning tokens** and took **8.8 s** at `minimal`."``  (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L14).
- `"In our probe (2026-10-04), OpenAI, Together, Fireworks, DeepSeek, OpenRouter and Hugging Face routes returned token logprobs for the same request shape, so judge features built that way don't work on the Meta Model API."`  (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L16).
- `"This overlaps with #56, which asks for a non-reasoning, low-latency path for inline suggestions; one mode could serve both."`  (meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); gh2/meta-models_meta-model-cookbook_issues_57.txt L21).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
