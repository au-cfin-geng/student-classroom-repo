# Assignment — Agentic Clinical Research Studio

## Course

This course teaches clinical and life-science researchers to design **agentic research workflows** using Claude, VS Code, GitHub, Skills, and tools. You will produce traceable, reviewable artifacts that constitute an auditable research record.

The clinical scenario throughout: brain tumour segmentation from FLAIR MRI.

You are not here to write software. You are here to write precise prompts, judge Claude's outputs against research standards, and commit artifacts that reflect your scientific reasoning.

---

## Your role

You are a **junior clinical AI investigator**.

You direct the research. Claude builds, runs, and summarizes. You judge the results.

Prompts are your experimental instruments. Better prompts improve experimental control.

---

## Lab structure

| Lab | Theme | What you practice |
|-----|-------|--------------------|
| Lab00 — Welcome to Agentic Clinical Research | Orientation | CLAUDE.md as project memory, first prompt-driven artifact |
| Lab01 — Prompt Contracts | Prompt engineering | Output contracts, permission design, role specification |
| Lab02 — Multi-Stakeholder Review | Communication | Adapting outputs for different audiences, honesty constraints |
| Lab03 — Literature Search Skills | Skills/tools | Building reusable Claude Skills, structured literature search |
| Lab04 — Tool / MCP-Aware Workflow | Tool use | MCP tool integration, tool-aware prompting |
| Lab05 — Subagents & Orchestration | Agentic pipelines | Subagent decomposition, orchestration, handoff |
| Capstone | Integration | Independent research workflow combining labs |

Extension labs (optional, Day 2):
- Extension06 — Controlled Experiments
- Extension07 — Clinical Translation
- Extension08 — Research Memory & Handoff

---

## Where you work

All student work for each lab happens in `LabXX/work/`.

```
Lab03/
└── work/
    ├── L3_literature_search_skill.md   ← your primary lab report
    ├── L3_literature_search.md         ← your search results artifact
    └── status.json                     ← completion status
```

**Do not edit `lecture-repo/`.** That directory contains course infrastructure.

**Do not scatter files in the repo root.** Everything goes in `LabXX/work/`.

---

## How to complete a lab

1. Open the dashboard: `make dashboard`
2. Read the lab page — understand the goal and prompt
3. Open `LabXX/do_lab_prompt.md` in VS Code
4. Paste it into Claude Code — Claude produces artifacts in `LabXX/work/`
5. Review and iterate on Claude's outputs
6. When the lab is done, paste `lecture-repo/prompts/finish_lab.md` into Claude Code

**Claude handles packaging.** You do not manually run submission commands.

When you paste the Finish Lab prompt:
- Claude reads your work in `LabXX/work/`
- Claude packages evidence into `LabXXSubmission/`
- Claude drafts `LabXXSubmission/submission.md` from your actual work
- You review Claude's draft — confirm or ask for changes
- Claude shows `git status` and asks before committing
- You decide when to push

---

## Required artifacts per lab

Claude checks these during packaging. GitHub Actions checks them on every push.

| Lab | Required files |
|-----|---------------|
| Lab00 | `Lab00/work/L0_orientation.md`, `Lab00/work/status.json` |
| Lab01 | `Lab01/work/L1_prompt_contract.md`, `Lab01/work/status.json` |
| Lab02 | `Lab02/work/L2_multi_stakeholder_review.md`, `Lab02/work/status.json` |
| Lab03 | `Lab03/work/L3_literature_search_skill.md`, `Lab03/work/L3_literature_search.md`, `Lab03/work/status.json` |
| Lab04 | `Lab04/work/L4_tool_mcp_workflow.md`, `Lab04/work/status.json` |
| Lab05 | `Lab05/work/L5_subagent_workflow.md`, `Lab05/work/L5_subagent_workflow_report.md`, `Lab05/work/status.json` |
| Capstone | `Capstone/work/capstone_report.md`, `Capstone/work/showcase.md`, `Capstone/work/status.json` |

`status.json` minimum schema: `{"status": "ok", "lab": "LabXX"}`

---

## Submission packages

After Claude runs the Finish Lab prompt, each lab produces a submission package:

```
Lab03Submission/
├── submission.md          ← Claude's draft; you review and confirm
├── evidence_manifest.json ← list of evidence files Claude found
└── status.json            ← ready_for_review flag
```

`submission.md` is Claude's synthesis of your work. It is not meant to be perfect — you are expected to review it and push back if it misrepresents what happened.

---

## What submission.md covers

Each lab's `submission.md` should address:

- **Clinical problem** — what were you investigating?
- **Agentic / Claude concept** — what prompt pattern did you apply?
- **What was produced** — what artifacts were created and what do they show?
- **Human verification** — what did you review, judge, or correct?
- **Limitations** — what failed or is uncertain?
- **Ready for review** — checklist

Capstone also includes:
- **Agentic workflow used** — which labs did you integrate?
- **Showcase summary** — 3–5 sentences for the showcase presentation

---

## Grading

**Automated (GitHub Actions):** On every push, the grader checks structure — artifact presence, JSON parseability, heading presence in `submission.md`. Results appear in the Actions tab.

Run locally anytime:
```bash
make progress    # friendly progress report
```

**Manual review:** The instructor reads selected `submission.md` files for:
- Quality of scientific reasoning
- Honesty about results — failures reported accurately, not obscured
- Groundedness in evidence — conclusions tied to specific artifacts
- Prompt craft — output contracts, role specification, constraints

Priority labs for manual review: Lab01, Lab03, Lab05, Capstone.

**You are not graded on achieving the best results.** You are graded on the quality of your process, reasoning, and artifacts.

---

## Submission

Your submission is this GitHub repository. **Submission = your final commit pushed before the deadline.** No separate upload is required.

Push at minimum once after each lab so the instructor can observe incremental progress.

---

## Academic integrity

Using Claude is required and intentional. The following are violations:

- **Fabricating artifacts.** All content in `LabXX/work/` must come from actual Claude interactions. Do not invent metric values, citations, or outputs.
- **Fabricating submission.md.** If Claude drafts your submission based on real evidence, that is expected. If you write fabricated evidence summaries by hand, that is a violation.
- **Copying another student's work.** Your artifacts must come from your own lab sessions.
- **Bypassing the honesty requirement.** If your lab work had limitations or failures, your submission must say so. A submission that accurately reports failure scores higher than one that conceals it.

---

## What good work looks like

- **Prompt-first.** Every lab was driven by structured prompts in Claude Code — not by direct file edits.
- **Evidence-grounded.** `submission.md` reflects what is actually in `LabXX/work/`.
- **Honest.** Limitations are named. Failures are explained.
- **Reviewed.** You pushed back on Claude's draft where it was wrong or imprecise.
- **Incremental.** Commit history shows lab checkpoints, not a single deadline dump.
- **Research-voiced.** Reports use research language: "I investigated X and found Y" not "I ran the script."
