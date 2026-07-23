---
name: start-practice
description: >
  Turns on the post-course Daily Practice — the one command to schedule the ~2-minute
  daily rep that keeps the ManagerGPT course skills alive. Use when the user says
  "/managergpt:start-practice," "turn on my daily practice," "set up my daily practice,"
  "start my practice," or "schedule my practice." Asks for a reliable time and an anchor
  habit, then creates the single recurring Daily Practice task. Does NOT create or change
  any other ritual. Runs in Claude Cowork and Codex.
version: 0.6.0
---

# Start Daily Practice

The one command to turn on the post-course **Daily Practice** ritual — a ~2-minute daily rep that keeps the course skills alive (see the `practice` skill for what a rep looks like). This *only* sets up the Daily Practice schedule; it deliberately doesn't create, reconcile, or touch any other ritual.

## Platform notes
- Cowork: `create_scheduled_task`. Codex: an automation created from Chat.

## How to run it

1. **Confirm they want it on.** This is a light post-course retention habit — one small rep a day.
2. **Pick a reliable time + anchor.** Ask when they'll actually do it (first coffee, first inbox open, end-of-day shutdown) and set the schedule to that **local** time. Tie it to an existing habit — hand to `tiny-habit` if they want to lock the anchor.
3. **Cadence.** Start **daily** for ~2 weeks to build the habit, then switch to **weekly**. Tell them they can ask you to taper to weekly once it's sticky.
4. **Check for an existing one first.** If a Daily Practice task already exists, offer to adjust its time instead of creating a duplicate — never duplicate.
5. **Create the single Daily Practice task** (draft-and-notify). Use this prompt:
   > "Run the ManagerGPT Practice skill in scheduled mode. Pick one 2-minute rep — adaptive to what's live in my day (a charged message, a hard conversation coming up), falling back to a rotation across the skills; use real material if available, else ask me for one moment. Present just today's rep in a short message and invite me to do it. Keep it to one rep, ~2 minutes; never run a long session, and never act on the real message I'm practicing on."
6. **Confirm** the time and that it's set, and suggest clicking **Run now** once to pre-approve the tools it uses.

## Note

This is the only ritual meant to be turned on *after* the course. The core rituals (Weekly Preview, Plan My Day, Retrospective) are set up during onboarding — this command leaves them alone by design.
