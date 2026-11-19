# Task contract (generation: 1, date: YYYY-MM-DD)

## Job
One paragraph: what to produce and for whom.

## Finish line
- Files to change: ...
- Checks that must pass: `command` ...
- Deliverable format: ...

## Effective instructions (this block replaces all earlier instruction blocks)
1. ...
2. ...

## Boundaries
- Do not install packages, use credentials, call external services or delete files unless listed here.
- Do not change files outside: ...
- If the task is ambiguous or an input is missing: stop and report; do not guess.

## State (owned by the harness; do not infer from history)
- Done: ...
- Pending: ...
- Counts/dates/versions: ...

## Inputs present
- `filename` (what it is)

## Output shape
```
<schema or labeled template; use "unknown" for anything unsupported>
For a sub-agent: {"status": "ok|blocked|failed", "summary": "<=3 sentences", "evidence": ["command or file:line that proves each claim"], "changed_files": [], "open_questions": []}
```

## Stop rule
Stop when the finish-line checks pass, or after N tool calls / M minutes, or when blocked. Report which one.
