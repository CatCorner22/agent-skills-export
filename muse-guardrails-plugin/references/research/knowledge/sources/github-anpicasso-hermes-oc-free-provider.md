# anpicasso/hermes-oc-free-provider — Muse integration findings

## Source

- **Title:** anpicasso/hermes-oc-free-provider — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-01
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/anpicasso_hermes-oc-free-provider_issues_3.txt`.
- **Source URL / scope:** https://github.com/anpicasso/hermes-oc-free-provider/issues/3 — Blank replies in OpenWebUI when streaming (2026-10-01); 2026-10-01

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.3

## Summary

Streaming deltas contain text that OpenWebUI does not receive correctly; provider-adapter parsing is implicated. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"OpenWebUI shows empty replies for `muse-spark-1.3-contributor-free`, only when streaming."`` (anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); gh2/anpicasso_hermes-oc-free-provider_issues_3.txt L2).
- Describes a mitigation or verification practice, not a guaranteed universal fix. `"- Workaround: switch the Hermes connection in OpenWebUI to Responses API type"` (anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); gh2/anpicasso_hermes-oc-free-provider_issues_3.txt L18).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Reply bubble stays empty, but non-streaming (`stream:false`) to same endpoint returns text fine"`` (anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); gh2/anpicasso_hermes-oc-free-provider_issues_3.txt L11).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Actual: zero text deltas, clean `stop`, with `completion_tokens > 0`"`` (anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); gh2/anpicasso_hermes-oc-free-provider_issues_3.txt L14).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"- Other not OpenCode models stream fine, so looks like the Responses -> Chat translator drops the text"` (anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); gh2/anpicasso_hermes-oc-free-provider_issues_3.txt L17).

## Data/numbers

- ``"OpenWebUI shows empty replies for `muse-spark-1.3-contributor-free`, only when streaming."``  (anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); gh2/anpicasso_hermes-oc-free-provider_issues_3.txt L2).
- ``"Actual: zero text deltas, clean `stop`, with `completion_tokens > 0`"``  (anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); gh2/anpicasso_hermes-oc-free-provider_issues_3.txt L14).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
