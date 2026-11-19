# Routing table (update as models change; last reviewed 2026-11-12)

| Task shape | First choice | Backup | Why |
|---|---|---|---|
| Must be right first try, no checker (live chat, advice, one-shot review) | Claude Opus/Sonnet 5.5 | GPT-6 class | highest first-shot reliability, abstains more |
| Thin spec, open-ended design, novel science | Claude Opus 5.5 | GPT-6 class | rebuild-from-spec 65% vs Kimi 31.5% |
| Long tool-heavy agent run with tests and retries | Kimi K3.1 Pro | Claude Sonnet 5.5 | near-parity at pass@2, about half the price |
| Deep web research with many tool calls | Kimi K3.1 Pro | Claude | leads browsing/MCP tables (vendor), strong GDPval |
| Large batch, overnight, budget-bound | Kimi K3.1 Pro / GLM 5.x | Claude Haiku 5.5 | token price |
| Data must stay on own hardware; fine-tuning | Kimi K3 (open weights) / GLM / Qwen | none closed | weights available |
| Fast interactive replies | Claude Haiku/Sonnet 5.5 | Kimi Highspeed at low effort | Kimi first token is slow at max effort |
| Visual frontend / 3D / CAD with screenshot loop | Kimi K3.1 Pro | Claude | strong vision + taste wins; verify behavior |
| Disciplined prose to a style guide | Claude Fable 5.x | Kimi + restraint pass | blind essay test |
| Multilingual (non-English) output | test both | — | Kimi reasoning drifts to English |

Grades: vendor tables for browsing/MCP; independent for cost, latency, rebuild-from-spec, hallucination. Re-check before large spend.
