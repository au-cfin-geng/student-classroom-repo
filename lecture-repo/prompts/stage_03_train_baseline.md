## Traditional workflow pain point
Students often start with complex models or optimized settings, making later comparisons meaningless. Without an honest baseline with fixed evaluation criteria, you cannot know whether any future change is an improvement.

## Claude / agentic method introduced
Claude as builder and evaluator; code generation with explicit output contracts (exact metric name, exact file paths, exact JSON structure); evaluation-driven prompting that defines success before execution.

## Anthropic Academy / Claude learning connection
> This mission aligns with concepts from Claude Code in Action; Claude Code 101; AI Capabilities and Limitations.
> Recommended external reading: Claude Code in Action; Claude Code 101; AI Capabilities and Limitations.
> (Note: this lab creates original clinical AI research exercises. It does not reproduce or contain Anthropic Academy course content.)

## Transferable PhD research skill
Use Claude to build the simplest measurable baseline for any task — with pre-defined evaluation criteria, fixed random seed, and exact artifact paths — before attempting any optimization.

---

# Mission 2 — Build the First Detector (Part 2): Train and Evaluate

## What this mission is about

Every comparison you will make in this lab depends on this baseline being
correct and reproducible. The goal is not a high Dice score — it is a score
you can explain. A reproducible baseline with an honest number is more
scientifically valuable than an optimized number you cannot trace.

---

## Prompt Principle: Specify evaluation criteria, not just execution

A prompt that names the exact metric, its formula, and its required range
makes Claude's evaluation verifiable. Without specifying "Dice score, range
0–1," Claude might compute a different metric, compute it incorrectly, or
report it in a way that cannot be compared across runs.

---

## Layer A — Base Prompt

> I need to train a baseline segmentation model on the imaging data in `data/sample/`
> and record the first quantitative result.
>
> Please do the following:
>
> 1. Look at what training code exists in `scripts/run_train.py`. If it needs
>    to be created or completed, write it now. The training should:
>    - Use a simple, deterministic model (a threshold, a basic U-Net-style architecture,
>      or the simplest approach that produces a mask)
>    - Set a fixed random seed (42) for reproducibility
>    - Run inference on the validation slices
>    - Compute Dice score for each slice and report the mean
>
> 2. Run the training/evaluation and tell me:
>    - How many slices were used for training and validation
>    - The mean Dice score on the validation set
>    - What model architecture or method was used
>
> 3. Save a loss or training curve to `outputs/figures/loss_curve.png`.
>
> 4. Write a training notes report to `reports/train_notes.md` with:
>    - Model description
>    - Training parameters (learning rate, epochs if applicable, seed)
>    - Validation Dice score
>    - Any observations about convergence or model behavior
>
> 5. Write a metrics file to `outputs/metrics/val_metrics.json`:
>    `{"dice": <value>, "n_slices": N}`
>
> 6. Write a status file to `outputs/status/stage_03_train_baseline.json`:
>    `{"status": "ok", "dice": <value>, "n_slices": N}`
>
> The Dice score must be a real number between 0 and 1. Do not fabricate it.

---

## Required outputs

| File | Minimum content |
|------|-----------------|
| `outputs/figures/loss_curve.png` | Training or evaluation curve figure |
| `reports/train_notes.md` | Model description, parameters, Dice result, observations |
| `outputs/metrics/val_metrics.json` | `{"dice": <float 0–1>, "n_slices": N}` |
| `outputs/status/stage_03_train_baseline.json` | `{"status": "ok", "dice": <float>, "n_slices": N}` |

---

## Layer B — Reflection Prompt

> Look at the validation Dice score from `outputs/metrics/val_metrics.json`
> and the training notes in `reports/train_notes.md`.
>
> Explain the result to me as if I were a **clinical collaborator** who knows
> medicine but not machine learning:
> - What does a Dice score of [X] mean in practical terms?
> - Is this result good, poor, or uncertain? What would a meaningful threshold be?
> - What is the single most likely reason this baseline does not perform better?
> - What would need to change for this model to be useful in a real clinical workflow?

---

## Layer C — Exploration Challenge

> Try one modification to the baseline to see if performance changes:
>
> - Change one hyperparameter (e.g., threshold value, number of training epochs,
>   or normalization method) and re-evaluate.
> - Document the result: what changed, what happened to Dice, and whether the
>   change was positive, negative, or negligible.
>
> Do NOT overwrite `outputs/metrics/val_metrics.json` — save the exploration result
> to `outputs/metrics/baseline_exploration.json` so the canonical baseline is preserved.
>
> *Why this matters: a controlled single-variable change is the foundation of
> Mission 4. Practice it now.*

---

## Discussion questions

- Why does the prompt require a fixed random seed? What would happen to reproducibility
  without one?
- What is the difference between training loss and validation Dice? Why does validation
  Dice matter more for evaluating model quality?
- If the Dice score is 0.05, should you move forward to Mission 3 or investigate first?
  What would you look for?

## Output contract
| File | Minimum content |
|------|-----------------|
| `outputs/figures/loss_curve.png` | Training or evaluation curve figure |
| `reports/train_notes.md` | Model description, parameters, Dice result, observations |
| `outputs/metrics/val_metrics.json` | `{"dice": <float 0–1>, "n_slices": N}` |
| `outputs/status/stage_03_train_baseline.json` | `{"status": "ok", "dice": <float>, "n_slices": N}` |

## What to inspect manually
Open outputs/metrics/val_metrics.json. Is the dice value a real float between 0 and 1? Open outputs/figures/loss_curve.png. Does the curve look like training happened, or is it flat/noise? Open reports/train_notes.md — does it honestly describe the model used?

## Transfer to your own PhD research
For your own research task, what would be the simplest measurable baseline and what metric would you use to evaluate it? How would you define "good enough" before you start training?

---
