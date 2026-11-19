---
name: provider-migration-checklist
description: "Move an application between model providers or hosts (OpenAI, Anthropic, Google, Moonshot, Bedrock, Foundry, OpenRouter, self-host) without silent regressions: a parity table for context, max tokens, reasoning controls, history round-trip, tool and structured-output rules, caching, usage field names, rate-limit units, unsupported parameters and data terms, plus a repeat-measured probe and a usage-field normalizer. Use before any provider or host switch, when behavior changes after one, or when billing fields come back empty. Ships migration-probe template and usage_normalize.py. Scope boundary: choosing which model is skill:model-router; cost analysis is skill:cost-per-task-meter."
---

# Provider migration checklist

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
Before the first production call on a new provider or host, and whenever quality, latency, cost or error rates change without a code change.

## Steps
1. Fill the parity table in `templates/migration-probe.md` from current docs for both sides. Write "unknown" rather than assuming parity; OpenAI-compatible means the request shape, not the features.
2. Normalize accounting first: `python3 scripts/usage_normalize.py responses.jsonl --out norm.jsonl` maps OpenAI, Anthropic and Gemini usage shapes to one record and lists fields the new provider does not return, so cache or reasoning tokens do not silently become zero in your dashboards.
3. Check the parameters that 400 on one side and are ignored on the other (temperature, top_p, penalties, reasoning controls, max tokens floor or cap); remove or branch them per provider.
4. Confirm reasoning history round-trips (field name, accepted on replay) and that tool schemas pass the new validator (skill:tool-schema-sanitizer).
5. Run the probe: the same 20 tasks, same harness, three repeats on the old provider first to measure noise; then the new one. Only differences larger than the noise band count. Score tool calls separately from text quality.
6. Record provider, model id, region and date in run logs; keep the rollback path for one release cycle.

## Evidence
- Hosted Kimi on Bedrock, Foundry/Fireworks and Moonshot differ in caching, effort controls and model entries; the same pattern holds for GPT and Claude across Azure, Bedrock, Vertex and first-party endpoints. Vendor docs.
- Adapter bugs on migration: `cache_creation_tokens` attribute errors, empty usage, unsupported-keyword 400s (OpenHands, LiteLLM, kimi-cli issues). Issue reports.
- Full notes: [references/evidence.md](references/evidence.md)
