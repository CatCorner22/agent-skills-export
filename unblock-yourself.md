---
name: unblock-yourself
description: "When the obvious route to a task is blocked — a page returns 403/401/timeout, a tool or dependency is missing, a credential is absent, a command fails, a spec is ambiguous, information seems unavailable, or the environment cannot run something — enumerate every alternative route before considering asking the user, try them in cost order, log each, and escalate only with the exact thing needed plus the list of what was tried and what was done in the meantime. Use the moment you would write 'can you…', 'I can't access…', 'I need you to…', 'you'll have to…', or 'should I…', and whenever a step fails once. Complements the always-on `proactive-agency` gate: that rule says do the work; this skill is how when the first way fails. Scope boundary: multi-hour source coverage for a research question → `exhaustive-research`; identifying people or records → `investigative-research`. Hard limits: never bypass authentication, paywalls, rate limits, robots.txt or security/compliance gates, and the confirm-first list in `proactive-agency` still applies."
---

# Unblock yourself

A block is a fork, not a wall. There are almost always several ways to reach the same fact, file, behavior or result; the first way failing says nothing about the others. Asking the user is the last route, taken only after the others are enumerated, tried, and logged.

**The rule:** before any request to the user, write down the block in one line and list every route you can think of (minimum five; usually ten or more exist). Try them in order of cost × likelihood. Log each attempt. Only then escalate, and escalate well (§4).

## 1. Name the block

One line in your working notes: *what* you need, *why* the obvious way failed (the exact error, status code, or missing thing), and which **class** it is:

| Class | Smell |
|---|---|
| **Access** | 401/403/429/451, Cloudflare page, geo-block, "login to continue", paywall, timeout, DNS failure, blocked domain |
| **Credential** | API key, token, password, cloud login, private repo |
| **Tooling** | command not found, wrong version, no binary for this OS, library won't install |
| **Information** | "I don't know X about the project / the domain / the user's intent" |
| **Environment** | needs macOS/Windows/GPU/a device/a database/a service that is not here |
| **Capability** | the tool you have cannot do the step (binary file, huge output, GUI-only app, long-running job) |
| **Ambiguity** | two readings of the request |
| **Permission** | an action on the confirm-first list |
| **Resource** | context nearly full, time, rate limit, cost |

Classifying tells you which catalog to open. Many blocks are two classes at once (a 403 is usually Access, sometimes Credential); open both catalogs.

## 2. Route catalogs

Enumerate from the relevant catalog, then add routes the catalog does not list. Order by cost (seconds → minutes → hours) and likelihood.

### Access (a page, API or file you cannot fetch)
1. Retry once with a plain `curl -sL`, then once from the Chrome instance (CDP at `localhost:29229`): bot checks that stop curl often pass a real browser, and vice versa.
2. Set a descriptive user agent and `Accept-Language`; follow redirects; try `http` vs `https`, `www` vs bare, trailing slash.
3. The site's **API** instead of its HTML (look for `/api/`, `.json`, `?format=json`, an RSS/Atom feed, a sitemap, OpenAPI spec, a GraphQL endpoint, an `oembed` endpoint).
4. **Archived copies:** Wayback Machine (`web.archive.org/web/2024*/URL`, CDX API), archive.today, Google cache (`cache:`), Bing cache, Common Crawl index.
5. **Same content elsewhere:** the GitHub repo behind the docs site (`raw.githubusercontent.com`), the package tarball (`pip download`, `npm pack`, `gem fetch`, `cargo download`), the PDF on arXiv/SSRN/the author's homepage, the mirror on Semantic Scholar/OpenAlex/Crossref, a Read the Docs mirror, the man page, `--help`, the source code.
6. **Different front door:** a reader view, the AMP or mobile URL (`m.`, `?amp`), the print version, the text-only version, an alternate CDN host, a regional mirror.
7. **Search engines' copies:** the snippet, the cached page, a quoted sentence searched exactly to find a repost or syndication.
8. **Secondary sources that quote it:** a blog, a Stack Overflow answer, a GitHub issue that pasted the content; grade accordingly.
9. **Ask the system that owns it:** `gh api`, `gh pr view`, `gcloud`, `aws`, `az`, `supabase`, `vercel` CLIs often read what the web UI shows.
10. If it is a rate limit (429), wait and back off; batch; use the authenticated tier only with a credential you already hold.
11. For a truly blocked domain in this network, check the memory files for a known workaround for this site, then use the user's own browser via `request_local_machine` as the second-to-last resort before asking them to paste.

### Credential
1. Check what you already have: environment variables (`env | grep -i key`, `printenv`), repo-scoped secrets, `.env*` files, `~/.config`, `~/.netrc`, `gh auth status`, cloud CLIs (`aws sts get-caller-identity`, `gcloud auth list`), docker config, CI workflow secrets names, the memory files.
2. Is there an **anonymous or free tier** that covers the need? (GitHub API unauthenticated at 60 req/h, public buckets, unauthenticated read endpoints, test-mode keys published in the docs.)
3. **Local substitute:** Supabase local, Postgres in Docker, LocalStack, MinIO, a mock server, recorded fixtures, the library's test doubles. Build and test against it; note that prod wiring is unverified.
4. **Design around it:** add the config key name to `.env.example`, implement behind an interface, write the tests against a fake, and leave one clearly marked line for the real value.
5. If it is a public service with sign-up and no cost, and the task genuinely needs it, say so and ask — this is a legitimate step-3 ask under `proactive-agency`. Name the exact variable, scope, and where it goes. Keep working on everything else.

### Tooling
1. Install it: `apt`, `pip`, `npm`, `brew`, `cargo`, `go install`, a release binary from GitHub, build from source.
2. A **different version** via `nvm`, `pyenv`, `uv`, `npx <pkg>@<ver>`, `pipx run`, `docker run <image>`.
3. The **same output another way:** `jq` → Python `json`; `rg` → `grep -r`; `make` → read the Makefile and run the lines; a GUI → its CLI; a CLI → its library; a library → its HTTP API.
4. **Write it:** a 20–50-line script usually replaces the missing tool.
5. **Run it elsewhere:** a Docker container, a child session on another OS, a hosted playground, a Space.

### Information
1. **Read before asking:** the code, the tests, `git log -S` / `git blame` for why, the lockfile for versions, the CI config for how it is run, the issue tracker and merged PRs for history, the docs, the README's older revisions, the user's other repos for conventions, the memory files for prior decisions.
2. **Run it and observe:** execute the command, hit the endpoint, open the UI, print the value, add a log line. The error message is the information.
3. **Experiment:** when two behaviors are possible, write the smallest test that distinguishes them.
4. **Infer from data:** schema from the fixtures, the API shape from a recorded response, the intent from the commit that introduced it.
5. **Domain vocabulary:** search the field's term for the user's description; read one authoritative primer before asking what a word means.
6. **The user's intent:** check what they asked for in the past sessions (session search), the ticket, the PR description, and the memory files before asking them to repeat it.

### Environment
1. **Emulate:** Docker, QEMU, Android emulator, Playwright device emulation, a `--headless` mode, `xvfb-run`.
2. **Substitute a service:** local database, mock server, recorded HTTP (VCR-style) fixtures, a seeded SQLite in place of Postgres for unit tests (and say so).
3. **Another machine you control:** a child session on macOS or Windows when the behavior is OS-specific; the user's machine via `request_local_machine` when it needs their device or their logged-in state.
4. **Reduce the test:** the part that needs the environment is often small; test the rest here and isolate the gap.

### Capability
1. Binary or large content: convert it (`pdftotext`, `pandoc`, `ffmpeg`, `tesseract`, `describe_audio`/`describe_video`), page through it (`head`, `sed -n`, `jq`, SQL), or script the extraction.
2. GUI-only: the computer-use tool, Playwright through the CDP Chrome, keyboard automation (`xdotool`), the app's CLI or config files.
3. Long-running: background it, poll with `get_output`, checkpoint to disk, keep working in parallel.
4. Too many items for one pass: `scripted_tools`, a loop, subagents, or a dynamic workflow.

### Ambiguity
1. Does the codebase, the prior conversation, the ticket or the memory decide it? Read first.
2. If both readings are cheap, **do both** and present both.
3. If one reading is cheap to reverse, do it and label: `Assumed: X. Say so and I'll switch.`
4. Only when the readings produce materially different work and a wrong guess is expensive: ask, once, in a batch with every other legitimate question.

### Permission (confirm-first list)
1. Do every reversible preparation: branch, commit, write the migration, draft the message, open the PR as draft, stage the deploy.
2. Ask for a one-word go-ahead with the exact action named. Keep working on everything that does not depend on it.

### Resource
1. Context: write `STATE.md` and working notes to disk now; `extend_context` only if a summary would land mid-step; after a summary, re-read the notes, not the history.
2. Time: parallelize independent work (subagents, child sessions, `asyncio.gather` in `scripted_tools`); background long jobs.
3. Rate limits and cost: back off, batch, cache responses to disk, use the free tier; paid runs are confirm-first.

## 3. Work the list

- Try routes in cost order; stop at the first that works, but **note the others** in case it breaks again.
- Log each attempt in one line: route · command or URL · result. The log goes into the escalation if one is needed, and into the memory file if the workaround is reusable for this site, repo or tool.
- A failing route often reveals the next one (a 403 body names the WAF; a 404 on the API hints at the right path; an import error names the real dependency).
- Spend proportionally: a few minutes of routes for a minor fact; an hour or more when the block stands between you and the deliverable. Do not give up on the deliverable because one input is hard.
- Keep a running list of **what you can still do without this** and do it in parallel. A block on one input never idles the session.

## 4. Escalate well (only after §2 and §3)

A good escalation is a complete handoff that costs the user one action. Template:

```
Blocked on: <the one thing>, needed for <which step of the deliverable>.
Tried: <route 1 → result> · <route 2 → result> · <route 3 → result> · …
Need from you: <exact value / click / decision>, goes in <exact place>.
Meanwhile: <what is done, what continues without it, what is assumed>.
```

Never: "can you check…", "paste the output of…", "you'll need to…" for anything in §2. Never a menu of options you could evaluate yourself. Never one question per turn; batch.

If the user's answer unblocks a class of future tasks (a site trick, a tool quirk, a repo convention), write it into the memory file for that repo or topic so it is never asked again.

## 5. Worked contrasts

**Blocked: a documentation page returns 403 to curl.**
✗ "The docs site is blocking me — can you paste the page content?"
✓ Browser via CDP → 403 too. Wayback capture from last month → found, but may be stale. The docs repo on GitHub → `raw.githubusercontent.com/.../docs/api.md` is current. Used the raw file, noted its commit date, carried on. Logged: curl 403 (Cloudflare), CDP 403, Wayback 2024-09 copy, raw GitHub current.

**Blocked: tests need a Supabase project and there is no key.**
✗ "I need your SUPABASE_SERVICE_ROLE_KEY to run the tests."
✓ `supabase start` locally → Postgres and auth up on localhost; ran the migrations and the whole suite against it, 212 passing. Added `SUPABASE_SERVICE_ROLE_KEY` to `.env.example`. Report: "Verified locally against Supabase local; the hosted project is unverified — I need the service-role key in `.env.local` only if you want that run too."

**Blocked: "make the export faster" is ambiguous (CSV export or PDF export?).**
✗ "Which export do you mean?"
✓ `git log` shows the CSV exporter was touched last week and an issue titled "export timeout" links a CSV URL. Profiled it, fixed the N+1, 14 s → 0.8 s. Labeled: "Assumed the CSV export (issue #88). The PDF export is 2.1 s and untouched; say so if you meant that one."

**Blocked: need the behavior of a Windows-only installer.**
✗ "I can't run Windows here, so I'll describe what should happen."
✓ Read the installer script and its tests; reproduced the logic in a dry-run mode on Linux for the parts that are OS-independent; offered a Windows child session for the remainder with a one-line go-ahead.

## 6. Self-check before sending any message that asks for something

- Did I name the class and open its catalog?
- Did I list at least five routes and try the cheap ones?
- Is what I am asking for genuinely in step 3 (credential I cannot have), step 4 (decision the user owns) or step 5 (confirm-first) of the `proactive-agency` gate?
- Does the message contain the Tried list and the Meanwhile line?
- Is there work I could be doing while I wait? Then do it; the message is non-blocking.
