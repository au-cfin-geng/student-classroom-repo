# M3 — Evidence-Based Diagnosis

## 1. Module Identity

A single aggregate metric does not tell you where a model fails, whether failures are systematic, or what causes them. In clinical AI research, this distinction is not academic: a failure hypothesis formed without evidence produces interventions that target the wrong problem. Brain tumour segmentation fails in specific, visually identifiable ways — over-segmentation in low-contrast boundary regions, under-segmentation of small satellite lesions, false positives driven by signal artifacts — but only if you look at the cases directly rather than averaging over them. This module teaches the diagnostic discipline that precedes any principled model improvement: using Claude as a visual debugger to move systematically from raw performance numbers to a specific, testable failure hypothesis grounded in image-level evidence.

---

## 2. Before / After

**Before Claude-assisted error analysis**

A researcher sees that mean Dice across validation slices is 0.61. They look at no individual cases. They reason: "the threshold is probably too low" or "we need more training data." They adjust the threshold, rerun, observe that Dice changed by 0.02, and cannot say whether the change addressed the actual failure mode or was noise. The improvement hypothesis is never tested against evidence — it is guessed and discarded.

**After Claude-assisted error analysis**

The researcher asks Claude to rank all validation slices by Dice, identify the worst-performing case, and produce a four-panel visualization: the raw FLAIR image, the ground-truth mask, the model's prediction, and an error map that distinguishes false positives (red), false negatives (blue), and true positives (green). Claude then describes what it sees — without yet explaining why — and only after the visual description does it propose a hypothesis. The result is a written error analysis tied to specific slice indices, specific visual patterns, and a prediction about what change would address the dominant failure mode. The next experiment is designed to test that prediction.

---

## 3. The Prompt Principle

**Observation before hypothesis.** The most common failure mode in AI-assisted research is asking a model to explain a result before asking it to describe the result. When you ask Claude "why does the segmentation fail on these slices?", you get speculation. When you first ask Claude to describe what it sees — the spatial distribution of errors, the shape of false positives, the regions where the model undershoots — and only then ask for an explanation, the explanation is anchored in evidence. Premature explanation is not just analytically weak; it actively generates confident-sounding hypotheses that are difficult to falsify because they were never tied to specific observations.

**Before (premature explanation prompt):**
```
The model has a mean Dice of 0.61 on the validation set. Why is it failing and
what should I change?
```
This prompt invites Claude to generate plausible-sounding explanations without examining any cases. The answer will be generic and untestable.

**After (observation-first prompt):**
```
I have per-slice Dice scores across 10 validation slices. Please:
1. Identify the best and worst performing slices by index.
2. Create a four-panel visualization for each: raw image, ground truth, prediction,
   error map (TP=green, FP=red, FN=blue).
3. Describe what you see in the worst-case figure — the spatial location, shape,
   and pattern of the errors — without yet explaining why they occur.
4. Only after that description: propose a specific, testable failure hypothesis.
```
The hypothesis that follows is constrained by the observation. It is falsifiable because it references a specific pattern in a specific case.

---

## 4. The Clinical Scenario in This Module

You have a trained intensity-threshold segmentation model with a baseline mean Dice score from Module 2. You do not know whether that score reflects a single hard case dragging down the average, systematic boundary failures across all cases, or good performance everywhere except one outlier. This module answers that question.

You will run per-slice evaluation across all 10 BraTS validation slices, rank them by Dice, and identify the best- and worst-performing cases. For each extreme, you will produce a four-panel error visualization. You will read those visualizations with Claude's assistance, using a structured prompt that sequences description before explanation. The module ends with a written error analysis report that contains a specific failure hypothesis — not "the model does poorly on some slices," but something like "the model generates large false positive regions in slices where the FLAIR signal in peri-tumoral edema is close in intensity to the core, leading to boundary over-segmentation." That hypothesis becomes the design constraint for Module 4.

---

## 5. Assignment

**Artifact:** `reports/error_analysis.md`

This report must contain:
- The best-case and worst-case slice indices and their Dice scores
- A visual description of the error patterns in the worst-case figure (written in your own words, not paraphrased from Claude output without attribution)
- A failure hypothesis that is specific and testable — it must name a visual or algorithmic cause and predict what type of change would address it
- A brief note on what evidence would falsify or confirm the hypothesis

**Make target:**
```
make error-analysis
```

**Additional outputs required:**
- `outputs/figures/error_analysis_best.png` — four-panel figure for best-case slice
- `outputs/figures/error_analysis_worst.png` — four-panel figure for worst-case slice
- `outputs/status/stage_04_error_analysis.json` — must include keys: `status`, `best_case` (with `slice_idx` and `dice`), `worst_case` (with `slice_idx` and `dice`), `n_slices`

Run `make error-analysis` from the project root. The pipeline will execute `scripts/error_analysis.py`, generate the figures, write the status file, and verify that all required outputs exist.

Inspect `outputs/figures/error_analysis_worst.png` manually before submitting. You should be able to state in one sentence what is visually wrong in that case. If you cannot, the error analysis is incomplete.

---

## 6. Reflection Questions

After completing the module, answer these three questions in your own words. Write your answers directly in `reports/error_analysis.md` under a "Reflection" heading.

1. **Observation vs. hypothesis.** In your own prompt session, at what point did Claude's output shift from describing what it saw to explaining why? Was the explanation tighter or looser than it would have been if you had asked for the explanation first? What does this tell you about prompt sequencing?

2. **Specificity of failure.** Compare the following two statements: "The model fails on hard cases" and "The model over-segments the tumour boundary in slices where peri-tumoral edema has FLAIR signal above 0.7 normalized intensity." What makes the second statement a hypothesis and the first a description? Does your failure hypothesis in `error_analysis.md` meet that standard?

3. **Clinical stakes.** If this segmentation algorithm were deployed in a radiotherapy planning workflow and its dominant failure mode was consistent false positive over-segmentation at the tumour boundary, what would the clinical consequence be for treatment margin planning? How would you communicate this risk in a methods paper?

---

## 7. Transfer to Your Own Research

The observation-before-hypothesis pattern is not specific to segmentation. Any time you use Claude to interpret results — classification errors, regression residuals, retrieval failures in a RAG pipeline, anomalies in a time series — the same discipline applies: look first, explain second.

In your own research:
- Identify the "worst cases" in your current model or analysis. What is the equivalent of the worst-case Dice slice in your domain?
- What would a four-panel error map look like for your task? What would the axes, panels, or decomposition show?
- Is your current failure analysis tied to specific examples, or is it conducted entirely at the level of aggregate metrics? If the latter, you are missing information that cannot be recovered from the metric alone.

A failure hypothesis that is not tied to specific observed cases is not a scientific hypothesis — it is a guess that uses the vocabulary of science. Claude can help you generate either kind. The prompt structure you use determines which one you get.

---

## 8. Success Criteria

Work in this module is complete and meets quality standards when all of the following are true:

**Technical outputs**
- `make error-analysis` exits with status 0 and all four required files are present
- `outputs/status/stage_04_error_analysis.json` contains `"status": "ok"` and both `best_case` and `worst_case` entries with valid `slice_idx` and `dice` values
- Both error figures are four-panel layouts with a visible error map that distinguishes TP, FP, and FN

**Written analysis**
- `reports/error_analysis.md` names specific slice indices and Dice scores — not just "the best slice" and "the worst slice"
- The failure hypothesis is specific enough to be testable: it names a visual pattern, a plausible mechanism, or an input characteristic, and it predicts what kind of change would address it
- The hypothesis is consistent with what is actually visible in `error_analysis_worst.png` — not a generic statement that could apply to any segmentation model

**Reflection**
- The three reflection questions are answered in complete sentences
- The answer to Question 1 shows that the student ran an observation-first prompt, not a hypothesis-first prompt
- The answer to Question 3 engages with the clinical context rather than restating the technical finding

Work that does not meet these criteria: a report that describes only the aggregate Dice score without examining individual cases; a failure hypothesis stated as "the model needs more training data" without visual evidence; error figures that are saved but not examined; reflection answers that quote Claude output without the student's own interpretation.
