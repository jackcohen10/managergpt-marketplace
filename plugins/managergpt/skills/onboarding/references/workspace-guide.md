# Workspace Guide

How to set up the folder structure where the Operating System lives. Read before the **Build the workspace** step in Hire.

---

## Why structure matters

The OS has real read/write access to whatever folder the user selects. A clean structure means Claude reads the right context before every task, outputs land somewhere predictable, and any mistakes stay contained to one folder. The user points the OS at this folder (their OS **Project**) at the start of each session.

## The architecture

```
[OS folder]/
├── CONTEXT/                  ← Who they are + how they work
│   ├── about-me.md
│   ├── working-style.md      (Outer Game / Inner Game / Both)
│   ├── org-and-team-context.md
│   └── brand-voice.md        (only if external-facing)
├── PROJECTS/                 ← Active work, one subfolder per project; tasks.md/xlsx if used
├── TEMPLATES/                ← Proven structures to reuse as patterns
├── OUTPUTS/                  ← Where Claude delivers finished work
└── weekly-reviews/           ← Reflection + weekly-plan records (the OS's memory across weeks)
```

Create `CONTEXT/`, `PROJECTS/`, `TEMPLATES/`, `OUTPUTS/` with `mkdir -p`; leave PROJECTS and TEMPLATES empty (the user fills them). `weekly-reviews/` is created by the Weekly Preview skill on first run, but you can create it now.

## Permission models — default to read/write-with-confirmation

AskUserQuestion:
```
"How should I handle your workspace folders?"
- Read/write with confirmation (Recommended) — I can update any folder but I show you
  the change and ask before saving. OUTPUTS is always writable.
- Read-only source folders — I read CONTEXT/PROJECTS/TEMPLATES but never modify them;
  only OUTPUTS is writable. Most cautious.
- Full read/write — I update files freely, no confirmation. For power users.
```

| Model | CONTEXT / PROJECTS / TEMPLATES | OUTPUTS |
|---|---|---|
| Read/write w/ confirmation (default) | read + write with confirm | read/write |
| Read-only source folders | read only | read/write |
| Full read/write | read/write | read/write |

Store the choice — it sets the **Folder Protocol** variant in Global Instructions (see `global-instructions-guide.md`).

**Regardless of model:** the hard delete rules always apply — never delete a file without explicit in-conversation permission, and scheduled/automated runs never delete (they move items to `pending-deletion/`).

## Naming convention

Files Claude creates follow `project_content-type_v1.ext` (e.g., `client-x_proposal_v1.docx`). Increment the version if a name already exists. Deliverables default to `OUTPUTS/`, organized in a subfolder per project mirroring `PROJECTS/`.

## If a workspace already exists

Acknowledge what's there; don't start over. Offer to organize loose context files into `CONTEXT/`, or adapt the Folder Protocol to their actual layout. Save outputs to `OUTPUTS/` either way.

## Quickstart variant

Just `CONTEXT/` and `OUTPUTS/`. Add the rest later — the structure scales.
