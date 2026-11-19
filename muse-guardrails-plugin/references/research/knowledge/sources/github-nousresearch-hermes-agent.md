# NousResearch/hermes-agent — Muse integration findings

## Source

- **Title:** NousResearch/hermes-agent — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-04–2026-10-20
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/NousResearch_hermes-agent_issues_132837.txt`, `gh2/NousResearch_hermes-agent_issues_141861.txt`, `gh2/NousResearch_hermes-agent_pull_140813.txt`.
- **Source URL / scope:** https://github.com/NousResearch/hermes-agent/issues/132837 — opencode-go: supports_vision_tool_messages=False veto is stale on responses/codex transport — native tool-result vision works live (2026-10-04); 2026-10-04
- **Source URL / scope:** https://github.com/NousResearch/hermes-agent/issues/141861 — [bug] Kanban worker posts chat/completions despite resolved api_mode=codex_responses: muse-spark on opencode-go gets 400 ModelProtocolUnsupported (2026-10-20); 2026-10-20
- **Source URL / scope:** https://github.com/NousResearch/hermes-agent/pull/140813 — fix(agent): accept reasoning effort max on Muse Spark 1.3 (2026-10-18); 2026-10-18

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.2; Muse Spark 1.3

## Summary

Vision flags, reasoning-effort clamping and worker transport propagation differ from live provider capability. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Bounds supported capabilities or reliability; it does not establish universal failure. ``"`OpenCodeGoProfile` sets `supports_vision_tool_messages=False` (`plugins/model-providers/opencode-zen/__init__.py`), citing Console-Go #104731 (`422 messages.N.tool.content.str`) and MiMo #47026 (`400 text is not set`)."`` (NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_132837.txt L3).
- Bounds supported capabilities or reliability; it does not establish universal failure. ``"Kanban worker on profile `readwhere` (model `muse-spark-1.3-contributor`, provider `opencode-go`) fails every LLM call with HTTP 400 `ModelProtocolUnsupported` ("Model does not support this protocol")."`` (NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_141861.txt L4).
- Describes a mitigation or verification practice, not a guaranteed universal fix. ``"Hermes clamped `max` down to `xhigh` on both the direct Meta route and the OpenCode Zen/Go Responses route, because those paths used a vocabulary that stopped at `xhigh`."`` (NousResearch/hermes-agent#140813, 2026-10-18; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_pull_140813.txt L5).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"The same model + provider + key works fine in regular (Telegram/CLI) sessions and via direct `POST /responses`."`` (NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_141861.txt L4).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. ``"- `POST /zen/go/v1/responses` `{model: muse-spark-1.3-contributor, input, max_output_tokens: 32}` → **200** with reasoning output."`` (NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_141861.txt L18).
- Bounds supported capabilities or reliability; it does not establish universal failure. ``"- `agent/image_routing._lookup_supports_vision('opencode-go', 'muse-spark-1.3-contributor')` → **True**, `decide_image_input_mode` → **native** (the model IS catalogued vision-capable)"`` (NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_132837.txt L11).
- Bounds supported capabilities or reliability; it does not establish universal failure. ``"- but `tools/vision_tools._accepts_tool_result_images` → **False**, veto first (`:564`) — so `vision_analyze`/`computer_use` captures always fall back to the aux-LLM text downgrade on Go, needlessly."`` (NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_132837.txt L12).
- Bounds supported capabilities or reliability; it does not establish universal failure. ``"Scope the veto to chat-completions transports: only return `supports_vision_tool_messages=False` for opencode-go when the active transport is chat-completions, and allow native tool-result media on responses/codex."`` (NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_132837.txt L15).

## Data/numbers

- ``"`OpenCodeGoProfile` sets `supports_vision_tool_messages=False` (`plugins/model-providers/opencode-zen/__init__.py`), citing Console-Go #104731 (`422 messages.N.tool.content.str`) and MiMo #47026 (`400 text is not set`)."``  (NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_132837.txt L3).
- ``"- `agent/image_routing._lookup_supports_vision('opencode-go', 'muse-spark-1.3-contributor')` → **True**, `decide_image_input_mode` → **native** (the model IS catalogued vision-capable)"``  (NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_132837.txt L11).
- ``"- but `tools/vision_tools._accepts_tool_result_images` → **False**, veto first (`:564`) — so `vision_analyze`/`computer_use` captures always fall back to the aux-LLM text downgrade on Go, needlessly."``  (NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_132837.txt L12).
- ``"Kanban worker on profile `readwhere` (model `muse-spark-1.3-contributor`, provider `opencode-go`) fails every LLM call with HTTP 400 `ModelProtocolUnsupported` ("Model does not support this protocol")."``  (NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_141861.txt L4).
- ``"- `POST /zen/go/v1/responses` `{model: muse-spark-1.3-contributor, input, max_output_tokens: 32}` → **200** with reasoning output."``  (NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_issues_141861.txt L18).
- ``"- `plugins/model-providers/meta-ai/__init__.py`: `build_api_kwargs_extras` clamps with `meta_ai_supported_efforts(model)` instead of the shared 1.2 ceiling."``  (NousResearch/hermes-agent#140813, 2026-10-18; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_pull_140813.txt L26).
- ``"Confirm `max` stays `max` for `muse-spark-1.3*` on meta-ai, opencode-go, and opencode-zen, and that `muse-spark-1.2` / `muse-spark` still clamp `max` to `xhigh`."``  (NousResearch/hermes-agent#140813, 2026-10-18; attribution: harness/router-side (dispatch/capability/effort handling); gh2/NousResearch_hermes-agent_pull_140813.txt L32).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
