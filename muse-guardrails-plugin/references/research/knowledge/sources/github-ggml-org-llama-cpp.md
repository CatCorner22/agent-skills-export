# ggml-org/llama.cpp — Muse integration findings

## Source

- **Title:** ggml-org/llama.cpp — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-11-10
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh/ggml-org_llama.cpp_pull_32017.txt`.
- **Source URL / scope:** https://github.com/ggml-org/llama.cpp/pull/32017 — chat : fix Muse Spark ignoring response_format json_schema (2026-11-10); 2026-11-10

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark (version unspecified); Muse Glimmer

## Summary

Top-level JSON schema is ignored or rejected around Muse’s generation prefill; the parser fix is harness-side. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"The Muse Spark parser ignores json_schema and only builds a grammar when tools are given."` (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L6).
- Maps the product or interface rather than measuring success. `"This is the same fix as #29615 for Muse Glimmer."` (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L8).
- Concerns model honesty, evaluation awareness or identity behavior; causal reach is limited to the reported setting. `"A raw GBNF grammar (case 2 in the issue) is not changed by this PR: a user grammar applies from the first token, as for other harmony-style models."` (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L13).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"So a top-level json_schema falls back to the server's schema grammar, which fails on the "<|start|>assistant" generation prompt prefill (400), and response_format is silently not applied."` (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L6).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"Build a response format rule for the final message when json_schema is set, with an eager grammar, and keep reasoning free-form."` (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L8).
- Maps the product or interface rather than measuring success. `"Added the same two test-chat cases as Muse Glimmer (direct final answer, and after a reasoning message)."` (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L12).
- Parser tests do not establish real-model end-to-end reliability. `"Not tested on the real model."` (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L13).

## Data/numbers

- `"So a top-level json_schema falls back to the server's schema grammar, which fails on the "<|start|>assistant" generation prompt prefill (400), and response_format is silently not applied."`  (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L6).
- `"This is the same fix as #29615 for Muse Glimmer."`  (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L8).
- `"A raw GBNF grammar (case 2 in the issue) is not changed by this PR: a user grammar applies from the first token, as for other harmony-style models."`  (ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); gh/ggml-org_llama.cpp_pull_32017.txt L13).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
