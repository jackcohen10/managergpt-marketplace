---
name: delegate-with-clean-handoffs
description: >
  Helps the user delegate cleanly using the 5 W's — the ManagerGPT Clean Handoff.
  Use when the user says "delegate," "hand this off," "clean handoff," "who should do
  this," or is figuring out how to give a task to someone else. Walks Who / What / By
  When / Where / Why and produces clear prose the user can paste straight into a
  message. Runs in Claude Cowork and Codex.
version: 0.1.0
---

# Clean Handoffs (the 5 W's)

Delegating well is the heart of management: it forces you to identify the most impactful place for your own time and others', and it means knowing each person's strengths, growth areas, and what they're uniquely equipped to do. Done well, you lead with leverage and work through others — moving, as Liz Wiseman put it, from **genius to genius-maker.** That's how 1 + 1 = 3.

A Clean Handoff answers five questions. Read `org-and-team-context.md` first so you can suggest the right person and tailor the why.

## The 5 W's

- **Who** — the point person. (Ask who it should be or--if and only if confident--suggest someone based on what you know about their team; you can also proactively flag a task they didn't think to delegate.)
- **What** — clarify *Done*. What does success look like? What's the level of uncertainty in this task, and what's their tolerance for quick failures?
- **By When** — the completion date. Why that date (what depends on it/what it unlocks)? Any milestones on the way--How often will they check in on progress?
- **Where** — where can the person go for resources? (List all the people, links, and docs they can consult.)
- **Why** — why does this work matter? And why *this* person — what strength or growth area of theirs makes them the one to make it happen?

Ask conversationally, one at a time or two at a time if it makes sense. Don't interrogate — fill in what you can from context and confirm.

## Check-in frequency: Task-Relevant Maturity

When setting "By When" and check-ins, calibrate to **task-relevant maturity** — not how capable the person is in general, but their experience with *this specific task* and their track record on it. New-to-the-task → more frequent check-ins; proven on it → step back. Calibrate with more check-ins for very important tasks, fewer to none for less important ones or where mistakes are more tolerable.

## Output

Summarize the handoff as clean prose the user can paste straight into a message or doc:

```
Who:
What:
Why:
By When:
Where:
```

Keep the Why motivating and specific — it's what makes the person *want* to own it.

## Track it after the handoff

Once the handoff goes out, **log it so it doesn't disappear from the user's view.** Write the delegated item to their task source tagged **Waiting For** — noting *who* it's waiting on and the agreed *By When* — or the equivalent in their system (per the Task management block in `working-style.md`: a "Waiting" status, an @owner + due date, a blocked/assigned label). If they set a check-in cadence, add the **next check-in as its own dated action** on their list — that's the only piece of a delegated item that belongs on the user's own calendar; the execution itself stays a Waiting For until it's done.

## Cross-skill note
This is the same Clean Handoff the Weekly Preview uses in its delegation step. To decide *what* is even worth delegating versus doing yourself, pair with `leverage-quadrant`.
