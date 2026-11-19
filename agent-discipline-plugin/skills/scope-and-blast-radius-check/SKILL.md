---
name: scope-and-blast-radius-check
description: "Before delete, drop, rm, force, reset, overwrite, deploy, migrate, publish, 'recreate the environment', or any absolute/~ path: resolve targets, confirm they are inside declared scope, classify reversible vs irreversible, and for irreversible actions stage everything then ask a one-word go-ahead. After any write, do a read-after-write check. Enforced by the scope-fence hook (`ad.py hook scope-fence`, `ad.py scope set`). Scope boundary: permission bookkeeping → `autonomy-ledger`; command-shape errors → `tool-call-validator`."
metadata:
  priority: 9
  bashPatterns:
    - '\b(rm\s+-r|git\s+push\s+--force|git\s+reset\s+--hard|drop\s+table|terraform\s+destroy|kubectl\s+delete|vercel\s+--prod|npm\s+publish)\b'
    - '\bad\.py (scope|fence-check)\b'
---
# Scope and blast-radius check

Documented incidents: a prod database wiped during a code freeze, `~` expanding to home and deleting a user's files, a dev/prod mix-up taking down a region. Common thread: the agent acted on a path or target it had not resolved, in an environment it had not confirmed.

## Before the action
1. **Declare scope once:** `ad.py scope set <repo root> [more roots] [--allow REGEX]`. Everything else is out of bounds for writes.
2. **Resolve every target:** absolute path (`realpath`), what `~`/`$VAR`/globs expand to, which database/cluster/account the connection string points at. Print it.
3. **Classify:** reversible (git checkout/revert, deleting a file you created, local rollback) → do it. Irreversible (listed in `scope-fence` DESTRUCTIVE: recursive delete, force push, history rewrite, prod deploy, publish, merge, non-local DB mutation) → step 4.
4. **Irreversible:** stage all reversible prep, show the exact command and resolved targets, ask for a one-word go-ahead, record it: `ad.py ledger add GRANT "<label>: <exact command>"`. The hook then lets exactly that through.

## After any write
Read-after-write before the next step: `ls -la`, `git status --short`, `wc -l`, `SELECT count(*)`, HTTP status. Report the number.

## Rules
- Dev/prod ambiguity is a hard stop: name the env in the command (`--env dev`, explicit DSN) or do not run it.
- Never widen scope silently to make a blocked command pass. Fix the path or ask.
- A fence denial is information: the path was probably wrong.
