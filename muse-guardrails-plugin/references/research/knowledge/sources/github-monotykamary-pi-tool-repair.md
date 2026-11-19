# monotykamary/pi-tool-repair — Muse integration findings

## Source

- **Title:** monotykamary/pi-tool-repair — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-06
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/monotykamary_pi-tool-repair_pull_6.txt`.
- **Source URL / scope:** https://github.com/monotykamary/pi-tool-repair/pull/6 — feat(grammar): add atem harness leak recovery (2026-10-06); 2026-10-06

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.3

## Summary

ATEM markup recovery mitigates leaked tool syntax; it does not establish which upstream model or harness introduced it. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"Muse Spark models served through tool gateways (observed: muse-spark-1.3-contributor via OpenCode Zen, openai-responses API) sometimes emit their native harness grammar as plain assistant text instead of a structured tool call."` (monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; gh2/monotykamary_pi-tool-repair_pull_6.txt L2).
- Describes a mitigation or verification practice, not a guaranteed universal fix. ``"This adds an opt-in `atem` grammar to the existing grammar-repair pipeline:"`` (monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; gh2/monotykamary_pi-tool-repair_pull_6.txt L4).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. ``"- strip the harness namespace (`default.bash` -> `bash`); names without a pi counterpart (`default.todo`) are dropped, never executed"`` (monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; gh2/monotykamary_pi-tool-repair_pull_6.txt L7).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"- recover complete `<atem:function_calls>` blocks as real toolCall entries (recover mode, known tools only)"`` (monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; gh2/monotykamary_pi-tool-repair_pull_6.txt L6).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"- strip dangling markers from truncated streams; ignore fenced code blocks"` (monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; gh2/monotykamary_pi-tool-repair_pull_6.txt L8).

## Data/numbers

- `"Muse Spark models served through tool gateways (observed: muse-spark-1.3-contributor via OpenCode Zen, openai-responses API) sometimes emit their native harness grammar as plain assistant text instead of a structured tool call."`  (monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; gh2/monotykamary_pi-tool-repair_pull_6.txt L2).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- gh2/monotykamary_pi-tool-repair_pull_6.txt: ATEM markup leak observed on this provider/harness route; opening envelope absence prevents reconstruction of a real call in #15737. Native Muse template syntax alone does not prove an output decoding defect in the model.
