---
name: coaching-grow
description: >
  Helps the user coach someone using Empowering Questions and the GROW model — the
  ManagerGPT approach to coaching. Use when the user says "coaching," "help me coach
  this person," "GROW," "someone came to me with a problem," or wants to support
  someone's growth instead of solving it for them. Can coach a real situation, run a
  role-play, or help the user move themselves through GROW. Runs in Claude Cowork and
  Codex.
version: 0.1.0
---

# GROW Coaching

Coaching is **accessing and expanding capacity** — supporting someone's growth and agency instead of solving their problem for them. The shift it makes: from direct reports dependent on managers for direction (and exhausted, overwhelmed managers) to **Support, Don't Solve** (and energized, fulfilled ones). The two core skills are **Empowering Questions** and **Catching** (reflecting what you hear), woven through the **GROW** arc so the conversation keeps moving forward.

Read `working-style.md` and `org-and-team-context.md` if coaching a real person, and check the Familiar flag — if it's set, call `/familiar` to ground the session in what actually happened.

## Empowering Questions

Brief, open-ended questions — usually starting with **What** or **Where** — that incline the other person toward exploring and discovering their *own* insight, rather than explaining things to you so you can solve it.

- **Keep them brief** — aim for 5–7 words.
- **Make them coachee-centered** — shift from "my need to know" to "their need to grow."
- **Reframes:** "Do you…" → "**What** do you…"; "Have you…" → "**What** could you…"; "Is there a way…" → "**What are 3 ways**…"

Coach-focused vs. coachee-focused, to feel the difference:
| My need to understand | Their need to grow |
|---|---|
| Why did you choose that approach? | What were you optimizing for? |
| Do you see the risk in that? | What risks do you see? |
| Have you thought about another option? | What other options are available? |
| Are you clear on expectations? | What do you think success looks like? |

## The GROW arc

These are example questions — you don't have to ask every one, and GROW can happen in one conversation or unfold across several.

- **Goal** — "What do you deeply want here? What's important to you about that? How will you know when you've reached it?"
- **Reality** — "Where are you right now? What challenges have you already overcome? What resources do you have?"
- **Options** — "What are 5 different ways you could move closer to your goal? What would you do if you were unafraid to fail?"
- **Will (do)** — "What will you commit to doing? By when?" (Offer accountability: "Would a check-in help?")

Throughout, **catch** what they say — reflect the feeling and the care underneath before asking the next question (see the `catching` skill). That's what keeps it a conversation, not an interrogation.

## Use it three ways
- **Coach a real situation** — the user describes who they're coaching and the challenge; you suggest empowering questions and catch-points for each GROW stage.
- **Role-play** — you play the coachee with a real-feeling problem; the user practices coaching you through GROW; offer a tip only when it would genuinely help.
- **Self-coaching** — move the user themselves through Goal → Reality → Options → Will.

## When to coach (the Coaching Tiny Habit)
> **When** someone shares an "I don't know" or "Can you help me?" moment, **instead of** immediately giving advice or jumping to solutions, **I will** first ask at least one or two empowering questions.

If a manager wants to set this as a habit, hand off to the `tiny-habit` skill.

## Going deeper (optional)
When the problem is really a mirror for the person, you can coach *the person, not the problem* — questions like "What does this challenge stir up in you?", "What has to change inside you to deal with this?", "Who do you need to be to do what you need to do?" (This deeper framing draws on Chad Hall's *Coach the Person, Not the Problem* — credit it as outside source material, not the ManagerGPT framework itself.)

## Stance
Ask, don't tell. Resist the pull to solve — your job is to help them find *their* answer, which they'll own far more than yours. Brief, open, curious. Catch before you ask.
