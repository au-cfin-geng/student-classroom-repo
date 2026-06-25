# L3 — Literature Search Skills

**Course:** Agentic Clinical Research Studio
**Day:** Day 3
**Estimated Time:** 90 minutes
**Core Concept:** Claude Skills, PICO Decomposition, Human Approval Checkpoints, Confidence Marking

---

## Overview

Systematic literature review is the foundation of evidence-based medicine, yet it remains one of the most time-consuming and inconsistently executed steps in clinical research. Researchers routinely spend days formulating search strategies, iterating across databases, and manually sorting hundreds of abstracts before reaching a working evidence base. Lab L3 introduces a reusable Claude Skill that operationalizes the PICO framework (Population, Intervention, Comparator, Outcome) to decompose a clinical research question into a structured, reproducible search strategy. Crucially, the lab embeds a human approval checkpoint between question decomposition and search execution, and requires the agent to attach explicit confidence markers to every synthesized claim. This lab exists because the literature search step is where research quality is most frequently degraded: vague questions produce vague searches, unreviewed search strings miss key evidence, and unqualified claims obscure uncertainty from downstream readers.

---

## Learning Objectives

- Decompose an open-ended clinical research question into a validated PICO structure using a reusable Claude Skill.
- Design and implement a human approval checkpoint that halts agentic execution until a researcher confirms the search plan before any retrieval begins.
- Apply confidence markers (High / Moderate / Low / Insufficient Evidence) to synthesized literature claims, distinguishing what the evidence supports from what remains uncertain.
- Evaluate the tradeoffs between search breadth and search precision, and articulate how PICO boundaries shape the evidence base a downstream agent will see.

---

## Clinical Bottleneck

Clinical researchers frequently begin a literature search with a broad, narrative question — "What is the best treatment for heart failure?" — and allow an AI assistant to interpret that question however it chooses. The result is either a search so broad that it returns thousands of irrelevant abstracts, or one so narrow that it misses pivotal trials. Neither outcome serves the researcher. The deeper problem is that the search strategy itself is invisible: the agent performs retrieval, returns results, and the researcher has no clear record of what question was actually operationalized. When the evidence base is later questioned during peer review, there is no audit trail. This lab addresses that bottleneck by making the question-to-strategy translation explicit, reviewable, and human-approved before any retrieval occurs.

---

## Agentic Concept

### Claude Skills

A Claude Skill is a reusable, self-contained prompt module that encapsulates a specific research capability. Rather than embedding all instructions in a single monolithic prompt, Skills are authored once and invoked by reference, promoting consistency across projects and researchers. The `literature_search_skill.md` artifact authored in this lab is a Skill: it defines inputs, expected reasoning steps, output format, and escalation criteria. Skills can be composed — a later lab will chain this Skill with a data extraction Skill — so authoring them with clean interfaces now reduces rework later.

### PICO Decomposition

PICO is the evidence-based medicine standard for structuring clinical questions. The four components are:

- **P — Population:** Who is the patient group? What are the inclusion criteria (age, diagnosis, disease stage, comorbidities)?
- **I — Intervention:** What exposure, treatment, or diagnostic test is being examined?
- **C — Comparator:** What is the control condition — placebo, standard of care, watchful waiting, or an alternative intervention?
- **O — Outcome:** What endpoints matter — mortality, hospital readmission, quality-of-life score, biomarker level?

A well-formed PICO transforms an ambiguous narrative question into a precise Boolean search strategy. The agent's job in this lab is to surface hidden assumptions in the researcher's question and propose PICO boundaries before proceeding. The researcher's job is to review and approve those boundaries.

### Human Approval Checkpoints

An approval checkpoint is a deliberate pause in agentic execution where the workflow cannot proceed until a human confirms the agent's proposed plan. In this lab, the checkpoint is placed after PICO decomposition and before any search string generation or retrieval. This placement reflects a key principle: errors in research design compound downstream. A five-minute review of the PICO structure is far cheaper than discovering three days later that the search excluded a critical comparator. The checkpoint output is recorded in the status JSON artifact so there is a timestamped record of what was approved and by whom.

### Confidence Marking

When the agent synthesizes findings from retrieved abstracts, every claim must carry an explicit confidence level. The four levels used in this course are:

| Level | Meaning |
|---|---|
| **High** | Multiple consistent RCTs or systematic reviews; low risk of bias |
| **Moderate** | Some consistent evidence; limitations in study design or sample size |
| **Low** | Limited, inconsistent, or indirect evidence |
| **Insufficient** | Evidence base too small or heterogeneous to draw conclusions |

Confidence marking is not optional annotation — it is a contractual statement to downstream readers and agents about how much weight to place on each claim. In later labs, a risk-of-bias agent will audit these labels.

---

## Before / After

### Before — Unstructured Prompt

> "Search the literature on heart failure treatments and summarize what you find."

This prompt offers no PICO boundaries, no approval step, and no instruction to qualify uncertainty. The agent will produce a summary, but it will be impossible to audit, replicate, or defend.

### After — Skill-Driven Prompt with Checkpoint

> "Using the `literature_search_skill`, decompose the following clinical question into PICO components and propose a search strategy. Pause and present the PICO structure for my approval before generating any search strings or retrieving abstracts. Attach a confidence level (High / Moderate / Low / Insufficient Evidence) to every synthesized claim in the final report.
>
> Clinical question: In adult patients hospitalized for acute decompensated heart failure with reduced ejection fraction, does early initiation of SGLT2 inhibitors prior to discharge, compared with standard guideline-directed medical therapy alone, reduce 90-day all-cause rehospitalization?"

---

## Assignment

1. **Read the Skill template.** Open `skills/literature_search_skill.md` and review the input schema, reasoning steps, and output format defined there. Note any fields you do not understand and write a one-sentence clarification for each in your lab report.

2. **Formulate your clinical question.** Select a clinical research question in your domain. Write it as a single sentence in natural language before any PICO decomposition. Record this raw question at the top of `reports/lab_03_literature_search_skill.md`.

3. **Run PICO decomposition.** Invoke the `literature_search_skill` with your raw question. The agent will return a structured PICO breakdown and a proposed search strategy. Do not proceed to the next step until you have received this output.

4. **Human approval checkpoint.** Review the agent's proposed PICO structure carefully. Ask yourself: Is the Population too broad or too narrow? Is the Comparator clearly specified? Are the Outcomes the ones that matter clinically? Revise the PICO if needed, then record your approval decision and any modifications in `outputs/status/lab_03_literature_search_skill.json` under the `approval` key.

5. **Execute the search.** Once the PICO is approved, instruct the agent to generate search strings and retrieve abstracts. The Skill will return a list of candidate references with brief relevance assessments.

6. **Synthesize with confidence markers.** Direct the agent to synthesize the retrieved evidence into a structured summary. Every claim must carry an explicit confidence level. The agent should also flag any PICO component for which evidence was insufficient.

7. **Write your lab report.** Complete `reports/lab_03_literature_search_skill.md` with: your raw question, the approved PICO, the search strategy, the synthesized evidence summary with confidence markers, and a 200-word reflection on what the approval checkpoint revealed that you would not have noticed otherwise.

---

## Required Artifacts

| File | Expected Content |
|---|---|
| `reports/lab_03_literature_search_skill.md` | Full lab report: raw question, PICO breakdown, approved search strategy, synthesized evidence with confidence markers, reflection |
| `skills/literature_search_skill.md` | Completed Skill definition: input schema, reasoning steps, output format, escalation criteria |
| `outputs/status/lab_03_literature_search_skill.json` | Machine-readable status record: PICO components, approval timestamp, approver, any modifications, confidence level distribution |

---

## Reflection Questions

1. At the approval checkpoint, did the agent's PICO decomposition match your intent? If it diverged, what assumption did the agent make that you had left implicit in your original question?

2. How did the confidence markers change the way you read the synthesized evidence? Were there claims you would have treated as settled that turned out to carry only Low or Insufficient confidence?

3. If this literature search Skill were handed to a colleague who had not read your original question, would the PICO structure and search strategy be sufficient for them to reproduce your search independently? What, if anything, would be lost?

---

## Success Criteria

Excellent work in this lab demonstrates the following:

- The PICO structure is clinically precise: Population has explicit inclusion criteria, Intervention and Comparator are distinguishable, and Outcomes are measurable endpoints rather than vague goals.
- The approval checkpoint record in the status JSON shows genuine engagement — either a modification to the agent's initial PICO, or a written justification for why no modification was needed.
- Every synthesized claim in the lab report carries a confidence level, and the assigned level is defensible given the evidence cited.
- The `literature_search_skill.md` Skill is written at a level of abstraction that would allow a different clinical question to be run through it without modification.
- The lab report reflection identifies at least one specific assumption or ambiguity that the PICO decomposition process surfaced.

---

## Instructor Notes

**Common failure mode — skipping the checkpoint:** Students who are comfortable with AI tools often instruct the agent to perform decomposition and retrieval in a single step. When this happens, there is no externalized PICO structure for the student to review. Remind students that the checkpoint is not a UX convenience — it is the mechanism by which the researcher takes intellectual ownership of the search strategy.

**PICO scope calibration:** Students in clinical specialties with sparse literature (rare diseases, pediatric subgroups) will encounter the Insufficient Evidence confidence level frequently. Frame this as a valid and important finding, not a failure. A clearly documented evidence gap is itself a contribution.

**Skill authoring quality:** The `literature_search_skill.md` artifact is graded on clarity of the input schema and escalation criteria, not just on whether the agent produced a search. A Skill that works once but cannot be reused or handed to a colleague does not meet the course standard.

**Facilitation tip — live demo:** If running this lab in a synchronous session, consider live-demoing the approval checkpoint moment: show the class the raw agent PICO output, solicit suggested modifications from the room, and only then approve and proceed. This makes the human-in-the-loop principle tangible rather than abstract.

**Cross-lab dependencies:** The `literature_search_skill.md` Skill authored here will be invoked again in Lab L6 (Evidence Synthesis Pipeline). Students who produce a poorly scoped Skill in L3 will encounter compounding problems in L6. Instructors may choose to review Skill files at the end of L3 before students proceed.
