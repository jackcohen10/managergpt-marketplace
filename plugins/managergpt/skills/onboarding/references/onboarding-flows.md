# ManagerGPT Onboarding — Detailed Flows

The full runbook behind the slim SKILL.md orchestrator. Each section is the step-by-step for one phase, including the exact AskUserQuestion wordings, templates, and routing. The spine is **Hire → Onboard → Intake → Gossip → Test Drive → Familiar → Closer.** Always: one or two questions at a time, encourage dictation, confirm before each phase change, save as you go, keep the "onboarding a new colleague" metaphor alive.

Platform note: where this says "Global Instructions," Cowork uses the Settings field and Codex uses `AGENTS.md`. Where it says "scheduled task," Cowork uses `create_scheduled_task` and Codex uses a Chat-created automation. Both platforms have **Projects** — the OS lives in one.

---

## Section 1: Entry-point routing

### First-time users (no context files found)

AskUserQuestion:
```
"What's your aim here today?"
- Set up my whole Operating System (the full onboarding, ~30–45 min)
- Get productive fast (Quickstart, ~15 min)
- Help me with one specific thing
```

- **Full** → run Hire → Onboard → Intake → Gossip → Test Drive → Familiar → Closer.
- **Quickstart** → Section 2.
- **One thing** → free text; route to the relevant phase or just help.

### Returning users (files/config exist)

Open warmly and name what you can see ("You've already got your workspace, about-me, and a Weekly Preview scheduled"). AskUserQuestion:
```
"Welcome back. What do you want to do?"
- Full refresh — re-interview and update everything
- Update specific pieces (workspace, tools, context files, automations…)
- Run the Test Drive again
- Help with one specific thing
```

Always read existing files first and present current values as defaults to keep or change. Never overwrite silently.

---

## Section 2: Quickstart (~15 minutes)

A stripped path to value. Skips Gossip, the calendar audit, and most of the Inner Game.

1. **Minimal workspace.** Create `CONTEXT/` and `OUTPUTS/` only. Explain: "CONTEXT holds who you are; OUTPUTS is where I deliver work. We can expand later."
2. **Three-question about-me** (AskUserQuestion, one at a time): what they do + the business; the tools they use daily; how they want the OS to work with them (ask first / just go on simple things / show a plan first).
3. **Generate `about-me.md`** from the answers; present and offer to refine.
4. **Where do tasks live — and do they want a fresh dock?** Ask the task-management first question with its four explicit options (Section 3.5) — even in Quickstart, don't shrink it to "where do your tasks live?" If they're on options 2–4, **offer Flow State first**, then a `tasks.md`/`tasks.xlsx` as the lighter alternative, so Plan My Day and Weekly Preview have somewhere to write. Never silently create `tasks.md` — the user picks.
5. **Minimal Global Instructions** — who they are, how they work, output defaults, the hard delete rules, and "If I haven't selected a Project, suggest opening the OS Project." Walk through pasting it in.
6. **Show what Full Setup adds** (Inner Game, team context, calendar audit, automations, Familiar) and invite them back anytime.

---

## Section 3: Phase 1 — HIRE

Say the intro line: *"First, we set up where your Operating System lives (it's just a set of folders and files) and what tools it can access."*

### 3.1 Capabilities — don't open with a question

Don't start with a capabilities quiz; it's confusing and stalls people on step one. Just begin. The OS needs **Skills** and **Code execution and file creation** on (Settings → Capabilities), but raise it only **reactively** — if something fails (can't create a file, a skill won't run), point them to Settings → Capabilities then. If a toggle is greyed out on a work account, their IT admin disabled it at the org level — help them figure out who to ask. (Codex: not gated this way — confirm the workspace is writable.)

**First, grab their Day 1 doc:** right after the intro, ask *"Do you have a doc from Workshop #1 — or any notes about your role, team, and goals? Drag it in or paste a link and I'll use it to pre-fill the rest."* If they share one, read it now and carry it through every phase (this replaces re-asking in Intake).

### 3.2 Build the workspace

1. Confirm a folder is selected (`request_cowork_directory` if not).
2. Create `CONTEXT/`, `PROJECTS/`, `TEMPLATES/`, `OUTPUTS/` with `mkdir -p`. Leave PROJECTS and TEMPLATES empty.
3. **Permission model** — AskUserQuestion, default to read/write-with-confirmation:
```
"How should I handle your workspace folders?"
- Read/write with confirmation (Recommended) — I can update any folder but I show you the change and ask first. OUTPUTS is always writable.
- Read-only source folders — I read CONTEXT/PROJECTS/TEMPLATES but never touch them; only OUTPUTS is writable.
- Full read/write — I update files freely. For power users.
```
Store the choice — it drives the Folder Protocol in Global Instructions. See `workspace-guide.md`.

### 3.3 Connect tools

Ask what they use daily (multiSelect: Google Workspace, Slack, Notion, a task tool, other). For each, `search_mcp_registry` then `suggest_connectors`. Verify with a quick read. Connect before building context files so you can pull from real material. See `connectors-guide.md`.

### 3.4 Calendar audit — don't block on it

A deep calendar read is slow, so **never stall the flow waiting for it.** Default: **defer it** — skip here and let the first **Weekly Preview** do the calendar read (it already does); just tell the user their OS will look at their calendar the first time they plan. Or run it quietly in the background while they answer the next questions and surface findings later (when generating `working-style.md`), not as a gate. If/when you do read 2–3 weeks, pull meeting load, recurring meetings to batch/decline/delegate, maker-time fragmentation, and likely Deep Work windows; feed the confirmed findings into the **Outer Game** of `working-style.md` (Deep Work windows + a starting daily-buffer estimate). Skip if no calendar is connected.

### 3.5 Task management (REQUIRED — connect, then configure)

**First question — ask it exactly, with the four options listed (even in Codex/plain text; don't soften it to "where do your tasks live?"):** *"Where do your tasks and to-dos live today — and do you love that system, or are you open to a fresh one?"* — **1. In an app I'm happy with** (Asana / Notion / Linear / Jira / Airtable / etc.); **2. A doc or spreadsheet**; **3. I have something, but I don't love it**; **4. Nothing consistent** — it's in my head / scattered. The question does double duty: *where* tasks live **and** *whether they want to keep that home or build a new one.* If they pick "In an app," ask which one. **Options 2, 3, and 4 all mean they're open to a better dock — route to the fallback and always offer Flow State first; never silently create `tasks.md`.**

Routing:
- **Option 1 (a tool they're happy with)** → connect it, then **configure**: run a discovery query before interviewing —
  - Asana → workspaces, projects, custom fields
  - Linear → teams, projects, workflow states
  - Notion → have them point you at the database, then read its properties
  - Todoist → projects, labels
  - Airtable → bases, tables, fields (ask which base/table holds tasks)
  Then interview them on their conventions and write the **Task management block** (see `task-management-guide.md`) into the Outer Game of `working-style.md`, mapping their structure to the canonical labels: **Today, Later, Someday/Maybe, Waiting For, Done** (record whatever they actually use).
- **Options 2, 3, or 4** → the **fallback**: **lead with Flow State** (the ManagerGPT task app) as the recommended dock — name it first. Only if they'd rather a plain file, build a task file mirroring the Next Actions template (columns **By When, Action, Priority, Project, Notes, Time**; a **This Week's Priorities 1 / 2 / 3-stretch** block; the **Daily Defining + Weekly Preview checklists** at the bottom). If they choose the file, ask format: **`tasks.xlsx`** (closest to the Next Actions spreadsheet) or **`tasks.md`** (lighter, plain text). **The user picks — Flow State, spreadsheet, or markdown; don't default to `tasks.md` on their behalf.** Create it in `PROJECTS/` and record the location + format in the Task management block.

**Daily buffer (ask here, save here):** *"Based on what you know about your typical days, how much buffer time should you leave each day for fighting fires and responding to unplanned opportunities?"* If the calendar audit proposed an estimate, offer it as the starting point. Save the answer to the Outer Game of `working-style.md` — Plan My Day reads it.

**Phase confirmation:** *"That's Hire — your workspace, connected tools (and a calendar read, if you connected one), and task management. Anything else before we give your OS its standing instructions?"*

---

## Section 4: Phase 2 — ONBOARD

Say the intro line: *"Now we give your Operating System its standing instructions — what to do every time you use it or it takes action."*

- **Auto-install the companion bundle — don't ask, just install** (Weekly Preview, Plan My Day, Clean Handoffs, Leverage Quadrant, Inner Dialogue, Catching, GAIN Feedback, GROW Coaching, Meta-Prompt, Tiny Habit). Name what they now have in one or two sentences.
- Tell them their Global Instructions get written at the end of Intake, from what's learned — so they're personal, not boilerplate.

---

## Section 5: Phase 3 — INTAKE

### 5.1 Use the Day-1 doc (already imported in Hire)

You asked for the Day-1 / Workshop #1 doc at the very start of Hire (3.1). If they shared one, pre-fill the context files from it so the interview is confirmation, not blank-slate typing. If they didn't have it then but mention it now, grab it here.

### 5.1b Feed the Context Library (doc-first, optional)

Invite their existing material across five layers — Company & strategy, Org principles & processes, Team, Personal, Initiatives — instead of interviewing every field: *"Share whatever you already have — drag in docs or point me at them, and we'll fill the rest over time. None of this is required."* Use AskUserQuestion (multiSelect) to pick the layers they have material for, read what they share, and extract into the right file: Company, Org + Team → `org-and-team-context.md`; Personal → `working-style.md` (Inner Game); Initiatives → a `PROJECTS/` subfolder. Reviews, 360s, scars, and leadership fears are **sensitive** — local only, flagged for the security review. See `context-files-guide.md`.

### 5.2 Generate about-me.md, org-and-team-context.md, working-style.md (3 sections), brand-voice.md

Run the interviews and build the files per `context-files-guide.md`. `working-style.md` always has **Outer Game**, **Inner Game**, and **Both — Habits & Rituals**. `org-and-team-context.md` where there's a company/org around them (skip if solo). `brand-voice.md` only if their role involves external content.

### 5.3 The Gap Check (don't skip)

Read the generated files back and ask: *"Here's what I think I know about you. What's wrong or missing?"* Let them correct before moving on. Full script in `context-files-guide.md`.

### 5.4 Generate Global Instructions

Distill the files into ~800 words and walk them through pasting into Settings → Cowork (Codex: `AGENTS.md`). Must include the line *"If I haven't selected a Project, suggest opening the OS Project,"* and the **hard delete rules** in both the Security Rules and the Folder Protocol. See `global-instructions-guide.md`.

**Phase confirmation:** files saved, Global Instructions installed. Move to Gossip.

---

## Section 6: Phase 4 — GOSSIP

- *"Who do you work with most? Direct reports, peers, your manager, key collaborators?"*
- For each: *"What would your Operating System need to know to be helpful when this person comes up?"*
- **Learn from real interactions (optional):** *"If you have transcripts from recent meetings (with speaker labels) or message threads with these people, you can upload them or paste them in — I'll pull out the patterns I'm noticing in how you work together."* Extract patterns (recurring dynamics, communication styles, friction points, what each person needs), **reflect them back for approval**, and only then fold the approved ones into `org-and-team-context.md` (and Inner/Outer Game if relevant).
- Write `org-and-team-context.md`. **If they work solo, keep it minimal and say so.**

---

## Section 7: Test Drive

Say the intro line: *"Pick something actually on your plate right now — something you'd normally tackle alone, without me."* Walk it end to end, saving to OUTPUTS/. Then frame the rhythm: *"This is the rhythm you'll use most days. I read your files first. I ask you the questions I need answered. You refine. Then I do the work."*

---

## Section 8: Familiar (offer this last; Mac only)

Offer Familiar (looksfamiliar.org): local screen-watching, on-device OCR via Apple, nothing leaves the computer, auto-redacts secrets, 48-hour screenshot deletion. Frame it as the upgrade that lets the OS ground itself in what they actually did. If they install it, walk through install + authorization, write the flag `Familiar: installed and authorized for use by skills.` to `working-style.md`, and tell them the Weekly Preview, Plan My Day, Catching, and Coaching skills now call `/familiar` to pull real activity. **Skip entirely for Windows.** See `familiar-guide.md`.

---

## Section 9: Closer — turn on the automations (by default)

Open: *"Welcome to your personalized AI operating system…"* Then set up the rituals **by default — don't ask whether, only when.** Each saves to the OS Project, notifies on each run, and is adjustable anytime. (Codex: create these as automations from Chat.)

- **Weekly Preview.** Walk the **timing table** interactively and let them choose (default **Sunday 8 PM**); tell them to also block it as a recurring calendar event. A scheduled run **drafts and notifies** — it never runs the full interview unattended.
- **Plan My Day.** Ask **when** (weekday mornings or evenings) and tie it to an existing habit.
- **Monthly context check-in** — last Friday of the month; re-reads context files, asks what changed, and **re-runs the task-management discovery**.

Then mention: *"There's also `/managergpt:protect` — a security review of your setup, anytime you want it."* See `scheduled-tasks-guide.md` for the draft-and-notify prompt pattern, the timing table, and cron reference.

---

## Section 10: Completion

Generate an `onboarding-checklist.md` in the OS Project showing what's set up (workspace, tools, task mapping, context files, Global Instructions, companion skills, automations, Familiar screen capture) and what's still available. Remind them: select the OS Project at the start of each session; add briefs to PROJECTS/ as they go; re-run this skill anytime to update any piece.
