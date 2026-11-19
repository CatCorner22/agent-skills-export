# anthropics/claude-code — Muse integration findings

## Source

- **Title:** anthropics/claude-code — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-09-17
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/anthropics_claude-code_issues_95021.txt`.
- **Source URL / scope:** https://github.com/anthropics/claude-code/issues/95021 — [BUG] /goal evaluator schema rejected by strict backends: required omits impossible (2026-09-17); 2026-09-17

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.3; Meta Model API

## Summary

The /goal evaluator sends an internally inconsistent strict schema; Meta rejecting that request is not itself a model defect. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. ``"The `/goal` Stop-hook evaluator sends an `output_config.format` JSON schema whose `required` array omits one of its own properties (`impossible`)."`` (anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); gh2/anthropics_claude-code_issues_95021.txt L4).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Any backend that enforces the strict schema subset (`required` must list every key in `properties`) rejects every evaluation with HTTP 400."`` (anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); gh2/anthropics_claude-code_issues_95021.txt L4).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. ``"Reproduced against Meta Model API `/v1/messages` (Anthropic-compatible endpoint, model `muse-spark-1.3`): each turn that reaches Stop while a goal is active fails and the goal never evaluates."`` (anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); gh2/anthropics_claude-code_issues_95021.txt L6).

## Data/numbers

- ``"Any backend that enforces the strict schema subset (`required` must list every key in `properties`) rejects every evaluation with HTTP 400."``  (anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); gh2/anthropics_claude-code_issues_95021.txt L4).
- ``"Reproduced against Meta Model API `/v1/messages` (Anthropic-compatible endpoint, model `muse-spark-1.3`): each turn that reaches Stop while a goal is active fails and the goal never evaluates."``  (anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); gh2/anthropics_claude-code_issues_95021.txt L6).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
