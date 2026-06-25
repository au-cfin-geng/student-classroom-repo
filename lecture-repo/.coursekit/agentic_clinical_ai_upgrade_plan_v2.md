# Agentic Clinical AI Upgrade Plan v2

**Created:** 2026-06-03
**Status:** Planning phase — no large edits made yet
**Scope:** All four repos in medical_ai_agentic_course_bootstrap

---

## 1. Current State Summary

### student-classroom-repo
- README.md: good but framing is "segmentation pipeline lab", not "agentic research methods lab"
- ASSIGNMENT.md: solid structure; missing explicit agentic skills section and traditional→Claude mapping table
- CLAUDE.md: comprehensive; missing artifact mirroring rule, prompt-trace directory policy, and stronger research-language emphasis
- prompts/: 10 files (`stage_00` through `stage_09`), all named `stage_XX_*.md` — tests check for these EXACT filenames, cannot rename without updating tests; all have Layer A/B/C + Discussion structure; missing "Traditional bottleneck", "Claude/agentic method", and "Anthropic Academy alignment" sections
- app/streamlit_app.py: 127KB, working dashboard; missing agentic method cards, completion summaries, optional exploration indicators, and prompt trace visibility
- tests/: 3 test files; `test_preflight.py` checks exact prompt filenames — cannot rename without updating this test
- scripts/: full set of 12 scripts; no changes needed for Phase 0
- .coursekit/: has design spec v1, classroom handoff, advisor preview, README

### student-preflight-repo
- README.md: functional; frames as "setup check", not "agentic workstation setup"
- ASSIGNMENT.md: minimal and pass/fail; no agentic framing
- CLAUDE.md: minimal and correct; needs no structural change, minor framing upgrade
- prompts/preflight.md: one file; needs agentic framing and Layer A/B/C structure
- tests/: present but not yet inspected in detail
- No dashboard

### teacher-ta-repo
- README.md: brief and functional
- docs/: has agentic_workflow.md, schema_alignment.md, github_classroom_setup, data_preparation, course_architecture, teacher_build_plan
- docs/instructor/: does NOT exist — must create
- No assessment rubric, no live facilitation guide, no learning analytics plan, no showcase spec
- Makefile: for demo runs, not for teaching materials

### medical-ai-agentic-course-site
- Built yesterday with good content but OLD information architecture
- Nav structure: course_map/, foundations/, mri/, medical_ai_workflow/, agentic_research/, lab_missions/, prompt_library/, handouts/, instructor_notes/
- Required new IA: getting-started/, clinical-ai/, agentic-research/, labs/, handouts/, readings/, instructor/, curriculum/
- Most content can be reused with remapping — not a full rewrite
- mkdocs.yml needs new nav; many files need to move or be renamed

---

## 2. What Already Works Well

1. The prompt Layer A/B/C + Discussion structure is pedagogically strong
2. The dashboard loop (dashboard → prompt → Claude → artifact → dashboard) is clear
3. Artifact paths and grading schema are well-defined and locked
4. CLAUDE.md honesty requirements and reproducibility rules are excellent
5. ASSIGNMENT.md mission sequence table is clean
6. The stage_07 (challenge plan) prompt is the strongest example of the new pattern — already has "plan before code", role-switching (developer vs devil's advocate), and structured output sections
7. stage_09 (translation memo) already has honesty constraint, audience framing, and multi-stakeholder reflection
8. Teacher-TA has good schema_alignment.md and agentic_workflow.md
9. The course site has substantial content on MRI, clinical AI, and metrics

---

## 3. What Is Missing from the Agentic / Claude Methodology Layer

### In student-classroom-repo
- Explicit "Traditional bottleneck" framing at the top of every prompt (currently implicit at best)
- Explicit "Claude / agentic concept introduced" section in every prompt
- "Anthropic Academy / Claude learning connection" section referencing public course titles
- "Transferable PhD research skill" callout at the end of every prompt
- Optional exploration artifact paths (outputs/prompt_trace/, reports/prompt_notes.md)
- Artifact mirroring rule in CLAUDE.md
- prompt_trace directory creation in bootstrap
- Dashboard: agentic method card per mission, completion takeaway, optional exploration indicator

### In student-preflight-repo
- Agentic framing in README (why Claude Code, not just "run this script")
- Layer A/B/C prompt structure
- "Transferable skill" callout
- Explicit connection to the main lab

### In teacher-ta-repo
- docs/instructor/ directory with all required files
- Assessment rubric
- Live facilitation guide
- Learning analytics research plan
- Showcase dashboard spec

### In course site
- New information architecture (getting-started/, clinical-ai/, agentic-research/, labs/, etc.)
- Anthropic Academy reading map
- Roles/tools/skills page with concrete examples
- Claude Code mental model page
- Every lab page with new structure (traditional bottleneck / Claude method / artifact / inspection / transfer)
- curriculum/ section

---

## 4. Files That Should Change by Repo

### student-classroom-repo
| File | Change type | Risk |
|---|---|---|
| README.md | Rewrite framing | Low — tested for length >200 chars |
| ASSIGNMENT.md | Add two sections | Low |
| CLAUDE.md | Add three new sections | Low |
| prompts/stage_00_bootstrap.md | Add 3 new sections | Low — can't rename |
| prompts/stage_01_fetch_sample.md | Add 3 new sections | Low |
| prompts/stage_02_load_visualize.md | Add 3 new sections | Low |
| prompts/stage_03_train_baseline.md | Add 3 new sections | Low |
| prompts/stage_04_error_analysis.md | Add 3 new sections | Low |
| prompts/stage_05_model_swap.md | Add 3 new sections | Low |
| prompts/stage_06_pack_report.md | Add 3 new sections | Low |
| prompts/stage_07_challenge_plan.md | Add 3 new sections | Low |
| prompts/stage_08_adapt_pipeline.md | Add 3 new sections | Low |
| prompts/stage_09_translation_memo.md | Add 3 new sections | Low |
| app/streamlit_app.py | Add agentic method cards, extend mission data | Medium |
| .coursekit/agentic_clinical_ai_upgrade_plan_v2.md | Create (this file) | None |

**CRITICAL CONSTRAINT:** Prompt filenames MUST remain `stage_XX_*.md`. Tests `test_preflight.py` checks for exact filenames. Do not rename.

### student-preflight-repo
| File | Change type | Risk |
|---|---|---|
| README.md | Reframe as agentic workstation setup | Low |
| ASSIGNMENT.md | Add agentic framing | Low |
| CLAUDE.md | Minor framing upgrade | Low |
| prompts/preflight.md | Upgrade to Layer A/B/C structure | Low |

### teacher-ta-repo
| File | Change type | Risk |
|---|---|---|
| docs/instructor/agentic_clinical_ai_teaching_guide.md | Create | None |
| docs/instructor/assessment_rubric_agentic_clinical_ai.md | Create | None |
| docs/instructor/live_classroom_facilitation.md | Create | None |
| docs/instructor/showcase_dashboard_spec.md | Create | None |
| docs/instructor/learning_analytics_research_plan.md | Create | None |

### medical-ai-agentic-course-site
| File/Directory | Change type | Risk |
|---|---|---|
| mkdocs.yml | Restructure nav (new IA) | Medium — build must pass |
| docs/getting-started/ | Create (4 pages) | Low |
| docs/clinical-ai/ | Create (7 pages, reuse from foundations/ + mri/) | Low |
| docs/agentic-research/ | Rename/move from agentic_research/ | Medium |
| docs/labs/ | Create (8 pages, reuse from lab_missions/) | Low |
| docs/handouts/ | Restructure existing (low risk) | Low |
| docs/readings/ | Create (2 pages) | None |
| docs/instructor/ | Create (5 pages, reuse from instructor_notes/) | Low |
| docs/curriculum/ | Create (1 page — the curriculum map) | None |
| OLD dirs (course_map/, foundations/, mri/, etc.) | Keep for now, can remove later | Low |

---

## 5. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Prompt rename breaks tests | HIGH if renamed | HIGH | Never rename; update in-place |
| Dashboard rewrite breaks working UI | Medium | High | Extend only; never rewrite structure |
| Site nav change causes build failure | Low | Medium | Run mkdocs build after every change |
| Streamlit code edit breaks display | Medium | Medium | Edit existing patterns, don't restructure |
| Missing import in new code | Low | Medium | Test after adding each section |
| Old site dirs cause nav conflicts | Low | Low | Add new dirs; leave old for transition |

---

## 6. Test Plan

### Before any changes
```bash
cd student-classroom-repo && make preflight   # baseline
cd student-classroom-repo && pytest -q tests/  # baseline
```

### After student-classroom-repo changes
```bash
cd student-classroom-repo && make preflight
cd student-classroom-repo && pytest -q tests/
```

### After preflight-repo changes
```bash
cd student-preflight-repo && make test 2>/dev/null || pytest -q tests/ 2>/dev/null
```

### After site changes
```bash
cd medical-ai-agentic-course-site && mkdocs build
```

### After teacher-ta changes
```bash
# Check markdown files exist and are readable
ls teacher-ta-repo/docs/instructor/
```

---

## 7. Rollback Plan

All repos are git-tracked. If changes break tests:
```bash
git diff HEAD          # see what changed
git checkout -- <file> # restore a specific file
git reset HEAD~1       # undo last commit if committed
```

No destructive operations are planned. All new files can be deleted. All edited files can be restored from git.

---

## 8. Mission-by-Mission Upgrade Matrix

| Mission | Stage file | Traditional workflow pain point | Claude / agentic concept introduced | Anthropic Academy alignment | Clinical AI concept | Prompt principle | Student action | Required artifact | Optional exploration | Transferable PhD research skill |
|---|---|---|---|---|---|---|---|---|---|---|
| Preflight | preflight.md | Environment setup fails silently, blocks scientific work | Claude Code as setup assistant + readiness audit; human approval loop | Claude Code 101; Introduction to Claude Cowork; AI Fluency: Framework & Foundations | Reproducible computational environment | Ask for checklist + explicit outputs + recovery plan | Run one natural-language preflight prompt to configure and verify workstation | outputs/status/preflight_complete.json; reports/preflight_report.md | Adapt checklist to own future project | Use Claude to audit any research environment before beginning a project |
| Mission 0 | stage_00 | Environment chaos; unclear when "ready" means ready; hidden dependencies | CLAUDE.md as project memory; explicit output contract; approval loop | Claude Code 101; Introduction to Claude Cowork; Claude Code in Action | Research environment readiness and reproducibility | Explicit task + expected output + exact file paths | Ask Claude to inspect project, verify dependencies, create directories, write machine-checkable artifacts | reports/env_check.md; outputs/status/stage_00_bootstrap.json | Hardware audit (GPU, RAM, disk) | Before doing science, make the research environment auditable |
| Mission 1 | stage_01 | Students jump to modeling before understanding data provenance, modality, and label quality | Claude as data steward; file inspection before action; tools/resources distinction | Claude 101; Claude Code in Action; AI Fluency: Framework & Foundations | Data provenance, MRI modality awareness, data integrity | Context before action; verify before modeling | Ask Claude to inspect the dataset, explain what exists, verify sample data, record data state | data/sample/; outputs/status/stage_01_fetch_sample.json; reports/data_notes.md | Visualize slice distribution, per-patient statistics | Use Claude to create a data receipt / data integrity report before any analysis |
| Mission 2 | stage_02 + stage_03 | Students start with complex models without a reference; evaluation criteria undefined | Claude as builder + evaluator; code generation with output contracts; evaluation-driven prompting | Claude Code in Action; Claude Code 101; AI Capabilities and Limitations | Baseline segmentation; Dice score; first measurable model behavior | Define success criteria before optimizing; build simplest measurable baseline first | Ask Claude to create visualization, train baseline, compute Dice, save metrics and figures, explain result | outputs/figures/sample_overlay.png; outputs/figures/loss_curve.png; outputs/metrics/val_metrics.json; reports/train_notes.md | Explore threshold variation without overwriting required artifacts | Use Claude to turn a vague modeling task into a reproducible baseline experiment |
| Mission 3 | stage_04 | Evaluation treated as a single number; failure modes invisible; no visual inspection | Claude as visual debugging assistant + hypothesis generator; critique prompting | AI Fluency for students; AI Capabilities and Limitations; Claude Code in Action | Best/worst cases; false positives/negatives; error maps | Observation → evidence → hypothesis | Ask Claude to identify best and worst examples, generate error maps, explain visible failure modes, write failure hypothesis | outputs/figures/error_analysis_best.png; outputs/figures/error_analysis_worst.png; reports/error_analysis.md | Dice distribution histogram; cluster analysis of failures | Use Claude to move from "the metric is low" to "here is the failure mechanism I can investigate" |
| Mission 4 | stage_05 | Students tweak many things at once; cannot attribute improvement to a cause | Claude as data scientist / algorithm engineer; controlled comparison; prompt-guided iteration | Claude Code in Action; Introduction to agent skills; AI Fluency: Framework & Foundations | Controlled improvement; preprocessing; postprocessing; model comparison | Change one thing; preserve baseline; compare with output contract | Ask Claude to propose one controlled improvement, preserve artifact paths, compare metrics, explain whether it truly improved | outputs/metrics/model_swap_comparison.json; outputs/figures/model_swap_comparison.png; reports/model_swap.md | Second improvement strategy in bonus outputs | Use Claude to run a controlled experiment rather than an uncontrolled coding tweak |
| Mission 5 | stage_06 + stage_07 | Pilot results not converted into a real research question or next-study design | Role switching: reviewer, supervisor, clinical collaborator; critique prompting; subagents as conceptual extension | AI Fluency for students; Introduction to subagents; Teaching AI Fluency; AI Capabilities and Limitations | From pilot result to study design: weakness, research question, method, success criterion, risk, fallback | Switch Claude's role from builder to reviewer before asking for next study | Ask Claude to attack the Day 1 experiment, identify strongest weakness, design structured next study | reports/challenge_plan.md; reports/day1_summary.md; outputs/status/stage_07_challenge_plan.json | Role-switching exercise: algorithm designer vs clinical safety reviewer perspectives | Use Claude as a skeptical reviewer or supervisor to improve research design |
| Mission 6 | stage_09 | Students overstate prototype capabilities; fail to communicate limitations to clinicians | Claude as clinical translator; audience-aware writing; honesty constraints; limitation-first reporting | Claude 101; AI Fluency: Framework & Foundations; AI Capabilities and Limitations | Clinical deployment gap; validation; oversight; communication; responsibility | Audience + honesty constraint + limitation-first output | Ask Claude to write translation memo for clinical collaborator, grounded in actual artifacts and metrics | reports/translation_memo.md; outputs/status/stage_09_translation_memo.json | Three-audience memo (radiologist, AI researcher, hospital administrator) | Use Claude to communicate technical research responsibly without overstating clinical readiness |

---

## 9. Execution Sequence

1. **Phase 0 (complete):** Inspect all repos, create this plan
2. **Phase 1:** Create curriculum map in course site (docs/curriculum/)
3. **Phase 2:** Upgrade student-classroom-repo (README, ASSIGNMENT, CLAUDE.md, prompts, dashboard)
4. **Phase 3:** Upgrade student-preflight-repo (README, ASSIGNMENT, CLAUDE.md, prompt)
5. **Phase 4:** Upgrade course site (new IA, new nav, new pages)
6. **Phase 5:** Upgrade teacher-ta-repo (docs/instructor/ with 5 new files)
7. **Phase 6:** Align missions across repos (done via Phases 2-5)
8. **Phase 7:** Add optional exploration infrastructure (prompt_trace dirs, dashboard cards)
9. **Phase 8:** Test all repos
10. **Phase 9:** Final report

**NOTE:** Phases 2-7 will be executed in parallel where safe (separate repos = no conflicts).
Tests must pass at end of Phase 8 before any commit is made.
