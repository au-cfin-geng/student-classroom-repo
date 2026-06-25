# Legacy: Multi-Repo System

This course was previously structured as four separate repositories:

| Old repo | Role | Status |
|----------|------|--------|
| `student-classroom-repo` | Student lab repo | **This repo — now the single canonical course repo** |
| `student-preflight-repo` | Separate environment preflight assignment | Superseded — preflight is now `make preflight` in this repo |
| `teacher-ta-repo` | Instructor materials, demo scripts | Superseded — instructor docs are now in `docs/instructor/` |
| `medical-ai-agentic-course-site` | MkDocs GitHub Pages tutorial site | Still live at https://au-cfin-geng.github.io/medical-ai-agentic-course-site/ — maintained separately as supplementary reading |

## Why consolidated

The multi-repo structure created conceptual fragmentation: students had one repo for preflight, another for the main lab, and instructors had a third repo with materials that were hard to keep in sync. The course identity was spread across four places.

This repo now contains everything needed to run the course:
- Student-facing: prompts, assignments, README, modules, dashboard
- Instructor-facing: docs/instructor/
- Infrastructure: scripts, tests, Makefile, GitHub Actions

## The tutorial website

The GitHub Pages site remains live and is referenced from `COURSE_OVERVIEW.md` as supplementary reading. It is not required for the course to run — everything essential is in this repo.

## Kim's demo prompt

The full demo prompt for a supervisor review (previously in `teacher-ta-repo/docs/instructor/kim_claude_prompt_full_demo.md`) is now in `docs/instructor/demo_prompt.md`.
