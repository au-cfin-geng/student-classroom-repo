# L6 — Evaluation & Controlled Experiments

**Concept:** One variable at a time, controlled comparison  
**Time:** 45 min · Day 2  
**Prompt file:** `prompts/stage_05_model_swap.md`

---

## Why this lab exists

The single most important word in experimental research is **attribution**: when a metric changes, you must be able to attribute that change to a specific cause. If two things change simultaneously, you cannot attribute the improvement to either one. The result is irreproducible and undefendable.

In computational research, this is violated constantly. Researchers change a preprocessing parameter, a model hyperparameter, and a data augmentation strategy in the same commit — then wonder why their next experiment can't reproduce the improvement. The problem is not Claude, not the data, not the metric — it is the absence of a controlled experimental design.

This lab teaches you to use Claude to implement controlled experiments. The key is that the constraint must appear explicitly in the prompt: "change ONLY the threshold from 0.5 to 0.6. Nothing else changes." Without that explicit constraint, Claude may make multiple changes it considers improvements — optimising your code while changing your variable, for instance — making the result uninterpretable.

The discipline of one variable at a time is not a limitation on creativity. It is what makes results citable. An experiment you can describe with "we changed X from A to B and measured metric M" is one you can defend in a paper, a grant, or a clinical review.

---

## The clinical problem this addresses

An AI system for clinical decision support must pass rigorous validation before deployment. That validation requires demonstrating that each design choice is evidence-based and documented. An undocumented, uncontrolled development history — "we tried things until it worked" — does not satisfy regulatory or clinical review standards.

The controlled experiment habit, built in research, transfers directly to the level of documentation required in clinical AI development.

---

## Before / After

**Before:**
```
Can you try to improve the Dice score? Try a few different approaches and see what works.
```

Claude changes multiple parameters, adds augmentation, adjusts the model, and reports an improved Dice. You cannot explain the improvement. Your supervisor asks which change drove the gain. You don't know. The result is not reproducible.

**After:**
```
You are a clinical methods researcher running a controlled experiment.

Baseline: Read outputs/metrics/val_metrics.json. Record the current Dice as baseline_dice.

Intervention: Change ONLY the threshold parameter in scripts/run_train.py from 0.5 to 0.6.
Nothing else changes.

Run the experiment. Save to outputs/metrics/lab_06_experiment_metrics.json with:
  baseline_dice: float
  intervention_dice: float
  threshold_baseline: 0.5
  threshold_intervention: 0.6
  change_description: str

Write the report to reports/lab_06_controlled_experiment.md with:
  - The single variable changed
  - Before/after metrics table
  - The null hypothesis
  - An honest interpretation

Write status to outputs/status/lab_06_controlled_experiment.json.
```

The second prompt specifies the single variable, records baseline, runs the intervention, and produces a documented comparison. The null hypothesis framing forces honest interpretation — if there is no significant change, that is a result, not a failure.

---

## Clinical scenario

Your baseline Dice is approximately 0.55. A colleague suggests that raising the segmentation threshold might reduce false positives in the boundary region — one of the failure modes from your error analysis. How do you test this suggestion as a controlled experiment rather than a guess?

---

## Assignment

1. Confirm `outputs/metrics/val_metrics.json` exists (from L5 or legacy pipeline).
2. Paste the lab prompt into Claude Code.
3. Before Claude runs the experiment, verify: has it touched only the threshold parameter?
4. After running, check `outputs/metrics/lab_06_experiment_metrics.json`.
   - Did Dice improve, decrease, or stay the same?
   - Was the magnitude of change what you expected?
5. Write your interpretation in `reports/lab_06_controlled_experiment.md`.
   - If the result was negative (Dice didn't improve), explain why that is still a useful result.

---

## Required artifacts

| Path | Contents |
|------|---------|
| `outputs/metrics/lab_06_experiment_metrics.json` | `baseline_dice`, `intervention_dice`, threshold values, `change_description` |
| `reports/lab_06_controlled_experiment.md` | Experimental report with hypothesis, before/after table, interpretation |
| `outputs/status/lab_06_controlled_experiment.json` | `status: "ok"` |

---

## Reflection questions

1. Did Dice improve? If so, can you fully attribute the change to the threshold — or could something else have varied?
2. How is this controlled experiment different from hyperparameter tuning? What makes it a research step rather than an engineering step?
3. What is the minimum number of runs needed to trust this result? Why can't you conclude from a single run?

---

## Negative results are results

If the threshold change did not improve Dice, your report should say so — and explain why this is a useful finding. Possible conclusions:

- The threshold is not the limiting factor; boundary detection quality (not cutoff) drives the metric
- The failure mode identified in L3/L4 is not addressable by threshold adjustment — a different intervention is needed
- The teaching dataset is too small to detect the effect of a 0.1 threshold change

All of these are scientifically valid conclusions. A report that says "result: no improvement; conclusion: threshold is not the right lever for this failure mode; next experiment: investigate preprocessing as suggested in L4" is better science than a result that reports improvement without explanation.

---

## Success criteria

- `outputs/metrics/lab_06_experiment_metrics.json` has all five required keys
- `reports/lab_06_controlled_experiment.md` names the single variable changed and includes a before/after table
- You can state the null hypothesis and interpret the result honestly, including if the result is negative
