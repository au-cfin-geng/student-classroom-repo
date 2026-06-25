# Course Roadmap — Clinical Claude

## Overview

The course runs over two days and is organized as seven sequential modules plus a capstone. Each module builds on the previous one. The modules cannot be reordered without breaking the scientific narrative.

---

## The research question

> Can a simple intensity-based segmentation algorithm detect brain tumours from FLAIR MRI with sufficient consistency to justify further investigation?

Students begin with this question unanswered. They end with a documented, honest answer — and a clear-eyed view of what it would take to move from their research prototype to clinical deployment.

---

## Day 1 — Foundation

**Goal:** Build a reproducible clinical AI pipeline from scratch, document every decision, and produce an evidence-grounded failure analysis.

| # | Module | Claude principle | Duration | Key output |
|---|--------|-----------------|----------|------------|
| M0 | Project Memory | CLAUDE.md + output contracts | 30 min | `reports/env_check.md` |
| M1 | Inspect Before You Model | Structured inspection | 20 min | `reports/data_notes.md` |
| M2 | Define Success First | Evaluation-driven prompting | 40 min | `outputs/metrics/val_metrics.json` |
| M3 | Evidence-Based Diagnosis | Observation → evidence → hypothesis | 40 min | `reports/error_analysis.md` |
| M4 | One Variable at a Time | Controlled experiment design | 30 min | `reports/model_swap.md` |
| — | Day 1 checkpoint | Commit + push | 10 min | `reports/day1_summary.md` |

**Day 1 milestone:** A documented baseline + one controlled improvement + a failure hypothesis grounded in visual evidence.

---

## Day 2 — Extension

**Goal:** Step back from execution and apply the two hardest Claude skills — reviewing your own work critically, and translating results honestly for a clinical audience.

| # | Module | Claude principle | Duration | Key output |
|---|--------|-----------------|----------|------------|
| M5 | The Reviewer Role | Role switching | 50 min | `reports/challenge_plan.md` |
| M6 | Honest Translation | Multi-audience honesty constraints | 40 min | `reports/translation_memo.md` |
| C | Capstone | Integration | 60 min | Student-designed artifact set |
| — | Showcase | 5-min presentation | 30 min | Oral + figure |

**Day 2 milestone:** A clinical translation memo that honestly names what the prototype is and is not — plus an independent investigation that demonstrates all seven Claude principles.

---

## Skill progression

The seven Claude principles are introduced in dependency order:

```
M0: Output contracts          ← you can't improve what you can't measure
M1: Structured inspection     ← you can't analyze what you haven't seen
M2: Evaluation-first          ← you can't compare without a baseline
M3: Evidence → hypothesis     ← you can't fix what you haven't diagnosed
M4: One variable              ← you can't attribute an improvement you can't isolate
M5: Role switching            ← you can't review what you only see as a developer
M6: Honesty constraints       ← you can't translate what you can't honestly assess
```

Each module is a prerequisite for the next. Module N's output is the raw material for module N+1.

---

## What grows in the repo

The repo starts sparse. This is what it looks like at each milestone:

**After M0:**
```
reports/env_check.md
outputs/status/stage_00_bootstrap.json
```

**After M2:**
```
+ reports/data_notes.md
+ reports/train_notes.md
+ outputs/figures/sample_overlay.png
+ outputs/figures/loss_curve.png
+ outputs/metrics/val_metrics.json
```

**After M4 (Day 1 checkpoint):**
```
+ reports/error_analysis.md
+ outputs/figures/error_analysis_best.png
+ outputs/figures/error_analysis_worst.png
+ reports/model_swap.md
+ outputs/metrics/model_swap_comparison.json
+ reports/day1_summary.md
```

**After M6 (Day 2 complete):**
```
+ reports/challenge_plan.md
+ reports/adapt_pipeline.md
+ outputs/metrics/challenge_comparison.json
+ reports/translation_memo.md
```

**After Capstone:**
```
+ Student-designed artifacts (varies)
+ Showcase figure
```

---

## Assessment milestones

| Milestone | When | What is checked |
|-----------|------|----------------|
| Day 1 checkpoint commit | End of Day 1 | Automated: all Day 1 artifacts present + valid |
| Day 2 checkpoint commit | Before showcase | Automated: all Day 2 artifacts present + valid |
| Showcase | End of Day 2 | Instructor: oral presentation of error analysis + translation memo |
| Final submission | Deadline push | Automated + manual review of reports/ |

Grade distribution: see `ASSIGNMENT.md`.

---

## For self-paced students

If running this course without a classroom, the two-day structure still applies:

- **Day 1** = work through M0–M4 in one session (3–4 hours total)
- **Day 2** = return after at least one night's rest — M5 requires stepping back from your own work
- **Capstone** = open-ended investigation on your own research question

The mandatory rest between Day 1 and Day 2 is not arbitrary. M5's role-switching exercise works better when you have some distance from your own Day 1 results.
