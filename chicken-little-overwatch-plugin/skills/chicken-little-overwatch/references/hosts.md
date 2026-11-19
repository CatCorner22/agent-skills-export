# Running on any host

Chicken Little Overwatch uses only Markdown instructions and 2 optional Python scripts that need nothing beyond the standard library. It needs no vendor tool, model, or API. Match the run to what your host can do, and state the match in the Plan.

## Capability ladder

| Host capability | How to run | What to state in Flags |
|---|---|---|
| Independent agents (Claude Code or Gemini CLI subagents, Cursor agents, Codex or Devin child sessions, or an API orchestrator that starts one model call per role) | Launch each role in `roles.md` as its own agent with the launch template. If you have the Chicken Little Overwatch Plugin, use its `clo-*` agents. | Which roles ran as independent agents, and which model ran each role |
| One agent with a shell and files | Run Steps 1-7 yourself. Run the scripts. Run each swarm role as a separate pass, in order. | RT7: one model simulated the swarm |
| Files but no shell | Read the references. Do the eye check in place of the scripts. | H7: only the eye check ran |
| Plain chat with no files or tools | Ask the user to paste the artifact and the requirements. Use the rules in `SKILL.md` and the sections of the references that the user can paste or attach. | H7, RT7, and each reference section that you could not read |

## Context budget

- Load `SKILL.md` first. Load each reference only at the step that names it.
- `one-way-optimal-language.md` is the largest file. Read its sections by heading, not all at once.
- For a long artifact, review it section by section. Keep one term list and one defect register for the whole artifact.
- If your context runs short, finish the current step, write the defect register and open placeholders, and continue from them.

## Model independence

- A second model or a fresh session adds a review pass. It does not prove anything (C2).
- When you can, run the Defender and the Arbiter on a different model or in a fresh context from the attack roles (D13).
- Record the model name and version for each role in the Verification register, because results depend on the model (lens L4).

## Install by host

| Host | Skill only | Full plugin |
|---|---|---|
| Any Agent Skills host | Copy the `chicken-little-overwatch` folder into the host's skills folder | Install the plugin folder; its root `plugin.json` follows the Agent Plugins standard |
| Claude Code | `~/.claude/skills/chicken-little-overwatch/` | `claude --plugin-dir ./chicken-little-overwatch-plugin`, or add the folder to a marketplace |
| Claude apps | Upload `chicken-little-overwatch.zip` under Settings, Capabilities, Skills | Not available; use the skill |
| Codex | `~/.agents/skills/chicken-little-overwatch/` or `<repo>/.agents/skills/` | Install the plugin folder |
| ChatGPT (plans with Skills) | Upload the skill zip on the Skills page | Not available; use the skill |
| Cursor | `.cursor/skills/chicken-little-overwatch/` | Install the plugin folder; Cursor reads `.cursor-plugin/plugin.json` |
| Gemini CLI | Install the plugin as an extension | `gemini extensions install ./chicken-little-overwatch-plugin` |
| Devin | Save the skill to a plugin | Install the plugin folder |
| Other chat apps | Paste `SKILL.md` into the project or system instructions, and attach the references as files | Not available |

Host menus and folder names change. If a path in this table fails, use the host's current documentation, and record the path that worked.
