# Instructor Teaching Guide — Clinical Claude

## Course Overview for Instructors

Clinical Claude is a two-day intensive workshop for clinical researchers — primarily physicians, radiologists, and biomedical engineers — who need to work credibly with AI-assisted image analysis pipelines. The course uses brain tumour segmentation from FLAIR MRI as a fixed clinical scenario throughout: students apply a simple intensity-threshold algorithm to ten BraTS teaching slices and evaluate it using Dice coefficient. The technical problem is intentionally simple; the learning is in the reasoning. Students learn to use Claude not as an answer machine but as a structured thinking tool — for hypothesis generation, failure analysis, and scientific communication. By the end of Day 2, every student should be able to state clearly what their algorithm got wrong, why it likely got wrong, and what they would need to do to trust a future version of it enough to present it to a collaborator. That is the bar.

---

## Day 1 Facilitation

### Opening (before M0–M1)

Tell students at the outset: "This course is about reasoning, not performance. A Dice score of 0.4 with a clear failure hypothesis is more valuable work here than a Dice score of 0.7 with no explanation." Establish this norm early and return to it. Students trained in competitive academic environments will try to optimize the metric. Redirect them explicitly.

### M0–M2: Setup and first run

These modules are largely mechanical. Your job is to make sure everyone finishes with a working pipeline before M3. Do not let the group diverge — hold the faster students at the starting line until the slowest student has output in `outputs/metrics/`. The most common failure point is environment setup; have a working reference environment available.

**The speed gap.** Faster students who finish M2 early should not skip ahead to M4. Direct them to Layer B and Layer C prompts within the current module. These are harder, slower prompts that ask Claude to explain tradeoffs or anticipate reviewer objections. This is better use of their time than rushing to a module they are not contextually prepared for.

### M3: The most important moment of Day 1

M3 is where students run their error analysis. After they have produced their figure and written their first failure hypothesis, stop the room and ask:

**"What would you need to see to be confident in your failure hypothesis?"**

Do not answer it for them. Write it on the board. Give students three minutes to write a response privately, then ask two or three to share. The goal is to surface the distinction between a hypothesis that is plausible and one that is testable. Students who cannot answer this question have not yet done the hard work of M3 — they have described output, not reasoned about cause.

---

## Day 2 Facilitation

### M4–M5: The pivot moment

At the start of Day 2, before students open their laptops, ask them to read back their M3 error analysis from Day 1. Then ask:

**"What would a reviewer say about this?"**

This is the M5 pivot. The purpose is to create critical distance from their own work before they begin refining it. Most students wrote something vague on Day 1 ("the algorithm missed some lesions near the boundary"). A reviewer would ask: which boundaries, under what conditions, and how often? Let students revise their hypothesis with this pressure applied before they continue.

### M6: The hardest module

M6 is the translation memo — converting technical findings into a clinical communication. It is the hardest module because most students' first drafts overclaim. A typical first-draft sentence: "This algorithm shows promising results for clinical deployment." That sentence is not defensible from ten teaching slices with no ground-truth comparison beyond the BraTS labels.

**Do not correct them before they write it.** Let them produce the first draft. Then ask them to read it back aloud and find the overstatement themselves. Ask: "Where did you claim more certainty than your data supports?" The act of finding it themselves is the learning. If a student cannot find the overstatement, point to the sentence and ask what the sample size was and whether they have an independent validation set. That is usually sufficient.

---

## What Instructors Must Not Do

**Do not run the pipeline for a stuck student.** Debugging a stuck pipeline is itself a core skill this course is designed to build. Give the student a Claude prompt structure and let them work through it. If they are genuinely blocked on an environment issue unrelated to learning, help with that specifically — but do not operate their pipeline.

**Do not characterize a Dice score as "good" or "bad."** A Dice score means nothing without a reference — the clinical context, the lesion size distribution, the comparator method. If you say "that's a good score," you have implicitly validated a way of thinking you are trying to dislodge. Instead ask: "Good relative to what?"

**Do not accept a report that states "the model achieved X%" without a denominator and a limitation statement.** X% on ten slices from one dataset is not a finding about algorithm performance in general. Require the student to state the N, identify at least one class of cases not represented in the sample, and name one condition under which they would expect the metric to degrade.

---

## Showcase Format

The course closes with a per-student or per-group showcase. The format is fixed:

- **5 minutes per student or group.** No extensions.
- **Required:** Display the `error_analysis` figure. State the failure hypothesis in one sentence. State one honest limitation of the analysis.
- **Not required:** A high Dice score. A polished visualization. A recommendation for clinical deployment.

Instructors should model the showcase standard in their own framing before the first student presents. The criterion is intellectual honesty under constraint, not technical performance. A student who says "I cannot distinguish my algorithm's failures from annotation noise in this dataset, and here is why that matters" has produced the best possible showcase result. Reward that.
