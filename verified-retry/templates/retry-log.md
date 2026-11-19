# Verified retry log

Task: <one line>
Checker (not editable by the agent): `command` / rubric file / validator
Budget: N tries, M minutes, $X

| Try | Model + settings | Checker result (quoted) | Diff reviewed for tamper? | Cost | Decision |
|---|---|---|---|---|---|
| 1 | | | | | retry / accept / escalate |
| 2 | | | | | |

Escalation rule: same failure class twice -> the spec or the checker is wrong, stop retrying.
Not covered by the checker: <list>
