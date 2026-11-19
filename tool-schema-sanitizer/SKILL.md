---
name: tool-schema-sanitizer
description: "Rewrite MCP and function tool definitions so strict providers accept them: invalid or digit-leading names, untyped anyOf/oneOf unions, $ref outside $defs, rejected validation keywords, untyped properties, duplicate names, missing descriptions, with per-provider profiles (strict, openai, anthropic, gemini, moonshot). Use when a tool-bearing request returns 400 or schema errors, when adding an MCP server to any agent, or before a provider switch. Ships tool_schema_sanitize.py. Scope boundary: output JSON schemas are skill:structured-output-contract; tool count and token budget are skill:tool-inventory-control."
---

# Tool schema sanitizer

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A request with tools fails validation, an MCP server is added, or the provider changes. One bad tool fails every turn that includes it.

## Steps
1. Dump the exact tool list the harness sends (MCP `tools/list` output or the OpenAI `tools` array) to `tools.json`.
2. `python3 scripts/tool_schema_sanitize.py tools.json --out fixed.json --profile strict`. Default profile applies every rule; `--profile openai|anthropic|gemini|moonshot` relaxes what that provider documents as accepted. Each change is printed; review renames, since the model will see the new name.
3. Use `fixed.json` in requests, or fix the MCP server's schema at the source and re-run until the script exits 0.
4. Keep a name map for renamed tools so results route back to the right server.
5. Prefer small tool catalogs; sanitize again whenever a server updates, and re-check profile rules against the provider's current schema page.

## Evidence
- Moonshot rejects digit-leading names, untyped anyOf and non-$defs $ref (kimi-cli issue 2531, QwenPaw issue 7959, nanobot issue 5040). Issue reports.
- OpenAI strict function calling accepts a JSON Schema subset; OpenAI and Anthropic names match ^[a-zA-Z0-9_-]{1,64}$; Gemini declarations accept an OpenAPI-style subset. Vendor docs; re-check.
- Full notes: [references/evidence.md](references/evidence.md)
