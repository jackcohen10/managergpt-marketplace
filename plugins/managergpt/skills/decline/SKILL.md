---
name: decline
description: >
  Drafts a meeting decline / "no" in the user's own voice — the ManagerGPT way to
  protect Deep Work and time without burning the relationship. Use when the user says
  "/decline," "decline this," "help me say no," "turn down this meeting," "draft a no,"
  "I can't make this," or forwards an invite they want to decline. Reads their saved
  decline voice and preference from working-style.md, writes a generous decline that
  offers async support or a redirect, and shows it for the user to send — never sends
  it automatically. Runs in Claude Cowork and Codex.
version: 0.1.0
---

# Decline

Saying no well is an Author move. Most over-full calendars come from reflexively accepting every invite (a classic Re-Actor behavior); a good decline protects the time that matters **without** making the other person feel dismissed. The ManagerGPT decline is generous: it declines the *meeting* while offering a path forward — async help, a redirect, or a smaller ask.

This skill **drafts** the decline. It never sends it — the user always sends it themselves after reading it.

---

## Platform notes (Cowork vs. Codex)

- **Standing instructions / voice:** Cowork reads the **Global Instructions** field plus the selected **Project**; Codex reads **AGENTS.md**. The decline voice and preference live in `working-style.md` either way.
- Both surfaces: draft in chat, the user copies and sends. If a mail/calendar tool is connected, you may *prepare* a reply for them to review — but **never send or auto-respond.**

---

## Before you draft

1. **Read `working-style.md` → "Protecting time & declining"** (Outer Game). You need:
   - **Decline preference** — *verbatim* (reuse their saved script as-is), *match-my-voice* (keep their tone, write a fresh version), or *ask me each time*.
   - **Their decline voice** — the scripts they chose on Day 1, kept as a tone reference.
   - **When to use** — the bar for what they protect (e.g., Deep Work blocks; anything that doesn't serve a weekly priority).
   If the file or block doesn't exist, ask once for a sentence or two in their voice, draft from that, and offer to save it for next time.
2. **Get the specifics** (ask only what you don't already have): who's asking, what the meeting is, when, and whether it collides with Deep Work or a priority. If they pasted the invite or message, read it.

---

## How to draft

Match the **preference**:
- **Verbatim** → use the saved script, lightly fitted to this invite.
- **Match-my-voice** → write a **fresh 1–2 sentence** decline in their tone. **Don't reuse the same wording every time** — the same colleagues see these, and a canned line reads as a form letter.
- **Ask each time** → offer a draft and a quick "want it warmer / shorter / firmer?"

A good decline usually does three things, in their voice:
1. **Appreciate** the ask briefly — no long apology.
2. **Decline clearly** — name a conflict or commitment without over-explaining or inventing excuses.
3. **Offer a path forward** — async support, a redirect to someone/something, or "send me a specific ask and I'll see what I can do." This is what keeps it generous rather than a flat no.

Keep it short. Mirror their formality. Don't pad with "so sorry" three times — one light acknowledgment is enough.

**Then show the draft for them to send.** Offer one round of adjustment (warmer, shorter, firmer, more/less async help). **Never send it, auto-reply, or decline the calendar event on their behalf** — drafting only; the user sends.

If declining surfaces real guilt or fear of how they'll be seen (a Re-Actor voice like "I can't say no or I'll be judged"), name it lightly and offer a quick `inner-dialogue` rather than just polishing the wording.

---

## Hard rules

- **Draft only — never send.** No auto-replies, no declining the calendar invite for them. Always show the text and let the user send it.
- **Don't invent commitments.** Decline honestly; if there's no real conflict, help them decide consciously rather than fabricate one.
- **Use their voice, not a generic one.** Pull from `working-style.md`; vary the wording on match-my-voice so it never sounds canned.
