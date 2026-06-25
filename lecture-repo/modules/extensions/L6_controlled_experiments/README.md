# L6 — Controlled Experiments (Extension)

**Course:** Agentic Clinical Research Studio
**Track:** Extensions
**Estimated Time:** 90–120 minutes
**Recommended Day:** Day 6 (after core labs L1–L5 are complete)

---

## 1. Overview

Clinical research depends on the ability to isolate causal relationships — to say with confidence that a specific intervention, parameter, or analytical choice produced a specific outcome. AI-assisted research workflows introduce a new failure mode: because agents can adjust multiple variables simultaneously, iterate rapidly, and produce outputs that look polished regardless of whether they reflect sound experimental design, researchers can inadvertently run confounded comparisons and mistake correlation for causation. Lab 6 exists to build the discipline of controlled experimentation directly into agentic workflows. Students practice the foundational principle that governs all valid inference in experimental science — vary one thing at a time, document everything else, and report honestly when results are negative or ambiguous. This lab treats the AI agent not as an oracle that produces answers, but as a collaborator that must be constrained to produce comparable, reproducible evidence.

---

## 2. Learning Objectives

- Design a single-variable experiment within an AI-assisted clinical research workflow, holding all other parameters constant across conditions.
- Produce structured baseline documentation before introducing any experimental variation, establishing a clear pre-change state of record.
- Apply rigorous metrics collection to both the baseline and experimental condition, enabling honest quantitative comparison.
- Report null or negative results with the same rigor and completeness as positive results, recognizing that honest negative findings are scientifically valuable.

---

## 3. Clinical Bottleneck

Systematic reviews, meta-analyses, and clinical decision support tools are only as reliable as the primary research they synthesize. A persistent bottleneck in medical AI development is the proliferation of non-comparable evaluations: studies that change prompt phrasing, model version, clinical domain, and evaluation rubric simultaneously, then attribute performance differences to a single cause. This problem is compounded in agentic pipelines where intermediate steps are automated and not always surfaced for inspection. The result is a literature full of conditional, non-generalizable claims that do not accumulate into reliable knowledge. Controlled experimental design — a discipline that clinical researchers already understand from randomized trials — is the corrective. This lab transfers that discipline from the wet lab or clinical trial setting into the AI workflow context.

---

## 4. Agentic Concept: One Variable at a Time

The core concept of this lab is **experimental control in agentic workflows**. When an AI agent assists with literature synthesis, data extraction, diagnostic drafting, or any structured research task, every configurable element of that pipeline constitutes a potential variable: the system prompt, the temperature setting, the retrieval strategy, the output format, the clinical domain, the document corpus, the evaluation rubric. A well-designed experiment freezes all of these except the one under investigation.

In practice, this means students must:

1. **Establish and document a baseline.** Before introducing any variation, run the agent on the target task and capture its full output, all parameter settings, and performance metrics. This baseline is the control condition. It must be documented in enough detail that another researcher could reproduce it exactly.

2. **Introduce exactly one change.** The experimental condition differs from the baseline in precisely one respect. The change should be motivated by a specific hypothesis — a belief that this variable affects a measurable outcome in a predictable direction.

3. **Hold everything else constant.** The same input documents, the same evaluation criteria, the same clinical context. Consistency is enforced deliberately, not assumed.

4. **Measure the same metrics across both conditions.** Metrics should be defined before running either condition, not selected after seeing results. This pre-registration discipline prevents unconscious metric-shopping.

5. **Report honestly regardless of direction.** A result that shows no difference, or shows the experimental condition performing worse, is not a failure of the experiment — it is a finding. Negative results constrain the space of valid claims and prevent the field from chasing noise.

The agentic context adds one layer of complexity not present in traditional experiments: the agent itself may introduce variability through stochastic outputs. Students learn to manage this through repeated runs, fixed random seeds where available, and explicit acknowledgment of output variance in their reports.

---

## 5. Before / After

**Before applying the concept:**

> "Try different prompting strategies on the radiology report summarization task and see which gives the best results. Adjust the temperature, change the instructions, and try adding more clinical context. Report what worked."

This prompt produces uncontrolled exploration. Any observed differences between conditions are uninterpretable because multiple variables changed simultaneously.

**After applying the concept:**

> "Establish a baseline by running the radiology report summarization task with the current system prompt, temperature 0.3, and no additional clinical context. Document all outputs and compute precision, recall, and hallucination rate. Then run a single experimental condition in which only the system prompt is changed — everything else remains identical. Report the difference in all three metrics and state explicitly whether the hypothesis was supported, not supported, or indeterminate."

This prompt enforces experimental control. The comparison is valid. The result, whatever it is, is interpretable.

---

## 6. Assignment

**Step 1 — Define your hypothesis.** Choose one variable in the clinical research task provided (e.g., system prompt phrasing, retrieval depth, output format constraint). Write a one-sentence hypothesis predicting how changing this variable will affect a specific measurable outcome.

**Step 2 — Document the baseline.** Run the agent on the assigned clinical task using the default configuration. Record all parameter settings in `outputs/status/lab_06_controlled_experiment.json`. Capture the full output and compute the pre-specified metrics. Save these to `outputs/metrics/lab_06_experiment_metrics.json` under the key `"baseline"`.

**Step 3 — Introduce the single experimental change.** Modify only the variable specified in your hypothesis. Run the agent on the identical task with the identical inputs. Record all parameter settings (they should differ from baseline in exactly one field). Compute the same metrics and save them to `outputs/metrics/lab_06_experiment_metrics.json` under the key `"experimental"`.

**Step 4 — Compare and interpret.** Calculate the difference between baseline and experimental metrics. Determine whether the result supports, contradicts, or is indeterminate with respect to your hypothesis.

**Step 5 — Write the experiment report.** Complete `reports/lab_06_controlled_experiment.md`. Include your hypothesis, the baseline documentation, the experimental condition documentation, the metric comparison, and your interpretation. If results are negative or null, state this directly and explain what can be concluded from a null result in this context.

**Step 6 — Reflect.** Answer the reflection questions at the end of this guide in your report's final section.

---

## 7. Required Artifacts

| File | Location | Expected Content |
|------|----------|-----------------|
| `lab_06_controlled_experiment.md` | `reports/` | Full narrative experiment report: hypothesis, baseline, experimental condition, metric comparison, honest interpretation |
| `lab_06_experiment_metrics.json` | `outputs/metrics/` | JSON object with `baseline` and `experimental` keys, each containing all pre-specified metrics and parameter settings |
| `lab_06_controlled_experiment.json` | `outputs/status/` | Status record including task configuration, variable changed, run timestamps, and completion status |

All three artifacts must be present for the lab to be considered complete. The metrics file must contain numeric values for both conditions — qualitative descriptions do not satisfy this requirement.

---

## 8. Reflection Questions

1. If your experimental result was null or negative, what does that finding actually tell you about the variable you manipulated? How would you communicate this result in a research context where stakeholders may be expecting positive findings?

2. What would have gone wrong if you had changed two variables simultaneously? Construct a specific example using your experimental setup to illustrate why the result would be uninterpretable.

3. How does the principle of controlled experimentation apply to the deployment context — that is, when an AI clinical research tool is updated in a live setting and multiple components change at once? What governance processes could enforce experimental control at the organizational level?

---

## 9. Success Criteria

Excellent work in this lab demonstrates the following:

- The baseline is documented in sufficient detail that a peer reviewer could reproduce it independently without asking the student any clarifying questions.
- Exactly one variable differs between the baseline and experimental conditions — this is verifiable by comparing the parameter records in the metrics JSON file.
- Metrics are defined in the hypothesis section and computed identically across both conditions; there is no evidence of post-hoc metric selection.
- The report's interpretation section is calibrated to the evidence: it does not overclaim from a single experimental run, it acknowledges uncertainty, and it states what follow-up experiments would be needed to strengthen the conclusion.
- Negative or null results are reported with the same structural completeness as positive results, including a scientific interpretation of what the null finding contributes.
- The reflection responses demonstrate transfer — the student connects the controlled experiment principle to contexts beyond the specific task in this lab.

---

## 10. Instructor Notes

**Facilitating the single-variable discipline.** The most common error students make is changing two variables at once, often without noticing. Before students run their experimental condition, ask them to read their baseline parameter record aloud and identify the single field that will change. This verbal check catches most confounds before they occur.

**Handling frustration with null results.** Students trained in software development or product contexts often interpret a null result as a failure of effort rather than a scientific finding. Reframe this explicitly: in a well-powered clinical trial, a null result on a pre-specified primary endpoint is a complete and publishable result. The same is true here. Spend time in debrief discussing papers and FDA submissions where negative findings shaped clinical practice.

**Managing stochastic agent outputs.** Temperature and sampling variability can produce different outputs across runs even when all parameters are held constant. Instructors should decide in advance whether to require multiple runs per condition (recommended for advanced cohorts) or to treat single-run outputs as provisional (acceptable for introductory use of this lab). Document whichever choice you make in the cohort's shared lab notes so that students have consistent guidance.

**Connecting to clinical trial methodology.** This lab lands more deeply when students with clinical backgrounds recognize the parallel to protocol-driven trial design. Explicitly invoke the concept of a pre-registered primary endpoint: the metric must be named before the experiment runs, not chosen after seeing results. Students with research experience will recognize this immediately; students without it benefit from a five-minute orientation to why pre-registration exists.

**Time management.** The baseline documentation step is frequently underestimated. Allocate at least 30 minutes specifically for baseline capture and metric computation before introducing the experimental variation. Students who rush the baseline produce reports that cannot support valid comparisons, which requires revision.

**Peer review pairing.** This lab works well with a structured peer review: each student exchanges their parameter records with a partner before running the experimental condition, and the partner verifies that exactly one variable differs. This creates accountability and surfaces confounds early, mimicking the role of a methods reviewer in clinical research.
