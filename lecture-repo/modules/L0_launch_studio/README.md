# L0 — Launch Studio

**Concept:** Project memory + output contracts  
**Time:** 30 min · Day 1  
**Prompt file:** `prompts/stage_00_bootstrap.md`

---

## Why this lab exists

The first question in any computational research project is: is the environment actually ready? This sounds like a setup task, not a research task — but environment failures are among the most common sources of irreproducible results. A script that runs on your machine may fail on another due to a different Python version, a missing package, or a missing directory.

This lab teaches two Claude principles that address this:

**Project memory** (CLAUDE.md): Claude reads this file on every session start. It gives Claude persistent knowledge about the project — naming conventions, output paths, which files to never touch, what the research goal is. Without it, Claude re-learns the same context each session, producing inconsistent behaviour.

**Output contracts**: A prompt that specifies exactly where output goes and what keys it must contain is auditable. Either `outputs/status/lab_00_launch_studio.json` exists with `status: ok`, or the step did not complete. You do not need to read Claude's chat response to know whether the step worked — you check the file.

---

## The clinical problem this addresses

Clinical AI research fails before it begins when the computational environment is untested. A broken dependency silently corrupts outputs. Missing output directories cause scripts to error in obscure ways hours into a run. An explicit environment audit — as a prompt-driven, artifact-producing step — converts setup from a hope into a verified condition.

---

## Before / After

**Before this principle:**
```
Hey Claude, can you check if my environment is ready?
```

Claude gives a conversational response. Maybe it checks some things, maybe not. The response is not checkable. The next person who runs the pipeline doesn't know what was verified.

**After this principle:**
```
You are a clinical research environment auditor. Read CLAUDE.md first.

Check: Python version >= 3.9, required packages (numpy, nibabel, matplotlib, torch),
output directory structure (outputs/status/, outputs/figures/, outputs/metrics/, reports/).

Write your findings to outputs/status/lab_00_launch_studio.json with keys:
  status: 'ok' or 'fail'
  python_version: str
  missing_packages: list[str]
  directory_checks: dict
  notes: str

Write a plain-language summary to reports/lab_00_launch_studio.md.
```

The second prompt produces an artifact. The artifact is checkable by automated tests, by a collaborator, and by the student themselves. The work is documented and reproducible.

---

## Clinical scenario

You have joined a clinical AI lab. A PhD student left the repo six months ago. Your supervisor asks you to confirm the computational environment is ready for the next phase of the brain imaging study.

There is no documentation. You don't know what packages were installed, what Python version was used, or whether the output directories are set up correctly.

Where do you start?

---

## Assignment

1. Open Claude Code in VS Code with this repo open.
2. Read `prompts/stage_00_bootstrap.md`.
3. Paste the prompt into Claude Code chat.
4. Claude reads CLAUDE.md, checks the environment, creates any missing directories, and writes the artifacts.
5. Verify: does `outputs/status/lab_00_launch_studio.json` exist? Open it. Does `status` say `ok`?
6. Answer the reflection questions in `reports/lab_00_launch_studio.md`.

---

## Required artifacts

| Path | Required key |
|------|-------------|
| `outputs/status/lab_00_launch_studio.json` | `status: "ok"` |
| `reports/lab_00_launch_studio.md` | Plain text report |

---

## Reflection questions

1. What would have happened if the prompt didn't specify the output file path?
2. Which part of CLAUDE.md was most useful to Claude? What was missing from it?
3. What still required your own judgment after Claude's audit?

---

## Transfer to your own research

Every new computational project benefits from a setup audit prompt. The CLAUDE.md pattern is especially useful for projects that span multiple sessions or multiple contributors. The output contract pattern applies to any step where you need to verify completion independently of the chat.

---

## Success criteria

- `outputs/status/lab_00_launch_studio.json` exists with `status: ok`
- `reports/lab_00_launch_studio.md` exists and is non-empty
- You can answer all three reflection questions with specific reference to what Claude produced
- You understand the difference between a conversational response and an artifact-producing step
