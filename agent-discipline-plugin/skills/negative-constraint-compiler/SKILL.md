---
name: negative-constraint-compiler
description: "Turn 'never / don't / must not' rules into positive, checkable steps and — through Muse Code hooks — into deny rules, because prose rules are context, not enforcement. Use when writing or editing AGENTS.md or a SKILL.md, or when a rule was violated despite being written down. Tooling: `ad.py rules lint|compile|rewrite`. Scope boundary: keeping rule files short → `rules-hygiene`; runtime path/command blocking → `scope-and-blast-radius-check`."
metadata:
  priority: 6
  pathPatterns:
    - '**/AGENTS.md'
---
# Negative constraint compiler

Models follow "do X before Y" far better than "never Z"; negations are dropped under load, and a rule that is only prose has no teeth. Muse Code's own documentation says only that it is "designed to follow" `AGENTS.md`; a hook can "block an action before it happens."

## Procedure for each negative rule
1. **Rewrite as a positive check with a trigger.** `Never write tests outside tests/` → `Before creating a test file: assert its path starts with tests/.` (`ad.py rules rewrite FILE` drafts these.)
2. **Decide the layer.** Would violating it cost > 10 minutes or any data? → it needs a hook, not a sentence. Else keep the one-line positive rule.
3. **Emit the hook.** `ad.py rules compile` produces a `hooks.json` fragment in the form of `hooks/hooks.json` with a deny regex per hookable rule (rm -rf, force push, push to main, destructive SQL, publish, committing .env, prod deploy). Paths → `ad.py scope set … --allow`.
4. **Keep the prose to one line** that points at the hook: `rm -rf outside build/ is blocked by hook; ask for a GRANT.`

## Lint (`ad.py rules lint`)
Flags: file > 150 lines; negation-only rules with no hook equivalent; vague rules ("be careful", "as appropriate") with no testable trigger.

## Rule-writing template
`When <trigger>, do <positive action>; check <observable>.` One line. No adjectives.
