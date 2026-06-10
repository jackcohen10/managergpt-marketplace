# ManagerGPT Marketplace

A one-plugin marketplace for the **ManagerGPT** cohort course. It installs a single plugin — `managergpt` — that turns Claude into a personalized **Operating System** for leaders and managers making the shift from **Re-Actor to Author**.

## What's inside

One plugin, `managergpt`, containing:

- **`onboarding`** — the front door. Personalizes the OS the way you'd onboard a new colleague: Hire → Onboard → Intake → Gossip, then a Test Drive and automatic setup of your rituals.
- **`weekly-preview`** — the core weekly planning ritual (close out the week, choose defined outcomes, block Deep Work, delegate).
- **`plan-my-day`** — Daily Defining: what today is really for, after your buffer.
- **`clean-handoffs`** — delegate cleanly with the 5 W's.
- **`leverage-quadrant`** — what's your Genius work vs. what to delegate.
- **`inner-dialogue`** — Move through a difficult emotion to the yearning underneath.
- **`catching`** — reflect feelings and the cares at the core.
- **`feedback-gain`** — prepare, refine, or practice feedback with GAIN.
- **`coaching-grow`** — empowering questions + the GROW model.
- **`meta-prompt`** — create and improve prompts.
- **`tiny-habit`** — make a new behavior stick (BJ Fogg).
- **`protect`** — an optional security review of your setup.

Each is invocable as `/managergpt:<skill>` (e.g. `/managergpt:onboarding`, `/managergpt:weekly-preview`, `/managergpt:protect`) — or just by asking.

## Install (for the cohort)

In Claude Cowork (desktop app) or Claude Code:

```
/plugin marketplace add jackcohen10/managergpt-marketplace
/plugin install managergpt@managergpt-marketplace
```

Then run `/managergpt:onboarding` to set up your Operating System.

> Hosted at `github.com/jackcohen10/managergpt-marketplace`. The marketplace name (`managergpt-marketplace`) comes from `.claude-plugin/marketplace.json` and can be renamed there.

## Repo structure

```
managergpt-marketplace/
├── .claude-plugin/
│   └── marketplace.json
└── plugins/
    └── managergpt/
        ├── .claude-plugin/
        │   └── plugin.json
        └── skills/
            ├── onboarding/        (SKILL.md + references/)
            ├── weekly-preview/
            ├── plan-my-day/
            ├── clean-handoffs/
            ├── leverage-quadrant/
            ├── inner-dialogue/
            ├── catching/
            ├── feedback-gain/
            ├── coaching-grow/
            ├── meta-prompt/
            ├── tiny-habit/
            └── protect/
```

## Validate before publishing

```
claude plugin validate .
```

Built for the ManagerGPT Maven cohort. © Jack Cohen, Brain Based Workplace.
