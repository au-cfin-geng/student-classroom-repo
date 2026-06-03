# Medical AI + Agentic Coding Lab

**PhD Course: Medical AI + Agentic Coding for Clinical Research**

> **Open in VS Code:** double-click `student-lab.code-workspace` — this gives you the intended student-facing view. Do not open the raw folder directly.

This is a **prompt-first clinical AI research lab**. You are a junior clinical AI investigator using VS Code + Claude Code as your research environment. Every mission teaches one clinical AI concept and one Claude / agentic research concept. Your work product is a growing set of artifacts in `outputs/` and `reports/`.

You do not need traditional programming fluency. You work by writing structured prompts in **VS Code + Claude Code**, guided by a local dashboard.

---

## Start here

```bash
pip install -r requirements.txt   # install dependencies (one-time)
make preflight                    # confirm environment is intact
make fetch-sample                 # download the teaching data
make dashboard                    # open the mission dashboard
```

---

## The loop

Every mission follows the same rhythm:

> **dashboard → prompt → VS Code + Claude Code → artifact → dashboard**

1. Open the dashboard (`make dashboard`) and read the current mission.
2. Copy the prompt shown in the dashboard into your Claude Code session.
3. Let Claude run the task — it reads the repo, writes or extends scripts, produces artifacts.
4. Return to the dashboard and inspect the new outputs.
5. When the mission checklist shows complete, create a checkpoint commit and push.

The dashboard is your **navigation and feedback console**. All Claude interaction happens in VS Code + Claude Code — not in the dashboard.

---

## Why not just give you finished code?

Traditional teaching gives you finished code to run. You execute it, observe the output, and move on. The code does the thinking; you observe.

This lab works differently. You use Claude to **inspect, build, verify, and explain**. The learning IS the prompting. When you write a prompt that specifies an output contract, asks Claude to state its plan before acting, and then verify the result against real metrics — you are practicing the judgment that separates a researcher from a script runner.

The scaffold (stages, tests, Makefile, grading artifacts) exists for **grading stability and classroom timing**, not to replace the scientific experience. The tests make sure required artifacts exist and are structurally valid. They cannot verify that you understood what you built. That is what the reports are for, and that is what the instructor reads.

The scientific experience — understanding the data, forming a hypothesis about failure, designing a controlled improvement, translating honestly to clinical language — belongs to you.

---

## What you generate

This repo starts intentionally sparse. You and Claude gradually fill it in:

```
prompts/          read these to guide each mission
outputs/
  figures/        PNG figures — overlays, loss curves, error maps
  metrics/        JSON metric files — dice scores, comparisons
  status/         per-stage completion checks
reports/          written mission summaries
```

`outputs/` and `reports/` are empty at the start. Filling them is the lab.

---

## Missions

| Mission | Goal | Key output | Claude / agentic method |
|---|---|---|---|
| 0 — Wake the Lab | Environment setup | `reports/env_check.md` | CLAUDE.md as project memory + output contract |
| 1 — Receive the Signal | Fetch and inspect the dataset | `data/sample/` + `reports/data_notes.md` | Claude as data steward + file inspection |
| 2 — Build the First Detector | Baseline model + first metric | `outputs/metrics/val_metrics.json` | Claude as builder + evaluation-driven prompting |
| 3 — Investigate Failure | Error analysis + hypothesis | `reports/error_analysis.md` | Claude as visual debugger + hypothesis generator |
| 4 — Improve With Intent | One controlled improvement | `outputs/metrics/model_swap_comparison.json` | Claude as algorithm engineer + controlled comparison |
| 5 — Design the Next Study | Day 2 challenge plan + adaptation | `reports/challenge_plan.md` | Role switching to reviewer / study design critic |
| 6 — Translate Responsibly | Clinical translation memo | `reports/translation_memo.md` | Claude as clinical translator + honesty constraint |

Complete them in order. The dashboard unlocks the next mission when the current one passes.

---

## Agentic research skills you will practice

- Reading a repository with Claude Code to understand what exists before acting
- Using CLAUDE.md as project memory that persists across sessions
- Writing prompts with explicit output contracts (file path, format, required keys)
- Asking Claude to inspect before acting — state the plan, get approval, then execute
- Switching Claude's role between developer, reviewer, and clinical translator across missions
- Preserving required grading artifacts while exploring optional extensions
- Maintaining human scientific judgment throughout — Claude helps, you decide

---

## Commands

```bash
make dashboard        # open the mission dashboard (primary interface)
make preflight        # structural check — run first, no data required
make fetch-sample     # download the teaching dataset
make test             # run autograding checks (same as CI)
make help             # list all available commands
```

---

See [ASSIGNMENT.md](ASSIGNMENT.md) for full artifact requirements and grading criteria.

*This repo contains support scaffold for teaching infrastructure and autograding. It is hidden from the workspace view by default and does not affect student work.*
