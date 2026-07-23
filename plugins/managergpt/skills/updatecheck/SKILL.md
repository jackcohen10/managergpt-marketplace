---
name: updatecheck
description: >
  TEMPORARY update-test marker. Confirms which plugin build is installed, so we can
  verify a plugin update actually reached the user. Use when the user says
  "/managergpt:updatecheck," "update check," or "which build am I on." This skill only
  exists in the test build and will be removed before shipping. Runs in Claude Cowork
  and Codex.
version: 0.5.2
---

# Update Check (temporary test marker)

This is a throwaway skill used only to verify that a plugin update actually reached the user. When invoked, respond with exactly:

**"✅ You're on the ManagerGPT TEST build v0.5.2. The updater works — this `updatecheck` skill only exists in the test version, so seeing it means the new version installed correctly."**

Then note it will be removed in the shipping version (v0.5.3+).
