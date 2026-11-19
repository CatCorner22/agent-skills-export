---
name: muse-api-integration-check
description: "Check empty replies and integration defects in Muse, Muse Spark, Muse Wonder, Meta AI, or Meta Model API; Scope boundary: skill:tool-call-validator, skill:completion-evidence-gate, and skill:model-sanity-regression own generic schema, success, and regression gates."
---

# Muse API integration check

## When it fires
Use when adding/changing a Muse route, parser, SDK, effort or token budget, and on empty replies, schema/tool errors, replay failures, 403s or unexplained usage.

## Steps
1. Record exact provider/model/version, endpoint, SDK/harness, region, tier and effort; apply `skill:model-sanity-regression` for the generic baseline. Must probe documented Chat Completions versus Responses support on THIS route, not assume conflicting reports establish one universal protocol.
2. Set a generous, route-valid output budget that leaves space after reasoning, bounded by the client budget; must inspect visible output and termination, not HTTP 200 alone. The reported 8,000-token router clamp is route-specific history, not a guaranteed minimum/fix or permission to spend without a cap.
3. Run [muse_response_check.py](scripts/muse_response_check.py) on the completed JSON response with the actual declared tool names and parameter schemas; must fail over or retry within a bounded budget on reasoning-only empty output, truncation or malformed calls. A valid structured tool-only turn is continuation, not an empty-answer failure or completed user task.
4. Apply `skill:tool-call-validator` to the full schema and execution contract. For strict json_schema rejection/ignoring, use only a documented compatible structured mode or plain JSON fallback and independently validate the FULL result; must not mark fallback output strict without validation.
5. Reject undeclared tool names, empty/malformed arguments and fractional/bool/string values for integer fields; optional whole-float coercion may preserve only finite, safe-range integral values satisfying declared bounds. Must not widen the allowlist or change a schema merely to accept a model call.
6. Treat visible tool markup, including dangling ATEM tags, as possible leakage, never executed work; must not execute recovered text automatically. Preserve redacted protocol evidence and use `skill:completion-evidence-gate` for success claims.
7. For Responses reasoning replay, preserve required summary (an empty array was accepted on the reported route), route/session binding and supported opaque fields; must not invent hidden reasoning, reuse stale encrypted blobs indiscriminately or assume the response checker validates replay inputs.
8. Check capability contracts before depending on logprobs or a non-reasoning mode, reported unavailable in the captured Meta Model API; must not manufacture scores or assume lowering effort disables reasoning.
9. Set a client-side request/token/currency budget with reserved in-flight cost, bounded retries and stop behavior when usage is missing; reconcile local accounting with provider records. Must not treat email alerts or a blank usage meter as a hard spending cap/free inference.
10. On region/free-tier 403 or token expiry, stop blind retries, verify official eligibility and refresh supported auth through the trusted flow; must not spoof regions, session IDs or headers to bypass policy. Log redacted status, not credentials, and distinguish expiration/accounting symptoms from a proven provider cause.

## Validator contract
From the plugin root: `python skills/muse-api-integration-check/scripts/muse_response_check.py --json input.json` (also accepts a JSON object string or `-` for stdin).
Input: `{ "response": { ... }, "declared_tools": ["search"], "tool_schemas": {"search": {"type":"object","properties":{"limit":{"type":"integer","minimum":0}}}}, "coerce_whole_floats": false }`.
Output: `ok`, protocol, visible text, flags with severity/path, normalized tool calls and coercion records; invalid responses exit 1, invalid CLI/config input exits 2. Must not execute any returned call automatically.
The pure checker handles completed Chat/Responses JSON, not raw SSE deltas, replay requests, HTTP/auth, complete JSON Schema or proof of factual/task success. Unsupported schema constraints block its tool check; use the existing full validator rather than ignoring them. Whole-float normalization is explicit opt-in and never mutates the input.

## Evidence
- **Family F7 (§7) — Probable; report §4 themes 1–2:** 9router #4736/#4387 and #4602/#4624, hermes #141861; empty-success/protocol symptoms mix upstream and harness causes; individual issues are not separately confidence-graded.
- **Report §4 theme 3 — Probable:** oh-my-pi #15737 and pi-tool-repair PR #6 report markup-as-text; closing tags alone cannot reconstruct a genuine call.
- **Family F10 (§7) — Established family-level evidence; §4 themes 4–7:** magpie #1448/#3152, llama.cpp PR #32017, claude-code #95021, sub2api PR #8044; preserve unclear/mixed attribution, not “all model defects.” These individual issues are ungraded in §4 except theme 3.
- **Report §2.5–6 — Probable; M6 (§7), §4 theme 9:** cookbook #57 and HN spending-cap reports; auth/usage issues include oh-my-pi #15551/#12306. Policy versus defect is unresolved for free-tier access.
- [Report](../../references/research/report.md), [issue evidence](../../references/research/evidence.md), [validator details](references/validator.md). Fixtures are modelled on captured issues, not live reproductions; no issue lifecycle or current fix status is inferred beyond the dated report.
