# Scheduled Tasks Guide

How to set up the recurring rituals in the **Closer**. These are turned on **by default** — don't ask whether, only when. Read before the Closer.

Cowork uses `create_scheduled_task`; Codex has automations that work the same way and are created from Chat — use whichever the platform provides. Both run in a fresh session with no conversation history, so each prompt must be **fully self-contained.** They run only while the computer is awake and the app is open, save output to the OS Project, and send a notification on each run.

---

## The draft-and-notify pattern (critical)

A scheduled run is **not interactive** — the user isn't there to answer questions. So the planning rituals must **draft a starting point and notify the user to finish interactively**, never run the full interview unattended. And per the hard rules, **scheduled runs never delete** — anything slated for removal goes to a `pending-deletion/` folder for review.

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
Prompt: Run the Weekly Preview skill in scheduled mode. Read my calendar (last week
and the week ahead), my task source and weekly-review history (per working-style.md),
and call /familiar if the flag is set. Draft a starting point — a short reflection
summary and 2–3 candidate priorities with rough Next Actions — save it to the OS
Project, and notify me to finish interactively. Do not run the full interview, change
the calendar, or delete anything.
Schedule: Sunday 8 PM (0 20 * * 0)
```

### 2. Plan My Day
Ask **when** — weekday mornings or evenings — and tie it to an existing habit.
```
Prompt: Run the Plan My Day skill in scheduled mode. Read today's calendar, this
week's priorities, open/overdue tasks, the daily buffer (working-style.md), and
/familiar if set. Draft available time after buffer, a short list of Today actions
tied to the week's priorities, and a suggested first task. Save to the OS Project and
notify me to finish interactively. Don't finalize or delete anything.
Schedule: weekday mornings (0 8 * * 1-5) — or the time they chose
```

### 3. Monthly context check-in
```
Prompt: Read my CONTEXT/ files and summarize each. Ask what's changed — new projects,
dropped tools, changed preferences, new people. Re-run the task-management discovery
query (working-style.md) and update the Task management block if my tool or
conventions changed. Save a brief log to the OS Project. Update files only with my
confirmation; never delete.
Schedule: last Friday of the month (0 9 24-31 * 5)
```

---

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
