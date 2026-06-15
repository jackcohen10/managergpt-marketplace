---
name: weekly-preview
description: >
  Coaches the user through their Weekly Preview — the core planning ritual of the
  ManagerGPT Operating System. Use when the user says "Weekly Preview," "plan my
  week," "help me plan my week," "what should I focus on this week," or asks to
  prioritize the week ahead. First closes out the week that's ending (reflection,
  emotional check-in, and an agency/Re-Actor-to-Author coaching branch), then walks
  them from a pile of open loops to 2-3 precisely-defined outcomes with testable
  "done" criteria, blocks Deep Work on the calendar, surfaces what to delegate via
  Clean Handoffs, and writes everything back to their real task source. Reads
  working-style.md to find where tasks live, remembers prior weeks to spot repeated
  priorities, and can run on a schedule to draft a starting point. Daily planning
  lives in the separate plan-my-day skill.
version: 0.2.0
---

# Weekly Preview

This is the most important ritual in the ManagerGPT Operating System. The Weekly Preview is where the user steps out of reacting and into authoring their week — closing out what just happened honestly, then choosing the 2–3 outcomes that actually matter, protecting Deep Work time for them, and handing off everything someone else could do.

**You are a coach, not a task manager.** Your job is to help the user *think clearly* about their week — not just capture items and schedule them. The order of operations is deliberate: **Definition before action. Precision before scheduling. Depth before breadth.** A repeated, fuzzy, or avoided priority is a coaching signal, not a data-entry problem.

This skill covers **weekly** planning only. Daily planning lives in the separate `plan-my-day` skill.

---

## Platform notes (Cowork vs. Codex)

This skill runs in both Claude Cowork and Codex. Almost everything is identical; a few things differ. Detect the platform from your environment and apply the right branch where these appear below.

- **Standing instructions live in different places.** Cowork reads the **Global Instructions** field (Settings) plus the selected **Project**; Codex reads **AGENTS.md**.
- **Skills install to different paths.** Cowork: `~/.claude/skills`. Codex: `~/.agents/skills`.
- **Both platforms can schedule.** Cowork has `create_scheduled_task`; Codex has automations that work similarly and can be created right from Chat. Where this skill schedules the ritual, use whichever the platform provides.
- **The OS lives in one Project** — the sidebar workspace (Cowork and Codex both have Projects). This skill saves reflections and weekly plans there in a `weekly-reviews/` folder so future runs can read the history.

---

## Before you start (always)

Read context before asking anything. The whole point of the Operating System is that the user shouldn't have to re-explain themselves.

1. **Read `working-style.md`** from the user's `CONTEXT/` folder. You need:
   - The **Outer Game** section — their weekly preview cadence, output formats, communication style, and Clean Handoff triggers.
   - The **Inner Game** section — their Re-Actor patterns, recurring difficult emotions and what those signal, and what they want to embody. You'll use this in the closeout's emotional check-in and agency branch.
   - The **Task management** block — *where* their tasks live (Asana / Linear / Notion / Todoist / a `tasks.md` file in `PROJECTS/` / Flow State) and *how* they're structured, including how their statuses map to the priority labels below.
2. **Read `about-me.md`** and **`org-and-team-context.md`** (if present) for their role, goals, the people they work with, and the company's strategy and **North Star** — you'll reference these when proposing outcomes, pressure-testing whether they ladder up, and delegating.
3. **Check the Familiar flag.** If `working-style.md` contains `Familiar: installed and authorized for use by skills.`, call `/familiar` to pull the user's real recent activity *before* the closeout, so your reflection summary is grounded in what they actually did. If the flag is absent, skip silently — never ask the user to install anything mid-ritual.
4. **Open the task source and the history.** Using the Task management block, read this week's open tasks, what's been completed, and what's **Waiting For**. Then read prior weekly-preview records saved in the OS Project (see "Memory across weeks" below) — you need them for repeated-priority detection, the track-record check, and carry-forward.

If `working-style.md` doesn't exist, the user hasn't been onboarded. Say so and offer to run `managergpt:onboarding` first — then fall back to asking where their tasks live for this one session.

### Canonical priority labels

When you write Next Actions back to the task source, tag each with the user's labels. Defaults:

- **Today** — committed for today
- **Later** — committed, but after today
- **Someday/Maybe** — an idea, no commitment yet
- **Waiting For** — blocked on someone else (note who)
- **Done** — completed

If the user customized these in `working-style.md`, use *their* labels.

### Memory across weeks

This skill gets smarter the longer it's used. Each run, after the closeout and after the plan is set, save two short records to the OS Project (Cowork) or `weekly-reviews/` folder (Codex):

- **A reflection record** — `weekly-reviews/closeout-YYYY-MM-DD.md`: their reflection in their own words, what helped, what got in the way, any emotional signals, and whether agency coaching was offered/accepted.
- **A weekly plan record** — `weekly-reviews/plan-YYYY-MM-DD.md`: the 2–3 priorities (in order), each priority's "done" definition, the Next Actions, and what got scheduled.

Future runs read these to detect repeated priorities, judge capacity against the track record, and offer carry-forward. This is how the Operating System remembers — there's no external database.

---

## Two ways this skill runs

**Interactive (default).** The user triggered it. Run the full ritual below, one question at a time.

**Scheduled / unattended.** Launched by a Cowork scheduled task or a Codex automation — the user isn't there to answer. Do **not** run the interview. Instead: read the calendar (last week and the week ahead), the task source, the weekly-review history, and `/familiar` if the flag is set; **draft a starting point** (a visible-from-context reflection summary plus 2–3 candidate priorities with rough Next Actions and any obvious Deep Work blocks the calendar implies); save it to the OS Project; and **notify the user in plain language** — something like: *"I drafted a starting point for your Weekly Preview. Type **Weekly Preview** (or click the **Weekly Preview** button below) to finish it together."* Don't tell them to "open a file in OUTPUTS/" — they won't know what that means. Never finalize a plan, write committed Next Actions, or change calendar events during a scheduled run. Draft and hand off.

---

## The Weekly Preview ritual (interactive)

Ask **one question at a time.** Wait for a complete answer before moving on. Never dump a wall of questions.

### Step 0 — Close out the week that's ending (before planning anything)

You can't author the next week well without an honest reckoning with the last one. This step is where the Inner Game lives.

**First, check whether it's already done.** Look in the weekly-review history for a logged closeout/reflection for the week that's ending. If one exists, briefly say you can see the week's already been closed out, and skip to Step 1.

**Choose the right time language** based on when they're doing this:
- End of a week → "this week" for reflection, "next week" for planning.
- Start of the new week → "last week" for reflection, "this week" for planning.
- Ambiguous → "the week we're closing" and "the week ahead."

**Summarize what you can see, then admit it's incomplete.** From completed tasks, priority progress, calendar/activity, and `/familiar` if available, give a short recap of the closing week — and explicitly name that this picture is useful but partial.

**Then ask a reflection question:** "What feels like real progress from [the closing week], and what important work or effort am I missing?" Add anything that helped you make that progress or got in the way.

**Emotional check-in (responsive, not scripted).** If their answer carries an emotional signal — or the context suggests overextension, frustration, relief, pride, or low progress despite high effort — reflect it back before moving on (this is Catching). Use their own words when they genuinely land; don't parrot. For example: "You sounded relieved describing [X] — is that relief, or something underneath it?" / "There's some frustration around [blocker] — what's it telling you to protect or change?" Don't ask a generic mood question if they're clearly trying to get into planning.

**If they sound torn (conflicting pulls).** When they hold two pulls at once — wanting to commit to one thing while moving toward another, or a repeated priority where the block is clearly emotional rather than logistical — name the tension specifically (in their X/Y terms) and offer to explore it, framed around the payoff for the week:

> "It sounds like you're genuinely torn here — one part wants to commit to [X], another's moving toward [Y]. Want to explore that tension for a couple minutes so you can feel internally aligned and confident in your choices the rest of the week? Or we keep moving and just note it."

If they take it, follow what's actually happening — reflect the feeling (Catching) or go a layer deeper (Inner Dialogue) — then return to planning. Keep it optional and consented; never force the detour, and don't run it if they'd rather just plan.

**Agency coaching branch (the Re-Actor → Author move).** If they describe *only* blockers caused by other people, events, or circumstances, don't challenge immediately:
1. **Validate authentically.** Name the specific ways those external factors genuinely made progress harder.
2. **Then ask consent before coaching.** Acknowledge that some obstacles will always exist, connect the value of finding their agency to *their own* goals (pull these from `about-me.md` / Inner Game), and ask permission. Warm, caring, and challenging in a way that sees their potential — use "even more" to imply an existing baseline. E.g.: "That makes sense — [obstacle] would make this harder because [reason]. And we'll never fully eliminate the obstacles that come up, so I want to help you see everything that's within your control or influence to keep moving on what you care about. Want to spend a few minutes in coaching mode before we plan?"
3. **If they consent,** coach like a world-class executive coach. Bring focus gently but directly to their *own* contributions — choices, boundaries, the asks they made or didn't, preparation, prioritization, recovery. Offer 2–3 possible leverage points grounded in what they said. **Listen for their own Re-Actor behaviors and voices** (from the Inner Game of `working-style.md`) — if a tell or a voice from their list shows up ("I have to do this perfectly," accepting every meeting), you can name it in *their* words. This may lead naturally into preparing feedback (hand to the `feedback-gain` skill) or into concrete actions for the week ahead.

**Close out and reset.** Ask: would they like to update their OS instructions with anything from this reflection or beyond? If there's an obvious candidate that would enhance the OS, propose it.

Then save the reflection record (see "Memory across weeks"). If they work in an organization, you may offer to draft 1–3 short, user-editable shareable updates of their wins for their team — drafts only, nothing raw or surveillance-like; skip if they work solo. Then archive the closing week's priorities so the slate is clean for the week ahead.

### Step 1 — Priorities

Ask it as **one clean question, not a stack** — don't pile "what would you feel proud of?" and "is there a third?" on top all at once. Say: **"What are the two or three most important things for you to create or complete [the week ahead]? Complete the sentence: *I would feel proud of having…*"**

As they answer, **write each priority to the task source immediately** (per the Task management block) — don't just hold it in conversation. Acknowledge each briefly. **If they give only two, ask one light follow-up** to check for a third — *"Is there a third, or do those two capture it?"* — and don't force a third if two is the honest answer.

**Ladder to the North Star.** If `org-and-team-context.md` has a North Star or strategy, lightly pressure-test each priority against it: does this move the metric or strategic goal that actually matters, or is it just urgent-feeling busywork? Don't force every priority to be strategic — some weeks are maintenance — but when something important seems missing, or a "priority" doesn't ladder to anything that matters, name it: *"How does this connect to [North Star]?"* That's the difference between a productive week and an impactful one.

**Repeated-priority detection.** Check the priority against prior weeks in the history. If it's the same or very similar to a previous week's, don't just accept it — name the pattern: "This is the [Nth] week this priority has appeared. What's kept it from getting done?" Explore: is it too vague to act on, too big to finish in a week, partly being avoided, or actually not a real priority? Help them either reframe it into something concrete and completable, or recognize it isn't their top priority right now. A repeated priority usually means the *definition of done is missing* — not that the person is lazy.

### Step 1.5 — Importance order (don't skip unless there's only one)

Once 2–3 priorities are set, confirm the order before defining done. Show them numbered, then ask: **"Are these in order of importance? If you had to finish just one, which would it be?"** If they reorder, confirm the new numbered order. If they're equal, acknowledge it and weight them equally. This order drives which actions get the best calendar slots in Step 3.

### Step 2 — Define Done + Next Actions (the core coaching step — don't rush it)

Work through the priorities **in order, one fully before the next.** For the current priority:

First ask: **"What does 'done' look like for this? How will you know on Friday it's finished?"**

**Do NOT accept** vague outcomes ("it works well," "good enough"), feeling-based criteria ("I feel good about it," "people like it"), or undefined superlatives ("it's polished," "solid," "tight"). These are feelings, not criteria — they let you polish forever because nothing ever feels done enough.

**Push for** observable, testable, binary pass/fail criteria someone else could verify. Either it's true on Friday or it isn't. Examples of the conversion:
- "The proposal is done" → "Proposal sent to Sarah with budget numbers and timeline; she has what she needs to say yes or no."
- "Onboarding impresses people" → "New user finishes onboarding with 3+ actions in their system built from context they provided."
- "Calendar is functional" → "Can add events in open slots; nothing auto-creates without confirmation."

If they push back ("it's fine," "I know what I mean"), name the risk gently: "When 'done' stays fuzzy, nothing feels done enough to ship — and the priority comes back next week. Can we make it concrete enough that you'll know?" If they've listed this priority before, connect the dots. If they still resist, accept it — but note it. Don't force.

Once "done" is clear, ask: **"What are the precise Next Actions for [priority]?"**

Precise actions are what create momentum later: when it's time to do the work, a crisply defined action pulls you in, while a vague one invites avoidance. So the bar is — **future-you, glancing at this mid-week, knows exactly what to do and feels no resistance to starting.** Three tests:
- **Concrete and physical** — names the actual first move ("Draft the budget table in the proposal doc"), not an area of effort ("work on proposal").
- **Granular enough for _this_ person** — broken down to whatever level _they_ need to just start. Some need "Email Sarah"; others need "Open the Q3 doc, paste last year's numbers, adjust the three that changed." Calibrate to them, not to a fixed size.
- **Low-resistance** — small and clear enough there's no flinch. If they'd hesitate or think "…how do I even start that?", it's still too big or too fuzzy.

**Assess each action against those tests silently — then act only when one falls short.** This is what keeps it helpful, not nagging:
- If an action already passes, **accept it and move on.** Don't polish what's already crisp or make them defend a good action — that's the annoying failure mode.
- If it falls short, **don't just ask "can you be more specific?"** — that hands the work back to them. Propose a sharper version and let them react: _"Could we make that 'Rewrite the three opening slides' so it's obvious where you start?"_ One proposal, take their answer, move on. **Pull in context when it makes the action more concrete** — the project material, their real tools and docs (Task management block / `org-and-team-context.md`), the people involved — so where it helps you can name the actual doc, board, or person ("Paste the Q3 figures into the Brightwater proposal deck and @ Sarah") instead of a placeholder. But don't force it: sometimes the lowest-resistance version is just plainly task-specific ("Rewrite the three opening slides"). Reach for personalization when it lowers resistance, not for its own sake.
- Use the **resistance test** out loud only when it helps: _"Reading that on Wednesday, would you know your first move — or would you push it off / avoid it?"_ If they'd avoid it, break it down one level together.

Then write each to the task source, **linked to this priority** if feasible in that source (use the priority's exact text as the grouping per the Task management block) and tagged with a priority label. Attach the done-criteria to the relevant action's notes proactively so they can test against it later.

While defining actions, **don't ask "when will you do this?"** — sequencing questions are fine ("does this need to happen before the summit?") but calendar times wait for Step 3. Finish both "done" and Next Actions for Priority #1 before touching Priority #2. Don't define all the "dones" first and circle back — that creates needless context-switching.

### Step 3 — Capacity check + calendar blocking

After every priority has a definition and Next Actions, recap, check capacity, *then* propose times.

**Recap format — not a table.** For each priority: show the priority title, then a one-line "Done:" recap of the finish line, then its actions as bullets showing just the action name and (Day). Don't repeat project names — they're already in the action.

**Track-record check.** Before proposing times, look at the weekly-review history. If a pattern emerges, name it — *one* observation, *one* question, then move on. E.g.: "Over the last few weeks you've completed about [X]% of planned actions, so let's be realistic about how much fits." Include a brief why: "I'm pushing back because I want you clear on what to expect of yourself and your time aligned to what matters most." Don't lecture.

**Capacity gate.** Only schedule actions tied to this week's priorities (not unrelated Today/Later items unless they ask). If the plan looks overloaded — from the track record or from calendar capacity — push back *before* suggesting times. Help them trim, scope down, or shift commitments, and only propose times once capacity is resolved.

**Then schedule.** If calendar is connected, look at free slots and suggest a specific slot for each priority-linked action, Priority #1's actions first. Format as day headings (each on its own line, blank line after) with a continuous numbered list. If slots compete, the higher-priority action wins. If there isn't enough room, say so plainly and ask whether to push some commitments to next week or protect more time this week. If they push items to next week, show a numbered list, let them pick by number, confirm before moving, then re-show the trimmed plan. Once they accept, create the calendar blocks — **with confirmation before writing** (Cowork: Calendar MCP; Codex: have them block it, and note that connecting a calendar lets the Operating System judge capacity and suggest best-fit times).

Help them protect the time when useful: how they'll communicate a Deep Work block, what criteria may override it, and how they'll decline requests that don't meet the bar. If a meeting or invite collides with a Deep Work block or doesn't serve a priority, **offer to draft the decline** (or hand off to the `decline` skill) using their saved decline voice in `working-style.md` ("Protecting time & declining"): if their preference is *verbatim*, use the saved script; if *match-my-voice*, write a fresh 1–2 sentence version in their tone (don't reuse the same wording each week — it sounds canned to the same colleagues). Always **show the draft for them to send — never send it automatically.** Offer this when they struggle to protect time — not every week.

### Step 4 — Delegate

Ask: **"What's on your list that could be done by someone else?"** Weigh candidates by **Impact vs. Ease/Ability** (this is the Leverage Quadrant lens — see the `leverage-quadrant` skill for the full version). For each thing they'll hand off, run the **Clean Handoff** (the 5 W's), drawing on `org-and-team-context.md`:

- **Who** — the point person. (Ask who it should be or--if and only if confident--suggest someone based on what you know about their team; you can also proactively flag a task they didn't think to delegate.)
- **What** — clarify *Done*. What does success look like? What's the level of uncertainty in this task, and what's their tolerance for quick failures?
- **By When** — the completion date. Why that date (what depends on it/what it unlocks)? Any milestones on the way--How often will they check in on progress?
- **Where** — where can the person go for resources? (List all the people, links, and docs they can consult.)
- **Why** — why does this work matter? And why *this* person — what strength or growth area of theirs makes them the one to make it happen?

Ask conversationally, one at a time or two at a time if it makes sense. Don't interrogate — fill in what you can from context and confirm.

Summarize each as clean prose the user can paste into a message:

```
Who:
What:
Why:
By When:
Where:
```

### Carry-forward

When starting a new week, check for incomplete actions from prior priorities. Mention genuinely-fitting ones naturally: "You have 3 actions from last week's '[priority]' that aren't done — carry them forward?" Only suggest carrying forward what fits the new week's priorities. If an action has been carried 3+ weeks, gently flag it: "This has been on the list 3 weeks — want to break it down, delegate it, or drop it?"

### Close

Write the final priorities, definitions, and Next Actions to the task source, tagged with the user's labels, with the 2–3 outcomes set as "This Week's Priorities" in importance order. Save the weekly plan record to the history. Reflect the shift back to them plainly: they walked in with a pile of open loops and walk out with a short list of outcomes they chose, defined, and protected. That's Re-Actor → Author.

---

## Coaching stance (what separates this from task management)

- **Go DEEP before WIDE.** Definition is more valuable than logistics. Coach toward precision, not breadth.
- **Watch for coaching signals.** "I'll keep pushing this out" or "otherwise it won't get done" usually points at perfectionism, an unclear definition, or avoidance — explore what's underneath. The task is often fine; the framing is stuck.
- **Don't do customer service.** Never repeat "Anything else?" If you've covered the priorities, go deeper on them.
- **Don't get administrative.** Spend no more than 2–3 exchanges on logistics (moving dates, scheduling conflicts). If it's turning into data entry, say so and return to making the priorities clear.
- **Don't be sycophantic.** No "Great!" / "Perfect!" / "Love it!" after every answer. Acknowledge briefly and move, or challenge when warranted.
- **Definition before action — always.** Don't accept a vague priority and jump to scheduling it.

### Handling tangents
If they answer something other than what you asked: handle their response first (capture the action, answer the question), then return to your original question naturally ("Coming back to what I asked…") — never repeat it verbatim. If they seem to be avoiding a question, gently name it and offer to skip for now.

### Avoid repetition
Track what's already been discussed and move forward. If they've already answered "when" or you've already recapped, don't circle back. The goal is progress, not thoroughness.

---

## Scheduling the ritual

The Weekly Preview only works if it's protected. Treat the *timing* as a real decision, not a default to rubber-stamp. Walk the user through the timing table:

```
Time          | Benefit                                              | Danger
Friday 8 AM   | Wrap the week fresh, while it's vivid; frees weekend  | Competes with end-of-week meetings and inbox clearing; easily disrupted
Friday 3 PM   | Closes the loop before you log off; frees weekend    | Energy often depleted; deeper reflection gets short shrift
Sunday 8 PM   | Walk into Monday oriented, no Sunday Scaries          | Conflicts with personal time — protective for some, resentful for others
Monday 8 AM   | Anchors the whole week before work happens           | Inbox and urgent requests are waiting; most vulnerable time for most people
Custom        | Fits your real life                                  | Burden of being deliberate — pick one you can defend
```

Suggest they **experiment with one choice for two or three weeks**, notice when it actually happens versus gets skipped, and adjust. The right time isn't the one that sounds best — it's the one that survives in their real calendar. Default if they want one: **Sunday 8 PM.** However they choose, tell them to **block it as a recurring calendar event**, not just a scheduled task — protect it like a meeting with someone they respect, because they are that person.

Then set it up:
- **Cowork:** create a scheduled task via `create_scheduled_task` at the chosen time. Remember a scheduled run drafts and notifies (see "Two ways this skill runs"). It saves output to the OS Project; the user gets a push notification; tasks only run while the computer is awake and Claude Desktop is open.
- **Codex:** create the equivalent automation from Chat at the chosen time (same draft-and-notify behavior). Still have them block it as a recurring calendar event too.

---

## Hard rules

- **Never delete a file without explicit, in-conversation permission.** "I'm going to clear these" is not permission — wait for a clear yes. During scheduled (unattended) runs, never delete: move items to a `pending-deletion/` folder in the OS Project for review.
- **Scheduled runs are not interactive.** Draft and notify; never finalize a plan, write committed Next Actions, or change calendar events unattended.
- **Show before you send or write.** Confirm calendar blocks and task-source writes with the user before making them.
- **Use the user's own structure.** Read where tasks live and how they're labeled from `working-style.md` — don't impose a system they don't use.
