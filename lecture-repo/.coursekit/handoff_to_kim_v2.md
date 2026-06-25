# Medical AI + Agentic Coding Lab — Handoff Note for Kim

**Date:** June 2026
**From:** Geng
**Re:** Updated course design + data fix + tutorial website

---

## 1. The data issue is fixed

The `make fetch-sample` failure you saw is now resolved. The teaching dataset was previously pointing to a hardcoded local path on my machine. It is now hosted on GitHub Releases and downloads automatically for anyone who runs:

```bash
make fetch-sample
```

No configuration needed. The data (256 KB) downloads from:
`https://github.com/au-cfin-geng/student-classroom-repo/releases/tag/v1.0-data`

Your existing clone should work immediately — just pull first:

```bash
git pull
make fetch-sample
make dashboard
```

---

## 2. What the lab is (updated design)

The course has been redesigned from a "run a segmentation pipeline" lab into an explicit **clinical AI research methods + Claude / agentic coding methodology** course.

### The central idea

Every mission now teaches two things in parallel:

> **A clinical AI concept** (what and why)
> **A Claude / agentic research concept** (how to do it better with AI)

The pattern for every mission is:

```
Traditional workflow pain point
→ Claude / agentic concept introduced
→ Prompt applied by student
→ Artifact produced
→ Result inspected manually
→ Transferable PhD research skill identified
```

Students are not learning to code. They are learning to **communicate research intent to an AI agent**, evaluate AI outputs with scientific judgment, and maintain human responsibility for research quality.

### The loop

```
dashboard → read prompt → VS Code + Claude Code → artifact → dashboard
```

The Streamlit dashboard is the mission cockpit. Claude Code (the VS Code extension / terminal CLI) is where students run prompts. The repo is intentionally sparse at the start — students fill it in as they work through missions.

---

## 3. The seven missions

| Mission | Theme | Claude / agentic concept taught |
|---|---|---|
| **Preflight** | Workstation setup | Claude as setup assistant + readiness audit |
| **Mission 0 — Wake the Lab** | Environment audit | CLAUDE.md as project memory + explicit output contract |
| **Mission 1 — Receive the Signal** | Data inspection | Claude as data steward; inspect before you model |
| **Mission 2 — Build the First Detector** | Baseline + evaluation | Builder + evaluator; define success before optimising |
| **Mission 3 — Investigate Failure** | Error analysis | Visual debugger + hypothesis generator; observation → evidence → hypothesis |
| **Mission 4 — Improve With Intent** | Controlled improvement | Controlled single-variable experiment; change one thing |
| **Mission 5 — Design the Next Study** | Study design | Role switching: developer → reviewer → study design critic |
| **Mission 6 — Translate Responsibly** | Clinical translation | Clinical translator role; honesty constraint; limitation-first reporting |

Each mission produces a set of graded artifacts (JSON status files, metric files, PNG figures, written reports). Grading is automated via `pytest` and rewards honest reasoning, not high Dice scores.

---

## 4. How to get started as a student / evaluator

### Prerequisites

- Python 3.9+ installed
- Git and GitHub access
- VS Code installed
- Claude Code extension installed in VS Code (or `claude` accessible in terminal)

### Step-by-step

```bash
# 1. Clone the student lab repo
git clone https://github.com/au-cfin-geng/student-classroom-repo.git
cd student-classroom-repo

# 2. Install dependencies (in a virtual environment recommended)
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Run structural preflight (no data needed)
make preflight
# Expected: 12/12 tests pass

# 4. Fetch the teaching dataset
make fetch-sample
# Expected: downloads 256 KB, 10 MRI slices ready

# 5. Open the mission dashboard
make dashboard
# Opens Streamlit at http://localhost:8501

# 6. Open VS Code and start Mission 0
code .
# In VS Code: open Claude Code panel, paste the prompt from prompts/stage_00_bootstrap.md
```

### Where to find the prompts

Each mission has a prompt file in `prompts/`:

```
prompts/stage_00_bootstrap.md       ← Mission 0: Wake the Lab
prompts/stage_01_fetch_sample.md    ← Mission 1: Receive the Signal
prompts/stage_02_load_visualize.md  ← Mission 2 (part 1): Visualise
prompts/stage_03_train_baseline.md  ← Mission 2 (part 2): Train + Evaluate
prompts/stage_04_error_analysis.md  ← Mission 3: Investigate Failure
prompts/stage_05_model_swap.md      ← Mission 4: Improve With Intent
prompts/stage_07_challenge_plan.md  ← Mission 5: Design the Next Study
prompts/stage_09_translation_memo.md ← Mission 6: Translate Responsibly
```

Each prompt file has three layers:
- **Layer A** — the base prompt (paste this into Claude Code to complete the mission)
- **Layer B** — a reflection prompt (run after Layer A to interpret the results)
- **Layer C** — an optional exploration/customisation prompt

---

## 5. The tutorial website

There is a companion tutorial website that students should read alongside the lab. It teaches the clinical AI concepts and agentic research methods that each mission applies.

**Website:** `https://au-cfin-geng.github.io/medical-ai-agentic-course-site/`

*(If the GitHub Pages deployment is still building, the source is at `https://github.com/au-cfin-geng/medical-ai-agentic-course-site`)*

### Site structure

| Section | What it covers |
|---|---|
| **Getting Started** | Course overview, classroom workflow, how to use the lab studio |
| **Clinical AI** | What is clinical AI, MRI basics, brain tumour segmentation, evaluation metrics, error analysis, clinical translation |
| **Agentic Research** | What is agentic research, Claude Code mental model, prompts as experimental instruments, roles/tools/skills, CLAUDE.md project memory, AI capabilities and limitations |
| **Lab Missions** | One page per mission: clinical motivation, traditional bottleneck, Claude method, expected artifact, how to inspect, reflection question, transfer to own research |
| **Handouts** | Printable cheat sheets: clinical AI, MRI, Dice metrics, Claude workflow, prompt patterns, responsible clinical AI checklist |
| **Readings** | Anthropic Academy reading map (public course titles mapped to lab missions), further reading |
| **Instructor** | Teaching plan, discussion prompts, live demo script, assessment rubric, showcase guide |

### Recommended reading sequence

Before each lab session, students read the corresponding tutorial pages:

| Before this mission | Read these site pages |
|---|---|
| Preflight + Mission 0 | Getting Started → Course Overview + Classroom Workflow |
| Mission 1 | Clinical AI → What Is Clinical AI + MRI Basics + Agentic Research → Claude Code Mental Model |
| Mission 2 | Clinical AI → Brain Tumour Segmentation + Evaluation Metrics |
| Mission 3 | Clinical AI → Error Analysis + Agentic Research → Role Switching |
| Mission 4 | Agentic Research → Prompts as Experimental Instruments + Tool Use and Output Contracts |
| Mission 5 | Agentic Research → Role Switching for Research |
| Mission 6 | Clinical AI → Clinical Translation + Agentic Research → AI Capabilities and Limitations |

---

## 6. Key design principles (for your course design reference)

1. **Prompt-first, not code-first.** Students direct Claude Code using natural language. The prompt is the experimental instrument. Better prompts = better experimental control.

2. **Artifacts over chat.** Grading is on committed files (JSON, PNG, MD reports), not on Claude's chat output. If the file doesn't exist, the work didn't happen.

3. **Honesty over performance.** Prompts and CLAUDE.md explicitly require honest reporting. A Dice score of 0.6 honestly analysed scores higher than 0.9 without explanation. Mission 6 explicitly teaches the difference between research prototype and clinical readiness.

4. **Human judgment maintained.** Every prompt has a Layer B reflection prompt that asks students to interpret the results themselves. Claude builds; the student judges.

5. **No Anthropic Academy content is included.** The tutorial site references public Anthropic course titles for recommended external reading, but all course content is original.

---

## 7. Files you should review

For your course design evaluation:

| File | What it is |
|---|---|
| `ASSIGNMENT.md` | Student-facing assignment spec (updated with agentic skills section) |
| `CLAUDE.md` | Claude's behaviour contract for the lab |
| `prompts/stage_00_bootstrap.md` | Example of the new prompt format (Traditional bottleneck → Claude method → Layer A/B/C → Transfer) |
| `prompts/stage_09_translation_memo.md` | The most clinically demanding prompt (Mission 6) |
| `.coursekit/agentic_clinical_ai_upgrade_plan_v2.md` | Full upgrade plan with mission-by-mission matrix |
| Tutorial site → Lab Missions section | One page per mission with full pedagogical structure |
| Tutorial site → Instructor section | Teaching plan, discussion prompts, rubric |

---

Questions or issues: ping Geng.
