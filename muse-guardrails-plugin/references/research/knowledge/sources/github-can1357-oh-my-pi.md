# can1357/oh-my-pi — Muse integration findings

## Source

- **Title:** can1357/oh-my-pi — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-09-17–2026-10-16
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/can1357_oh-my-pi_issues_12306.txt`, `gh2/can1357_oh-my-pi_issues_15551.txt`, `gh2/can1357_oh-my-pi_issues_15737.txt`.
- **Source URL / scope:** https://github.com/can1357/oh-my-pi/issues/12306 — opencode-zen: muse-spark-1.3-contributor-free returns 403 FreeTierError in OMP while working in OpenCode (2026-09-17); 2026-09-17
- **Source URL / scope:** https://github.com/can1357/oh-my-pi/issues/15551 — /usage: muse-code shows "no usage data" after Meta account token expires — no re-login hint (refresh "none") (2026-10-13); 2026-10-13
- **Source URL / scope:** https://github.com/can1357/oh-my-pi/issues/15737 — muse-code/muse-wonder-1.0` prints tool-call markup as plain text instead of making a tool call (2026-10-14); 2026-10-14

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.3; Muse Wonder / Full where specified; Muse Code; Meta Model API; Meta AI / meta.ai

## Summary

Free-tier gates, expired-token usage UI and Wonder tool markup are separate failures; later probes qualify early hypotheses. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. ``"`muse-spark-1.3-contributor-free` works successfully through OpenCode, but the same model returns HTTP 403 `FreeTierError` when used through OMP."`` (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_12306.txt L4).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"`/usage` (and `omp usage --provider muse-code`) shows `Muse Code — 1 account, no usage data` once the Meta account OAuth token expires."`` (can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_15551.txt L4).
- Maps the product or interface rather than measuring success. ``"Using the built-in `muse-code` provider with `muse-wonder-1.0` (auto-discovered after logging in with a Muse Code subscription, default catalog entry, no custom `models.yml`), the assistant when finishing prewalk wrote the"`` (can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_15737.txt L7).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. ``"- omp's leak-repair code (`packages/ai/src/utils/stream-markup-healing.ts`, chosen by `detectStreamMarkupHealing` in `packages/catalog/src/compat/resolve.ts`) only covers documented chat-template formats on OpenAI-compatible chat"`` (can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by roboomp, 2026-10-14; gh2/can1357_oh-my-pi_issues_15737.txt L73).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. `"403 Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"` (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_12306.txt L9).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. ``"The same API key that gets `403 (type=FreeTierError) OpenCode's free tier can only be used from within OpenCode` from OMP succeeds from the genuine `opencode` CLI, so nothing is wrong with the key, the account, or the model id."`` (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by insodimension, 2026-09-18; gh2/can1357_oh-my-pi_issues_12306.txt L198).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. `"Fabricated session IDs always return 403 FreeTierError regardless of headers, endpoint path, or tool count."` (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by Lakshit-Gupta, 2026-10-13; gh2/can1357_oh-my-pi_issues_12306.txt L230).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Following up on the 2026-10-13 report that the header patch stopped working because Zen now validates `x-opencode-session` as a server-registered session: I could not reproduce that today (2026-10-16)."`` (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by jaskaran-ai, 2026-10-16; gh2/can1357_oh-my-pi_issues_12306.txt L257).

## Data/numbers

- ``"`muse-spark-1.3-contributor-free` works successfully through OpenCode, but the same model returns HTTP 403 `FreeTierError` when used through OMP."``  (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_12306.txt L4).
- `"403 Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"`  (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_12306.txt L9).
- ``"The same API key that gets `403 (type=FreeTierError) OpenCode's free tier can only be used from within OpenCode` from OMP succeeds from the genuine `opencode` CLI, so nothing is wrong with the key, the account, or the model id."``  (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by insodimension, 2026-09-18; gh2/can1357_oh-my-pi_issues_12306.txt L198).
- `"Fabricated session IDs always return 403 FreeTierError regardless of headers, endpoint path, or tool count."`  (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by Lakshit-Gupta, 2026-10-13; gh2/can1357_oh-my-pi_issues_12306.txt L230).
- ``"Following up on the 2026-10-13 report that the header patch stopped working because Zen now validates `x-opencode-session` as a server-registered session: I could not reproduce that today (2026-10-16)."``  (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by jaskaran-ai, 2026-10-16; gh2/can1357_oh-my-pi_issues_12306.txt L257).
- ``"So the bridge turns the loud refusal into a quiet wrong answer. `/v1/responses` returns the actual text. `/v1/chat/completions` returns 200 with an empty `content` and no error, which most clients read as success."``  (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by ebouther, 2026-10-16; gh2/can1357_oh-my-pi_issues_12306.txt L300).
- ``"Worth settling for #12556 before the gate work: routing this id as `openai-responses` is the right call, because a chat-shaped path doesn't fail loudly here, it returns nothing."``  (can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by ebouther, 2026-10-16; gh2/can1357_oh-my-pi_issues_12306.txt L302).
- ``"`/usage` (and `omp usage --provider muse-code`) shows `Muse Code — 1 account, no usage data` once the Meta account OAuth token expires."``  (can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_15551.txt L4).
- ``"The underlying error is a 401 from `POST https://api.meta.ai/muse-code/key`, visible only in debug logs."``  (can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_15551.txt L4).
- ``"I'm triaging this as an enhancement, not a bug: the 401 is Meta revoking an account token that OMP has no way to refresh, and `/usage` currently gives the same generic row for every kind of usage-fetch failure."``  (can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by roboomp, 2026-10-13; gh2/can1357_oh-my-pi_issues_15551.txt L52).
- ``"Using the built-in `muse-code` provider with `muse-wonder-1.0` (auto-discovered after logging in with a Muse Code subscription, default catalog entry, no custom `models.yml`), the assistant when finishing prewalk wrote the"``  (can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); gh2/can1357_oh-my-pi_issues_15737.txt L7).
- ``"- `muse-code` runs `muse-wonder-1.0` over `openai-responses` with native function calling (`packages/catalog/src/compat/rules/providers/muse-code.kdl`, which inherits the `meta` seed rows). omp sends structured `tools` and reads"``  (can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by roboomp, 2026-10-14; gh2/can1357_oh-my-pi_issues_15737.txt L71).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- gh2/can1357_oh-my-pi_issues_12306.txt: Free-tier client gate can be intentional policy. Later October 16 test could not reproduce required registered-session claim; preserve disagreement. Empty Chat-vs-Responses bridge verified in captured report; do not promote an IP theory to confirmed Meta cause.
- gh2/can1357_oh-my-pi_issues_15737.txt: ATEM markup leak observed on this provider/harness route; opening envelope absence prevents reconstruction of a real call in #15737. Native Muse template syntax alone does not prove an output decoding defect in the model.
