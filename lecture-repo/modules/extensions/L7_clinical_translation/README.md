# L7 — Clinical Translation (Extension)

**Course:** Agentic Clinical Research Studio
**Track:** Extensions
**Estimated Time:** 90–120 minutes
**Suggested Day:** Day 4 or Day 5 (after core agentic pipeline labs)

---

## 1. Overview

Clinical research generates findings that must travel across a wide spectrum of audiences — from biostatisticians who demand confidence intervals and p-values, to patients who need plain-language summaries, to hospital administrators who require concise risk-benefit framing. The same underlying evidence must be communicated differently depending on who is reading it and what decisions they will make. This lab exists because AI-assisted writing tools, when used naively, produce a single register of output and treat all readers as interchangeable. Lab L7 trains students to explicitly encode audience identity and communication constraints into their agentic prompts, and to recognize the class of hard constraints — called MUST NOT honesty constraints — that apply regardless of audience. The lab confronts a real tension in clinical AI: adapting language to serve the reader must never shade into distorting the evidence to please the reader.

---

## 2. Learning Objectives

- Construct audience-parameterized prompts that produce genuinely distinct clinical communications from identical underlying data.
- Identify and apply MUST NOT honesty constraints — the class of instructions that remain fixed across all audience adaptations.
- Recognize common failure modes in audience-aware writing, including over-simplification that removes clinically material nuance and over-qualification that obscures actionable findings.
- Produce a structured multi-audience translation artifact that demonstrates both linguistic flexibility and evidential fidelity.

---

## 3. Clinical Bottleneck

Translating research findings into clinical practice fails at the communication layer more often than at the evidence layer. A well-powered trial with a statistically significant primary endpoint frequently fails to change prescribing behavior because the findings were communicated to clinicians in a format optimized for journal reviewers rather than for bedside decision-making. Simultaneously, patient-facing materials derived from the same trial are often either patronizingly vague or technically inaccessible. Health systems conducting internal quality improvement research face a third translation problem: their executive and operations audiences need risk-adjusted outcome summaries, not hypothesis-testing language.

The bottleneck is not that the research is weak — it is that no single human expert has the bandwidth to re-author findings across four or five distinct registers simultaneously, with consistency and speed. Agentic systems are well-positioned to address this bottleneck, but only if they are constrained to preserve evidential integrity while adapting surface form.

---

## 4. Agentic Concept: Audience-Aware Writing with MUST NOT Honesty Constraints

**Audience-aware writing** is the practice of holding the semantic content of a communication constant while varying its register, vocabulary, framing, and emphasis to match the cognitive context of the intended reader. In agentic prompt design, this means explicitly naming the audience, their decision context, their baseline knowledge, and their tolerance for uncertainty — and instructing the model to adapt accordingly.

This is not the same as simplification. A patient-facing summary and a clinical investigator briefing may differ dramatically in vocabulary while both accurately representing the finding that "the intervention reduced 90-day readmission by 18% (95% CI 6–29%, p = 0.003) in patients with moderate-to-severe heart failure." The patient version might read: "People in the study who received this treatment were noticeably less likely to return to the hospital within three months." The investigator version preserves the quantitative detail. Both are honest.

**MUST NOT honesty constraints** are the fixed floor beneath all audience adaptation. They are the class of instructions the model must never violate regardless of how the audience is parameterized:

- MUST NOT remove, suppress, or soften findings that indicate harm, adverse events, or null results.
- MUST NOT state or imply statistical significance that is not present in the source data.
- MUST NOT omit population restrictions (age, comorbidity, study setting) that limit generalizability.
- MUST NOT present secondary endpoints as primary outcomes.
- MUST NOT use hedging language to manufacture apparent uncertainty around robust findings, or certainty language to paper over genuine uncertainty.

The pedagogical core of this lab is that students learn to separate what can vary (language register, level of technical detail, structural emphasis) from what cannot vary (the evidence itself, its limitations, and its applicable population). An agentic system that adapts language while preserving these constraints is clinically useful. One that adapts evidence to match audience preference is dangerous.

---

## 5. Before / After

### Before — Naive Prompt

```
Summarize the trial results from the attached report for a general audience.
```

This prompt produces a single output with no audience specificity. The model guesses at register and almost always defaults to a generic clinical-abstract style. Critical findings may be softened because "general audience" implies non-expert, and the model may interpret non-expert as requiring comfort rather than accuracy.

### After — Audience-Parameterized Prompt with MUST NOT Constraints

```
You are a clinical research communicator. I will provide you with a structured summary
of trial results. Produce three separate outputs:

1. CLINICIAN BRIEF (audience: attending hospitalist, decision context: prescribing or
   protocol adoption, format: 150 words, include: effect size with CI, NNT if computable,
   population restrictions, adverse event rate)

2. PATIENT SUMMARY (audience: adult patient with high school reading level, decision
   context: informed consent discussion, format: 150 words, no statistical notation,
   plain-language framing of benefit and risk)

3. OPERATIONS SUMMARY (audience: hospital QI committee, decision context: resource
   allocation and policy change, format: 150 words, include: population affected,
   estimated readmission reduction, cost implication if provided)

MUST NOT constraints that apply to all three outputs:
- Do not omit adverse events or null secondary endpoints.
- Do not imply broader generalizability than the study population supports.
- Do not use language that implies certainty where the confidence interval is wide.
- Do not convert relative risk reduction to absolute terms without stating both.

Source data: [attached]
```

---

## 6. Assignment

**Step 1.** Read the provided source trial summary (supplied in the lab materials folder). Note the primary and secondary endpoints, the study population, the adverse event profile, and any subgroup findings.

**Step 2.** Write a naive single-audience summary of the trial results as if you were not yet aware of audience-aware writing. Save this as your baseline. You will compare it against your final output.

**Step 3.** Identify three distinct audiences relevant to this trial's clinical context. For each audience, document: their role, their decision context, their technical baseline, and their tolerance for quantitative detail.

**Step 4.** Draft your MUST NOT honesty constraints list. Review the source data and identify the findings that are most at risk of being softened, omitted, or distorted under audience pressure. These become your constraint list.

**Step 5.** Construct your audience-parameterized prompt following the After pattern above. Run the prompt and collect the three outputs.

**Step 6.** Perform a fidelity audit: for each output, verify that every MUST NOT constraint was honored. Flag any violations and revise the prompt to address them.

**Step 7.** Write a one-page reflection comparing your naive baseline summary against your three audience-parameterized outputs. What was gained? What constraint violations did you find and fix?

**Step 8.** Save your final outputs and status file as described in the Required Artifacts table below.

---

## 7. Required Artifacts

| Artifact | Path | Expected Content |
|---|---|---|
| Lab report | `reports/lab_07_clinical_translation.md` | Narrative documentation of your process: audience definitions, MUST NOT constraint list, prompt design rationale, fidelity audit results, and reflection comparing naive vs. parameterized outputs. Approximately 600–900 words. |
| Status file | `outputs/status/lab_07_clinical_translation.json` | JSON object with fields: `lab_id`, `status` (completed/in-progress), `audiences_defined` (array of audience names), `must_not_constraints` (count), `fidelity_violations_found` (integer), `fidelity_violations_resolved` (integer), `timestamp`. |

---

## 8. Reflection Questions

1. Where did your audience-parameterized outputs diverge most sharply from one another? Was that divergence a sign of successful adaptation, or did it reveal a tension between serving the reader and preserving the evidence?

2. Review your MUST NOT constraint list. Were there any findings in the source data that you were tempted to soften or omit for a particular audience? What was the nature of that temptation — was it driven by the audience's assumed preference, by uncertainty about the finding itself, or by some other factor?

3. If an attending clinician and a patient were given your respective summaries of the same trial, could they both make well-informed decisions? Where does the risk of downstream miscommunication lie, and how would you address it in a real deployment?

---

## 9. Success Criteria

Excellent work in this lab demonstrates:

- Three audience outputs that are meaningfully distinct in register and structure, not superficial paraphrases of each other.
- A MUST NOT constraint list that is specific to the source data — not a generic boilerplate checklist, but a list grounded in the actual risk points of this particular trial.
- A fidelity audit that is honest: violations found and not fixed are more valuable than violations not found at all, because they demonstrate the student understands what to look for.
- A reflection that engages with the tension rather than resolving it prematurely — the best reflections acknowledge that audience-aware writing is an ongoing judgment problem, not a solved one.
- A status JSON that accurately reflects the audit counts, including any unresolved violations.

---

## 10. Instructor Notes

**Running this lab:** This lab works best when the source trial summary contains at least one null secondary endpoint, one adverse event finding, and one subgroup result that does not replicate in the overall population. These are the three most common sites of distortion in audience-adapted clinical writing, and students need all three to stress-test their constraint lists.

**Common failure modes to watch for:**
- Students who write three outputs that differ only in sentence complexity but not in structural emphasis or decision-framing. Push them to ask: what would a clinician act on in this summary that a patient would not need to know?
- Students who write MUST NOT constraints that are too abstract ("do not mislead the reader") rather than grounded in the specific data ("do not omit the 12% rate of grade-3 adverse events in the elderly subgroup").
- Students who complete the fidelity audit by asserting compliance without evidence. Require them to quote the source data and the output side by side for each constraint.

**Discussion prompt for debrief:** Ask students to name a real clinical context where audience-adapted communication caused harm — not through malice, but through a well-intentioned simplification that removed a material limitation. The history of cancer screening communication (mammography, PSA testing) offers rich examples. This grounding exercise prevents the lab from feeling abstract.

**Extension for advanced students:** Ask students to design a fourth audience output — a regulatory summary for an IRB or ethics board — and to articulate how the constraint structure differs when the audience has institutional authority over the research itself rather than downstream decision-making based on it.
