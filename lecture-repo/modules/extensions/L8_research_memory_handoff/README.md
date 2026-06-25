# L8 — Research Memory & Handoff (Extension)

**Concept:** CLAUDE.md as evolving memory, decision logs, project handoff documents  
**Time:** 45 min · Day 2 (Extension)  
**Prompt file:** `prompts/stage_10_research_memory.md`

---

## Overview

Every clinical AI research project accumulates invisible knowledge: why a preprocessing step was changed, which failure mode was deprioritized and why, what a collaborator said in a meeting that shaped a design decision, what the next investigator needs to know before touching the pipeline. This knowledge lives in the heads of the people who built the system — and it evaporates when they leave the project.

CLAUDE.md is the mechanism by which an agentic research environment holds its own memory. A well-maintained CLAUDE.md is not documentation in the traditional sense. It is a living decision log: a structured, evolving record of the reasoning behind the current state of the repository. When a new investigator — human or AI — enters the project, CLAUDE.md is what tells them what has been tried, what was decided, and what the project is currently committed to. Without it, every new session restarts from scratch. With it, the agent picks up where the last session ended.

This lab teaches students to treat CLAUDE.md as a research instrument — not a technical configuration file, but an epistemological record of how this investigation has evolved.

---

## Learning Objectives

- Understand why agentic research sessions lose context between runs and how CLAUDE.md addresses this structural problem.
- Write a decision log that records not just what was done but why — distinguishing rationale from implementation detail.
- Produce a project handoff document that allows a new investigator to resume work without losing accumulated research knowledge.
- Recognize the difference between a CLAUDE.md that serves as a research memory and one that merely describes the file structure.

---

## Clinical Bottleneck

Clinical AI research projects fail at handoff. A postdoc who spent six months developing a lesion detection pipeline leaves the group. The pipeline exists in the repository. The results exist in the reports. But the reasoning does not: why was the intensity threshold set to 0.35, not 0.40? Why was the low-contrast failure mode deprioritized? What did the radiologist collaborator say about the edge cases that shaped the final evaluation protocol? What is the next experiment that the departing investigator would have run?

The new investigator inherits code and artifacts but not judgment. They must rediscover decisions that were already made — often by making the same mistakes. In a funded research program, this is a significant cost. In a clinical AI study with a regulatory horizon, it can mean months of delay.

The same problem occurs within a single investigator's work when using agentic AI tools. Each Claude Code session begins without memory of prior sessions. Without an explicit handoff artifact — a structured record of where the project stands and why — the AI assistant is as uninformed as the new postdoc. It will ask questions that were already answered, make decisions that were already made, and miss the accumulated judgment that makes the project coherent.

---

## Agentic Concept

CLAUDE.md, in its fullest form, is a **project state document** — a structured record that allows an agentic session to resume a research project with accumulated context rather than starting from a blank slate.

A minimal CLAUDE.md tells an agent what files to avoid touching and where outputs go. A research-grade CLAUDE.md does something more demanding: it records the current state of the investigation, the decisions that have been made and the reasoning behind them, the open questions the project is committed to answering, and the constraints that govern future work.

Three distinct document types serve this function at different granularities:

**The decision log** records individual choices with their rationale. "Changed preprocessing threshold from 0.40 to 0.35 on 2026-06-15: improved sensitivity on low-contrast cases by 4 Dice points at the cost of 2 points specificity on high-contrast cases. Accepted this tradeoff based on the radiologist's judgment that false negatives are the more dangerous error in this clinical context." This is not a commit message. It is a scientific record.

**The evolving CLAUDE.md** incorporates those decisions into the project's ongoing instructions. The agent does not have to re-read the decision log every session; the current CLAUDE.md already reflects what has been decided. When a decision is made, CLAUDE.md is updated to encode its implications as standing instructions.

**The handoff document** is a point-in-time synthesis produced when the project is being transferred — to a new investigator, a new collaborator, or the next phase of the study. It summarizes the current state of the investigation, the most important decisions and their rationale, what remains open, and what the next investigator should do first.

The relationship between these three artifacts mirrors the relationship between a lab notebook (decision log), a protocol (CLAUDE.md), and an onboarding brief (handoff document) in a conventional wet lab. The innovation in agentic research is that the AI assistant reads all three — and can both update them and act on them.

---

## Before / After

**Before:**
```
Continue working on the brain tumour segmentation project.
```

A new Claude Code session receives this prompt. It reads the repository, finds the scripts, inspects the outputs — and asks: "What would you like me to do?" It has no memory of what was decided last session, no record of why the current configuration exists, and no awareness of the open questions the investigation is committed to answering. Every session begins from scratch.

**After:**
```
You are a clinical AI investigator resuming a brain tumour segmentation project.

Read CLAUDE.md before taking any action. CLAUDE.md is the authoritative record of:
  - The current state of the investigation
  - Decisions that have been made and cannot be revisited without justification
  - Open questions the project is committed to answering
  - The next planned experiment

After reading CLAUDE.md, read reports/decision_log.md for the detailed rationale
behind each major decision.

Then:
1. Confirm the current project state in plain research language
2. Identify the next planned experiment from CLAUDE.md
3. State what you would do next, and why

Do not modify any files until the investigator approves your plan.
Write your session opening summary to reports/lab_08_research_memory_handoff.md.
Write session status to outputs/status/lab_08_research_memory_handoff.json.
```

The second prompt treats CLAUDE.md as a research instrument. The session opens with orientation rather than confusion. The agent confirms what it knows, identifies the next step, and waits for approval. The accumulated judgment of prior sessions is preserved and acted on.

---

## Assignment

1. **Read the current CLAUDE.md.** Before writing anything, read the project's CLAUDE.md and assess it honestly: does it record decisions and their rationale, or does it only describe file structure and naming conventions? Note what is missing.

2. **Write a decision log entry.** Choose one decision that was made during your work this week — a preprocessing choice, a model selection, a metric threshold, a tradeoff between sensitivity and specificity. Write a decision log entry that records: what was decided, when, what the alternatives were, and the rationale for the choice made. Add this entry to `reports/decision_log.md` (create the file if it does not exist).

3. **Update CLAUDE.md to reflect the decision.** Find the section of CLAUDE.md most relevant to your decision. Update it to encode the decision as a standing instruction — not as a historical note, but as current guidance that will govern future sessions. If no relevant section exists, add one.

4. **Write a project handoff document.** Imagine you are handing this project to a new investigator who has never seen the repository. Write a structured handoff document that covers:
   - The research question the project is answering
   - The current state of the investigation (what has been done, what the results show)
   - The two or three most important decisions made and why they were made
   - The open questions that remain
   - What the new investigator should do in their first session
   
   Write this document as the opening section of `reports/lab_08_research_memory_handoff.md`.

5. **Run the resumption prompt.** Use the "After" prompt above (adapted to your project state) to open a new Claude Code session. Observe whether the session opens with correct orientation. Note any gaps where the agent misunderstood or missed a key decision.

6. **Close the loop.** Add a brief reflection at the end of `reports/lab_08_research_memory_handoff.md`: what did the agent get right, what did it miss, and what would you add to CLAUDE.md to close those gaps?

---

## Required Artifacts

| Path | Expected Content |
|------|-----------------|
| `reports/lab_08_research_memory_handoff.md` | Handoff document (project state, key decisions, open questions, next steps) followed by session resumption observation and reflection. Approximately 600–900 words. |
| `outputs/status/lab_08_research_memory_handoff.json` | `{"status": "ok", "decisions_logged": <integer>, "handoff_sections": ["project_state", "key_decisions", "open_questions", "next_steps"]}` |

---

## Reflection Questions

1. When you ran the resumption prompt, what did the agent know and what did it miss? Trace the gap to a specific absence in CLAUDE.md or the decision log — what text, if added, would have closed it?

2. A decision log records why a choice was made, not just what was chosen. What is the research cost of having records of what without records of why? Give a concrete example from clinical AI research where missing rationale caused a downstream problem.

3. CLAUDE.md is described in this lab as an "epistemological record." What distinguishes an epistemological record from a technical specification? What would a CLAUDE.md look like that was technically complete but epistemologically empty?

---

## Success Criteria

Excellent work in this lab looks like the following:

- The decision log entry records a real decision with genuine rationale — not a description of what the code does, but an explanation of why the choice was made over its alternatives.
- The updated CLAUDE.md section reads as standing guidance, not as retrospective documentation. A new investigator reading it would know what the project is committed to, not just what happened.
- The handoff document is oriented toward the new investigator's first session: it tells them what they need to know before they touch anything, not just what exists in the repository.
- The session resumption observation is specific: the student can point to a sentence in the agent's session-opening summary and say whether it was correct, and trace any error to a specific gap in the written record.
- The reflection question answers demonstrate that the student understands the distinction between memory as a technical artifact (file contents) and memory as a research instrument (the accumulated judgment those contents encode).

---

## Instructor Notes

**The common failure mode in this lab** is students writing a CLAUDE.md update that describes rather than prescribes. "The preprocessing threshold was changed to 0.35 because it improved performance on low-contrast cases" is a description. "Use preprocessing threshold 0.35. Do not change this without consulting the error analysis in reports/error_analysis.md, which establishes the tradeoff that justified this value" is a prescription. Push students toward the latter form. The test is: if a new agent reads this, will it know what to do, or will it only know what happened?

**On decision log writing**: Most students will write entries that are too thin. Encourage them to answer: what were the alternatives? what evidence was used to choose? what would justify revisiting this decision in the future? A good decision log entry is the answer to the question a new investigator would ask six months from now.

**On the resumption exercise**: Encourage students to actually open a new terminal session (or use Claude Code's `/clear` command) before running the resumption prompt, so they experience the blank-slate problem directly rather than in a session that already has the context loaded in its window.

**On the epistemological question**: This is a deliberately hard reflection question. Students who answer it well will distinguish between a CLAUDE.md that constrains behavior (technical specification) and one that transmits judgment (epistemological record). The core idea: a technically complete CLAUDE.md tells the agent what files to write to; an epistemologically complete one tells the agent what the project is for, what it has learned, and what it cannot do without justification. The second is the harder document to write — and the more valuable one.

**Extension for advanced students**: Have them write a CLAUDE.md for a hypothetical project they know well from prior work (thesis chapter, published paper, grant project) and ask: if an AI agent read only this document, could it reason about this project the way you can? What is missing? This often produces the clearest articulation of what research memory actually contains.
