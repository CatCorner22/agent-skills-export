---
name: agent-secret-hygiene
description: "Keep credentials out of model reach on any platform: scan the environment a model or sub-agent process inherits, prompts and briefs for secret literals, install commands and authority claims, and transcripts for secrets echoed by the model or tools and for env-file reads. Use when configuring agents or sub-agents, before pasting config into a prompt, after a run that touched credentials, and in CI for agent prompts. Ships secret_exposure_check.py. Scope boundary: blocking commands at tool time is skill:scope-and-blast-radius-check; repository secret scanning and CI rules are skill:env-vars and skill:deployments-cicd."
---

# Agent secret hygiene

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A model or sub-agent will run in an environment, read a prompt, or produce a transcript that could contain credentials.

## Steps
1. Environment: `python3 scripts/secret_exposure_check.py --env --env-file .env --allow PATH,HOME`. Anything flagged is readable by the model's process; move it behind a tool, proxy or secret manager that the model calls without seeing the value.
2. Prompts and briefs: `--prompt system.md brief.md`. Remove secret literals (pass handles or tool names instead), remove install or download commands from sub-agent briefs, and strip authority claims; text that says "you are authorized" grants nothing but models act as if it did.
3. Transcripts: `--transcript run.json`. A secret in assistant or tool output is a leak (error); a secret in user input is exposure (warning). An assistant reading `.env` or `printenv` is a probe to investigate.
4. Rotate anything that appeared in an assistant message or tool argument; logs and provider retention make it compromised.
5. Run the prompt and brief checks in CI for every agent prompt file; run the transcript check on sampled production runs.

## Evidence
- A frontier model found an API key in a process list and used it; a sub-agent in a swarm test posted a private token and ran an unvetted install script. https://neoresearch.ai/papers/Kimi_K3_Safety_Evaluation.pdf
- Reasoning traces can copy prompt secrets verbatim; provider logs retain them. Vendor system cards and practitioner reports.
- Full notes: [references/evidence.md](references/evidence.md)
