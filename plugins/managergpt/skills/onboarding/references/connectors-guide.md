# Connectors Guide

How to connect the tools the OS reads from. Read before the **Connect tools** step in Hire.

---

## What connectors do

Connectors link Claude to external platforms (Google Drive, Gmail, Calendar, Slack, task tools, etc.) so it can read the user's real material — no copy-paste. Connect *before* building context files so the Intake interview becomes confirmation rather than blank-slate typing, and so the calendar audit and task-management discovery have data to work with. Use `search_mcp_registry` to find a connector and `suggest_connectors` to present a connect button.

## Tool → search keywords

| Tool | Keywords |
|---|---|
| Google Drive | `["google","drive","docs"]` |
| Gmail | `["google","gmail","email"]` |
| Google Calendar | `["google","calendar","schedule"]` |
| Slack | `["slack","messaging","chat"]` |
| Notion | `["notion","wiki","docs"]` |
| Asana | `["asana","tasks","project"]` |
| Linear | `["linear","issues","project"]` |
| Todoist | `["todoist","tasks"]` |
| Airtable | `["airtable","database","tables"]` |
| Microsoft Teams | `["teams","microsoft","chat"]` |
| Outlook | `["outlook","microsoft","email","calendar"]` |

## Priority order for the OS

1. **Calendar** — powers the calendar audit and the Weekly Preview's Deep Work blocking.
2. **The task tool** — required for the planning rituals (see `task-management-guide.md`).
3. **Drive / Docs** — lets Intake pull from the Day-1 doc and existing material.
4. **Gmail / Slack** — lets Plan My Day surface "Next Actions from incoming messages," and lets Gossip learn from real threads.

Don't push everything at once — connect what matters for the rituals, add more later.

## Verify each connection

After connecting, run a quick read to confirm: Calendar → "What's on my calendar this week?"; Drive → "Find my most recently edited doc"; the task tool → "List my active projects." If a tool has no connector, be honest and suggest a bridge (e.g., sync Calendly into Google Calendar).

## Privacy note

Most connectors are read-first; the user can disconnect anytime in Settings → Connectors. If they hesitate, reassure them and connect only what the rituals need.
