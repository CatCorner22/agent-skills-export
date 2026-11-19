# Sub-agent brief: {task name}

Goal: {one sentence; what done looks like}
Context the sub-agent needs (it sees nothing else):
- Paths/repo: {absolute or repo-relative}
- Facts and decisions already made: {constraints, versions, choices}
- Do not: {files not to touch; no git push; no installs; no credentials; no external posts}

Inputs (attached or by path): {list each by name}
Steps (suggested, not mandatory):
1. {}
2. {}

Return format (exact):
```json
{"status": "ok|blocked|failed", "summary": "<=3 sentences", "evidence": ["command or file:line that proves each claim"], "changed_files": [], "open_questions": []}
```
Budget: {max tool calls}, {max minutes}, {max tokens}. Stop and return status "blocked" when the budget is hit, an input is missing, or the task is unclear. Do not guess.
