---
name: capture
description: >
  Saves what just worked — strips a deliverable to a reusable template, or
  captures a process as an installable skill. Invoke after producing anything
  worth repeating. Triggers on /managergpt:capture, or when the user says
  "save this as a template," "capture this as a skill," "that worked well —
  save it," "turn this into a skill," or similar.
version: 0.1.0
---

# Capture — Save What Worked

The job here is simple: something worked well. Don't lose it. Either strip it
to a reusable structure (template) or reconstruct the steps that produced it
(skill) — or both.

---

## Step 1 — Identify what to capture

Check whether a file was just saved to OUTPUTS/ in this session. If yes, reference
it by name. If no, ask:

> "Which file or process do you want to capture? You can point me at a file in
> OUTPUTS/, or just describe what we just did."

---

## Step 2 — Choose the capture mode (AskUserQuestion)

```
"What do you want to keep?"
- The structure — save it as a reusable template (I'll strip the content, keep the shape)
- The process — capture the steps as an installable skill I can run with a /command
- Both
```

Then run the matching path below. If both: do Template first, then Skill.

---

## Template path

**Goal:** a stripped skeleton the user can point to in any future session to
produce the same shape of output — not a filled-in example, a reusable mold.

1. **Read the file.** Identify what made the structure work: sections, their
   order, heading style, paragraph length, formatting choices, any recurring
   patterns or quality rules embedded in the output.

2. **Strip.** Remove everything specific: names, dates, numbers, project
   details, company names, personal references. What's left should be
   placeholders and structure only.

3. **Add a two-line header** at the top of the template:
   ```markdown
   <!-- When to use: [one line — what situation this is for] -->
   <!-- What it produces: [one line — the shape/format of the output] -->
   ```

4. **Propose a filename.** Something descriptive: `weekly-update.md`,
   `client-brief.md`, `1on1-prep.md`. Ask if that name works or if they want
   something different.

5. **Save to TEMPLATES/** with the confirmed filename.

6. **Update TEMPLATES/index.md** (create it if it doesn't exist). Each entry
   is one line:
   ```
   - [filename] — [one-line description of when to use it]
   ```
   Append — never overwrite existing entries.

7. **Show the saved template** briefly: "Here's what I kept — [preview the
   first few lines]. Does the structure look right?" Let them adjust before
   closing.

**Using a template later:** The user can say "Use the template in
TEMPLATES/[filename]" or just reference what they want ("draft a weekly update
like last time") — the Global Instructions already tell Claude to check
TEMPLATES/ before creating matching content.

---

## Skill path

**Goal:** reconstruct the method that produced the result and install it as a
callable `/command` — so next time it runs the same way, with the same quality
bar, without the user having to re-explain it.

1. **Reconstruct the steps.** Based on what happened in this session, write a
   plain-language version of the process:
   ```
   Here's how we approached this:
   1. [step]
   2. [step]
   ...
   ```
   Include any rules that shaped the output quality (things you checked,
   constraints you followed, sequencing decisions).

2. **Show it and confirm.** Present the reconstructed steps:

   > "Here's what I'd turn into a skill — is this roughly how you'd want
   > to run it again? Anything missing or off?"

   Adjust based on their response before proceeding.

3. **Name the skill and trigger.** Ask:

   > "What should I call this skill, and what phrase should trigger it?
   > (e.g., 'draft weekly update' or `/weekly-update`)"

4. **Hand off to skill-creator.** Once the steps are confirmed and named,
   invoke the skill-creator with the reconstructed steps and name as the
   brief:

   > "I'm going to hand this to skill-creator now to turn it into a proper
   > SKILL.md and install it. It may ask you a few questions to sharpen it —
   > that's the good part."

   Skill-creator handles the SKILL.md formatting, quality checklist, and
   installation to `~/.claude/skills/`.

---

## Closing

After any capture, say what was saved and where:

- Template: *"Saved to TEMPLATES/[filename]. Say 'use the template in
  TEMPLATES/[filename]' anytime you want the same structure."*
- Skill: *"Skill-creator is building it now. Once installed, trigger it with
  [trigger phrase] or `/[command]`."*

Don't recap the whole session. One sentence per thing saved.
