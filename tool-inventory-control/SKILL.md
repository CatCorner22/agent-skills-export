---
name: tool-inventory-control
description: "Keep the set of tools sent to a model small, distinct and well described, loading the rest on demand. Works with any tool-calling API or MCP setup. Use when an agent has more than about 20 tools, picks the wrong tool, ignores tools, or spends a large share of its context on tool schemas. Ships an inventory checker."
---

# Tool inventory control

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
An agent exposes many tools, several MCP servers, or large tool schemas.

## Steps
1. Measure: `python3 scripts/tool_inventory_check.py request.json`. It reports tool count and estimated schema tokens, and flags duplicate or near-duplicate names, missing or short descriptions, near-identical descriptions and oversized parameter lists. Defaults: 30 tools, 8,000 tokens.
2. Split tools into core (always present) and on-demand. Expose a `find_tools(query)` tool that returns matching definitions from a catalog kept outside the prompt.
3. Write descriptions in the form "Use when ...; returns ...". Rename look-alikes. Put rare options behind a single `options` object with described fields.
4. Add on-demand tools by appending so cached prefixes survive; drop them when the step ends.
5. Re-measure after changes; record the token saving and the wrong-tool rate before and after.

## Evidence
- Moonshot K3 tool-calling guide: large inventories eat context and raise wrong-tool picks; load tools per request. Vendor. https://platform.kimi.ai/docs/guide/kimi-k3-tool-calling-best-practice
- Anthropic and OpenAI tool-use guidance makes the same points about tool count and description quality; the script's token estimate (chars/4) is rough.
- Full research notes: [references/evidence.md](references/evidence.md)
