# L0 — Agentic Clinical Research Studio

**Lab:** L0 — Agentic Clinical Research Studio
**Day:** Day 1 — Orientation
**Estimated Time:** 60–90 minutes
**Core Concept:** Workspace setup, CLAUDE.md as project memory, prompt → artifact → commit loop

---

## 1. Overview

This lab establishes the foundational infrastructure every subsequent module depends on. Before a clinical researcher can delegate meaningful work to an AI agent, that agent must understand the research context — the study population, data conventions, regulatory constraints, and the investigator's scientific priorities. This lab introduces CLAUDE.md as a living project-memory document: a structured brief that persists across agent sessions and eliminates the cognitive overhead of re-orienting the model each time a new task begins. Students configure their workspace, author their first CLAUDE.md, and execute the core loop that anchors the entire course: issue a research prompt, produce a documented artifact, and commit both the artifact and any updated context to version control. Researchers who complete this lab leave with a reproducible studio environment and a mental model for treating AI-assisted research as a traceable, auditable workflow rather than an ad hoc chat session.

---

## 2. Learning Objectives

- Configure a reproducible agentic research workspace with standardized directory conventions and a version-controlled project brief.
- Author a CLAUDE.md that encodes study context, data provenance, analytical constraints, and communication preferences in a form an AI agent can use across sessions.
- Execute the prompt → artifact → commit loop and articulate why each step serves the goals of reproducible clinical research.
- Distinguish between ephemeral chat interactions and persistent, auditable agent workflows, and explain why the distinction matters for research integrity.

---

## 3. Clinical Bottleneck

Clinical researchers working with AI assistants face a recurring problem: every new conversation begins from zero. The model has no memory of the study design, the cohort exclusion criteria, the variable naming conventions, or the interpretive cautions the investigator spent months learning. This forces researchers to either paste long context blocks into every prompt — an error-prone and time-consuming workaround — or accept that the agent will produce outputs that are superficially plausible but scientifically misaligned with the actual study. The consequence is wasted iteration cycles, inconsistent outputs across lab members, and artifacts that cannot be traced back to a documented analytical rationale. Without a shared, version-controlled context layer, AI assistance in clinical research remains a convenience tool rather than a reliable methodological partner.

---

## 4. Agentic Concept: CLAUDE.md as Project Memory and the Prompt → Artifact → Commit Loop

An agentic workflow differs from a conversational one in three ways: it is stateful, traceable, and composable. CLAUDE.md is the mechanism that makes it stateful. Rather than a README for human readers, CLAUDE.md is a machine-readable brief that the agent loads at the start of every session. A well-authored CLAUDE.md encodes the study's scientific purpose, the structure and provenance of its data, the constraints that govern valid analysis (ethical, regulatory, statistical), and the investigator's preferences for output format and communication style. When the agent reads this document before acting, it operates within the boundaries of the actual research context rather than a generic prior.

The prompt → artifact → commit loop is the unit of traceable work in an agentic research studio. A prompt is a scoped research request — not a casual question, but a structured directive that specifies the input, the expected output type, and the success criterion. An artifact is a named, versioned output file: a report, a JSON status object, a processed dataset, or a figure. Committing the artifact to version control alongside any updates to CLAUDE.md closes the loop: a future investigator — or the same investigator six months later — can reconstruct exactly what question was asked, what context the agent was operating in, and what it produced.

This loop also enforces a discipline that benefits the research process independent of AI: it requires researchers to specify their questions precisely before they look at results, and it ensures that outputs are documented rather than lost in a chat transcript. The loop is intentionally minimal in this first lab so that students internalize it as a reflex before the complexity of later modules is introduced.

---

## 5. Before / After

**Before applying the concept:**

> "Can you help me analyze my clinical trial data? I have a CSV with patient outcomes and I want to see if the treatment worked."

This prompt provides no study context, no variable definitions, no population constraints, and no output specification. The agent must guess at every decision point. The result is unlikely to be scientifically valid and cannot be reproduced.

**After applying the concept:**

> "Using the study context in CLAUDE.md — specifically the CABG cohort definition, the primary endpoint of 30-day MACE, and the pre-specified covariate set — generate a structured analysis plan for the primary endpoint comparison. Write the plan to reports/lab_00_agentic_studio.md and update outputs/status/lab_00_agentic_studio.json with today's status. Commit both files with a message describing what was specified."

This prompt is scoped, context-anchored, output-specified, and traceable. The agent has everything it needs to act without guessing, and the output is immediately auditable.

---

## 6. Assignment

**Step 1 — Initialize the workspace.**
Verify the directory structure under `modules/L0_agentic_studio/` matches the course conventions: `outputs/status/`, `reports/`, and `data/` subdirectories should exist. Create any that are missing.

**Step 2 — Author CLAUDE.md.**
Open `CLAUDE.md` at the repository root. Following the provided template, complete all required sections: study title and scientific question, cohort definition and key exclusion criteria, data dictionary summary (at minimum the primary endpoint variable and its coding), analytical constraints (e.g., pre-specified covariates, imputation rules), regulatory or ethical notes, and output format preferences. Write in precise, declarative language — the document is instructions to an agent, not a narrative for a grant committee.

**Step 3 — Execute the first prompt → artifact loop.**
Issue the following prompt to Claude Code: "Read CLAUDE.md and produce a one-page research studio orientation report for this project. Save it to `reports/lab_00_agentic_studio.md`. Include: study context summary, the three most important analytical constraints, and a recommended workflow for the next five lab sessions."

**Step 4 — Generate the status artifact.**
Issue a second prompt: "Write a JSON status file to `outputs/status/lab_00_agentic_studio.json`. Include keys: `lab`, `status`, `timestamp`, `study_title`, `context_loaded` (boolean), and `notes`."

**Step 5 — Commit the loop.**
Stage and commit `CLAUDE.md`, `reports/lab_00_agentic_studio.md`, and `outputs/status/lab_00_agentic_studio.json` with a descriptive commit message. The commit message should state what context was established and what artifacts were produced.

**Step 6 — Peer review.**
Exchange your CLAUDE.md with a lab partner. Evaluate whether a new investigator could orient an AI agent to your study using only that document. Note at least one gap and revise before the debrief.

---

## 7. Required Artifacts

| File | Location | Expected Content |
|------|----------|-----------------|
| `lab_00_agentic_studio.json` | `outputs/status/` | Valid JSON with keys: `lab`, `status`, `timestamp`, `study_title`, `context_loaded`, `notes` |
| `lab_00_agentic_studio.md` | `reports/` | One-page orientation report: study context summary, top three analytical constraints, recommended workflow for subsequent labs |
| `CLAUDE.md` | Repository root | Completed project brief with all required sections populated; version-controlled |

---

## 8. Reflection Questions

1. What information did you find hardest to specify precisely when writing CLAUDE.md, and what does that difficulty reveal about your current understanding of your own study?

2. Compare the two prompts in the Before/After section. What specific elements of the "after" prompt do the work of preventing scientific errors — and could any of those elements be moved into CLAUDE.md so they do not need to be repeated in every future prompt?

3. A colleague argues that committing agent outputs to version control is unnecessary overhead because "the model can just regenerate them." Construct a counterargument grounded in research reproducibility standards.

---

## 9. Success Criteria

Excellent work in this lab demonstrates the following:

- CLAUDE.md is specific enough that a colleague unfamiliar with the study could use it to orient an AI agent without asking the author any clarifying questions.
- The orientation report in `reports/lab_00_agentic_studio.md` reflects the actual study context from CLAUDE.md — not generic AI boilerplate — and the three analytical constraints listed are scientifically accurate and operationally useful.
- The status JSON is valid, correctly typed, and timestamped; the `context_loaded` field is `true` and can be verified by inspecting the commit that precedes it.
- The commit message is precise: it names what context was established, not merely that "files were added."
- The student can explain, without reference to notes, why each element of the prompt → artifact → commit loop exists and what breaks if any element is omitted.

---

## 10. Instructor Notes

**Facilitation priority.** The single most important outcome of this lab is not the artifacts — it is the moment students realize that writing CLAUDE.md is harder than they expected. That difficulty is the point. Resist the urge to provide a fill-in-the-blank template that removes the friction; the friction is diagnostic.

**Common failure modes.** Students frequently write CLAUDE.md in the style of a grant abstract — narrative, hedged, and ambiguous. The agent cannot act on "a diverse patient population with complex comorbidities." Push students to replace every vague phrase with a specific, testable criterion. A useful test: can a research coordinator apply the criterion to a single patient record without judgment calls?

**The commit step.** Many students skip or rush the commit. Emphasize that the commit hash is what makes an artifact auditable. If a result cannot be traced to a specific version of CLAUDE.md, it cannot be reproduced. This is a research integrity issue, not a software engineering preference.

**Peer review pairing.** Pair students across study domains when possible. A cardiologist reviewing an oncologist's CLAUDE.md will ask naive questions that reveal exactly the assumptions the author forgot to document.

**Timing note.** Students with prior version control experience will finish Steps 1–4 in under 30 minutes and spend the remaining time deepening CLAUDE.md. Students new to git should be paired with a peer for Step 5 — the commit mechanics should not consume the lab's cognitive budget.

**Connection to later modules.** Every subsequent lab imports CLAUDE.md as its starting context. Students who produce a weak CLAUDE.md in L0 will accumulate compounding errors across the course. Consider a brief whole-group share-out at the end of this lab where two or three students read their cohort definition aloud for critique.
