# Agentic Clinical Research Studio — Advisor Preview

**Version:** v3 (Phase 2 Redesign)
**Date:** June 2026
**Prepared by:** Geng (gs@cercare-medical.com)

---

## What this is

**Agentic Clinical Research Studio** is a lab-based graduate course teaching clinical and life-science researchers to design agentic research workflows that produce traceable, reviewable, clinically responsible artifacts.

The tools taught: Claude, VS Code, GitHub, Skills, MCP tools, structured prompts, stakeholder roles, and subagents.

The clinical scenario: brain tumour segmentation from FLAIR MRI using a teaching BraTS-format dataset.

This is not a programming course. Students write prompts as research protocols, judge Claude's outputs against clinical research standards, and commit artifacts as their research record.

---

## Course structure (v3)

| Component | Description |
|-----------|-------------|
| **6 core labs** (L0–L5) | Independent, 40–50 min each — prompt contracts, stakeholder review, literature skills, tool/MCP workflows, subagent orchestration |
| **Capstone** | 60 min — integrated agentic workflow, three tiers (basic/medium/advanced) |
| **3 extensions** (L6–L8) | Optional, 35–45 min each — controlled experiments, clinical translation, research memory |

Labs are **independent** — students can do them in any order after L0.

---

## What changed from v2 → v3

| v2 (Phase 1) | v3 (Phase 2 — current) |
|-------------|------------------------|
| "Clinical Claude" identity | "Agentic Clinical Research Studio" identity |
| L0–L7 framing | L0–L5 core + Capstone + L6–L8 extensions |
| Blue-grey dashboard | Cream/off-white long-form lesson pages (Academy-inspired) |
| Lab pages: brief cards | Lab pages: full lesson (concept, scenario, before/after, assignment, artifacts, reflection) |
| L5 = "Agentic Coding" | L5 = "Subagents & Orchestration" (non-developer framing) |
| L2 = "Role-Based Review" | L2 = "Multi-Stakeholder Review" (medical research stakeholders, not developer roles) |
| No handouts directory | 10 handout files with 10-section structure |
| Phase 1 module guides | Phase 2 module guides (new lab structure) |

---

## Lab topics

| Lab | Title | Agentic Concept | Day |
|-----|-------|-----------------|-----|
| L0 | Agentic Research Studio | Workspace + project memory + artifact loop | 1 |
| L1 | Prompt Contracts | Inputs, permissions, output schema | 1 |
| L2 | Multi-Stakeholder Review | Role prompting, stakeholder simulation | 1 |
| L3 | Literature Search Skills | Skills, PICO, approval gates, confidence marking | 1 |
| L4 | Tool & MCP Workflows | Context engineering, permission design | 1 |
| L5 | Subagents & Orchestration | Specialised subagents, handoff protocols | 2 |
| CAP | Capstone Mini-Project | Integration of 3+ concepts | 2 |
| L6 | Controlled Experiments | One variable, baseline, honest results | 2 |
| L7 | Clinical Translation | Audience writing, honesty constraints | 2 |
| L8 | Research Memory & Handoff | CLAUDE.md evolution, decision logs | 2 |

---

## Assessment

Students are **not** graded on model performance metrics. Grading dimensions:

1. Artifact presence (automated via GitHub Actions)
2. Report quality (written reasoning in `reports/*.md`)
3. Honesty (did they report actual findings, including failures?)
4. Prompt craft (output contracts, role specification, constraints)
5. Scientific judgment (evaluation of results, not just production)

---

## Implementation status

| Component | Status |
|-----------|--------|
| Course dashboard (`app/streamlit_app.py`) — v3 identity, cream design, L0–L8 labs | Complete |
| START_HERE.md — updated for Agentic Clinical Research Studio | Complete |
| CLAUDE.md — updated course identity section | Complete |
| `prompts/00_start_agentic_studio.md` | Complete |
| `handouts/` directory — 10 handout files (10-section template each) | Workflow in progress |
| Module guides — L0–L5, extensions, capstone | Workflow in progress |
| Legacy pipeline (scripts, tests, Makefile, M0–M6 guides) | Preserved |
| Preflight validation | 12/12 passing |
| Python syntax check | Clean |

---

## Quick start for review

```bash
git clone https://github.com/au-cfin-geng/student-classroom-repo
cd student-classroom-repo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make preflight       # 12 structural checks
make fetch-sample    # downloads 256 KB teaching dataset
make dashboard       # opens dashboard at http://localhost:8501
```

Select any lab from the sidebar to see the full lesson page.

---

## Contact

Questions: **gs@cercare-medical.com**
Student repo: https://github.com/au-cfin-geng/student-classroom-repo
