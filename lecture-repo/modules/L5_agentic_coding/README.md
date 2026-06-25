# L5 — Agentic Coding for Clinical Data

**Concept:** Plan → edit → run → inspect → revise  
**Time:** 50 min · Day 2  
**Prompt file:** `prompts/stage_03_train_baseline.md`

---

## Why this lab exists

Agentic coding is not "ask Claude to write a script." It is a supervised iterative loop in which Claude plans a step, writes or edits code, runs it, inspects the output, diagnoses any problems, and revises — all in a single session. You are the supervisor of this loop, not a passive observer.

The distinction matters for clinical research because the agentic loop produces more than a script — it produces a research artifact with a traceable methodology. Claude doesn't just write `scripts/lab_05_student_analysis.py`; it explains what it did at each step, runs the script, verifies that the output has the expected schema, and reports when something unexpected happens.

Your role in the loop:
1. **Write a precise enough initial prompt** that Claude starts on the right track
2. **Inspect intermediate outputs** — not just the final result, but the intermediate files Claude reads and the reasoning it offers at each checkpoint
3. **Redirect** when Claude's choices diverge from your research question
4. **Validate the final artifact** against your research goal, not just against whether the file exists

The common failure mode: students give a vague first prompt, Claude produces something plausible, students accept it without validation. The file exists, the Dice score is there — but the methodology has a subtle flaw (wrong data split, wrong seed, wrong metric aggregation) that won't surface until someone tries to reproduce it.

---

## The clinical problem this addresses

A researcher needs per-slice Dice coefficients — not the average — to identify which specific slices fail and why. Asking for per-slice analysis rather than aggregate analysis is the difference between a Dice of 0.58 overall and discovering that three specific slices have Dice below 0.3, which is the failure pattern that informs the next experiment.

Manual scripting would take hours and would likely contain bugs the researcher doesn't detect. The agentic loop with Claude produces the analysis in one session — but only if the researcher supervises the loop carefully.

---

## Before / After

**Before:**
```
Write me a script that analyses my brain MRI data.
```

Claude writes a generic analysis script. It may aggregate where you needed per-slice. It may use the wrong threshold. It may not save to the path CLAUDE.md specifies. The script may run, produce output, and still not answer your actual research question.

**After:**
```
You are a clinical data scientist implementing a per-slice segmentation analysis.

Step 1: Read scripts/run_train.py. Understand the data loading and threshold model.
Step 2: Implement scripts/lab_05_student_analysis.py that:
  - Loads data from data/sample/
  - Runs the intensity threshold model with threshold=0.5
  - Computes Dice coefficient per slice (not average)
  - Identifies the 3 slices with lowest Dice
  - Saves per-slice metrics to outputs/metrics/lab_05_per_slice_dice.json
    with keys: per_slice_dice (list), worst_slices (list[int]), mean_dice (float)
  - Writes a summary to reports/lab_05_agentic_coding.md
Step 3: Run the script. If it errors, diagnose and fix.
Step 4: Write status to outputs/status/lab_05_agentic_coding.json.

Use random seed 42. Run from repo root.
```

The second prompt gives Claude a specific implementation specification, not a vague goal. The per-slice requirement is explicit. The output schema is specified. The seed is fixed. The path convention follows CLAUDE.md.

---

## Clinical scenario

Your error analysis suggested that the segmentation model fails badly on certain slices — but you only have the aggregate Dice score. To design a meaningful next experiment (which variable to change, and why), you need to know which specific slices fail and by how much.

How do you use Claude Code to implement this analysis correctly, in a way that produces a result you can defend to your supervisor?

---

## Assignment

1. Confirm `data/sample/` exists: `make fetch-sample` if needed.
2. Paste the lab prompt into Claude Code.
3. After Claude writes `scripts/lab_05_student_analysis.py`, read it before you run it:
   - Does the path logic use `Path(__file__).resolve().parents[1]` as CLAUDE.md requires?
   - Does it compute per-slice Dice, not aggregate?
   - Is the random seed set to 42?
4. After the script runs, open `outputs/metrics/lab_05_per_slice_dice.json`.
   - What are the 3 worst slices?
   - Do these make anatomical sense? (Boundary slices, tumour edge slices?)
5. Write your findings in `reports/lab_05_agentic_coding.md`.

---

## Required artifacts

| Path | Contents |
|------|---------|
| `scripts/lab_05_student_analysis.py` | Per-slice analysis script |
| `outputs/metrics/lab_05_per_slice_dice.json` | `per_slice_dice`, `worst_slices`, `mean_dice` |
| `reports/lab_05_agentic_coding.md` | Summary with worst-slice interpretation |
| `outputs/status/lab_05_agentic_coding.json` | `status: "ok"` |

---

## Reflection questions

1. At which step in the agentic loop did Claude's choices most diverge from what you expected?
2. What would have gone wrong if you had accepted the first output without reading the script?
3. How is supervising Claude's agentic loop similar to supervising a junior research assistant?

---

## Extension

Ask Claude to add a visualisation: plot Dice per slice as a bar chart, highlight the 3 worst in red, save to `outputs/figures/lab_05_per_slice_dice.png`. Inspect the figure: what pattern do you see? Are the worst slices clustered or distributed?

---

## Success criteria

- `scripts/lab_05_student_analysis.py` exists and runs without error from the repo root
- `outputs/metrics/lab_05_per_slice_dice.json` has the three required keys with correct types
- `reports/lab_05_agentic_coding.md` includes an interpretation of the worst-slice results
- You can explain why you read the script before running it
