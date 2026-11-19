# yetone/magpie — Muse integration findings

## Source

- **Title:** yetone/magpie — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-09–2026-10-31
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/yetone_magpie_issues_1448.txt`, `gh2/yetone_magpie_issues_3152.txt`.
- **Source URL / scope:** https://github.com/yetone/magpie/issues/1448 — gateway: Muse Code on Cline's Muse Spark 1.3 free fails with undeclared_tool (Upstream called a tool not declared by the client) (2026-10-09); 2026-10-09
- **Source URL / scope:** https://github.com/yetone/magpie/issues/3152 — [Bug] Tool calls fail when model emits whole floats (e.g. limit 8.0) - Codex strict int parsing (2026-10-21); 2026-10-21

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.3; Muse Code

## Summary

Undeclared tools and whole-float integer arguments expose gateway/parser boundaries; some proposed causes remain unverified. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns agent workflow behavior; model and orchestration contributions must be separated. `"model failed: stream protocol error: undeclared_tool: Upstream called a tool not declared by the client (response: resp_6ac97ca6d2ed1e1268fc4a6a)"` (yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_1448.txt L7).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"handle_output_item_done:build_tool_call: error=failed to parse tool_search arguments: invalid number"` (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_3152.txt L19).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. ``"A client that parses its tool arguments strictly (Codex reads `tool_search`'s `limit`, `exec_command`'s `yield_time_ms`/`max_output_tokens`, `write_stdin`'s `session_id` as u64/usize/i32 though its own schemas say `number`)"`` (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by ggbdpq, 2026-10-21; gh2/yetone_magpie_issues_3152.txt L66).
- Real-session baseline parse failures versus zero with integral-float normalizer. Gateway/client schema mismatch, not established malformed numeric value from model. `"6/7 and 20/21 parse errors without the fix, 0 in both runs"` (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by ggbdpq, 2026-10-23; gh2/yetone_magpie_issues_3152.txt L135).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"- Sandbox repro (temporary HOME, magpie built from main, real muse 1.4.4, a fake chat-completions upstream): when the upstream calls `bogus_tool`, muse doesn't fail."`` (yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_1448.txt L14).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. ``"It rejects the call as "unknown tool `bogus_tool`", feeds its tool list back to the model and goes on."`` (yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_1448.txt L14).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"A fake upstream that sends this error message mid-stream reproduces the user's error text."` (yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_1448.txt L14).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"In the repro, a chat-stream error chunk `{"error":{"code":"…","message":"…"}}` reached the client as `server_error`, so its code was lost."`` (yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_1448.txt L36).

## Data/numbers

- `"model failed: stream protocol error: undeclared_tool: Upstream called a tool not declared by the client (response: resp_6ac97ca6d2ed1e1268fc4a6a)"`  (yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_1448.txt L7).
- ``"- Sandbox repro (temporary HOME, magpie built from main, real muse 1.4.4, a fake chat-completions upstream): when the upstream calls `bogus_tool`, muse doesn't fail."``  (yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_1448.txt L14).
- ``"failed to parse function arguments: invalid type: floating point `25000.0`, expected u64"``  (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_3152.txt L31).
- ``"failed to parse function arguments: invalid type: floating point `73472.0`, expected i32"``  (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_3152.txt L32).
- ``"Response-side: canonicalize integral-valued float literals in emitted tool-call arguments before forwarding to Codex (`8.0` -> `8`), same value-preserving rule as #6255."``  (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; gh2/yetone_magpie_issues_3152.txt L47).
- ``"A client that parses its tool arguments strictly (Codex reads `tool_search`'s `limit`, `exec_command`'s `yield_time_ms`/`max_output_tokens`, `write_stdin`'s `session_id` as u64/usize/i32 though its own schemas say `number`)"``  (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by ggbdpq, 2026-10-21; gh2/yetone_magpie_issues_3152.txt L66).
- `"Tested the proposed fix end-to-end on Windows 11 with a real Codex + muse-spark session — it resolves the issue for me."`  (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by 1024MrL, 2026-10-23; gh2/yetone_magpie_issues_3152.txt L108).
- ``"A number in a tool call's arguments written with a fraction of zeros (`8.0`, `2500.0`, `-3.00`) reaches the agent without the fraction, on relayed and translated replies, streamed or whole."``  (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by yetone, 2026-10-31; gh2/yetone_magpie_issues_3152.txt L171).
- `"6/7 and 20/21 parse errors without the fix, 0 in both runs"` Real-session baseline parse failures versus zero with integral-float normalizer. Gateway/client schema mismatch, not established malformed numeric value from model. (yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by ggbdpq, 2026-10-23; gh2/yetone_magpie_issues_3152.txt L135).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
