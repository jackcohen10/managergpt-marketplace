# Familiar Guide

How to offer and set up Familiar. **Offer this last** — after the Test Drive — and **only on Mac.** Skip entirely for Windows users.

---

## What Familiar is

Familiar (looksfamiliar.org) is a local screen-watching app for Mac. It quietly observes what's on screen so the OS can ground its rituals in what the user *actually* did, not just what they remember to report. Privacy is the headline:

- **Local only** — OCR runs on-device via Apple; nothing leaves the computer.
- **Auto-redacts secrets** — passwords, keys, and similar are stripped.
- **48-hour deletion** — screenshots are deleted after 48 hours.

## Why it's offered last

It's an upgrade, not a prerequisite. Onboarding should deliver a working OS first; Familiar is the thing that makes the next Weekly Preview noticeably sharper. Offering it at the end means the user has already seen the value and can opt in with context — and the OS gets adjusted in one clean step if they do.

## How to offer it

Frame the value, then the privacy, then ask:

> "One optional upgrade: Familiar. It watches your screen locally so your OS can ground its weekly and daily planning in what you actually worked on — instead of relying on memory. Everything stays on your Mac: OCR runs on-device, it auto-redacts secrets, and screenshots delete after 48 hours. Want to set it up? It'll make your next Weekly Preview a lot sharper."

## If they install it

1. Walk them through download, install, and authorization (granting screen access).
2. **Adjust the OS:** write the flag to `working-style.md` (Outer Game):
   ```
   Familiar: installed and authorized for use by skills.
   ```
3. Tell them what changes: the **Weekly Preview, Plan My Day, Catching, and Coaching** skills check this flag and call `/familiar` to pull real recent activity before interviewing — so their reflections and proposals come grounded in reality.

## If they decline (or are on Windows)

No flag, no change. The skills simply skip the `/familiar` step and rely on the calendar, task source, and what the user tells them. Never nag — it can be offered again later via a re-run of onboarding.
