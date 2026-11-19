# Running on Muse

Chicken Little Overwatch uses only Markdown instructions and 2 optional Python scripts that need nothing beyond the standard library. Match the run to what your Muse surface can do, and state the match in the Plan.

## Capability ladder

| Muse surface | How to run | What to state in Flags |
|---|---|---|
| Muse Code with subagents | Launch each role in `roles.md` as its own subagent with the launch template. With the plugin, start Muse Code with `--agents "$(cat agents.json)"` and name the `clo-*` agent for each role. | Which roles ran as independent subagents, and which model ran each role |
| Muse Code with 1 agent (no subagents in this build, or a headless `muse exec` run) | Run Steps 1-7 yourself. Run the scripts. Run each swarm role as a separate pass, in order. | RT7: one model simulated the swarm |
| Files but no shell | Read the references. Do the eye check in place of the scripts. | H7: only the eye check ran |
| The Meta AI app or meta.ai, with no files or tools | Ask the user to paste the artifact and the requirements. Use the rules in `SKILL.md` and the sections of the references that the user can paste or attach. | H7, RT7, and each reference section that you could not read |

## Context budget

- Load `SKILL.md` first. Load each reference only at the step that names it.
- `one-way-optimal-language.md` is the largest file. Read its sections by heading, not all at once.
- For a long artifact, review it section by section. Keep one term list and one defect register for the whole artifact, in files, because Muse loses detail when a long session compacts.
- If your context runs short, finish the current step, write the defect register and open placeholders, and continue from them.

## Model independence

- A second model or a fresh session adds a review pass. It does not prove anything (C2).
- When you can, run the Defender and the Arbiter on a different Muse model or in a fresh context from the attack roles (D13). Set the `model` field of those agents in `agents.json`; Muse Code falls back to the lead's model when an ID isn't available, and tells the lead which model ran.
- Record the model ID for each role in the Verification register, because results depend on the model (lens L4). `muse export` records the model ID that each subagent ran on.

## Install

| Install | How |
|---|---|
| Skill only, for every project | `muse skills install ./skills/chicken-little-overwatch --scope user`, or copy the folder to `~/.agents/skills/chicken-little-overwatch/` |
| Skill only, for 1 repository | Copy the folder to `<repo>/.agents/skills/chicken-little-overwatch/` |
| Full plugin | Put the plugin folder in the workspace, install the skill as above, and start Muse Code with `--agents "$(cat agents.json)"` |
| The Meta AI app | Paste `SKILL.md` into the chat, and attach the references as files |

Muse Code changes. If a command in this table fails, use Meta's current documentation, and record the command that worked.
