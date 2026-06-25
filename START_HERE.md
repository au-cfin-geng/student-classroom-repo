# START HERE — Agentic Clinical Research Studio

Welcome. This is the first file you read.

---

## What this course is

A lab-based course for clinical and life-science PhD researchers. You will learn to design **agentic research workflows** — using Claude, VS Code, GitHub, Skills, and tools — to turn research bottlenecks into traceable, verifiable artifacts.

The clinical scenario throughout: brain tumour segmentation from FLAIR MRI.

You are not here to write software. You are here to write precise prompts, judge Claude's outputs against research standards, and commit artifacts that constitute an auditable research record.

---

## Step 1 — Install VS Code

Download and install **Visual Studio Code** from [code.visualstudio.com](https://code.visualstudio.com).

---

## Step 2 — Install Claude Code

Inside VS Code:

1. Open the Extensions panel (`Cmd+Shift+X` on Mac · `Ctrl+Shift+X` on Windows)
2. Search for **Claude Code**
3. Click Install — sign in when prompted

Or from the terminal:
```bash
npm install -g @anthropic-ai/claude-code
```

For current installation details, search: **"Claude Code installation guide docs.anthropic.com"**

---

## Step 3 — Open this repo in VS Code

```bash
git clone https://github.com/au-cfin-geng/student-classroom-repo
cd student-classroom-repo
```

Then in VS Code: **File → Open Workspace from File → `student-lab.code-workspace`**

The workspace shows the simple structure: course dashboard + lab folders + submission folders.

---

## Step 4 — Start the dashboard

```bash
make dashboard
```

Or open Claude Code and paste `lecture-repo/prompts/00_start_agentic_studio.md` — Claude will start everything for you.

---

## The simple model

```
Work in LabXX/work/  →  Paste Finish Lab prompt  →  Claude creates LabXXSubmission/  →  GitHub checks
```

| What you do | Where |
|-------------|-------|
| Read the lesson, get the prompt | Course dashboard (`make dashboard`) |
| Do all lab work | `LabXX/work/` (e.g. `Lab01/work/`) |
| Finish and package | Paste `lecture-repo/prompts/finish_lab.md` into Claude Code |
| Claude creates submission | `LabXXSubmission/` (Claude does this — you do not run commands) |
| Check progress | `make progress` |

**You do not manually run package commands. Claude handles submission packaging.**

---

## Lab order

| Day 1 | Day 2 |
|-------|-------|
| Lab00 — Welcome to Agentic Clinical Research | Lab05 — Subagents & Orchestration |
| Lab01 — Prompt Contracts | Capstone Mini-Project |
| Lab02 — Multi-Stakeholder Review | Extension06 — Controlled Experiments (optional) |
| Lab03 — Literature Search Skills | Extension07 — Clinical Translation (optional) |
| Lab04 — Tool / MCP-Aware Workflow | Extension08 — Research Memory & Handoff (optional) |

---

## How Claude finishes each lab

After completing each lab activity in `LabXX/work/`:

1. Open `lecture-repo/prompts/finish_lab.md` in VS Code
2. Paste its full contents into Claude Code
3. Claude reads your work, packages evidence, and drafts `LabXXSubmission/submission.md`
4. You review Claude's draft — confirm or ask for changes
5. Claude asks before committing — you decide when to push
6. GitHub Actions checks submission structure automatically

---

## Checking your progress

```bash
make progress    # friendly progress report — always succeeds
make dashboard   # visual progress in the dashboard
```

---

## What gets graded

1. **Artifact presence** — automated (GitHub Actions on every push)
2. **Report quality** — Claude's draft of your `submission.md`, which you confirm
3. **Honesty** — did you report what you actually found, including failure cases?
4. **Prompt craft** — do your prompts use output contracts, role specification, constraints?
5. **Scientific judgment** — do you evaluate results, not just produce them?

See `ASSIGNMENT.md` for the full grading spec.
See `lecture-repo/docs/assessment_model.md` for the grading language.

---

## Contact

Questions or setup problems: **gs@cercare-medical.com**
