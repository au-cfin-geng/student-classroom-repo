# Repository Architecture — Clinical Claude

This document is for instructors, teaching assistants, and course maintainers. It describes how the repository is structured, why it is structured that way, and what must not be changed without understanding the downstream consequences.

---

## Two-Layer Architecture: Student-Visible vs. Hidden

The repository presents a deliberately curated surface to students. Two VS Code workspace files control what students see:

**`student-lab.code-workspace`** — the workspace students open. It hides the following directories via VS Code `files.exclude` settings:

- `app/` — the Streamlit dashboard and its supporting logic
- `scripts/` — all Python execution scripts
- `tests/` — the autograding test suite
- `.coursekit/` — design spec, internal tooling, grading rubrics
- `artifacts/` — raw versioned artifacts before promotion to `outputs/`
- `.github/` — CI workflow definitions
- `.session_archives/` and `.student_state/` — runtime state managed by the dashboard

**`instructor-full.code-workspace`** — opens the full tree. Instructors and TAs should use this exclusively.

**Student-visible directories:**

| Path | Purpose |
|---|---|
| `prompts/` | The stage prompt files students read and execute with Claude Code |
| `outputs/` | Figures, metrics, and status files produced during the course |
| `reports/` | Written analysis artifacts students generate |
| `data/` | The BraTS teaching slices (10 FLAIR images + ground truth masks) |
| `modules/` | Module design guides — the conceptual layer students read |
| `docs/` | Course-facing documentation including this file |
| `README.md` | Entry point for new students |
| `ASSIGNMENT.md` | Full assignment specification with grading criteria |
| `CLAUDE.md` | The project-level contract Claude reads before acting |

---

## Why Scripts Are Hidden

The central pedagogical intent of this course is that **students direct Claude with prompts, not scripts directly**. When scripts are visible, students reach for `python scripts/run_train.py` rather than writing a structured prompt that instructs Claude to run the segmentation pipeline. This short-circuits the learning objective.

Hiding `scripts/` forces the correct student interaction model: the dashboard shows the mission, the student writes a prompt, Claude executes the prompt and drives the scripts, and the student evaluates the artifact. The scripts exist to give Claude reliable, deterministic execution paths. They are not the object of study; the prompts are.

The `make` targets in `Makefile` remain available to students through the terminal, and `ASSIGNMENT.md` references them explicitly. These are intentional escape hatches for debugging and re-running stages. They are not the primary workflow, but students should not be blocked by a silent script failure when the Makefile can diagnose it directly.

---

## Stage-to-Module Mapping

The course has two parallel organizational layers that serve different purposes.

**Stages** (`stage_00` through `stage_09`) are the implementation layer. Each stage prompt file in `prompts/` drives one discrete research operation: environment bootstrap, data fetch, visualization, baseline segmentation, error analysis, model comparison, report packing, challenge planning, pipeline adaptation, and clinical translation. Stages execute sequentially and produce deterministic artifacts.

**Modules** (`modules/m0-project-memory/` through `modules/m6-honest-translation/`, plus `modules/capstone/`) are the conceptual layer. Each module teaches one Claude principle: project memory, inspect-before-acting, defining success metrics, evidence-based diagnosis, single-variable control, reviewer roleplay, and honest translation. A module may span multiple stages, or a single stage may contain work relevant to more than one module.

The module guides are what students read to understand *why* they are doing something. The stage prompts are what they execute to *do* it. Both layers are required; neither is redundant. Do not conflate them when writing course updates — changes to one do not automatically update the other.

---

## How Grading Works Technically

Automated grading uses `pytest` against the `tests/` directory. Three test files define the grading contract:

- `test_preflight.py` — structural checks that run before any data is present. Verifies that required directories, configuration files, and scripts exist. Students run this first with `make preflight`.
- `test_scripts_exist.py` — confirms that all execution scripts referenced by the Makefile are present and importable.
- `test_artifacts.py` — checks artifact presence and structure after stages have been executed. Verifies that output files exist at expected paths, that metrics files are valid JSON with required keys, that figures are non-empty, and that report files meet minimum length requirements.

The test suite does not evaluate scientific quality. It enforces artifact contracts: the right files exist at the right paths, are non-empty, and carry the required structure. Human review of `reports/` files evaluates reasoning quality, clinical grounding, and prompt craft. CI runs `make test` on every push.

---

## CLAUDE.md as Design Authority

`CLAUDE.md` is read by Claude Code at session start. It defines the student interaction model, mission architecture, allowed file paths per stage, output contracts, naming rules, and the tone and constraints Claude applies throughout the course. It is the operational contract between Claude and the student.

The deeper design authority is `.coursekit/student_lab_os_design_spec_v1.md`. If `CLAUDE.md` and the design spec conflict, the design spec governs. `CLAUDE.md` provides shortcuts and concrete path rules; the design spec provides conceptual and pedagogical authority. Instructors who modify course behavior should update both documents and check for inconsistencies between them.

---

## What Not to Change

Three categories of change will silently break the course without producing obvious errors:

1. **Prompt file names.** The dashboard, the Makefile, the test suite, and `ASSIGNMENT.md` all reference stage filenames by exact name. Renaming `stage_03_train_baseline.md` to anything else breaks navigation, grading, and student instructions simultaneously.

2. **Artifact output paths.** `test_artifacts.py` checks specific paths under `outputs/figures/`, `outputs/metrics/`, and `outputs/status/`. Scripts write to these paths. If you move an artifact, you must update the script, the test, and `ASSIGNMENT.md` together — not just one.

3. **Test contracts.** The pytest tests define the grading contract. Relaxing a test without updating `ASSIGNMENT.md` creates a false pass. Tightening a test without updating the scripts creates a false fail. Changes to `tests/` require coordinated review across the full course.

Additive changes — new modules, new reflection questions, additional figures, extended reports — are low risk. Structural changes to the above three categories require full regression testing before deployment.

---

## Legacy Note

This repository was previously part of a multi-repo system in which course infrastructure, student-facing content, and grading lived in separate repositories. It is now the **single canonical course repository**. All content, tooling, grading, and documentation live here. References in older notes or commit history to a separate `course-infra` or `autograder` repository are obsolete. Do not attempt to restore or reconcile with those prior repositories.
