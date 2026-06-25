# Clinical Claude Course — Course Overview

## Course Identity

**Clinical Claude** is a module-based course teaching researchers how to use Claude effectively for clinical AI research. It is not a programming course. It is not a dashboard demo. It is a structured curriculum for medical researchers who want to work with AI as a genuine research partner — with the rigor, honesty, and judgment that clinical work demands.

Every module in this course is organized around one Claude best practice or capability, taught entirely through a realistic clinical or medical research scenario. The scenario is real: brain tumour segmentation from MRI using the BraTS dataset. The problems are real: unclear environment, bad baselines, undocumented changes, overclaimed results. The solutions are practical: Claude-assisted research workflows that actually scale.

---

## Terminology

| Term | Meaning | Used in |
|------|---------|---------|
| **Module** | Student-facing learning unit, M0–M6 plus Capstone | `modules/`, dashboard, ASSIGNMENT.md |
| **Stage** | Internal implementation step that generates artifacts | `scripts/`, `outputs/status/`, Makefile |
| **Artifact** | Graded output: status JSON, PNG figure, metric file, or written report | `outputs/`, `reports/` |
| **Capstone** | Final integrated project with independent research design | `modules/capstone/` |
| **Mission** | Legacy term for module; retained in dashboard narrative labels (e.g., "Wake the Lab") but not in course documentation |

Each module is implemented by one or more stages. Students interact with modules; stages are scaffolding they do not need to study directly.

---

## The Central Claim

**The single most important thing a clinical researcher can learn about Claude is this:**

Claude is a capable collaborator, not an oracle. The researcher who writes a clear, constrained, evidence-grounded prompt gets a better result than the researcher who types a vague question. The researcher who reads and judges Claude's output — rather than accepting it — produces better science. The researcher who maintains human responsibility for clinical claims — rather than outsourcing them to Claude — is the one who can defend their work.

This course teaches that capability. Every module is a step toward it.

---

## Pedagogical Model: Four Layers

The course is designed to operate simultaneously on four pedagogical layers. Students may not notice all four explicitly, but every module engages all of them.

**Layer 1 — Operational**
How to use Claude + VS Code + GitHub to actually accomplish research tasks. This is the how-to layer. Students need it before anything else can work.

**Layer 2 — Prompt craft**
Why some prompts work better than others. Why output contracts, role assignment, constraints, and specificity matter. This is the craft layer. Students who master it get consistently better outputs from Claude.

**Layer 3 — Research reasoning**
Why the researcher must still judge validity, limits, and evidence — regardless of how good Claude's output looks. This is the judgment layer. It prevents the dangerous error of treating Claude's output as a result rather than as a draft.

**Layer 4 — Translation across audiences**
How the same result must be communicated differently to yourself, a collaborator, a clinician, a PI, a reviewer, and a technical peer. This is the communication layer. Clinical AI research fails not just when models fail, but when results are communicated without appropriate context and humility.

---

## Module Map

Each module is organized around one Claude best practice, taught through one clinical research scenario.

| # | Module | Clinical problem | Claude capability | Prompt principle |
|---|--------|-----------------|-------------------|-----------------|
| M0 | Project Memory | Repo chaos, unclear readiness | CLAUDE.md as persistent project context | Explicit output contracts |
| M1 | Inspect Before You Model | Blind modeling on unknown data | Claude as data steward | Structured inspection before action |
| M2 | Define Success First | Optimizing without a baseline | Evaluation-driven prompting | State the goal before the method |
| M3 | Evidence-Based Diagnosis | Debugging by intuition | Claude as visual debugger | Observation → evidence → hypothesis |
| M4 | One Variable at a Time | Undocumented, uncontrolled changes | Controlled experiment design | Specify exactly what changed and why |
| M5 | The Reviewer Role | Only developer perspective | Role switching | Ask Claude to challenge your own work |
| M6 | Honest Translation | Overclaiming prototype results | Multi-audience translation | Honesty constraints in prompts |
| C | Capstone | Full pipeline, real judgment calls | Integration of all 7 principles | Your own design |

See `modules/` for the detailed guide for each module.

---

## Course Structure

The course runs over two days in a supervised lab setting, but the material is designed to be self-paced.

**Day 1 — Foundation (Modules 0–4)**
Build the clinical AI pipeline from scratch. Master the first four Claude patterns. Produce a documented set of research artifacts.

**Day 2 — Extension (Modules 5–6 + Capstone)**
Critique and extend your own work. Learn the two hardest Claude skills: reviewing your own outputs honestly, and translating research results into clinical language without overclaiming.

**Timeline within Day 1:**

| Time | Module | Estimated duration |
|------|--------|--------------------|
| 0:00 | M0: Project Memory | 30 min |
| 0:30 | M1: Inspect Before You Model | 20 min |
| 0:50 | M2: Define Success First | 40 min |
| 1:30 | M3: Evidence-Based Diagnosis | 40 min |
| 2:10 | M4: One Variable at a Time | 30 min |
| 2:40 | Checkpoint — commit + dashboard review | 20 min |

**Timeline within Day 2:**

| Time | Module | Estimated duration |
|------|--------|--------------------|
| 0:00 | Review Day 1 results | 20 min |
| 0:20 | M5: The Reviewer Role | 50 min |
| 1:10 | M6: Honest Translation | 40 min |
| 1:50 | Capstone: Independent design | 60 min |
| 2:50 | Showcase: Present artifacts + failure analysis | 30 min |

---

## The Student's Role

Students are positioned as **junior clinical AI investigators**.

Their job is not to write code. Their job is to:
- Write structured prompts that direct Claude with precision
- Judge Claude's outputs against the research question
- Produce artifacts (figures, metrics, reports) that constitute evidence
- Reason honestly about what the results mean
- Translate results appropriately for different audiences

The repo begins intentionally sparse. As each module is completed, the repo fills with real research artifacts. This growth is visible in the commit history — and is partly how the instructor monitors progress.

---

## What Students Do NOT Do

- They do not directly edit scripts (Claude writes and runs them)
- They do not need to understand the implementation in depth
- They do not submit chat output (only committed artifacts count)
- They are not graded on achieving a high Dice score

---

## What Students ARE Graded On

1. **Artifact presence** — automated (GitHub Actions / pytest)
2. **Report quality** — the written reasoning in `reports/`, assessed manually
3. **Honesty** — does the student report what they actually found?
4. **Prompt craft** — does the student use prompts with clear specifications?
5. **Scientific judgment** — does the student evaluate results, not just produce them?

Grading details: see `ASSIGNMENT.md`.

---

## The Clinical Problem

This course uses brain tumour segmentation from MRI as its teaching dataset.

**Why this problem?**
- It is a real, active research area
- It has well-understood failure modes that are clinically meaningful
- The Dice coefficient is a clean, interpretable metric
- Error analysis is visually demonstrable
- The gap between research prototype and clinical deployment is starkly evident

Students work with 10 annotated MRI slices from the BraTS 2016/2017 dataset. This is a teaching subset — enough to compute real metrics, small enough to run on a laptop, clinically meaningful enough to take seriously.

**The research question the course uses:**
> Can a simple intensity-based segmentation algorithm detect brain tumours from FLAIR MRI with sufficient consistency to justify further investigation?

By the end of the course, students have a documented, honest answer to this question — plus a clear-eyed assessment of what it would take to move from a research prototype to clinical deployment.

---

## Course Philosophy

**Prompt-first, not code-first.**
The prompt is the experimental instrument. Better prompts improve experimental control — just as a better protocol improves a clinical trial. Students who write vague prompts get vague results. Students who write precise prompts get precise results they can judge.

**Artifacts over chat.**
Grading is on committed files — not on Claude's conversational output. If the file doesn't exist, the work didn't happen. This is intentional: it trains the habit of producing verifiable evidence, not just running a chat session.

**Honesty over performance.**
The grading system rewards honest analysis of a Dice score of 0.55 more than evasion about a Dice score of 0.90. Clinical researchers who cannot honestly report failure are dangerous.

**Human judgment maintained.**
Every module has a reflection prompt that asks the student to interpret the results before moving on. Claude builds; the student judges. This boundary is non-negotiable.

---

## Relation to Anthropic's Claude Ecosystem

This course aligns with Claude best practices as taught in Anthropic Academy. It does not reproduce Anthropic Academy content. All course materials are original.

Students who want to go deeper on Claude prompt craft after this course are encouraged to explore Anthropic Academy's public course offerings — particularly courses covering Claude Code and agentic workflows.

---

## For Instructors

See `docs/instructor/` for:
- Teaching guide (module-by-module facilitation notes)
- Assessment rubric (100-point scale, 8 dimensions)
- Live classroom facilitation notes
- Showcase formats
- Discussion questions

The full demo prompt for a supervisor or instructor review is in `docs/instructor/demo_prompt.md`.
