---
name: internal-focus-group
description: Test work with a simulated focus group of the real people who will receive it, before it ships. Use when the user runs /internal-focus-group, asks "how would my audience react", or wants feedback on a draft, proposal, product, or piece of content prior to presenting or publishing it. Each persona reacts in their own voice with their own biases, then reactions are synthesized into concrete revisions.
---

# Internal Focus Group

Run any idea or finished product past a group of personas who mirror your target audience — before it ever goes live. Where `ask-the-board` asks *experts for advice*, this skill asks *the actual recipients for reactions*: the client reading the proposal, the manager reviewing your week, the audience watching the video.

Inspired by the practice of cloning your own manager to get their feedback on your work every week before they ever see it.

The forcing function is the point: you cannot build a focus group without deciding exactly who the work is for. If you cannot name the members, you do not know your target audience yet — and that is the first problem to fix.

## Focus group setup (first use)

Personas live in `knowledge/focus-group/`, one file per member.

### 1. Identify the real people

Ask the user to name the specific people (or hyper-specific archetypes) who will receive the final product. **Be specific**: not "person A" but "Brian from college — skeptical of fitness fads, busy dad, will stop reading at the first buzzword." 3–6 members works best. Members should differ in the ways the real audience differs (skeptic vs. enthusiast, novice vs. expert, buyer vs. user).

### 2. Build each persona

For public figures, gather material with the `web-scraping` skill and save it via `ingest-source`. For private people, interview the user about them. Save to `knowledge/focus-group/<name-slug>.md`:

```markdown
# <Name>

- **Represents:** <which slice of the target audience>
- **Relationship to the work:** <client / manager / viewer / buyer / teammate>

## Context & background

<Who they are, what they care about, what their day looks like.>

## Voice

<How they give feedback: blunt, polite-but-noncommittal, detail-obsessed, skims everything...>

## Biases & triggers

- **Wins them over:** <what earns their enthusiasm>
- **Loses them:** <pet peeves, dealbreakers, buzzwords, formats they hate>

## Feedback history

- <dated entries of real feedback they have given, added over time>
```

### 3. Enhance clones over time

Whenever a member gives *real* feedback in real life, add it to their persona's Feedback history (directly or via the `improve-system` experience mode). The clones get sharper with every real data point.

## Running a focus group session

When the user runs `/internal-focus-group <work to review>`:

1. Read every persona file in `knowledge/focus-group/`.
2. Read the work being tested (draft, proposal, script, product description, screenshots).
3. Have each member react **in character** — first impression, what lands, what loses them, what they would say out loud vs. what they would only think. Each member reacts with their own context, voice, and biases; do not let them blur into one polite reviewer.
4. Synthesize into actionable revisions.

### Response format

```markdown
## Focus group: <work being reviewed>

### <Member 1>
- **First impression:** <gut reaction in their voice>
- **What works for them:** <...>
- **What loses them:** <specific moments/sections and why>
- **Would they act on it?** <yes/no/maybe, and what would tip them>

### <Member 2>
...

## Synthesis
- **Consensus reactions:** <what most of the group felt>
- **Polarizing elements:** <what split the group, and which side matters more for the goal>
- **Top 3 revisions before shipping:** <concrete, prioritized changes>
- **Ship verdict:** <ready / revise first / rethink>
```

Example: `/internal-focus-group — run this project proposal through our focus group to get feedback prior to my presentation.`

## Rules

- Honest beats kind: a focus group that only compliments is worthless. Surface the reaction the user least wants to hear.
- Ground reactions in each persona's recorded biases and feedback history, not generic criticism.
- Simulated feedback is a rehearsal, not a substitute — for high-stakes work, recommend validating with at least one real person after revising.
