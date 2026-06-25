# M5 — The Reviewer Role

## Module Identity

Researchers are the worst reviewers of their own work. This is not a character flaw — it is a structural problem. The developer perspective is built around forward momentum: the hypothesis, the implementation, the measurement. That perspective is essential for producing results. It is actively harmful when evaluating them. The same Dice improvement that reads as "promising" to the developer reads as "confounded by seed sensitivity and insufficient baseline characterization" to a methods reviewer. Both descriptions can be true. The developer rarely volunteers the second one.

This module teaches a specific Claude capability: **role switching**. The same information given to Claude under a different role assignment produces fundamentally different analytical output. A prompt that says "summarize these results" produces a summary. A prompt that says "act as the methods reviewer for this study and identify the three most important weaknesses" produces a critique. The role assignment is not cosmetic. It changes what Claude attends to, what it treats as a problem, and what it chooses to surface. Understanding this — and using it deliberately — is one of the most practically useful skills in using LLMs for research.

---

## Before / After

**Without role switching:**

A researcher runs an experiment that shows Dice improving from 0.61 to 0.67. They write a methods note saying the adaptation succeeded. They move on. The improvement may be real. It may also be due to a different random seed, a different preprocessing order that happened to match the validation set, or a success criterion that was quietly adjusted after seeing the result. The developer perspective does not flag these possibilities because it is not structured to look for them.

**With role switching:**

The same researcher uses Claude in reviewer mode: "You are the methods reviewer for this study. Your goal is to find the three most important threats to validity in this result." Claude now attends to confounds, asks about the baseline characterization, notes that the pre-specified success criterion appears slightly different from the one in the challenge plan. The developer and the reviewer are looking at the same data. They are answering different questions. Running both perspectives before moving to the next stage is not pessimism — it is minimum scientific hygiene.

---

## The Prompt Principle

**Assign a role and give it a mandate.**

A role assignment changes what Claude treats as salient. Without a role, Claude defaults to a collaborative, helpful summarization posture — it synthesizes what you have, fills in obvious gaps, and presents the work in a reasonable light. That is fine for drafting. It is wrong for evaluation.

The structure of an effective reviewer prompt has three parts: the role, the mandate, and the constraint. The role tells Claude whose perspective to take. The mandate tells Claude what to optimize for. The constraint forces specificity.

**Before (no role assignment):**

> Summarize the results of the Day 2 challenge experiment and whether it achieved its goals.

This produces a summary. It may be accurate. It will not be adversarial. Claude will not volunteer what is wrong with the study design unless the design is obviously broken.

**After (role assignment with mandate):**

> Act as the methods reviewer for this study. Your goal is to identify the three most important weaknesses in the challenge plan and its implementation. For each weakness, state: (1) what the problem is, (2) why it matters for the validity of the result, and (3) what would need to change to address it.

This prompt produces a different class of output. The role ("methods reviewer") signals adversarial analysis. The mandate ("identify the three most important weaknesses") forces prioritization rather than a laundry list. The three-part structure for each weakness produces actionable specificity rather than vague concerns. The difference is not in Claude's knowledge — it is in the instruction structure that activates a different analytical posture.

A secondary role — the **clinical safety reviewer** — further extends this. The technical developer asks "does Dice improve?" The clinical safety reviewer asks "what would need to be validated before this change gets near a patient?" These are not the same question. In clinical AI, both questions are required. They often conflict.

---

## The Clinical Scenario in This Course

By Mission 5, you have produced a substantial evidence base: a baseline Dice score, an error analysis, a hypothesis about the failure mode, a controlled model swap, and a Day 1 summary report. You have also written a pre-specified challenge plan that commits, in writing and before execution, to a research question, a proposed method, a success criterion, and failure conditions.

Mission 5 has two parts. In Part 1 (stage_07_challenge_plan), you write the challenge plan itself — the formal study design for Day 2. In Part 2 (stage_08_adapt_pipeline), you implement the plan and measure the result against the pre-specified success criterion.

The reviewer role is embedded throughout both stages, but it is central to the Layer B prompts. After writing the challenge plan, you run a structured two-perspective critique: the **methods reviewer** checks whether the proposed change is specific enough to be reproducible by someone else; the **devil's advocate** identifies the assumption in the plan most likely to be wrong. These are not optional extensions. They are the check between plan-writing and implementation — the structural defense against building an experiment that was designed to succeed.

After implementation, the same discipline applies in reverse: the outcome report must honestly state whether the pre-specified success criterion was met, and it must not revise the criterion retroactively to accommodate the result.

---

## Assignment

**What you produce:**

- `reports/challenge_plan.md` — A structured six-section research design document with Identified Weakness, Research Question, Proposed Method, What Would Count as Success, Risks and Failure Conditions, and What I Would Try Next if This Fails. The research question must follow the form: "Does [intervention X] improve [metric Y] compared to [baseline Z] in [context C]?" The success criterion must be specific and measurable. After completing Layer B, the plan also includes a `## Critique Response` section addressing the strongest objections raised by the methods reviewer and devil's advocate.
- `outputs/metrics/challenge_comparison.json` — The numerical comparison: baseline Dice, new Dice, delta, and a short description of what changed.
- `reports/adapt_pipeline.md` — An adaptation report that describes what was implemented, reports the numerical result, and states clearly whether the pre-specified success criterion was met (yes / no / partially).

**Make targets:**

```
make challenge-plan
make adapt-pipeline
```

**What the artifacts should contain:**

The challenge plan is a commitment device. It should be uncomfortable to write — if it is easy, the research question is not specific enough. "Improve segmentation" is not a research question. "Does replacing the fixed intensity threshold with an adaptive threshold based on local FLAIR statistics improve Dice by more than 0.05 on the 10-slice validation set compared to the Day 1 baseline?" is a research question.

The adaptation report is an honest accounting. It must read like the results section of a scientific paper, not a project update. If the result was negative, say so. If the success criterion was not met, say so. A negative result reported honestly is a scientific result. A retroactively adjusted criterion is not.

---

## Reflection Questions

Answer the following in your own words after completing both stages. There is no single correct answer to any of these questions. The quality of the answer depends on the specificity of your reasoning.

1. You ran the same result through two roles — methods reviewer and devil's advocate. Did the two perspectives surface different weaknesses, or did they converge on the same issues? What does that tell you about whether the critique was genuinely adversarial, or whether Claude was pattern-matching to generic study design concerns?

2. The challenge plan asks you to specify "a result that would cause you to abandon this direction" before running the experiment. In practice, did you follow that criterion honestly, or did you find yourself reasoning around it after seeing the result? What would it take to make pre-specified abandonment criteria work in your own research?

3. The clinical safety reviewer and the algorithm designer are given the same data but asked different questions. In your challenge plan and adaptation, were there any points where the two perspectives would have recommended different actions? If they conflict, how would you decide which perspective governs the decision?

---

## Transfer to Your Own Research

The reviewer role is not a Claude trick. It is a structured method for creating the external perspective that peer review is supposed to provide — before the manuscript is written, when the course of the project can still change.

In practice, most researchers produce a result, draft an explanation, and submit. The reviewer role inverts this: you articulate the strongest case against your own result before writing the explanation. If the strongest case against it cannot be addressed, you have identified the central weakness of your study. If it can be addressed, you have written the rebuttal section before the referee asks for it.

Applied to your own PhD research: before writing the results section of any chapter, write a two-paragraph critique of your strongest result using the methods reviewer role. Then write a two-paragraph response. If you cannot write the response, the result is not ready to report. If you can, you have pre-empted the most damaging review comments before submission.

The same applies to clinical AI specifically. For any system that will be evaluated in a clinical context, the clinical safety reviewer role is not optional — it is the mechanism by which you distinguish "technically interesting" from "safe to study in patients." A Dice improvement of 0.06 on a 10-slice teaching dataset is technically interesting. Whether it survives the clinical safety reviewer's question — "what would need to be validated before this change gets closer to clinical use?" — is a different and harder question, and answering it is the point.

---

## Success Criteria

Good work in this module looks like the following:

- The research question in `reports/challenge_plan.md` follows the specified form and names a specific metric, intervention, baseline, and context. It is not a restatement of a goal.
- The success criterion is measurable in a single sentence without interpretation. "Performance improves" fails this test. "Dice improves by more than 0.05 on the validation set" passes it.
- The critique in the Layer B reviewer prompt identifies at least one specific weakness that is genuinely specific to this study — not a generic concern like "sample size is small." Generic concerns are not reviews; they are hedges.
- The adaptation report states the outcome against the pre-specified criterion without retroactive adjustment. If the criterion was not met, the report says so in plain language in the first paragraph, not buried after a discussion of partial improvements.
- The `challenge_comparison.json` values are consistent with the `adapt_pipeline.md` narrative. Metrics and prose must agree.

Poor work looks like: a research question that is actually a goal statement; a success criterion defined as "improvement"; a critique that lists three generic weaknesses applicable to any study; an adaptation report that quietly moves the goalposts; or a status file that says "ok" when the implementation did not match the plan.

The reviewer role is a check on motivated reasoning. The assignment is not graded on whether Dice improved. It is graded on whether the student can maintain scientific honesty when the result is ambiguous or negative — and whether the reviewer prompt was used as a real check rather than a formality.
