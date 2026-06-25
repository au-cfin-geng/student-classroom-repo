# M4 — One Variable at a Time

## Module Identity

The most common error in iterative model development is not choosing a bad algorithm — it is changing two things at once and not knowing which one mattered. In clinical AI, this mistake is compounded: regulators, ethics boards, and clinical colleagues will ask you exactly which modification produced the improvement you are claiming. If you cannot answer because you changed the threshold, the preprocessing, and the architecture in the same run, your result is not science — it is anecdote. This module teaches the discipline of controlled experimentation using Claude as an algorithm engineer. The Claude principle at work here is *comparative specification*: a prompt that names exactly one change, preserves the baseline, and requires explicit reasoning about why that change was expected to help forces the researcher to think like an experimentalist before they ever touch the code.

---

## Before / After

**Before Claude:** A researcher sees a poor validation Dice score after training and begins improving the pipeline. They adjust the intensity normalization, lower the threshold, switch from a fixed cutoff to an adaptive one, and add a morphological post-processing step — all in the same afternoon. On the next evaluation run, Dice improves from 0.51 to 0.63. The researcher reports a 12-point improvement. A reviewer asks: which change drove it? The researcher cannot say. They run an ablation study three weeks later, which contradicts the original report. The paper is held.

**With Claude:** The researcher has a documented hypothesis from Mission 3 identifying low-contrast boundary regions as the dominant failure mode. They write a prompt that names that hypothesis, specifies one change — adaptive thresholding to handle inter-slice intensity variation — holds everything else constant (same data split, same random seed, same evaluation script), and requires both the baseline Dice and the new Dice to be reported alongside a written explanation of the causal logic. Claude implements, runs, and records the result. If Dice improves, the researcher knows why. If it does not, the hypothesis is falsified and the next prompt begins from that honest finding.

---

## The Prompt Principle

**Principle: Specify what changed and require a comparison.**

A prompt that names exactly one modification, requires both old and new metrics to be recorded, and demands an explanation of why the change was expected to help forces experimental discipline that produces defensible results. This is not a constraint on Claude's creativity — it is a constraint on the experimental design, and it mirrors the discipline that peer review requires.

**Before (undisciplined prompt):**

> Improve the segmentation model. Try different thresholds and preprocessing, and see if the Dice goes up.

This prompt produces uninterpretable output. Multiple changes will be made. If the metric improves, causality is unknown. If it regresses, the source of the problem cannot be isolated. The result is not reproducible because the researcher does not know what to reproduce.

**After (controlled prompt):**

> My error analysis in `reports/error_analysis.md` identified the dominant failure mode as intensity variation across slices causing the fixed threshold to misclassify boundary voxels. I want to test one targeted change: replace the fixed intensity threshold with an adaptive per-slice threshold (Otsu's method). Hold everything else constant — same data split, same random seed 42, same evaluation script, same metric. Record the baseline Dice from `outputs/metrics/val_metrics.json` and the new Dice after the change. Explain why adaptive thresholding was expected to address the identified failure mode. Save results to `outputs/metrics/model_swap_comparison.json` with keys: `baseline_dice`, `new_dice`, `delta`, `change_description`. Report the result honestly — a negative delta is a valid scientific result.

This prompt produces a single, attributable, reproducible experiment. The change is named. The reasoning is explicit. The comparison is mandatory. The honesty clause prevents the researcher from unconsciously discarding negative results.

---

## The Clinical Scenario in This Course

You are working with 10 teaching FLAIR MRI slices from the BraTS dataset and a baseline intensity-threshold segmentation algorithm. In Mission 3, you ran an error analysis that identified a specific failure mode — likely boundary misclassification, false positives in non-tumour high-intensity regions, or threshold sensitivity to inter-slice normalization differences. That analysis produced a documented hypothesis in `reports/error_analysis.md`.

In this module (Mission 4, stage `stage_05_model_swap`), you take that hypothesis and test it with one controlled change. You run the prompt in `prompts/stage_05_model_swap.md` using Claude Code. Claude reads your error analysis, proposes one algorithm modification directly motivated by your documented failure mode, implements it in `scripts/model_swap.py`, runs the evaluation on the same data split, and writes the comparison. You receive a figure showing before/after results, a JSON file with the numerical comparison, and a written report that states whether your hypothesis was supported.

The key scientific act in this module is not the algorithm change itself — it is the discipline of holding everything else constant and accepting the result regardless of direction. A negative delta is not a failed experiment. It is a falsified hypothesis, which is how science works.

---

## Assignment

**Make target:** `make model-swap`

**Prompt to run:** `prompts/stage_05_model_swap.md`

**Required outputs:**

| File | Required content |
|------|-----------------|
| `outputs/metrics/model_swap_comparison.json` | `{"baseline_dice": X, "new_dice": Y, "delta": Z, "change_description": "..."}` |
| `outputs/figures/model_swap_comparison.png` | Side-by-side or overlay comparison figure showing before/after segmentation results |
| `reports/model_swap.md` | Written description of the change made, the numerical result, and whether the hypothesis was supported or falsified |
| `outputs/status/stage_05_model_swap.json` | `{"status": "ok", "baseline_dice": X, "new_dice": Y, "delta": Z, "change_description": "..."}` |

**What the JSON must contain:** `baseline_dice` must match the value in `outputs/metrics/val_metrics.json` from Mission 2 — same baseline, no recomputation. `new_dice` is the result after the single change. `change_description` must be specific: it should name the exact algorithmic modification, not describe it in vague terms ("improved thresholding" is not acceptable; "replaced fixed threshold 0.5 with per-slice Otsu threshold" is).

**What the report must contain:** The report is not a description of what Claude did. It is your scientific record: what the hypothesis was, what change was made to test it, what the numerical result was, and what conclusion follows. If the delta is negative, the report should state that the hypothesis was not supported and propose what the result implies about the actual failure mechanism.

---

## Reflection Questions

Answer these in your own words after completing the mission. There is no single correct answer — the quality of the response reflects how carefully you engaged with the experiment.

1. **On experimental control:** Your prompt specified the same random seed and data split as the baseline. Why does this matter? What would be different about the comparison if the model swap used a different random seed?

2. **On negative results:** Suppose your new Dice is lower than the baseline. What does that tell you scientifically? Is this a failure of the experiment, a failure of the hypothesis, or something else? How does it change what you would do next?

3. **On the change description:** You were required to write a `change_description` in the JSON output. Why is a machine-readable, specific description of the algorithmic change important for clinical AI development, beyond satisfying this assignment's output contract?

---

## Transfer to Your Own Research

The controlled single-variable experiment is not specific to image segmentation. In any research pipeline — a natural language processing model for clinical notes, a survival analysis pipeline, a radiomics feature extraction workflow — the same principle applies: when you change something, change one thing, measure the same metric, and record why you expected the change to help.

Consider your current or planned research pipeline. Identify one place where you or your team has made, or might make, multiple simultaneous changes in response to a poor result. Now design a prompt that would force a controlled test: what is the one variable to change? What is the baseline metric? What is the specific reasoning that connects the failure mode you observed to the intervention you are proposing? What would falsification of your hypothesis look like?

The practice of writing that prompt — before running anything — is the transferable skill from this module. The Claude capability (implementing, running, and comparing) is only useful if the experimental frame you bring to it is rigorous.

---

## Success Criteria

Strong work in this module looks like the following:

- `baseline_dice` in `model_swap_comparison.json` is identical to `dice` in `val_metrics.json`. Any discrepancy indicates the baseline was not preserved.
- `change_description` is specific enough that a colleague could reproduce the exact change from the text alone, without reading the code.
- `reports/model_swap.md` connects the change to the hypothesis in `reports/error_analysis.md` — the experiment is motivated, not arbitrary.
- The report does not spin the result. If delta is negative or near zero, the report says so and interprets it correctly.
- The comparison figure shows actual segmentation differences between baseline and new method — not just metric bars.
- The reflection responses demonstrate that the student understands *why* experimental control matters, not just *that* the prompt required it.

Work that does not meet these criteria: a positive delta with a vague `change_description`; a report that describes what Claude did rather than what the experiment found; a `baseline_dice` that does not match the previously established baseline; reflection responses that paraphrase the question rather than answering it.
