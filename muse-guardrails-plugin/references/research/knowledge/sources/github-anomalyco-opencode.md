# anomalyco/opencode — Muse integration findings

## Source

- **Title:** anomalyco/opencode — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-09-13–2026-10-24
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/anomalyco_opencode_issues_48741.txt`, `gh2/anomalyco_opencode_issues_51649.txt`, `gh2/anomalyco_opencode_issues_57804.txt`.
- **Source URL / scope:** https://github.com/anomalyco/opencode/issues/48741 — Opencode Zen critical errors on Muse Spark family when model recieves a image/does a tool call (2026-09-13); 2026-09-13
- **Source URL / scope:** https://github.com/anomalyco/opencode/issues/51649 — Infinite response loop or smth issue (2026-09-27); 2026-09-27
- **Source URL / scope:** https://github.com/anomalyco/opencode/issues/57804 — Model Beam Free stuck in a loop thinking and reading (2026-10-21); 2026-10-21

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.2; Muse Spark 1.3

## Summary

Stale encrypted reasoning, repeated responses and model aliases produce failures with route/session-dependent and partly unresolved causes. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Error: Error from provider (Console): Upstream request failed: [invalid_request_error] reasoning `encrypted_content` was not issued to this caller when requesting any Muse Spark model on Zen."`` (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); gh2/anomalyco_opencode_issues_48741.txt L4).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. `"With Muse Spark 1.3 free model (at least with this model), there is an issue where the shell command is executing and has been executing at the same time thinking process of the model is executing and when the shell thing ends"` (anomalyco/opencode#51649, 2026-09-27; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); gh2/anomalyco_opencode_issues_51649.txt L4).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. `"> * [[OpenCode Go] muse-spark-1.3-contributor gets stuck in repeated Read/Search loops and fails t"` (anomalyco/opencode#57804, 2026-10-21; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by zzz-creator, 2026-10-21; gh2/anomalyco_opencode_issues_57804.txt L75).
- Concerns open-weight deployment/training or licensing, not necessarily hosted inference. ``"Proper fix still belongs in core (drop + retry without the blob on `invalid_encrypted_content`)."`` (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by unurgunite, 2026-09-13; gh2/anomalyco_opencode_issues_48741.txt L100).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. `"Whenever you just idle it for 3 minutes or 5 minutes, the next chat will get this error."` (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by MrSaikatS, 2026-09-13; gh2/anomalyco_opencode_issues_48741.txt L109).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"Fixed by creating new session, but even on this new session it will have this problem again so I can't have long sessions."` (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by pegasusearl, 2026-09-13; gh2/anomalyco_opencode_issues_48741.txt L76).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Same root cause as #43557: after a restart, OpenCode replays the stale `reasoning.encrypted_content` blob (bound to the previous caller/key) and upstream rejects it with `not issued to this caller`."`` (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by unurgunite, 2026-09-13; gh2/anomalyco_opencode_issues_48741.txt L96).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"It fixed my old sessions However the next error will still happen, I tried two attempts and both failed, same error message."` (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by pegasusearl, 2026-09-13; gh2/anomalyco_opencode_issues_48741.txt L118).

## Data/numbers

- ``"Same root cause as #43557: after a restart, OpenCode replays the stale `reasoning.encrypted_content` blob (bound to the previous caller/key) and upstream rejects it with `not issued to this caller`."``  (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by unurgunite, 2026-09-13; gh2/anomalyco_opencode_issues_48741.txt L96).
- `"Whenever you just idle it for 3 minutes or 5 minutes, the next chat will get this error."`  (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by MrSaikatS, 2026-09-13; gh2/anomalyco_opencode_issues_48741.txt L109).
- `"In our case the poisoned turn broke mid-tool-chain, and everything after it failed for a day: service-restart drains, fresh prompts, and compaction all hit the same 400."`  (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by darkred1145, 2026-09-14; gh2/anomalyco_opencode_issues_48741.txt L172).
- `"Same error on 1.18.30 when **resuming an old Muse 1.3 session after idle** (no image required)."`  (anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by 1837620622, 2026-09-14; gh2/anomalyco_opencode_issues_48741.txt L189).
- `"With Muse Spark 1.3 free model (at least with this model), there is an issue where the shell command is executing and has been executing at the same time thinking process of the model is executing and when the shell thing ends"`  (anomalyco/opencode#51649, 2026-09-27; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); gh2/anomalyco_opencode_issues_51649.txt L4).
- ``"The free Muse models (`muse-spark-1.2-contributor-free` and `muse-spark-1.3-contributor-free`) have been removed from the free tier, so this no longer applies."``  (anomalyco/opencode#51649, 2026-09-27; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by Tarquinen, 2026-10-20; gh2/anomalyco_opencode_issues_51649.txt L39).
- `"> * [[OpenCode Go] muse-spark-1.3-contributor gets stuck in repeated Read/Search loops and fails t"`  (anomalyco/opencode#57804, 2026-10-21; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by zzz-creator, 2026-10-21; gh2/anomalyco_opencode_issues_57804.txt L75).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- gh2/anomalyco_opencode_issues_48741.txt: Distinct users report restart, idle, images, or mid-tool-chain variants; stripping stale encrypted reasoning helps some sessions, others fail again. Provider IP/key binding remains unverified; no single universal cause established.
- gh2/anomalyco_opencode_issues_57804.txt: Main issue is Beam, not Muse. Retain only explicit Muse-related cross-reference, not other-model loops as independent Muse evidence.
