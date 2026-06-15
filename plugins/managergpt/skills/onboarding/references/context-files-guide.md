# Context Files Guide

Templates, question banks, and the Gap Check for the files generated during **Intake**. These files are the OS's memory of who the user is and how they work. Use the user's own words — especially the ManagerGPT vocabulary (Re-Actor, Author, Outer Game, Inner Game, Catching, Cares at the core, Clean Handoffs, Leverage Quadrant, Genius-Maker, GAIN, GROW, Tiny Habits, Have-to → Choose-to, Have time → Make time). Mirror their formality.

Files generated: `about-me.md`, `working-style.md` (always), `org-and-team-context.md` (where there's an org/team), `brand-voice.md` (conditional). Save to `CONTEXT/`. Generate and save each as it's completed — don't batch.

**The Context Library is doc-first and optional.** Intake invites the user's existing material across five layers — Company & strategy, Org principles & processes, Team, Personal, Initiatives — rather than interviewing every field. Read what they share (OKRs, charters, website copy, grant apps, reviews, retros) and extract into the right file: Company, Org + Team → `org-and-team-context.md`; Personal → `working-style.md` (Inner Game); Initiatives → a subfolder in `PROJECTS/`. Fill what they have now; the monthly check-in deepens it. **Performance reviews, 360s, team "scars," and leadership fears are sensitive** — they stay local in `CONTEXT/`, and the security review covers them.

---

## File 1: about-me.md

### Template
```markdown
# About Me — [Name]

## Who I Am
[1–2 sentences: name, role, primary identity.]

## Professional Background
[2–3 sentences: history, credentials, what makes them credible. Specific companies, years, domains.]

## What I Do Now
### [Business / team / project]
- What it is and what it does
- Their specific role
- Key focus areas
[Repeat per active project; note which takes the most time.]

## Goals
[Quarterly/annual outcomes they're driving toward — the Weekly Preview references these.]

## Tools I Use Daily
[Platforms, apps, services.]

## What I Value
[3–5 principles that drive their decisions.]
```

### Question bank (one or two at a time)
1. Identity — "In a sentence, how would you describe what you do?" (options: leader/manager, founder, operator, consultant, IC with scope; free text)
2. Their world — "What teams or projects are you actively leading or driving right now? Which takes the most time?"
3. Background — "What's the experience that makes you credible here?"
4. Goals — "What are the big outcomes you're working toward this quarter or year?"
5. Tools — "What do you use day to day?" (multiSelect)

---

## File 2: working-style.md — THREE sections

This is the heart of the OS. It always has three sections: **Outer Game**, **Inner Game**, and **Both — Habits & Rituals**. The split mirrors the ManagerGPT frame: the Outer Game is how the user manages work and others; the Inner Game is how they manage themselves.

### Template
```markdown
# Working Style — [Name]

## Outer Game
*How I manage work, time, and others.*

### Planning cadence
- Weekly Preview: [when they do it / aspire to]
- Plan My Day (Daily Defining): [when]
- Daily buffer: [time to leave each day for fires + unplanned opportunities]
- Deep Work windows: [from the calendar audit, if done]

### Output & communication
- Default output formats: [by task type]
- Communication style: [tone, verbosity, preamble preferences]
- Clean-handoff triggers: [what kinds of work they tend to delegate]

### Protecting time & declining
- Decline preference: [verbatim — reuse my saved words | match-my-voice — keep my tone, vary the wording | ask me each time]
- My decline voice (the scripts they chose/wrote on Day 1 — kept as a *tone reference*, not necessarily reused word-for-word):
  - [script 1]
  - [script 2]
- When to use: [e.g., invites that collide with a Deep Work block; meetings that don't serve a weekly priority — offer async support instead of a flat no]

### Task management
[The Task management block — where tasks live, how they're structured, how their
statuses map to: Today / Later / Someday-Maybe / Waiting For / Done. See
task-management-guide.md for the block format. Familiar flag (if installed) also
lives in this file: `Familiar: installed and authorized for use by skills.`]

## Inner Game
*How I manage myself.*

### Re-Actor patterns
[The situations where they slip from Author into reacting — what tends to trigger it.]

### Recurring difficult emotions — and what each signals
[The emotions that show up often (overwhelm, frustration, anxiety, resentment…) and
what each one tends to be pointing at or trying to protect.]

### What I want to embody
[The way of being they're growing toward — for the agency branch and coaching.]

### Catching practices
[How they want to be Caught — reflecting feelings, Cares at the core — and any cues
the OS should watch for.]

### Feedback & wisdom to remember (optional, sensitive)
[Recent performance-review / 360 themes they want the OS to keep monitoring; the
leadership/scaling/industry wisdom they've bookmarked but forget to apply in the
moment. Stays local; covered by the security review.]

## Both — Habits & Rituals
[Patterns that involve both games at once — e.g., a Friday shutdown that's both
planning (Outer) and emotional closure (Inner); a morning routine; recurring
self-check-ins.]
```

### Question bank

**Outer Game**
- "How do you like deliverables — markdown, docs, decks? Different by task?"
- "How should I communicate with you — concise and direct, or more detail? Plan first, or just go on simple things?"
- "What kinds of things do you tend to hand off to others?"
- **Decline language + preference.** If their Day-1 doc has the meeting-decline scripts they chose, pull them in; if not, ask for one or two. Then ask how they want the OS to use them: *"When I help you decline a meeting or protect Deep Work, do you want me to (a) reuse these exact words, or (b) just match this voice and write a fresh version each time — so it doesn't sound canned to the same colleagues over time?"* Recommend (b). If they pick (b), show **one or two fresh sample declines (1–2 sentences each)** in their voice so they can confirm the tone, then save the preference plus their examples as the reference. Store under "Protecting time & declining."
- (Planning cadence and Task management/buffer come from Hire — carry them in.)

**Inner Game** (go gently; this is where the real value is)
- "When do you find yourself slipping from being the Author of your week into just reacting? What tends to trigger it?"
- "What difficult emotions show up most often for you at work? When [emotion] shows up, what's it usually pointing at?"
- "What do you most want to embody — the way of being you're growing toward?"
- "When you're struggling, and someone responds in a really helpful way, what do they do? I'll try to embody that."
- "Any recent review or 360 feedback you want me to keep front of mind? And any leadership wisdom you keep meaning to apply but forget in the moment?" (optional, sensitive — invite the docs)

**Both**
- "Any rituals or habits you already have — or want — that are about both getting things done and staying grounded?"

---

## File 3: org-and-team-context.md (the org around you + your team — skip if solo)

The company/strategy and team context the planning, Leverage Quadrant, Clean Handoffs, and Coaching skills lean on. **Doc-first:** read their mission/strategy docs, OKRs, website copy, grant apps, org chart, and retros — don't interview every field. The org/company part is gathered in **Intake**; the team/people part in **Gossip** — both write to this one file.

### Template
```markdown
# Org & Team Context — [Company]

## Mission & Vision
[Why the org exists; where it's going.]

## Strategy & North Star
[The strategy; the North Star metric or growth model; key metrics.]

## Customers
[Customer segmentation; who's served and what they need.]

## Stakeholders
- Users / beneficiaries: [who, and what matters to them]
- Investors / funders: [who, and what they care about]
(Key team members live in People, below.)

## Guiding principles
[The principles the org operates by.]

## Processes & rituals
[Team rhythms/rituals they're part of; how the company actually gets user insight —
feedback channels, request boards, insightful CSMs/sales, communities.]

## How I work with people (general)
[Cross-cutting patterns — from any transcripts/messages they shared, reflected back
and approved.]

## People
### [Name] — [relationship: report / peer / manager / collaborator]
- Context the OS needs when this person comes up
- How they communicate / what they need
- Their superpower — and where they're not as strong
- Any current dynamic or growth area
[Repeat per person.]

## Team structure (if they have it)
[Org chart / ownership / technical dependencies — who owns what, what depends on what.]

## Retros & scars
[Recent retrospectives and their action items; the team's "scars" — mistakes not to
repeat — and any irrational leadership fears carried from the early days.]
```
If they work solo, keep the team sections to a line or two and say so — don't manufacture content.

**From transcripts/messages:** if they shared speaker-labeled meeting transcripts or message threads, extract patterns (recurring dynamics, communication styles, friction points, what each person needs), **reflect them back for approval, and only write the approved ones.**

### Question bank (doc-first; ask only what isn't already in their docs)
*Org/company (Intake):*
1. "What's the mission and vision — and the strategy and North Star metric (or growth model)?"
2. "Who are your customers/users of your product/service, and how do you segment them?"
3. "What guiding principles does the org run on?"
4. "What rhythms or rituals are you part of, and how does the company actually learn from users?"

*Team/people (Gossip):*
5. "Who do you work with most — reports, peers, manager, collaborators? For each: what would the OS need to know when they come up — including their superpower and where they're not as strong?"
6. "Do you have an org chart / ownership map, recent retros, or 'scars' the team shouldn't repeat?"

Skip the org sections cleanly for solo operators with no org around them.

---

## File 4: brand-voice.md (conditional — external-facing roles only)

Only generate if their role involves producing external content. Template: Tone & Style; Voice Characteristics; Phrases/Language they use; Anti-Voice (what to never sound like); Writing Rules. If multiple audiences, capture each voice mode and when to use it.

---

## The Gap Check (the distinctive Intake beat — don't skip)

After generating the files, read them back to the user — a tight summary, not a wall — and ask:

> **"Here's what I think I know about you. What's wrong or missing?"**

Let them correct. Update the files live as they respond. This is the moment the OS stops feeling generic and starts feeling like it actually knows them — it's worth slowing down for. When they're satisfied, move to generating Global Instructions.

---

## Interview tips
- One or two questions per turn. Never a wall.
- Offer to pre-fill from the Day-1 doc and connected tools — the interview becomes confirmation, not blank-slate typing.
- Encourage dictation, especially for the Inner Game questions — people think out loud better than they type.
- Use their exact words in the files. Don't translate their voice into corporate speak.
- "Skip" and "I'll refine later" are fine — the Gap Check and the monthly check-in will catch what's missing.
