# Capstone Mini-Project

**Lab:** Capstone Mini-Project — Independent Agentic Research Workflow
**Core Concept:** Integration of at least three course concepts into an independent agentic research workflow
**Estimated Time:** 3–4 hours
**Course Position:** Final integrative lab, following completion of all core modules (L0–L5)

---

## Overview

This lab is the culminating experience of the Agentic Clinical Research Studio. It does not introduce new tools or prompt patterns. Instead, it requires students to exercise the full set of skills acquired across the course — operational definitions, evidence-first diagnosis, single-variable experimental control, adversarial review, and honest clinical translation — as a coordinated whole, applied to a research question of their own choosing.

The lab exists because integration is a distinct skill from acquisition. Students who have mastered each prior module in isolation frequently struggle to sequence the correct pattern at the correct decision point when no scaffolding tells them which one to use. The capstone creates exactly that condition. A student who can write a good failure analysis prompt when the lab instructions say "now write a failure analysis" has demonstrated comprehension. A student who knows to write the failure analysis before writing the translation memo — without being prompted — has demonstrated judgment. The capstone is a test of judgment. The instructor's role is not to guide students through the sequence but to watch how they navigate it and use that observation as diagnostic evidence of where their understanding is still shallow.

---

## Learning Objectives

- Formulate a specific, falsifiable clinical AI research question and commit it to writing before running any experiments.
- Select and sequence prompt strategies from prior modules — operational definitions, diagnostic evidence-first prompting, single-variable control, adversarial review — in response to the demands of an original investigation rather than prescriptive lab instructions.
- Produce an honest failure analysis that distinguishes between what the data shows, what the method cannot resolve, and what would constitute a genuine falsifying result.
- Communicate findings to a clinical audience by separating the claim supported by evidence from the inference that requires further investigation.

---

## Clinical Bottleneck

Small-scale AI validation studies in clinical research — the kind conducted by radiology residents, oncology fellows, and clinical informatics researchers who have learned some ML — routinely conflate exploration with experiment. The research question is written after the results are known. Multiple variables are changed between runs. The failure analysis is a paragraph that says "performance was lower on difficult cases." The clinical implication section reads as though the Dice coefficient measured on 10 slices constitutes evidence of deployment readiness.

This pattern is not produced by bad intentions. It is produced by the absence of a structured research workflow and the absence of a collaborator who enforces scientific discipline at each decision point. The capstone addresses this bottleneck by requiring students to implement, in sequence and under their own direction, the exact workflow that guards against each of these failure modes: a pre-registered question, an experimental log with timestamps, a controlled single-variable design, a failure analysis document, a translation memo, and a clinical presentation to an audience that has no obligation to be impressed by effort.

---

## Agentic Concept

The concept under examination in this lab is **workflow composition under self-direction**: the ability to deploy an agentic research assistant not as an oracle that produces answers, but as a structured collaborator whose role at each stage is defined by the investigator.

In prior modules, students learned individual prompt strategies in prescribed contexts. Here the prompting scaffolding is removed. Students must recognize which research phase they are in — question formulation, baseline characterization, experimental execution, failure diagnosis, translation — and choose the appropriate prompt pattern for that phase. This requires understanding the workflow as a whole, not as a sequence of isolated exercises.

The agentic dimension is not simply "use Claude to help." It is the specific discipline of assigning Claude a bounded, reviewable role at each stage and maintaining the investigator's authority over the questions that require scientific judgment: whether the hypothesis is correct, whether the evidence is sufficient, whether the clinical claim is defensible. A student who asks Claude to evaluate their findings and accepts the output without interrogating its reasoning has not demonstrated agentic research competence — they have demonstrated prompt execution. The distinction is observable in the artifacts: a student who uses Claude as a genuine collaborator will have artifacts that show iteration, disagreement, and revision; a student who uses Claude as a generator will have artifacts that are polished on first attempt and contain no dead ends.

The capstone also tests the student's ability to operate the multi-role prompt model developed across the course. Different phases require different Claude roles: at the question formulation stage, Claude should act as a study design critic; during data analysis, as a statistical reviewer; during failure analysis, as an adversarial interpreter; during translation, as a clinical communication editor. Students who assign Claude the same undifferentiated "assistant" role across all phases will produce work that is uniformly adequate and nowhere excellent.

---

## Before / After

**Before — undirected prompt:**

> "Help me analyze my brain tumor segmentation results and write up what I found."

This prompt produces a summary. It does not produce a research contribution. Claude will describe the metrics, note high and low values, and generate paragraph-length text that sounds like a methods section. The student receives output that feels complete and is scientifically empty. There is no hypothesis, no controlled comparison, no failure analysis, no translation discipline.

**After — directed, phase-aware, role-assigned prompt:**

> "I am in the failure analysis phase of my capstone. My hypothesis, committed before running experiments, was that the threshold segmentation algorithm would show disproportionately low Dice on slices with tumour fractions below 5% of slice area because threshold methods depend on sufficient true-positive voxel counts to stabilize the metric. Here are my per-slice Dice scores and tumour fraction estimates: [data]. Act as an adversarial statistical reviewer. Identify the strongest argument against my hypothesis given this evidence. Flag any confounds I have not controlled for — in particular, whether Dice instability at small tumour fractions reflects algorithm failure or metric artefact. Tell me what additional evidence would distinguish between those two explanations."

This prompt is investigable. It has a phase (failure analysis), a pre-registered hypothesis, a specific data input, an explicit role assignment (adversarial reviewer), and a defined output requirement (the strongest counter-argument plus a discriminating test). The student will receive a response they can disagree with, revise, and build on. The first prompt produces a document. The second produces a scientific exchange.

---

## Assignment

**Step 1 — Commit a research question.**
Before opening any data file or running any code, write your research question in `reports/capstone_report.md`. State the question, the hypothesis, and what a falsifying result would look like. This document must exist with a timestamp prior to your first experimental run. It is the baseline against which your final report will be evaluated.

**Step 2 — Select a capstone direction.**
Choose one of the five viable directions described in the course guide: alternative failure mode investigation, preprocessing hypothesis test, tumour fraction subgroup analysis, clinical case report format, or follow-up study protocol. If you propose a variant, document the justification in your research question file.

**Step 3 — Design the experiment.**
Identify exactly one variable you will change or one stratification you will introduce. Write the experimental design — what will be held constant, what will vary, what the unit of analysis is, and what metric will adjudicate the outcome — before running anything. Use Claude in the role of study design critic to identify weaknesses in your design.

**Step 4 — Execute and log.**
Run your investigation, recording each step in a working experimental log. Log entries should include: what you did, what the output was, what you concluded, and what you decided to do next. Log failures and dead ends. This log is evidence of scientific process and will be evaluated as such.

**Step 5 — Conduct a failure analysis.**
After collecting results, identify at least one failure mode with supporting evidence from your metrics or figures. Use Claude in the adversarial reviewer role. Ask it to identify the strongest argument against your finding before you write your conclusions. Revise the analysis in response to the critique.

**Step 6 — Write the translation memo.**
Write the section of `reports/capstone_report.md` that addresses clinical implications. Apply the translation discipline from the course: state what the findings support, what they do not support, and what a clinical reader should not conclude. Use Claude in the clinical communication editor role to identify any overclaiming.

**Step 7 — Prepare the showcase.**
Write `reports/capstone_showcase.md` as a five-minute structured presentation. Follow the sequence: question, method, finding, failure and limit, clinical relevance. Each section corresponds to one minute. The showcase must include a failure analysis figure and a stated limitation.

**Step 8 — Update status.**
Write `outputs/status/capstone.json` with at minimum: `{"status": "ok", "research_question": "<one sentence>", "direction": "<A/B/C/D/E>", "hypothesis_supported": true/false/null, "artifacts_complete": true}`.

---

## Required Artifacts

| File | Expected Content |
|------|-----------------|
| `reports/capstone_report.md` | Full research report: pre-registered question, experimental design, results, failure analysis, translation memo. The question section must be dateable to before the first experimental run. |
| `outputs/status/capstone.json` | Valid JSON with fields: `status`, `research_question`, `direction`, `hypothesis_supported`, `artifacts_complete`. All fields required. |
| `reports/capstone_showcase.md` | Five-section presentation document (question, method, finding, failure and limit, clinical relevance). Must include a reference to or embedding of a failure analysis figure. |

---

## Reflection Questions

1. At what point did your original hypothesis turn out to be wrong, incomplete, or untestable with the data available to you? What did you do at that decision point? What would a less careful investigator have done?

2. What is the strongest argument against your central finding? Where does that argument originate — from the data, the method, the sample size, or the clinical context? What evidence would be needed to overcome it?

3. If you were advising a clinical team considering deployment of the algorithm you investigated, what is the one finding from your capstone they would need to understand first? How would you communicate it to a surgeon who has no interest in the Dice coefficient?

---

## Success Criteria

Excellent capstone work has the following properties:

**Research question:** Specific enough that a colleague could reproduce the experiment without asking for clarification. Written before experiments were run, with evidence from timestamps or log entries.

**Experimental design:** One variable changed. Baseline preserved. Rationale tied to a failure hypothesis from earlier in the course. Negative results reported honestly rather than explained away.

**Failure analysis:** At least one failure mode identified with supporting evidence from metrics or figures — not from speculation. The adversarial review step is visible in the artifacts as a revision, not just as a mention.

**Translation memo:** Contains at least one explicit statement of what the findings do not support. Clinical claims are proportionate to the evidence: a 10-slice Dice analysis supports a provisional hypothesis, not a deployment recommendation.

**Showcase:** A clinical audience member who was not in this course could follow the argument from question to finding to limitation. The presentation is oriented toward explaining the finding, not defending the student's effort.

**Reflection:** Honest acknowledgment of where the investigation fell short, including at least one place where the original hypothesis was revised in response to evidence rather than confirmed despite evidence.

Capstone work falls below the passing threshold when: the research question was written after experiments (detectable from log timestamps); the failure analysis attributes all failures to insufficient data without specifying what the data did show; the translation memo would embarrass a clinical collaborator; or the showcase presents Dice improvement without any account of what the algorithm still fails to do.

---

## Instructor Notes

**The most common failure mode** is students who write the research question after running experiments. This is detectable from `.lab_history/` commit timestamps. Make it explicit in pre-capstone orientation that the question document is the first artifact, not the last. Consider requiring students to share the question document with you before proceeding to Step 3.

**The second most common failure mode** is undifferentiated Claude use. Students who assign Claude the same "helpful assistant" role across all phases produce work that is superficially complete but lacks the evidence of genuine intellectual exchange that characterizes good capstone work. During check-ins, ask students: what role did you assign Claude for this specific phase? If they cannot answer, they are likely not using the multi-role prompt model.

**Direction D (clinical case report) and Direction E (follow-up study protocol)** are appropriate for students with strong clinical backgrounds but weaker computational skills. Direction D requires no code execution. Direction E requires rigorous scientific reasoning but no metrics. Both are evaluated entirely on the quality of scientific judgment. Instructors should prepare to evaluate these directions against different success criteria than Directions A–C.

**Translation memo overclaiming** is nearly universal in first drafts. Schedule a brief group review of translation memos before the showcase where students read each other's clinical implication sections and identify one overclaim in each. Peer review at this stage is more effective than instructor feedback because students recognize the overclaiming pattern in others' writing before they can reliably identify it in their own.

**The showcase is evaluated as communication to a clinical audience**, not as a defense to an ML panel. Instructors who do not have clinical backgrounds should invite a clinical collaborator to attend the showcase, or assign a clinical framing exercise where students explain their work to a non-ML colleague and report back what questions arose.

**Grading note:** Per the course rubric, do not penalize lower Dice scores unless the explanation of those scores is absent or dishonest. A capstone that found no improvement but reasons carefully about why is better science than one that found improvement it cannot explain. Reward honest reporting of negative results explicitly, in public, during the showcase session. Students need to see that scientific honesty is valued in evaluation, not just in principle.
