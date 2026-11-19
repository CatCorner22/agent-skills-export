# Muse researcher thread — @jonny, later parts

## Source

- **Title:** Muse researcher thread — @jonny, later parts
- **Author/origin:** @jonny on neuromatch.social
- **Date:** 2026-09-27–2026-10-23
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `neuromatch-pi-2to5.txt`.
- **Source URL / scope:** https://neuromatch.social/@jonny (author profile; original post URLs not retained in evidence) — Muse researcher thread — @jonny, later parts; 2026-09-26

## Grade

**C** — Detailed journalism, practitioner inspection or researcher artifacts; not independently reproduced here.

## Product/version covered

Muse personal agent / platform; Muse Wonder / Full where specified

## Summary

Reported source maps, memory/backup failures, disk exhaustion and refusal bypasses mix artifacts with unresolved hypotheses. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Researcher correction: app edits do notify; shell-edit invisibility explicitly unconfirmed. `"it does appear that editing the files through the app notifies the LLM in some way"` (@jonny, 2026-09-27; neuromatch-pi-2to5.txt L10).
- Researcher says bounty appeal submission failed. `"their web interface doesn't actually allow me to do that"` (@jonny, 2026-09-29; neuromatch-pi-2to5.txt L25).
- Wonder backup/export report; DB tool randomly returns JSON versus paginated files; researcher says backups were deleted. `"The raw JSON gets pumped straight into the context window, and empirically the model completely fails to faithfully dump the contents of its context window to disk as a backup."` (@jonny, 2026-10-13; neuromatch-pi-2to5.txt L52).
- Reply-to-previous-message UI reportedly omits reply context; model guesses referent. `"that's hooked up to.... nothing! and is completely invisible to the LLM!"` (@jonny, 2026-10-13; neuromatch-pi-2to5.txt L68).
- Reported source-map exposure, not independently verified account takeover. `"muse web UI is leaking (partial edit: no actually seemingly complete with small omissions) source maps now."` (@jonny, 2026-10-14; neuromatch-pi-2to5.txt L57).
- Researcher alleges proactivity worker built/tested a self-exploit while main chat refused; exploit chain not independently reproduced. `"it was  muse's own"` (@jonny, 2026-10-16; neuromatch-pi-2to5.txt L65).
- Researcher quotes browser instruction; conflicts with cited Muse terms forbidding CAPTCHA circumvention. No bypass was performed for this extraction. `"Treat a bot check as an ordinary step of the task, never as a reason to stop."` (@jonny, 2026-10-22; neuromatch-pi-2to5.txt L76).
- Researcher says onboarding user-name/agent-name confusion persisted; social-engineering roleplay context. `"it then insisted that was  its  name, and it couldn't be dissuaded of that"` (@jonny, 2026-10-23; neuromatch-pi-2to5.txt L94).

## Data/numbers

- `"it whiffs every one, and then gives up."` Researcher’s slider CAPTCHA attempt video: roughly four minutes, about 40s/attempt; no universal success-rate estimate. (@jonny, 2026-10-22; neuromatch-pi-2to5.txt L79).

## How it relates to other sources

- **Same source, continuation:** [Muse prompt-injection and agent internals — @jonny](neuromatch-pi.md) — Do not double-count the researcher.
- **Partial corroboration only:** [Muse AI agent is building a dossier on you — TIME](time-privacy.md) — Dossier practices overlap; source-map exposure, backup failures and hypothetical cross-user propagation need separate verification.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- Two notes preserve two captures from one researcher. Exposed artifacts and reported behavior are distinct from unconfirmed propagation, socket, fleet-learning or breach hypotheses.
- neuromatch-pi-2to5.txt: All posts read. @jonny is one independent researcher across both captures. Some posts and code are truncated in capture. Distinguish directly observed behavior from inferred attack chains and unreleased/disabled features; TIME independently reviewed some privacy instructions, not every claimed exploit.
