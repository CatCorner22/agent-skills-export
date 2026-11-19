# Wei-Shaw/sub2api — Muse integration findings

## Source

- **Title:** Wei-Shaw/sub2api — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-12
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/Wei-Shaw_sub2api_pull_8044.txt`.
- **Source URL / scope:** https://github.com/Wei-Shaw/sub2api/pull/8044 — fix(apicompat): add required summary to replayed reasoning input items (2026-10-12); 2026-10-12

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.3

## Summary

Replayed reasoning items need a required summary; a compatibility serialization fix is not proof of broken reasoning in the model. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"A Claude Code (`/v1/messages`) request that replays a thinking block is forwarded to a Responses upstream with a `reasoning` input item that has `encrypted_content` but **no `summary`**."`` (Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); gh2/Wei-Shaw_sub2api_pull_8044.txt L4).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. ``"The Responses API requires `summary` on every reasoning input item (an empty array is valid), and strict upstreams reject the request:"`` (Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); gh2/Wei-Shaw_sub2api_pull_8044.txt L4).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Also verified against a live OpenCode Go upstream: `muse-spark-1.3-contributor` answered 400 to a replayed thinking block before the change and 200 after it, over several multi-turn tool loops; `deepseek-v4.1-flash` and Gemini"`` (Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); gh2/Wei-Shaw_sub2api_pull_8044.txt L21).

## Data/numbers

- ``"A Claude Code (`/v1/messages`) request that replays a thinking block is forwarded to a Responses upstream with a `reasoning` input item that has `encrypted_content` but **no `summary`**."``  (Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); gh2/Wei-Shaw_sub2api_pull_8044.txt L4).
- ``"Also verified against a live OpenCode Go upstream: `muse-spark-1.3-contributor` answered 400 to a replayed thinking block before the change and 200 after it, over several multi-turn tool loops; `deepseek-v4.1-flash` and Gemini"``  (Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); gh2/Wei-Shaw_sub2api_pull_8044.txt L21).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
