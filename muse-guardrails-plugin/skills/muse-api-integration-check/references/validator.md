# Response checker contract and issue-modelled coverage

This is a supplemental, pure response check, not the generic tool-call-validator, a complete JSON Schema implementation, a streaming assembler, a replay serializer or permission to execute tools. It performs no network access, tool execution or filesystem access in `check_response`; only the CLI reads its specified input.

## Inputs and outputs

`check_response(response, declared_tools=None, tool_schemas=None, coerce_whole_floats=False)` accepts a parsed canonical Chat Completions or Responses JSON object. The CLI takes an envelope using those same keys through `--json` (object string, file or stdin `-`). Tool declarations are unique, exact function-name strings, not provider tool-definition objects; schemas map each name to its parameter schema.

- `ok` means no error-level flag from these checks, not factual correctness, task completion, full-schema validity or action approval.
- Empty visible text is always flagged: error for empty/reasoning-only responses, info for a structured tool-only continuation. Invalid/undeclared calls still cause errors. Hidden reasoning is not exposed as a visible answer.
- Chat length termination and Responses max-output-token incompleteness cause errors even with partial text. Non-completed Responses status also blocks acceptance. Upstream error objects and malformed/unknown structures are failures.
- Tool markup detection is a heuristic for ATEM open/closing tags and common tool-call markers outside fenced code; explanatory examples in fences are ignored. Prose discussing markup can still be flagged. Never promote detected text into executable calls or infer a tool name from dangling tags.
- Tool names must match the supplied allowlist exactly; absent declarations block calls. Namespace stripping is NOT performed. Missing schemas warn and set schema_checked false; a real full-schema validator is still required before execution.
- Arguments must decode to an object. This checker traverses object properties, required keys, additionalProperties and arrays/items; validates basic scalar types, enum and minimum/maximum; and blocks unsupported keywords rather than pretending to apply them. Supported annotation keys are title, description, default and $schema; defaults are never inserted. Full schema handling remains with the existing generic skill.
- Integer fields reject bools, strings and fractional/nonfinite floats. With explicit opt-in, finite integral floats with absolute value ≤2^53−1 normalize to int; all supplied bounds still apply. Large floats are rejected because their original precision cannot be trusted. Existing JSON integers remain exact. No rounding, clamping or unsigned/range assumptions are inferred from a field name.
- Normalized tool calls are copied proposals labelled with source JSON paths, never executed; input objects and schemas remain unchanged. Multiple Chat choices remain labelled alternatives, not a merged executable plan.
- CLI exit codes: 0 accepted by the supplemental checks; 1 response flags contain errors; 2 invalid configuration/CLI JSON/file. Raw SSE, extra trailing data and nonfinite JSON constants are rejected rather than silently parsed as a full completion. No usage/billing/auth state is verified.

## Fixture provenance

All fixtures are small synthetic JSON bodies modelled on captured public issues, not captured private responses or local reproductions. The report date is 2026-11-10; issue origins/fix lifecycle can be uncertain.

| Fixture theme | Source | Report confidence/scope |
|---|---|---|
| Reasoning exhausts output budget / empty success | decolua/9router #4387 and #4736 | Report §4 theme 1 ungraded individually; family F7 (§7) Probable |
| Wrong protocol error body | decolua/9router #4602/#4624 | Report §4 theme 2; route/harness-specific, individually ungraded |
| Dangling ATEM tags instead of structured calls | can1357/oh-my-pi #15737; monotykamary/pi-tool-repair PR #6 | Report §4 theme 3 Probable; incomplete markup cannot reconstruct a call |
| Undeclared tool | yetone/magpie #1448 | Report §4 theme 4 ungraded individually; family F10 (§7) Established, upstream attribution unclear |
| Integral floats / client integer contract | yetone/magpie #3152 | Report §4 theme 5 ungraded individually; family F10 (§7) Established, not proof of malformed numerical value from the model |

Encrypted reasoning replay requires request-side serialization work (sub2api PR #8044); no response-only check can guarantee replay summary presence or blob/session validity. Strict schema, auth, token expiry, region policy and budget issues likewise require the API skill's non-script checks.
