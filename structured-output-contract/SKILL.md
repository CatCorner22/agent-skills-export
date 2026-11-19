---
name: structured-output-contract
description: "Make model JSON output parse and conform on any provider: normalize the schema to the strict subset (all required, additionalProperties false, optional fields nullable, rejected keywords dropped), validate the returned JSON against it, strip fences and prose, and run one bounded repair pass with a generated repair prompt. Use when code parses model output, when json_schema requests are rejected, when outputs come back fenced or with extra keys, and when a pipeline silently accepts malformed JSON. Ships structured_output.py normalize|validate. Scope boundary: tool/function schemas are skill:tool-schema-sanitizer."
---

# Structured output contract

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
Downstream code will parse what the model returns.

## Steps
1. Write the schema you actually need. Mark fields you cannot guarantee as optional; the normalizer turns them nullable rather than letting the model invent values. Allow the string `"unknown"` where a value may be unsupported.
2. `python3 scripts/structured_output.py normalize schema.json --out strict.json`. It drops keywords strict validators reject, sets `additionalProperties: false` and `required` for every object. Use `strict.json` in the request (`response_format` json_schema with strict true, or the provider's equivalent) and in validation.
3. Ask for JSON only, no fence, no prose, and parse `message.content`; never parse reasoning fields.
4. `python3 scripts/structured_output.py validate strict.json output.json --repair-prompt`. It strips a fence or leading prose (and reports that), then checks types, required, extra keys, enums and nested items. On violations it prints a repair prompt listing each one.
5. Retry at most once with the repair prompt plus the original request. A second failure is a schema or task problem: loosen the schema, split the task, or route to a model with native strict mode.
6. Log validation failures per field; a field that fails often is one the model cannot fill from the inputs and should become nullable or be removed.

## Evidence
- OpenAI strict mode and Moonshot's validator accept a JSON Schema subset (all properties required, additionalProperties false, limited keywords); other providers differ in which keywords they reject. Vendor docs; re-check.
- Provider-adapter bugs forward unsupported keywords verbatim and fail whole requests (kimi-cli issue 2531, nanobot issue 5040). Issue reports.
- Fenced JSON and leading prose are the most common parse failures in practice across models. Practitioner.
- Full notes: [references/evidence.md](references/evidence.md)
