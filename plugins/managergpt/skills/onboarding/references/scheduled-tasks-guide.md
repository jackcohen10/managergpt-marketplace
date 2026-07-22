# Scheduled Tasks Guide

How to set up the recurring rituals in the **Closer**. These are turned on **by default** — don't ask whether, only when. Read before the Closer.

Cowork uses `create_scheduled_task`; Codex has automations that work the same way and are created from Chat — use whichever the platform provides. Both run in a fresh session with no conversation history, so each prompt must be **fully self-contained.** They run only while the computer is awake and the app is open, save output to the OS Project, and send a notification on each run.

---

## The draft-and-notify pattern (critical)

A scheduled run is **not interactive** — it fires at a set time whether or not the user is there to answer questions. So the planning rituals must **draft a starting point and notify the user to finish interactively**, never attempt the full interview unattended. (If they tried, they'd either stall waiting for answers no one's there to give, or invent the user's answers and write a fake reflection into the files.) Say *why* in the prompt — "since no one is present to answer" — so it's clear this is by design, not a watered-down version. The full interactive Weekly Preview / Plan My Day still runs whenever the user triggers it themselves. And per the hard rules, **scheduled runs never delete** — anything slated for removal goes to a `pending-deletion/` folder for review.

Each prompt should: read the relevant context (calendar, task source, weekly-review history, `/familiar` if the flag is set) → draft → save to the OS Project → notify.

---

## The three default automations

### 1. Weekly Preview
The timing is a real decision — walk the **timing table** interactively and let the user choose (don't just pick):

| Time | Benefit | Danger |
|---|---|---|
| Friday 8 AM | Wrap the week fresh, while it's vivid; frees the weekend | Competes with end-of-week meetings and inbox clearing |
| Friday 3 PM | Closes the loop before logging off | Energy depleted; reflection gets short shrift |
| Sunday 8 PM | Walk into Monday oriented, no Sunday Scaries | Conflicts with personal time |
| Monday 8 AM | Anchors the week before work happens | Inbox is waiting — most vulnerable slot for most people |
| Custom | Fits their real life | Burden of being deliberate |

Default **Sunday 8 PM**. Suggest they experiment for 2–3 weeks and also block it as a recurring **calendar event**.
```
Prompt: Run the Weekly Preview skill in scheduled DRAFT mode. Read my calendar (last
week and the week ahead), my task source and weekly-review history (per
working-style.md), and call /familiar if the flag is set. Draft a starting point — a
short reflection summary and 2–3 candidate priorities with rough Next Actions — save it
to the OS Project, and notify me in plain language: "I drafted a starting point for your
Weekly Preview — type Weekly Preview (or click the button below) to finish it together."
This run is unattended, so draft only and stop there: do not attempt the full
interactive interview (no one is present to answer the reflection or priority
questions), and do not change the calendar, send messages, or delete anything. The full
interview happens when I run it myself.
Schedule: Sunday 8 PM (0 20 * * 0)
```

### 2. Plan My Day
Ask **when** — weekday mornings or evenings — and tie it to an existing habit.
```
Prompt: Run the Plan My Day skill in scheduled DRAFT mode. Read today's calendar, this
week's priorities, open/overdue tasks, the daily buffer (working-style.md), and
/familiar if set. Draft available time after buffer, a short list of Today actions
tied to the week's priorities, and a suggested first task. Save to the OS Project and
notify me in plain language: "I drafted a starting plan for your day — type Plan my
day (or click the button below) to finish it together." This run is unattended, so
draft only and stop there: do not attempt the full interactive session (no one is
present to answer), and don't finalize or delete anything. The full session happens
when I run it myself.
Schedule: weekday mornings (0 8 * * 1-5) — or the time they chose
```

### 3. Monthly retrospective backstop (Tune Your OS)
Runs the `retrospective` skill — the self-improvement loop. The **main** cadence is every other Weekly Preview (the preview offers it). This scheduled task is only a **floor**: it makes sure a retrospective happens at least once a month even if previews were sparse, and it **skips itself** if one already ran this month.
```
Prompt: Monthly retrospective backstop. FIRST check weekly-reviews/ for a retro-*.md
dated in the current calendar month. If one exists, do nothing and send no
notification — a retrospective already happened this month. Otherwise, run the
Retrospective skill in scheduled DRAFT mode: read my context files and my history
across the last few weeks — weekly-review history, plan records, task completion
(including anything carried 3+ weeks and Waiting For), calendar adherence, and
/familiar if set. Spot patterns: buffer accuracy, completion rate, repeatedly deferred
or delegable work, recurring Re-Actor behaviors/voices, Deep Work protection. Also note
what's changed (new projects, dropped tools, new people) and whether the
task-management mapping still holds. Draft the findings and a few proposed
working-style.md tweaks, save the draft to the OS Project, and notify me in plain
language: "I reviewed the last few weeks and have a few small tweaks to suggest — type
'tune my OS' to go through them together." This run is unattended, so draft only: do
not change any context file or apply changes (no one is present to confirm).
Schedule: last Friday of the month (0 9 24-31 * 5)
```

---

### 4. Daily Practice (post-course retention — optional)
Runs the `practice` skill — a ~2-minute rep that keeps the course skills warm. Designed to start **after the course**: daily for ~2 weeks, then taper to weekly. Anchor it to a reliable time the user picks.
```
Prompt: Run the Practice skill in scheduled mode. Pick one 2-minute rep — adaptive to
what's live in my day (a charged message, a hard conversation coming up), falling back
to a rotation across the skills; use real material if available, else ask me for one
moment. Present just today's rep in a short message and invite me to do it — e.g.
"2-min practice: [rep]. Reply when you're ready." Keep it to one rep, ~2 minutes; never
run a long session, and never act on the real message I'm practicing on.
Schedule: a reliable daily time the user chooses (e.g. 0 8 * * 1-5) for ~2 weeks, then
switch to weekly.
```

## Cron quick reference (local time, not UTC)

| Schedule | Cron |
|---|---|
| Weekdays 8 AM | `0 8 * * 1-5` |
| Sunday 8 PM | `0 20 * * 0` |
| Friday 3 PM | `0 15 * * 5` |
| Monday 8 AM | `0 8 * * 1` |
| Last Friday of month | `0 9 24-31 * 5` |

---

## Tips

- One ritual at a time; confirm the schedule before creating.
- Only schedule tasks that use tools the user actually connected.
- Tell them tasks run only while the computer is awake and the app is open.
- Everything is adjustable later (`update_scheduled_task` / the Codex automation UI).
- Also mention the optional `/managergpt:protect` security review.
