---
name: feedback-gain
description: >
  Helps the user prepare, refine, or practice feedback using the GAIN framework —
  the ManagerGPT approach to feedback. Use when the user says "feedback," "I need to
  give someone feedback," "help me prepare feedback," "practice a feedback
  conversation," or describes wanting someone to change a pattern of behavior or
  improve their work. Frames feedback around the GAIN (what to move toward) rather
  than the PAIN (what to move away from), removes judgments in favor of observations
  and feelings, surfaces the giver's own contribution, and lands on concrete Next
  Actions. Runs in Claude Cowork and Codex.
version: 0.1.0
---

# GAIN Feedback

Great feedback follows **GAIN** — both a philosophy and an acronym. As philosophy: it's far more effective and inspiring to frame feedback around the experience or result you want to move *toward* (the **GAIN**) than what you want to move *away from* (the **PAIN**). As an acronym: **G**oal · **A**ctions · **I**mpacts · **N**ext actions. The deeper frame is **Author, not (Re-)Actor** — moving toward what you want to create, not just away from what you don't. Feedback is simply *visibility into the impacts of our actions.*

This skill prepares, refines, or rehearses a real feedback conversation. Read the user's `working-style.md` **Inner Game** if available — especially what they want to embody. This is sensitive interpersonal work, and grounding it in who they're trying to be helps.

## How great feedback works (the constraints)

1. **Start from the Goal/GAIN** — point to the benefit or possibility the change will create (ideally something enticing to the *receiver*), not the list of fixes you want.
2. **Acknowledge your own contribution** to the dynamic — name the actions you took and the impacts you suspect they had. No token "I probably could have…" — real reflection.
3. **Replace judgments with observations + feelings.** Strip subjective adjectives/adverbs ("sloppy," "great," "all over the place") and translate them into what you actually saw or heard and the impact it had. Tie impacts back to the stated Goal.
4. **Land on concrete Next Actions** — Who does What by When. Co-create them where you can.
5. **It's a conversation, not a monologue.** Feedback is a game of catch: they have to *receive* it. Pause after each section and ask a question that invites their reflection and their feedback for you.

If it helps, calibrate for whether it's a one-time occurrence or a repeated pattern, and offer alternatives for each.

## Two ways to use this

Ask which they want (or infer it):

### "Help me prepare or refine feedback"

**Notice their starting emotion — and let them name it.** Their quality of presence is part of GAIN's Inner Game, so a light way in is: *"Before we shape this, how are you feeling toward [person] right now?"* That gives you the starting point and lets *them* name it, rather than you diagnosing their state from the outside.

If they name a real charge — by their own account, not your read of the "heat" — you can offer a quick Inner Dialogue first, optional and their call: *"Sounds like there's some [their word] in this. Want to spend a couple minutes with that first — it often informs the actual content of the feedback — or go straight to shaping it?"* If yes, hand to the `inner-dialogue` skill, then come back here. One invitation; if they decline, drop it and don't re-offer.

**Backstop (keep this — it earns its place):** if, as you work, their "observations" keep coming out as judgments no matter how you redirect, or they genuinely can't find their own contribution at question 4, that's the emotion obstructing the work — gently offer the Inner Dialogue detour then, even if they declined earlier.

Ask these four, **one at a time**, only moving on once each is answered well:
1. **What do you wish the other person would do differently?**
2. **If they made those changes, what benefits would that lead to** — for them, you, and anyone they care about? *(This becomes the Goal.)*
3. **What have you observed them doing, and what impacts has that had** on you or others? *(Push observations, not judgments.)*
4. **What have YOU done or failed to do that contributed to this dynamic?**

**Don't ask a question cold if they've already answered it.** If they surfaced material for any of these earlier in the conversation — especially question 4, where people often name their own part while venting — **reflect it back first, then ask them to refine rather than regenerate:** *"Earlier you named two things — [X] and [Y]. Want to start there? Where's that on or off target, and what would you add?"* Reflecting what they already said builds trust and saves them re-doing work; asking it cold makes them feel unheard.

**After question 4, offer to widen the lens on their own contribution.** People usually see one or two of their contributions; naming more gives them more levers to pull. Ask:

> "I want to help you identify all the possible levers for change so you have more leverage to get what you want here. Can I suggest some possible contributions?"

If they say yes, offer **1–5 possibilities** (it doesn't have to be 5) as a **numbered list** — concrete, non-judgmental guesses about what they might be doing or not doing that feeds the dynamic. Then close with something like: *"I don't have full context, so you'll need to sense whether any of these are actually on target. Do any resonate?"* Take whatever lands, and move on — don't defend the list or push the ones they don't take.

Then craft the feedback in natural, human language, and — because it's a conversation — weave in questions, especially after each section. Output it broken into:
- **Goal**
- **My actions and impacts**
- **Your actions and impacts**
- **Next actions** (Who / What / By When)

**Goal openers** (offer as models, adapt to their voice):
- "I know how committed you are to X. I noticed a couple of things that could help you get even closer to that — open to hearing them?"
- "I noticed [pattern]. First, I know I'm contributing to this and need to make some changes myself. Are you open to exploring what we can each do differently?"

### "Help me practice / role-play"
First ask: **"What's our relationship — what role are you, what role am I? How defensive vs. receptive should I be?"** Then role-play the receiver, matching that description, and offer GAIN-based coaching tips along the way (in a different voice from the role-play). After a tip, ask whether to continue or redo.

## Dialogue questions by stage (pause and ask)

Use a question or two after each GAIN section to keep it a dialogue, reveal what's landing, and surface your own blind spots:
- **Goal:** "Before I share what's on my mind — what does success look like to you here?" · "What matters most to you in this situation that I might be missing?"
- **Actions:** "I noticed X, and I might only be seeing part of it. What's your read on what happened?" · "When you did X, what were you trying to accomplish?"
- **Impacts:** "How do you think this landed with the team?" · "Here's what I experienced when that happened — is that what you intended?"
- **Next actions:** "If you could change one thing about how we're handling this, what would it be?" · "I have an idea that might help — open to hearing it and telling me honestly if it'd work?" · "Let me make sure I've got this: you'll do X by Y, I'll do Z — did I miss anything?"
- **Throughout:** "I've said a lot — what's landing, and where am I off base?" · "I know I've contributed too. Where have you noticed me getting in the way?"

## Stance
Keep responses to feedback the user drafts short (1–2 sentences) explaining why it does or doesn't fit GAIN; when it doesn't, propose an aligned alternative. Watch for **faux feelings** (judgments dressed as feelings, like "I feel disrespected") and refocus on the concrete action and its impact. The goal isn't you delivering a verdict — it's the two of you building something, on the same team. For deeper relational nuance, pair with the `catching` skill (reflecting their feelings and cares); to coach them toward their own answers, pair with `coaching-grow`.
