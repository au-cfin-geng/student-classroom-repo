# Clinical Claude

**A module-based course: using Claude for clinical AI research**

> Open in VS Code: double-click `student-lab.code-workspace`

You are a junior clinical AI investigator. Over two days, you will build, evaluate, diagnose, and improve a brain tumour segmentation model — using Claude as your research partner at every step.

This is not a programming course. Every task in this course is driven by prompts you write in VS Code + Claude Code. The research is real. The results are real. The judgment is yours.

---

## Quick start

```bash
pip install -r requirements.txt   # one-time setup
make preflight                    # confirm the environment is intact
make fetch-sample                 # download the teaching dataset
make dashboard                    # open the course dashboard
```

---

## The course in one loop

```
dashboard → write a prompt → VS Code + Claude Code → inspect artifact → dashboard
```

The dashboard shows your current module, the expected outputs, and your progress. Claude runs in VS Code. Artifacts (figures, metrics, reports) accumulate in `outputs/` and `reports/` as you work. Those artifacts are what you submit.

---

## Seven modules + one capstone

Each module teaches one Claude principle through one clinical research scenario.

| Module | Clinical scenario | Claude principle |
|--------|------------------|-----------------|
| **M0 — Project Memory** | Lab setup chaos | CLAUDE.md as project context |
| **M1 — Inspect Before You Model** | Blind modeling on unknown data | Structured inspection first |
| **M2 — Define Success First** | No baseline to compare against | Evaluation-driven prompting |
| **M3 — Evidence-Based Diagnosis** | Guessing why the model fails | Observation → evidence → hypothesis |
| **M4 — One Variable at a Time** | Untracked, undocumented changes | Controlled experiment design |
| **M5 — The Reviewer Role** | Only seeing your own work | Role switching: developer → critic |
| **M6 — Honest Translation** | Overclaiming prototype results | Multi-audience honesty constraints |
| **Capstone** | End-to-end clinical AI judgment | Your own design |

Complete them in order. See `modules/` for the design guide for each module.

---

## What you produce

The repo starts sparse. You fill it in:

```
outputs/
  figures/        MRI overlays, loss curves, error maps
  metrics/        Dice scores, comparisons
  status/         Per-module completion signals
reports/          Written analysis — what you found and what it means
```

`outputs/` and `reports/` are empty at the start. Filling them is the course.

---

## Commands

```bash
make dashboard        # open the course dashboard (primary interface)
make preflight        # structural check — no data needed
make fetch-sample     # download teaching dataset
make test             # run autograding checks
make help             # list all commands
```

---

## Why this approach

Traditional courses give you finished code to run. You observe the output and move on. The code does the thinking; you watch.

This course works differently. You direct Claude with structured prompts that specify what to do, how to do it, and what output to produce. When the prompt is vague, the result is vague. When the prompt names the exact output file, defines the required keys, and specifies the success criteria — the result is verifiable.

The habit you are building is this: **before using Claude on a research task, define what a good result would look like.** That habit is what makes AI useful in clinical research rather than dangerous.

---

For the full course design, see [COURSE_OVERVIEW.md](COURSE_OVERVIEW.md).
For assignment details and grading, see [ASSIGNMENT.md](ASSIGNMENT.md).
