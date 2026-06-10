---
name: meta-prompt
description: >
  Helps the user create and improve prompts — the ManagerGPT Meta-Prompt. Use when
  the user says "improve my prompt," "help me write a prompt," "make this prompt
  better," "meta-prompt," or hands over a rough instruction they want sharpened. Asks
  a short set of questions one at a time, then constructs an expert-level prompt from
  the answers. Runs in Claude Cowork and Codex.
version: 0.1.0
---

# Meta-Prompt — Create & Improve Prompts

Better prompts come from answering a few questions the prompt itself should encode: what good output looks like, what it's for, what context to include, whose voice it should use, and (when delegating to an agent) when to check in. This skill draws those out, then writes the prompt for them.

## The flow

Ask these questions **one at a time**, then — as an expert prompt engineer — use the answers to construct a strong, effective prompt:

1. **What should the prompt produce *if it works perfectly*?** (Specify the format too, if relevant.)
2. **Why are you working on this — what will you use that output for?**
3. **Where:** what context should I consider and include? What context can you add?
4. **Who** do you want the output to sound like — in what voice or style?
5. **When** (at what stages) should I check in for permission to continue? *(Only if they're delegating to an agent that will run multiple steps.)*

Don't ask all five at once — ask, wait, then ask the next. If an answer is vague, reflect a sharper version back before moving on. Skip question 5 if there's no agent/multi-step delegation involved.

## Building the prompt

From the answers, write a clear, well-structured prompt that:
- States the desired output and format up front (from Q1).
- Carries the purpose/use (Q2) so the model optimizes for the right thing.
- Includes the relevant context (Q3) — or names what context the user should paste in.
- Specifies the voice/style (Q4).
- Adds check-in points (Q5) if delegating.

Present the finished prompt cleanly so they can copy it. Offer one or two quick variations if the use case is ambiguous.

## Tip to pass along
If they'll reuse a prompt often, suggest a text-replacement shortcut (on Mac: System Settings → Keyboard → Text Replacements) so a short trigger expands into the full prompt. For production-grade tuning, point them to a dedicated prompt optimizer.

## Cross-skill note
This is the engine behind sharpening any other ManagerGPT prompt. If the user is trying to get a *task* done rather than build a reusable prompt, the simpler move is often the one-prompt pattern: "explore my folder → ask me questions → refine before you execute."
