# Clinical Claude — Advisor Preview

**Version:** v1 prototype  
**Date:** June 2026  
**Prepared by:** Geng

---

## What this is

**Clinical Claude** is a module-based graduate course teaching researchers how to use Claude for clinical AI research. It is not a programming course and not a generic AI tools workshop. It is a structured curriculum organized around realistic clinical research bottlenecks, where each module teaches one Claude best practice by solving a problem that real medical AI researchers face.

The clinical scenario throughout the course: brain tumour segmentation from FLAIR MRI, using the BraTS 2016/2017 dataset. The algorithm: a simple intensity-threshold model. The metric: Dice coefficient. The course is not about building a good model. It is about learning to research responsibly using AI assistance.

---

## Why the redesign matters

The previous version of this lab was structured as a "segmentation pipeline lab" — students ran stages, produced outputs, and were graded on artifact presence. The pedagogical intent was present but implicit: students could complete the lab without understanding why prompts were structured the way they were, or why one approach to Claude was better than another.

The redesigned version makes the pedagogy explicit. Every module now answers four questions for the student:

1. What clinical research bottleneck does this address?
2. What Claude capability helps with it?
3. What does good use of that capability look like (before/after prompt examples)?
4. How does this transfer to my own PhD research?

This turns a lab into a course.

---

## What students learn

The course teaches Claude use across seven principles, each grounded in a clinical scenario:

| Module | Clinical bottleneck | Claude principle |
|--------|---------------------|-----------------|
| M0 | Setup chaos, unclear readiness | Project memory + output contracts |
| M1 | Blind modeling on unknown data | Structured inspection before action |
| M2 | No baseline to compare against | Evaluation-driven prompting |
| M3 | Debugging by intuition, not evidence | Observation → evidence → hypothesis |
| M4 | Undocumented, uncontrolled changes | Controlled experiment design |
| M5 | Developer-only perspective on own work | Role switching: developer → reviewer |
| M6 | Overclaiming prototype results | Multi-audience honesty constraints |

The capstone requires students to design and run an independent investigation applying all seven principles, ending with a 5-minute showcase to a non-ML audience.

---

## How GitHub monitoring works

Instructors observe student progress through the GitHub repository:

- **Commit history** shows module-level progress (students are required to commit after each module)
- **GitHub Actions** run `pytest` automatically on every push, checking artifact presence and schema validity — results are visible in the Actions tab
- **`reports/`** contains the written analysis files the instructor reviews manually
- **`outputs/metrics/`** contains JSON metric files with Dice scores and comparison results

No separate submission system is needed. The pushed repository is the submission.

---

## What is implemented now

| Component | Status |
|-----------|--------|
| Student lab repo (this repo) | Complete — all 7 modules, 10 prompt files, scripts, tests |
| Module design guides (M0–M6 + Capstone) | Complete — `modules/*/guide.md` |
| Capstone rubric | Complete — `modules/capstone/CAPSTONE_RUBRIC.md` |
| Course dashboard (Streamlit) | Complete — runs locally with `make dashboard` |
| Automated grading (pytest + GitHub Actions) | Complete — 67 tests, CI configured |
| Assignment documentation | Complete — `ASSIGNMENT.md` |
| Instructor teaching guide | Complete — `docs/instructor/teaching_guide.md` |
| Instructor demo prompt | Complete — `docs/instructor/demo_prompt.md` |
| Teaching dataset | Complete — hosted on GitHub Releases, downloads via `make fetch-sample` |
| Pedagogical documentation | Complete — `COURSE_OVERVIEW.md`, `docs/pedagogy.md`, `docs/roadmap.md` |
| Tutorial website (supplementary) | Live — https://au-cfin-geng.github.io/medical-ai-agentic-course-site/ |

---

## What remains for first delivery

| Item | Priority | Notes |
|------|----------|-------|
| Student cohort assignment setup | High | GitHub Classroom assignment needs to be created using this repo as template |
| Preflight assignment | Medium | Can be handled via `make preflight` in this repo; separate preflight repo is no longer needed |
| Assessment rubric (M0–M6) | Medium | Capstone rubric is done; module-level rubric for formative assessment is not yet written |
| Layer C exploration prompts | Low | Existing prompt files have Layer C stubs; not required for delivery |
| Post-course survey / learning analytics | Low | `docs/instructor/learning_analytics_research_plan.md` in teacher repo contains design |

---

## Quick start for review

```bash
git clone https://github.com/au-cfin-geng/student-classroom-repo
cd student-classroom-repo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make preflight       # 12 structural checks — confirms repo integrity
make fetch-sample    # downloads 256 KB teaching dataset from GitHub Releases
make dashboard       # opens the course dashboard at http://localhost:8501
```

For a fully guided demo (Claude sets everything up and walks through the course), see `docs/instructor/demo_prompt.md`.

---

## Contact

Questions or issues: Geng (gs@cercare-medical.com)
