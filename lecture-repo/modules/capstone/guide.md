# Capstone — Independent Clinical AI Investigation

## Module Identity

This capstone is not an exercise. It is a small research project. You have spent the preceding modules learning to inspect data before touching it, define success operationally, diagnose failures with evidence, run controlled single-variable experiments, apply external review, and translate findings honestly. The capstone asks you to deploy those skills as an integrated whole — with a question of your own, an experimental design you can defend, and a presentation aimed at a clinical audience that has no obligation to take your work seriously unless you earn it.

The principle under examination here is the one that runs beneath every prior module: **Claude is a collaborator, not an oracle.** The investigator sets the question, interprets the evidence, and is accountable for the clinical claim. Claude compresses the distance between question and answer, but the scientific judgment is yours. This module tests whether that division of labor is real.

---

## Before / After

**Without structured Claude-assisted workflow:**
A researcher finishes a course, runs a few experiments informally, records numbers in a spreadsheet, and writes a methods section that says "we evaluated the algorithm on BraTS slices." The failure modes are undescribed. The clinical implications are asserted, not argued. There is no record of what was tried that did not work.

**With the workflow this course has built:**
A researcher formulates a specific, falsifiable question, commits it to a prompt, executes against documented infrastructure, records what changed and what did not, produces an honest failure analysis with evidence, and delivers a presentation that separates what was found from what it means — and acknowledges the gap between them.

The capstone is graded on the second of these. Not on the Dice score.

---

## The Prompt Principle

The capstone does not introduce a new prompt pattern. It requires you to select and combine the patterns you have learned. The key discipline is knowing which pattern applies at each stage:

- When you are designing the question: use the **operational definition** pattern from M2.
- When you are diagnosing results: use the **evidence-first diagnostic** pattern from M3.
- When you are running experiments: use the **one-variable protocol** from M4.
- When you are reviewing your own work: use the **adversarial reviewer** pattern from M5.
- When you are writing up findings: use the **honest translation** discipline from M6.

A capstone prompt session might open like this:

**Before (undirected):**
> "Help me analyze my brain tumor segmentation results and write up what I found."

**After (directed, pattern-aware):**
> "I am investigating whether the intensity-threshold segmentation algorithm performs differently on BraTS slices with small tumour fractions (less than 5% of slice area) versus large tumour fractions (greater than 15%). My hypothesis is that Dice scores will be lower for small-tumour slices because threshold-based methods are sensitive to the absolute number of true-positive voxels. Here are my per-slice metrics: [data]. Act as a statistical reviewer. Identify weaknesses in my subgroup definition, flag any confounds I have not controlled for, and tell me what this finding does and does not support clinically."

The second prompt is investigable. The first is a request for a summary.

---

## The Clinical Scenario in This Course

You are working with 10 BraTS FLAIR slices and a simple intensity-threshold segmentation algorithm. The infrastructure from prior modules is available: the scripts, the metrics pipeline, the dashboard, the status logs.

Your task is to pose a question about this algorithm and dataset that you did not answer in M3 or M4, and to answer it using the tools and methods of this course. The question must be answerable with the data you have. You are not expected to acquire new data.

The BraTS dataset and the segmentation algorithm are constrained enough that you cannot escape into complexity. That is deliberate. Precision of reasoning matters more than scale of dataset.

---

## Viable Capstone Directions

Choose one of the following, or propose a variant with written justification:

**Direction A — Alternative failure mode investigation.**
M3 identified one primary failure mode. Hypothesize and investigate a second failure mode not examined there. Define it, measure it, and determine whether it is real or artefactual.

**Direction B — Preprocessing hypothesis test.**
Propose a specific preprocessing modification (contrast normalization, slice-level histogram adjustment, or similar) with a documented mechanistic hypothesis for why it would improve or change Dice performance. Run it. Report whether the hypothesis was supported, partially supported, or falsified — and what the evidence was in each case.

**Direction C — Tumour fraction subgroup analysis.**
Stratify the 10 slices by tumour fraction (small, medium, large, by area). Test whether Dice performance differs systematically across strata. Characterize the relationship and assess whether it has a clinically meaningful interpretation.

**Direction D — Clinical case report format.**
Write a structured clinical case report around the findings from M3 and M4. The case report should follow standard clinical format (presentation, investigation, findings, assessment, plan) applied to an AI algorithm evaluation rather than a patient encounter. The "patient" is the algorithm. The "presenting problem" is its performance failure.

**Direction E — Follow-up study protocol.**
Design (but do not implement) a rigorous follow-up study that would adequately test a specific clinical claim arising from your M3 or M4 findings. The protocol should specify: the clinical question, the patient population, the algorithm, the outcome measure, the sample size rationale, the failure modes to be monitored, and the stopping rules. This direction is evaluated entirely on scientific rigor — there are no metrics to run.

---

## What to Produce

Regardless of direction, you must produce all of the following:

1. **Research question document** (`reports/capstone_question.md`): One to two paragraphs. States the question, the hypothesis, and the criterion for what would constitute a falsifying result. Must be written before any experiments are run.

2. **Experimental log** (`reports/capstone_log.md`): A chronological record of what you ran, what changed, what the results were, and what you concluded at each step. Not a polished write-up — a working log with timestamps and honest entries including dead ends.

3. **Failure analysis** (`reports/capstone_failure_analysis.md`): What did not work, what the evidence suggests about why, and what you would need to determine whether the hypothesis is correct or the method is flawed.

4. **Translation memo** (`reports/capstone_translation.md`): What your findings mean for a clinical audience. Apply the M6 discipline: what this study does support, what it does not support, and what a clinician should and should not conclude from it.

5. **Showcase slides or equivalent** (`reports/capstone_showcase.md` or PDF): Five minutes of material. Structure is specified in the next section.

There is no single `make` target that validates the capstone, because the capstone varies by direction. What must be verified: all four report files are present, all referenced metrics files exist in `outputs/metrics/`, and the showcase document is complete.

---

## The Showcase Presentation

The showcase is five minutes. It is structured as follows:

**Minute 1 — The question.**
State your research question in one sentence. State your hypothesis. State what a falsifying result would look like. If you cannot do this in one minute, the question is not yet defined.

**Minute 2 — The method.**
What did you change, what did you hold constant, and why. What was your unit of analysis. What metric did you use and why it is appropriate.

**Minute 3 — The finding.**
What the data shows. Present the central result with evidence. Do not hedge prematurely. State what happened.

**Minute 4 — The failure and the limit.**
What did not work or what remains unresolved. What the data does not support. What would be required to extend this finding to a clinical claim.

**Minute 5 — The clinical relevance.**
One clinical implication that is defensible given what you found. One thing a radiologist or oncologist should not conclude from this work. One next step that would be scientifically worth pursuing.

The showcase will be evaluated on whether a non-ML clinician could follow it. Assume the audience knows what Dice coefficient is and what BraTS is. Assume they do not know your prior modules and will not give you credit for effort.

---

## Reflection Questions

Answer these in writing after completing the capstone. Each answer should be one substantial paragraph.

1. At what point in your capstone did your original hypothesis turn out to be wrong, incomplete, or untestable with the data you had? What did you do? What would a less careful investigator have done at that same decision point?

2. What is the strongest argument against your central finding? Where does that argument come from — the data, the method, the sample size, the clinical context, or somewhere else? What evidence would you need to overcome it?

3. If you were advising a clinical team that wanted to deploy the algorithm you investigated, what is the one finding from your capstone that they would need to understand before doing so? How would you communicate it to a surgeon who has no interest in Dice coefficients?

---

## Transfer to Your Own Research

The capstone structure transfers directly to any small-scale AI evaluation study in clinical research. The pattern is:

- Commit to a falsifiable question before running experiments.
- Log experiments in real time, including failures.
- Separate the failure analysis from the results section — they are different documents for different purposes.
- Write the translation memo last and treat it as a constraint: do not let the results section drift into claims the translation memo cannot support.
- Present to a clinical audience, not a machine learning audience. The ML audience will forgive hand-waving about Dice. The clinical audience will not forgive hand-waving about patients.

The prompt strategy also transfers. The value of structured prompting is not that it makes Claude smarter. It is that it forces the researcher to be explicit about what they are actually asking — which is most of the work.

---

## Success Criteria

Good capstone work has these properties:

- The research question is specific enough that a colleague could reproduce the experiment without asking for clarification.
- The experimental log shows evidence of iteration — at least one decision that changed based on intermediate results.
- The failure analysis identifies at least one failure mode with supporting evidence from the metrics, not from speculation.
- The translation memo contains at least one explicit statement of what the findings do not support.
- The showcase presentation could be followed by a clinician who was not in this course.
- The reflection questions are answered honestly, including acknowledgment of where the investigation fell short.

Capstone work fails if:

- The research question was written after the experiments (this is detectable from the log timestamps).
- The failure analysis attributes failures to "insufficient data" without specifying what the data did show.
- The translation memo overstates the clinical significance of a 10-slice Dice analysis.
- The showcase presentation is oriented toward defending the student's effort rather than explaining the finding.

The standard is not perfection. The standard is honesty about what was done and what it means.
