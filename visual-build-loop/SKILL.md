---
name: visual-build-loop
description: "Run any vision-capable model in a build, render, compare-to-target, fix loop for frontends, dashboards, charts, slides, games and 3D scenes, with behavior and data checks so looks-right does not pass for works-right. Use when a model builds something visual, turns a mockup or screenshot into code, or reviews rendered output. Ships a visual-target template. Scope boundary: browser automation mechanics are skill:playwright-cli; product-level end-to-end verification is skill:verification."
---

# Visual build loop

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A model builds or checks a web page, dashboard, chart, slide deck, game or 3D scene.

## Steps
1. Fill `templates/visual-target.md`: reference image or URL, viewports, checkable must-have elements, behavior checks, and three chart values to spot-check against source data.
2. Build, render (headless screenshot, engine capture), and send the render back with: "Compare to the target. List each mismatch with its location. Fix the top three." One round at a time.
3. After each round run the behavior checks (clicks, inputs, edge cases) and the data spot-checks by script or by hand. Human-preference wins on visual tests measure taste, not correctness.
4. Do not trust the model for counting or fine reading in images; count with code or a second pass. Independent vision evals show counting as a weak spot across models.
5. Stop after 3-5 rounds or when remaining mismatches are cosmetic. Log each round in the template.

## Evidence
- Frontend arena leaderboards are human preference tests; they do not test behavior. Journalism/leaderboard methodology.
- Roboflow Vision Evals: counting is a weak category across models (one frontier model 46% on counting). https://playground.roboflow.com/
- Chart-reading hallucination is common when data is absent or dense; spot-checking three values catches most fabricated axes. Practitioner.
- Full notes: [references/evidence.md](references/evidence.md)
