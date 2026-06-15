---
name: leverage-quadrant
description: >
  Helps the user prioritize with the Leverage Quadrant — deciding what's their
  Genius work to do versus what to delegate, a ManagerGPT framework. Use when the
  user says "leverage quadrant," "what should I focus on," "what should I delegate,"
  "I'm overloaded," "prioritize my projects," or wants to find the highest-leverage
  use of their time. Stack-ranks their work by impact, sorts it by whether it's
  uniquely theirs, and points to what to give away. Runs in Claude Cowork and Codex.
version: 0.1.0
---

# Leverage Quadrant

**Leverage is amplifying the impact of your inputs** — working through others to extend what you can create. The questions at the heart of it: *Which "Legos" do you give away? And what's the 5x-bigger Lego tower you could build if you did?*

This skill sorts the user's real workload so they can put their time where it has the most leverage — their **Genius** work — and hand off the rest, moving from genius to **genius-maker**.

Read `about-me.md` and **`org-and-team-context.md`** (their goals, and the company's North Star, strategy, and key metrics) and, if connected, their task source — so you can pull the actual list instead of starting blank, and judge impact against what the org actually cares about.

## The exercise

1. **List 7–10 big projects or tasks** currently on their plate — 2–3 words each. (Offer to pull them from their task source.)
2. **Stack-rank by impact on the North Star / strategic goals** (from `org-and-team-context.md`) — most impactful at the top, least at the bottom.
3. **Place each on the quadrant** by two questions:
   - **Impact** — high or low for the company's North Star / strategic goals? Anchoring impact to the *real metric* keeps this honest: a task can feel important and still not move what matters.
   - **Is it something you and only you are equipped to do?** — is this uniquely yours (where you create the most value), or could someone else do it well enough (especially with a Clean Handoff)?

## Reading the quadrant

| | **High impact** | **Low impact** |
|---|---|---|
| **Uniquely yours** | **DO THIS** — your highest leverage. Protect Deep Work time for it. This is the 5x Lego tower. | **Be careful** — satisfying but not moving the needle. Time-box it; don't let it crowd out the top-left. |
| **Others could do it** | **DELEGATE** — the biggest unlock. Hand off cleanly (use `delegate-with-clean-handoffs`). Develop the person while you free your time. | **Minimize / drop / automate** — batch it, decline it, or systematize it. |

The point isn't to do more — it's to concentrate your time on the top-left and give away as much of the right column as you can. Surfacing one or two big things to delegate is usually the highest-value outcome of the exercise.

## Output
Show the quadrant filled in (a simple table works; or offer the draggable **Interactive mode** below if they'd rather place it visually). For everything in the **Delegate** box, offer to run a Clean Handoff right now — and once handed off, **track it as a Waiting For** in their task source (who + By When, or the equivalent status per the Task management block), with any check-in as its own dated action; the `delegate-with-clean-handoffs` skill does this. For the **Do** box, offer to block Deep Work time (or feed it into the next Weekly Preview) or ask if there are items here where they would prefer to hire someone and can use this as the start of a job description.

## Interactive mode (optional — Cowork & Codex)

Some people place faster by *dragging* than by answering item-by-item. An interactive quadrant ships with this skill at `${CLAUDE_PLUGIN_ROOT}/skills/leverage-quadrant/assets/` (`quadrant.html` + `serve.py`). Offer it when they'd rather sort visually; otherwise the conversational version above is the default. Either way **you** rank the items by impact first and hand them over pre-placed — the user adjusts, they don't start from a blank grid.

The user sets two dimensions per item (impact ↑, others-can-do →), then clicks **Complete and prep delegation**. Axes: top-left = Do this, top-right = Delegate, bottom-left = Be careful, bottom-right = Minimize. How the result comes back differs by surface:

- **Cowork** — create an artifact from `quadrant.html`, injecting the ranked items as `window.LQ_ITEMS = [{n,imp,oth}, …]` (imp/oth are 0–100; default 50). On **Complete and prep delegation**, the page calls `sendPrompt()` and the placements land back in chat.
- **Codex** (in-app browser; needs the Browser plugin) — write the ranked items to `items.json` beside the asset, run `python3 serve.py`, and open `http://localhost:8000/quadrant.html` in the in-app browser. On **Complete and prep delegation**, the page POSTs to the local server, which writes `placements.json`; read that file to continue. (The page also falls back to downloading `placements.json` if no server is present.)

Once you have the placements (from either surface), continue exactly as in **Output**: Delegate box → Clean Handoff + track as Waiting For; Do box → protect Deep Work / feed the next Weekly Preview. If neither interactive path is available, just use the conversational table — nothing is lost but the dragging.

## Cross-skill note
This is the same Impact-vs-Ease/Ability lens the Weekly Preview uses in its delegation step. Pair with `delegate-with-clean-handoffs` to actually hand off what you decide to give away.
