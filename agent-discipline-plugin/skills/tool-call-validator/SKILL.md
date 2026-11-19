---
name: tool-call-validator
description: "Before a tool call with a path, URL, or destructive flag: confirm cwd is the intended workspace, args match the schema, output size is bounded; after it: surface non-zero exits and stderr verbatim and never repeat an identical failing call more than twice without changing something. Use on every shell/file/HTTP tool call in an agent session; hooked as `ad.py hook validate-call`. Scope boundary: blast radius → `scope-and-blast-radius-check`; fetch decisions → `inventory-before-fetch`."
metadata:
  priority: 6
---
# Tool-call validator

Tool misuse looks like model stupidity but is usually mechanical: wrong cwd, a glob that didn't expand, a parser/wrapper mismatch, or the same failing command retried five times.

## Pre-call (5-second check)
- **cwd:** `pwd` matches the repo you mean to touch? Relative paths resolve where you think?
- **Schema:** every required arg present; strings vs lists; flags belong to this tool's version (`--help` once beats three failed guesses).
- **Bound the output:** `-q`, `head`, `--json | jq`, `2>&1 | tail -50`.
- **Destructive flags** (`-f`, `--force`, `--hard`, `-r`) → `scope-and-blast-radius-check`.

## Post-call
- Exit code and stderr, **verbatim**, in your reasoning and your report. "It errored" is not a report.
- Same call failed twice → stop; the hook blocks a third identical attempt. Change the input, the route, or the diagnosis. Write what you changed.
- Empty output is a result: check it is the expected empty, not a wrong path.
- Open-model/wrapper setups: a malformed tool call may be a parser mismatch; verify the JSON shape before blaming the model.

## Banned
Retry loops with no diff · swallowing stderr · `|| true` to make it green · guessing flags four times.
