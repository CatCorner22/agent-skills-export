# Provider / model migration probe

From: <provider, model id, region>  To: <provider, model id, region>  Date:

## Feature parity (fill from current docs; "unknown" is a valid cell)
| Feature | From | To |
|---|---|---|
| Model id and version pin | | |
| Context window actually served | | |
| Max output tokens default and cap | | |
| Reasoning/thinking control name and values | | |
| Reasoning history round-trip (field name; accepted on replay?) | | |
| Tool calling: parallel calls, strict schemas, name rules | | |
| Structured output mode and schema subset | | |
| Prompt caching: automatic/explicit, block size, TTL, price fields | | |
| Usage field names (input, cached, cache write, output, reasoning) | | |
| finish/stop reason values | | |
| Rate limit units (RPM/TPM; reserved on max_tokens?) | | |
| Unsupported params that return 400 (temperature, top_p, penalties) | | |
| Data residency, retention, training-use terms | | |

## Probe (same 20 tasks, same harness, repeat 3x on the old provider first to measure noise)
| Metric | From | To | Noise band |
|---|---|---|---|
| Quality (hidden tests / rubric) | | | |
| Tool calls: right function, parseable args, schema-valid | | | |
| TTFT / tokens per second | | | |
| Cost per successful task | | | |
| 4xx/5xx and retry counts | | | |

Decision and rollback plan:
