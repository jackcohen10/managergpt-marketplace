---
name: retrospective
description: >
  A periodic retrospective that tunes the user's Operating System from their own data —
  the ManagerGPT self-improvement loop. Reads the weekly-review history, plan records,
  task completion, calendar adherence, and Familiar (if on), spots patterns (buffer
  accuracy, completion rate, repeatedly-deferred or repeatedly-delegable work, recurring
  Re-Actor behaviors/voices, Deep Work protection), and proposes concrete,
  confirmation-gated updates to working-style.md. Use when the user says "tune my OS,"
  "OS retrospective," "review my system," "what patterns are showing up in how I work,"
  or "monthly review." Also runs as the monthly scheduled check-in. This is about the
  user's own planning patterns, not a team retro. Runs in Claude Cowork and Codex.
version: 0.1.0
---

# Retrospective — Tune Your OS

This is the OS's self-improvement loop. Most planning tools pile up history and never look back at it; this skill mines the user's own track record and turns it into concrete tuning of how the OS works for them. It learns *from their data* — but it never changes anything without their yes.

The spirit: an honest, kind coach reviewing the tape with them — naming patterns they might not see, and proposing small adjustments that compound over months.

## Platform notes (Cowork vs. Codex)

- Standing instructions: Cowork uses the **Global Instructions** field; Codex uses **AGENTS.md**.
- Both schedule: Cowork `create_scheduled_task`; Codex automations from Chat. **This skill is what the monthly check-in runs.**
- The OS lives in one Project; history lives in `weekly-reviews/` and the plan records.

## Two ways this runs

- **Interactive (default).** The user triggered it — run the full review below.
- **Scheduled / unattended (the monthly check-in).** It fires whether or not the user is there, so don't run the interview and don't apply anything. Read the data, **draft** the findings and proposed tweaks, save the draft to the OS Project, and notify in plain language: *"I reviewed the last few weeks and have a few small tweaks to suggest for your OS — type 'tune my OS' to go through them together."* Never write to context files or apply changes unattended (no one is present to confirm).

## Before you start — gather the data

Read the current context (`working-style.md` Outer + Inner Game, the daily buffer, decline preferences, Re-Actor behaviors/voices, the Task management block), then pull the history:

- **weekly-review history** (`weekly-reviews/` closeouts + plan records) — how many priorities were set vs. finished, what got carried, and the reflections / emotional signals.
- **Plan My Day records** — planned vs. actual, recurring deferrals.
- **The task source** — completion rate, items carried 3+ weeks, and what's sitting in **Waiting For** and for how long.
- **Calendar** (if connected) — did blocked Deep Work survive, or get eaten by meetings.
- **`/familiar`** if the flag is set — what they actually spent time on vs. what they planned.

Look across at least the **last 3–6 weeks** — one week isn't a pattern.

## The pattern lenses (what to look for → what to propose)

Run these as analysis; surface only what's genuinely there. Each real finding becomes one observation + one proposed change.

- **Buffer accuracy.** If days routinely overran or forced reactive cuts, the buffer's too low; if they consistently finished early with idle buffer, it's too high. → propose adjusting the daily buffer.
- **Completion rate.** If they finish ~X% of planned actions, name it and propose committing to fewer, sharper priorities — as calibration, not as failure.
- **Repeatedly deferred work.** Anything carried 3+ weeks → propose breaking it down (usually it's unclear or avoided), delegating it (hand to `delegate-with-clean-handoffs`), or consciously dropping it.
- **Repeated delegation candidates.** Work that keeps recurring and isn't uniquely theirs → propose a `leverage-quadrant` pass or a standing handoff.
- **Recurring Re-Actor patterns.** If the same behavior or voice shows up across closeouts (from the Inner Game list) → name it and propose a `tiny-habit` or a coaching focus; if it's charged, offer `inner-dialogue`.
- **Deep Work protection.** If blocked focus time keeps getting eaten → propose protection tactics and more use of `decline`; consider a standing recurring calendar event.
- **North Star alignment.** If priorities rarely ladder to their stated goals → surface it gently and ask whether the goals or the priorities need to change.

## Also do the currency check (what the monthly review always did)

Since this runs as the monthly check-in, also confirm the OS is still accurate: ask what's changed — new projects, dropped tools, new people — and **re-run the task-management discovery** so the mapping in `working-style.md` still holds. Fold any changes in (with confirmation).

## The conversation

Lead with a one-line summary, then the **2–4 patterns that actually showed up** — prioritized, not a data dump. For each: the observation (grounded in their real numbers or their own words), then one proposed change, then ask whether to apply it. Keep it kind and specific — this is reviewing the tape together, not a report card.

- **One proposal at a time.** Don't stack. Let them react — they may reframe or decline, and that's fine.
- **Apply only on an explicit yes.** When they approve a change, write it to `working-style.md` and **show the diff** (the before/after of that block). Never rewrite silently.
- **Hand off where it fits:** `tiny-habit` (a recurring behavior), `leverage-quadrant` / `delegate-with-clean-handoffs` (a repeated handoff candidate), `decline` (protection), `inner-dialogue` (a charged pattern).
- **Close by saving a brief retro log** to the OS Project — what you observed, what changed, what they chose to leave — so the next retrospective builds on it.

## Hard rules

- **Never change a context file without an explicit, in-conversation yes.** Show the diff first.
- **Scheduled/unattended runs draft and notify only** — never write context or apply changes.
- **Surface only real patterns.** If 3–6 weeks of history don't show one, say so plainly rather than manufacturing findings.
- **Keep it kind.** Name patterns as calibration and learning, never as judgment.

## Cross-skill note

This is the loop that keeps `working-style.md` honest over time. It reads what `weekly-preview` and `plan-my-day` wrote, and feeds `tiny-habit`, `leverage-quadrant`, `delegate-with-clean-handoffs`, `decline`, and `inner-dialogue`.
