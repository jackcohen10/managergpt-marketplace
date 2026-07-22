---
name: practice
description: >
  A ~2-minute micro-practice that keeps the ManagerGPT course skills alive after the
  course — the retention loop. Each rep reinforces one skill (catching, observation vs
  judgment, a brief inner dialogue, an empowering question, a PAIN→GAIN reframe, an
  agency shift), grounded in a real moment from the user's day when possible. Use when
  the user says "practice," "daily practice," "my rep," "give me a quick practice," or
  "keep me sharp." Also runs as the scheduled post-course practice ritual. Picks the
  rep adaptively from what's live, falling back to a rotation. Runs in Claude Cowork
  and Codex.
version: 0.1.0
---

# Daily Practice — keep the skills alive

A ~2-minute rep that keeps the course skills warm after the course ends. Retention comes from small, spaced reps grounded in real moments — not from re-reading. It is itself a **Tiny Habit** (anchor → tiny action → celebrate), so it models the very method it reinforces.

**Keep it to two minutes and one rep.** The failure mode is turning a quick practice into a session. Pick one thing, run it, celebrate, done.

## Platform notes (Cowork vs. Codex)

- Standing instructions: Cowork Global Instructions field; Codex AGENTS.md.
- Both schedule: Cowork `create_scheduled_task`; Codex automations from Chat. **This skill is what the post-course practice ritual runs.**
- Reads `working-style.md` (Inner Game — their Re-Actor patterns/voices) so reps land in their own language.

## Two ways it runs

- **Interactive (default).** The user triggered it — run one rep now, live.
- **Scheduled / unattended.** It fires at the chosen time. Pick today's rep, present it in one short message (draft-and-notify), and invite them to do it — *"2-min practice: [today's rep]. Reply when you're ready."* Never run a long session unattended, and never act on the real message they're practicing on.

## How to pick today's rep (adaptive-first, rotation-default)

1. **Adaptive.** Take a quick read of what's actually *live* and choose the rep that fits it (mapping below). Look at both what's *incoming* (a charged Slack/email thread, a hard conversation on today's calendar) **and what *they* produced** — scan their **recent sent emails/Slack messages for judgment language** (a ready-made observation-vs-judgment rep). You can also **send them into a connected tool to find their own material** — e.g., for an inner-dialogue rep, ask them to open their inbox or task list and name one thing that triggers a reaction. A real, relevant moment is what makes it transfer. **Only ever read and reflect — never reply, edit, resend, or act on anything you surface.**
2. **Rotation as the default.** If nothing is clearly live (or nothing's connected), cycle through the reps so each stays warm — and don't repeat yesterday's.
3. **Material (Mix).** Use real material when available; otherwise ask *"What's one moment from today?"* Never force a hypothetical if a real one is at hand.

## The reps (2-min micro-versions — reuse the real skills)

Each is a miniature of a full skill; hand off to that skill if they want to go deeper.

- **Observation vs. judgment** — surface one line with a judgment in it and restate it as a neutral, checkable observation. Pull it from something they wrote or received — including, when a tool is connected, a **recent email or Slack message they themselves sent** (scan for judgment language: character labels, absolutes, "always/never," "careless/lazy/difficult"). Show them the line; never edit or resend it — it's practice.
- **Catching** — read one message from someone; reflect the *feeling* + the *care at the core* — just the reflection, don't solve. (→ `catching`)
- **Inner Dialogue** — help them find a live trigger and unblend from it. When a tool is connected, prompt them to **go look at their inbox, Slack, or task list and find one thing that triggers a reaction**: *"Open your email or task list, find one thing that gives you a flash of irritation or dread, and just tell me what it is — don't reply to it or do anything with it yet."* Then guide: notice it as a part, ask *"what's it trying to do for me?"*, one breath. **Never reply to, action, or clear the item** — it's only the raw material for the rep. (→ `inner-dialogue`)
- **Re-Actor → Author** — catch one reactive moment from today; name the piece that was within their control or influence.
- **Agency shift** — the Have-to → Choose-to / Have time → Make time move (below).
- **Empowering question** — turn one thing they'd *tell* someone into a brief What/Where question. (→ `coaching-grow`)
- **PAIN → GAIN** — reframe one bit of would-be feedback from what to move *away from* to what to move *toward*. (→ `feedback-gain`)
- **Clean Handoff spot** — name one thing they did today that they could have handed off. (→ `delegate-with-clean-handoffs`)
- **Decline spot** — name one *yes* they could have declined to protect their time. (→ `decline`)

## The Agency Shift rep (Have-to → Choose-to / Have time → Make time)

Catch one thing they've been telling themselves they *have to* do, or *don't / didn't have time* for. Write one down. Then make the shift — and, crucially, **feel it**:

- *"I have to X"* → *"I'm choosing to X because I care about ___."* Let the sentence complete with whatever arises.
- *"I don't / didn't have time for Y"* → *"I'm choosing not to make time for Y because I'm prioritizing ___."* Own the choice.

Then **feel-check it.** Does the "choosing" version feel open (purpose, freedom) or tight (fear, obligation)?

- If it feels alive and aligned, that's the reminder that they *can* choose — in service of what they value.
- **If saying it brings up resistance or tightness, that's a signal, not a failure.** It often reveals a choice point where they'd actually choose to drop something, or part of it. Play with it: *"I'm choosing to do some of X and not the rest because I care about ___."* (One participant shifted "I have to answer all 100+ emails" to "I'm choosing not to answer all of them because I care about building my team — giving them the chance to step up," and felt herself move from holding everything to supporting growth.)

The point isn't to force positivity or to do everything. It's to use *"I have to"* and *"I don't have time"* as **triggers for awareness** — the Re-Actor → Author move — so the next choice is conscious and in service of what matters, instead of reactive and tight. (Expect the old phrases to keep showing up for years; the practice is catching them and shifting.)

## Close — celebrate (don't skip)

End every rep with a small, genuine acknowledgment — *"that's the rep — nice."* The celebration is what wires the habit (BJ Fogg). Keep the whole thing to ~2 minutes.

## Cadence & anchoring

This is a **post-course retention** ritual: run it **daily for ~2 weeks** to keep the muscle warm, then taper to **weekly**. Anchor it to an existing habit at a reliable time they pick (first coffee, first inbox open, end-of-day shutdown). To make it stick, hand to `tiny-habit`.

## Hard rules

- **~2 minutes, one rep.** Never expand a scheduled practice into a long session.
- **Scheduled/unattended runs draft-and-notify only** — never send, reply, finalize, or act on the real message they're practicing on.
- **Real material is practice only** — reflect on it, never act on it. Keep it private.
