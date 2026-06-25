# Modules — Agentic Clinical Research Studio

Design guides for instructors and advanced students. One guide per lab, explaining the pedagogical rationale, assignment details, and success criteria.

---

## Core Labs (L0–L5)

| Folder | Lab | Concept | Time |
|--------|-----|---------|------|
| `L0_agentic_studio/` | L0 — Agentic Research Studio | Workspace, project memory, artifact loop | 45 min |
| `L1_prompt_contracts/` | L1 — Prompt Contracts | Inputs, permissions, output schema | 40 min |
| `L2_multi_stakeholder_review/` | L2 — Multi-Stakeholder Review | Role prompting, stakeholder simulation | 45 min |
| `L3_literature_search_skills/` | L3 — Literature Search Skills | PICO, Skills, approval gates, confidence marking | 45 min |
| `L4_tool_mcp_workflows/` | L4 — Tool & MCP Workflows | Context channels, permissions, audit trails | 45 min |
| `L5_subagent_workflow/` | L5 — Subagents & Orchestration | Specialised subagents, handoff protocols | 50 min |
| `capstone/` | Capstone Mini-Project | Integration of 3+ concepts | 60 min |

## Extension Labs (L6–L8)

| Folder | Lab | Concept | Time |
|--------|-----|---------|------|
| `extensions/L6_controlled_experiments/` | L6 — Controlled Experiments | One variable, baseline, negative results | 45 min |
| `extensions/L7_clinical_translation/` | L7 — Clinical Translation | Audience writing, honesty constraints | 40 min |
| `extensions/L8_research_memory_handoff/` | L8 — Research Memory & Handoff | CLAUDE.md evolution, decision logs | 35 min |

---

## Legacy Module Guides (v1 — M0–M6)

The original M0–M6 module guides remain in place as reference. They describe the internal pipeline stages used in L5 and L6 (controlled experiments).

| Folder | Module | Stage |
|--------|--------|-------|
| `m0-project-memory/` | M0 — Project Memory | `make bootstrap` |
| `m1-inspect-first/` | M1 — Inspect First | `make fetch-sample`, `make visualize` |
| `m2-define-success/` | M2 — Define Success | `make smoke-train` |
| `m3-evidence-diagnosis/` | M3 — Evidence Diagnosis | `make error-analysis` |
| `m4-one-variable/` | M4 — One Variable | `make model-swap` |
| `m5-reviewer-role/` | M5 — Reviewer Role | `make challenge-plan` |
| `m6-honest-translation/` | M6 — Honest Translation | `make translation-memo` |

---

## Prompt Mapping (legacy → Phase 2)

Several Phase 2 labs reuse the underlying pipeline prompts:

| Phase 2 Lab | Prompt file |
|-------------|-------------|
| L0 | `prompts/00_start_agentic_studio.md` |
| L1 | `prompts/stage_02_load_visualize.md` |
| L2 | `prompts/stage_07_challenge_plan.md` |
| L5 | `prompts/stage_03_train_baseline.md` |
| L6 | `prompts/stage_05_model_swap.md` |
| L7 | `prompts/stage_09_translation_memo.md` |
