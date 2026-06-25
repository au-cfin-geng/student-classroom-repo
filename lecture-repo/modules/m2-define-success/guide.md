# M2 — Define Success First

## 1. Module Identity

The most common methodological error in clinical AI is not overfitting, not data leakage, not label noise — it is the absence of a defined success criterion at the start of the experiment. Researchers optimize before they have a baseline. They try different thresholds, swap architectures, tune preprocessing — and at the end they cannot answer the question a clinical collaborator will immediately ask: "Better than what?"

This module addresses that problem directly. In the context of brain tumour segmentation from FLAIR MRI, you will build the simplest possible detector, measure it against a pre-specified metric, and record the result before touching any optimization. The Claude capability at the center of this module is evaluation-driven prompting: writing a prompt that names the metric, defines its valid range, specifies the exact output format, and demands honesty about the result. A prompt structured this way forces clarity before execution — from you and from Claude.

---

## 2. Before / After

**Before Claude-assisted workflow:**

A researcher downloads the dataset, writes a segmentation script, looks at a few overlays, and decides informally that it "looks reasonable." They store the result in a notebook variable. Three days later, after swapping the model, they cannot find the original number. If they can, they are not sure whether the metric was computed the same way. The "baseline" comparison in their paper is reconstructed from memory.

**After Claude-assisted workflow:**

Before any code is written, the prompt specifies the evaluation contract: Dice score, range 0–1, saved to `outputs/metrics/val_metrics.json` with the exact key `dice`. Claude writes a script that computes the metric, saves it to the required path, and also writes a training notes report and a status file. The baseline is a real artifact with a real number. Every future comparison has a fixed point of reference.

---

## 3. The Prompt Principle

**Principle: State the goal before the method.**

Most prompts for code generation describe the method ("write a training loop that..."). Evaluation-driven prompting inverts this: it states what success looks like first, then asks for the implementation that produces it. This matters because it forces the prompt-writer to commit to a definition of done before choosing a method. It also makes Claude's output verifiable — you can check whether the required output exists, whether the value is in range, and whether it matches what was claimed.

**Before (method-first prompt):**

> Write a Python script that trains a segmentation model on the brain tumour slices and evaluates it. Save the results to a file.

This prompt is underdetermined. "Results" could mean anything. "A file" could be anywhere. The metric could be accuracy, IoU, F1, or a custom scoring function. There is no way to verify the output against the prompt.

**After (evaluation-first prompt):**

> I need to train a baseline segmentation model on the imaging data in `data/sample/`. Before any optimization, I need a single honest number.
>
> The evaluation metric is Dice coefficient: `2 * |pred ∩ true| / (|pred| + |true|)`, a float between 0 and 1. A value of 0 means no overlap; 1 means perfect overlap.
>
> Required outputs:
> - `outputs/metrics/val_metrics.json` with keys `{"dice": <float>, "n_slices": N}`
> - `outputs/figures/loss_curve.png` showing the training or evaluation curve
> - `reports/train_notes.md` describing the model, parameters, and result honestly
>
> Use the simplest method that produces a real mask. Set random seed 42. Do not fabricate the metric. If the result is poor, report it.

The second prompt is verifiable. Every output has a location, a format, and a range constraint. "Do not fabricate the metric" is not redundant — it is a research integrity instruction that belongs in any clinical AI prompt that produces numbers.

---

## 4. The Clinical Scenario in This Course

In this module you are executing Mission 2 — Build the First Detector. The clinical task is brain tumour segmentation from FLAIR MRI. You have 10 teaching slices from the BraTS dataset. The segmentation algorithm is an intensity-threshold method: pixels above a threshold in the FLAIR image are classified as tumour.

This is intentionally simple. A threshold segmenter is not a competitive clinical AI system. That is the point. You are not here to produce a publishable Dice score. You are here to establish a number you can explain, reproduce, and compare against. The threshold segmenter is the "nothing" against which everything else will be measured.

Your task in this module is to run `stage_03_train_baseline` using the prompt in `prompts/stage_03_train_baseline.md`. You will use Claude Code to execute the prompt. Claude will write or complete `scripts/run_train.py`, run the segmentation, compute Dice for each validation slice, and write the required artifacts. You will then inspect the outputs manually — not to judge whether the Dice is good, but to verify that the artifacts exist, the metric is a real float, and the training notes honestly describe what was done.

The make target is `smoke-train`. Run it after the stage completes to confirm the required files are present and the status file reads `"status": "ok"`.

---

## 5. Assignment

**Artifact you produce:** Three files that together constitute a reproducible baseline record.

1. `outputs/metrics/val_metrics.json` — the canonical baseline metric. Required key: `dice` (float between 0 and 1). Required additional key: `n_slices` (integer). This file must not be overwritten by any subsequent exploration. It is the fixed reference point for the rest of the course.

2. `outputs/figures/loss_curve.png` — a figure showing the training or evaluation curve. For a threshold segmenter, this will show per-slice Dice scores rather than an epoch-by-epoch loss. Verify that it is a real figure, not a blank or an error placeholder.

3. `reports/train_notes.md` — a plain-language description of the model (intensity threshold, threshold value), the evaluation setup (number of slices, train/validation split), and the result (mean Dice, honest assessment of performance). This file is a research record, not a log. Write it as you would a methods note in a lab notebook.

**Make target:** `smoke-train`

**What the artifact should contain:** The `val_metrics.json` should show a Dice score that reflects the actual performance of an intensity threshold on FLAIR data — likely in the range of 0.3–0.6, possibly lower depending on threshold selection. A value of 0.0 or 1.0 should be treated as an error. The `train_notes.md` should name the threshold value used, describe what the number means in practical terms, and note any obvious failure patterns visible in the validation slices.

---

## 6. Reflection Questions

Answer these questions in your own words after completing the module. Write your answers in `reports/train_notes.md` under a section titled "Reflection."

1. **Why does the prompt require the metric formula, not just the metric name?** Dice score can be computed differently (macro vs. micro averaging, handling empty masks). What would happen to reproducibility if two researchers computed "Dice score" using different implementations?

2. **Your baseline Dice score is a real number. What does it mean for a clinical collaborator?** A radiologist reviewing brain tumour segmentations needs to understand what a Dice of 0.4 implies about the practical utility of the segmentation. Translate your result into a sentence that a clinician without ML training could evaluate.

3. **The prompt instruction "Do not fabricate the metric" seems obvious. Why is it necessary?** In clinical AI development, what pressures or incentives might lead a researcher — or an AI assistant — to report a metric that does not reflect the actual computation? What is the consequence for downstream decisions?

---

## 7. Transfer to Your Own Research

The baseline-first principle applies to any quantitative research task, not just image segmentation. Before you begin optimizing anything in your own work, ask: what is the simplest measurable reference point, and what is the metric that will define improvement?

For clinical AI research specifically: a baseline is not just a scientific convenience. It is an ethical requirement. A model that claims to improve patient outcomes must improve over something — over a defined standard of care, over a human reader, over the previous algorithm. Without a pre-specified baseline metric, "improvement" is a claim that cannot be verified.

When you return to your own research, apply this pattern:

- Before writing any model training code, write the evaluation function and verify it on a toy case.
- Before any experiment, write the output contract: what file, what format, what keys, what valid range.
- After the baseline run, lock the result. Never overwrite it with an exploratory run. Use separate paths for exploration (this course uses `outputs/metrics/baseline_exploration.json` for this purpose).
- When reporting results to collaborators, include the baseline number alongside every improvement claim.

The habit this module builds is not technical. It is scientific: define what you are measuring before you try to improve it.

---

## 8. Success Criteria

Good work in this module looks like the following:

- `outputs/metrics/val_metrics.json` exists, contains a `dice` float between 0 and 1 (exclusive), and contains `n_slices` as an integer. The file was not hand-edited — it was written by the script.
- `outputs/figures/loss_curve.png` exists and shows a real figure with axis labels. A flat line at zero is not acceptable unless that is what the algorithm actually produced, in which case the training notes must explain why.
- `reports/train_notes.md` names the threshold value, describes the validation split honestly, reports the Dice score, and does not claim the result is better than it is.
- `make smoke-train` exits with no errors.
- The student can explain the Dice score verbally: what it measures, how it is computed on this dataset, and what the number implies about clinical usefulness.

Work that does not meet the standard:

- A Dice score of exactly 0.0 or 1.0 without explanation.
- A `train_notes.md` that reports "good performance" without citing the number.
- A `val_metrics.json` with keys that do not match the required contract (`dice`, `n_slices`).
- A figure that is blank, a default matplotlib placeholder, or not saved to the required path.
- A script that only runs successfully from a specific directory other than the repo root.

The test for this module is not whether your Dice score is high. It is whether your baseline is honest, reproducible, and fixed — a reference point that will still be valid when you are comparing models in Mission 4.
