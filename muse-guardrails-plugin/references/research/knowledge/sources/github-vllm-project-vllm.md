# vllm-project/vllm — Muse integration findings

## Source

- **Title:** vllm-project/vllm — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-18–2026-11-10
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh/vllm-project_vllm_issues_64632.txt`, `gh2/vllm-project_vllm_pull_62345.txt`.
- **Source URL / scope:** https://github.com/vllm-project/vllm/issues/64632 — [Tracking] Muse Spark Open Improvement (2026-10-30); 2026-10-30
- **Source URL / scope:** https://github.com/vllm-project/vllm/pull/62345 — [Bugfix][Security] muse: fix quadratic attribute scans in tool-call extraction (2026-10-18); 2026-10-18

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark Open 816B-A42B

## Summary

Parser complexity, FP32 RoPE handling and deployment-image freshness are runtime-specific defects/mitigations. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"- [x] #63871 — Fix dummy-loaded Muse MegaMoE weights"` (vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); gh/vllm-project_vllm_issues_64632.txt L10).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"Bound Muse's ATEM attribute scans to a single tag and avoid reparsing tool calls on streaming deltas that cannot complete an invocation."` (vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); gh2/vllm-project_vllm_pull_62345.txt L4).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"- [x] #62757 — Share one RoPE cache sized by max_model_len"` (vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); gh/vllm-project_vllm_issues_64632.txt L22).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"- [ ] #63078 — Keep FP32 RoPE tables in FP32"` (vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); gh/vllm-project_vllm_issues_64632.txt L23).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. `"There are couple of parallel bug fixes around a tiny accuracy issue that is affecting couple of models including Muse Spark."` (vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); comment by amd-mghanimi, 2026-11-10; gh/vllm-project_vllm_issues_64632.txt L55).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"The attribute classes previously allowed `<`, so a failed attribute search could restart at each open tag and rescan the remaining suffix."`` (vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); gh2/vllm-project_vllm_pull_62345.txt L50).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"The streaming gate checks a window extending `len(close) - 1` characters before the new delta, so delimiters split across deltas still trigger parsing. `max(previous_count, len(calls))` preserves the emission cursor on deltas"`` (vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); gh2/vllm-project_vllm_pull_62345.txt L52).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"| Non-streaming | 1849 ms | 0.99 ms | 0.98 ms |"` (vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); gh2/vllm-project_vllm_pull_62345.txt L65).

## Data/numbers

- `"- [x] #63871 — Fix dummy-loaded Muse MegaMoE weights"`  (vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); gh/vllm-project_vllm_issues_64632.txt L10).
- `"- [x] #62757 — Share one RoPE cache sized by max_model_len"`  (vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); gh/vllm-project_vllm_issues_64632.txt L22).
- `"- [ ] #63078 — Keep FP32 RoPE tables in FP32"`  (vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); gh/vllm-project_vllm_issues_64632.txt L23).
- ``"The streaming gate checks a window extending `len(close) - 1` characters before the new delta, so delimiters split across deltas still trigger parsing. `max(previous_count, len(calls))` preserves the emission cursor on deltas"``  (vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); gh2/vllm-project_vllm_pull_62345.txt L52).
- `"| Non-streaming | 1849 ms | 0.99 ms | 0.98 ms |"`  (vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); gh2/vllm-project_vllm_pull_62345.txt L65).
- `"| Streaming | >25000 ms | 19448 ms | 378 ms |"`  (vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); gh2/vllm-project_vllm_pull_62345.txt L66).

## How it relates to other sources

- **Runtime versus specification:** [Muse Spark Open 816B-A42B — Meta model card](hf-card.md) — RoPE precision and parser defects are implementation findings, not direct contradictions of architecture claims.
- **Different runtime:** [Muse Spark Open on Mac Studio — Apple ML Research](apple-mlx.md) — MLX performance is not a reproduction of vLLM parser/weight/image problems.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
