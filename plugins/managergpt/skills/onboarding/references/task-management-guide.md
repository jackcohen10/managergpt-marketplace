# Task Management Guide

How to connect and configure the user's task source during **Hire**, and how to write the **Task management block** that the planning skills (Weekly Preview, Plan My Day) read. This block is what makes those rituals write to the user's *real* system instead of an invented one.

---

## The first question

*"Where do your tasks and to-dos live today?"* — Asana / Linear / Notion / Todoist / Airtable / Another tool / A spreadsheet or doc / I have something but don't love it and am interested in changing it / Nothing consistent — it's in my head.

It's more than a 4-button form holds, so present it as a short list they click the closest match to or dictate. Capture "Another tool" as free text.

- **A real tool they're happy with** → connect, then configure (below).
- **A spreadsheet/doc, "don't love it," or nothing** → the fallback (below).

---

## Configure a connected tool: discover, then interview

Before asking anything, run a **discovery query** so you're interviewing against their real structure, not a blank slate:

| Tool | Discover |
|---|---|
| Asana | workspaces, projects, sections, custom fields |
| Linear | teams, projects, workflow states, labels |
| Notion | have them point you at the tasks database, then read its properties/select options |
| Todoist | projects, sections, labels, priorities |
| Airtable | bases, tables, fields (ask which base/table holds tasks) |

Then interview on conventions: which project/list holds their active work, which field carries status/priority, how they mark something as waiting on someone else, where "this week's priorities" would live. Keep it to a few questions.

---

## The canonical priority labels

Map their real statuses to these (the skills read the labels, not the tool's native names):

- **Today** — committed for today
- **Later** — committed, but after today
- **Someday/Maybe** — an idea, no commitment yet
- **Waiting For** — blocked on someone else (note who)
- **Done** — completed

Users can customize the label names — record whatever they actually use, and note the mapping.

---

## The Task management block (write this into working-style.md → Outer Game)

```markdown
### Task management
- Source: [Asana / Linear / Notion / Todoist / Airtable / Flow State / PROJECTS/tasks.xlsx / PROJECTS/tasks.md]
- Where active work lives: [workspace/project/list/base+table]
- Priority labels (their term → canonical):
  - [their "Now"] → Today
  - [their "Next"] → Later
  - [their "Backlog"] → Someday/Maybe
  - [their "Blocked"] → Waiting For
  - [their "Done"] → Done
- This Week's Priorities live in: [where]
- How actions link to a weekly priority: [field / sub-tasks / grouping — or "not feasible in this tool"]
- Notes: [anything a skill should know before writing here]
```

The planning skills read this block to know where to write, how to tag, and how (or whether) to link a Next Action to a weekly priority.

---

## Fallback: no tool, a loose spreadsheet/doc, or "don't love it"

Offer two paths:

1. **Flow State** (the ManagerGPT task app) — the most integrated option; if they're open to a new tool, point them there.
2. **A task file** mirroring the Next Actions template. If they choose this, **ask the format:**
   - **`tasks.xlsx`** — closest to the Next Actions spreadsheet; sortable and filterable.
   - **`tasks.md`** — lighter, plain text, easy to read in the repo.

Either format uses the same structure: columns **By When, Action, Priority, Project, Notes, Time**; a **This Week's Priorities (1 / 2 / 3-stretch)** block; and the **Daily Defining + Weekly Preview checklists embedded at the bottom**. Create it in `PROJECTS/` and record the location + format in the Task management block.

### tasks.md skeleton
```markdown
# Tasks

## This Week's Priorities
1.
2.
3. (stretch)

## Next Actions
| By When | Action | Priority | Project | Notes | Time |
|---|---|---|---|---|---|
|  |  | Today |  |  |  |

---
## Weekly Preview checklist
- Prioritize: 2–3 outcomes I'd be proud of by Friday
- Block Deep Work + meetings for them
- Delegate via Clean Handoffs (5 W's)
- Clean up the system

## Daily Defining checklist
- Availability: calendar minus buffer
- Define: precise Next Actions tied to this week's priorities
- First: the very first action (what/who am I avoiding?)
```

For `tasks.xlsx`, build the same columns and blocks as sheets/sections (use the xlsx skill).

---

## Daily buffer

Captured in Hire, stored in the Outer Game of `working-style.md`: how much time to leave each day for fires and unplanned opportunities. If the calendar audit produced an estimate, offer it as the starting point. Plan My Day reads this to compute real available time.

---

## Monthly re-check

The monthly context check-in re-runs the discovery query so the block stays accurate when the user's tool, projects, or conventions drift.
