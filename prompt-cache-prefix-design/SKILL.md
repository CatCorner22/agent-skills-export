---
name: prompt-cache-prefix-design
description: "Design request layouts that hit provider prompt caches on Anthropic, OpenAI, Kimi and similar APIs: stable prefix first, dynamic fields last, fixed settings, measured hit rate. Use when building agent loops, batch jobs or chat products that resend a system prompt, tool list or reference text, or when cached token counts stay low. Ships a request checker."
---

# Prompt cache prefix design

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
The same instructions, tools or documents go to the model more than once within the cache window.

## Steps
1. Order requests: system prompt, tool definitions, long reference text, then conversation. Everything stable goes before anything that changes.
2. Remove dynamic text from the stable part: dates, "today is", request IDs, random seeds, user names. Place them in the latest user turn.
3. Keep settings constant per workflow: model, effort or thinking budget, system text. Some providers (Kimi) drop cache hits when reasoning effort changes.
4. Add tools by appending; never reorder or edit earlier tool definitions mid-session.
5. Match the cache window: Anthropic 5 minutes by default (1 hour option), Kimi 5m or 1h TTL, OpenAI automatic on recent prefixes. Keep scheduled jobs inside the window so hits renew.
6. Check two consecutive requests: `python3 scripts/cache_prefix_check.py req1.json req2.json`. It flags dynamic text in the prefix, setting changes, and where the requests first diverge.
7. Measure: read cached-token fields in `usage` per workflow and track the hit rate. Cache writes can cost more than reads; a prefix used once is not worth caching.

## Evidence
- Kimi context caching guide: 1/10 hit price, separate write billing, 5m and 1h TTL, block-based, no dynamic fields in prefix. Vendor. https://platform.kimi.ai/docs/guide/context-caching
- Anthropic and OpenAI document prefix-based caching with similar rules; verify the current windows in their docs before relying on the numbers above.
- Practitioner note: switching Kimi `reasoning_effort` invalidates prefix hits. Single-source. https://prompt-architects.com/blog/261-kimi-k3-prompt-templates-long-context
- Full research notes: [references/evidence.md](references/evidence.md)
