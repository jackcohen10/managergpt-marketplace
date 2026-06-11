# Skills Guide

What the companion skills are. Read before the **Onboard** phase.

---

## The companion skill set (ships with the plugin — nothing to install)

The entire Operating System is one plugin (`managergpt`), so all of these came with it the moment the user installed ManagerGPT — there's no separate install step. The point of the Onboard phase is just to **confirm they're active and name what the user has**, so the standing instructions can reference them. Each is callable as `/managergpt:<skill>` or just by asking.

| Skill | What it does |
|---|---|
| **Weekly Preview** | The core weekly ritual — close out the week, choose 2–3 defined outcomes, block Deep Work, delegate via Clean Handoffs. |
| **Plan My Day** | The daily ritual (Daily Defining) — availability after buffer, precise Next Actions tied to the week, decide the first move. |
| **Clean Handoffs** | Delegation via the 5 W's (Who / What / By When / Where / Why). |
| **Leverage Quadrant** | Genius vs. delegate prioritization (Impact vs. Ease/Ability). |
| **Inner Dialogue** | Move through a difficult emotion to the yearning underneath. |
| **Catching** | Rehearse / prep / debrief empathic listening — feelings + Cares at the core (you do it live). |
| **GAIN Feedback** | Prepares/refines feedback with the GAIN framework. |
| **GROW Coaching** | Rehearse / prep / debrief coaching — empowering questions + GROW (you do it live). |
| **Meta-Prompt** | Creates and improves prompts. |
| **Tiny Habit** | BJ Fogg after / I-will / celebrate habit design. |

These are the skills that embody the ManagerGPT frameworks. The planning and interpersonal ones read `working-style.md` and check the Familiar flag.

## How skills work

A skill is a set of instructions Claude follows when triggered (by a phrase or a `/command`). Tell the user they can type `/` in any Cowork chat to see the commands their installed skills add. Skills produce more structured, higher-quality output than a generic prompt because they encode the method.

## Cross-surface install (important)

Skills **don't auto-sync across surfaces.** A desktop install isn't a browser install isn't a Codex install — same files, different install paths (`~/.claude/skills` for Cowork, `~/.agents/skills` for Codex). **Standardize the cohort on Cowork in the desktop app.** Browser is a separate optional install via claude.ai → Customize → Skills. Mobile is **Dispatch** (remote control of the desktop) — nothing installs on the phone; the desktop is the brain and must be on.

## Discovering more

Beyond the bundle, use `search_plugins` / `suggest_plugin_install` for role-specific needs, and the document skills (docx, pptx, xlsx, pdf) which are useful for almost everyone. Don't overwhelm — recommend a couple that match what they described.
