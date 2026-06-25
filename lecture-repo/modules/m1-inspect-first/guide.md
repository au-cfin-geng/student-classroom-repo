# M1 — Inspect Before You Model

## Module Identity

Clinical AI projects fail in a specific, recurring pattern: the researcher opens the data, runs a model, sees a number, and treats the number as meaningful. What they have skipped is the inspection step — the systematic act of looking at the data before computing anything. In brain tumour segmentation from FLAIR MRI, this omission is consequential. FLAIR intensities vary by scanner, acquisition protocol, patient age, and preprocessing pipeline. A threshold that produces a Dice of 0.72 on your training slices may be responding to scanner-specific intensity drift rather than tumour signal. You will not know this unless you looked first.

This module introduces Claude as a data steward: an agent that reads, describes, and flags concerns about data before any analysis begins. The Claude capability at the centre of this module is structured inspection — using prompts that explicitly defer computation and demand observation. The principle is simple and enforceable: Claude should not touch a model parameter until it has told you what it found.

---

## Before / After

**Before (typical workflow):**

A researcher receives a new dataset. They run their existing preprocessing pipeline. They inspect a few slices visually, decide the data looks reasonable, and fit their model. Data notes are never written down. Problems surface weeks later during result review, when tracing them back to data issues is expensive.

**After (Claude-assisted workflow):**

The researcher asks Claude to inspect the data files before any script is run. Claude reads the FLAIR array dimensions, checks for NaN or inf values, reports intensity distribution statistics, identifies whether masks are binary, and flags any inconsistencies. This inspection is written into a structured notes file. The researcher reviews it before proceeding. Anomalies caught at this stage — a slice with an all-zero mask, an unusually compressed intensity range — are addressed before they silently corrupt the experiment.

---

## The Prompt Principle

**Principle:** Inspection is not overhead — it is part of the experiment. Ask Claude to read, describe, and flag concerns before any computation begins.

This requires a deliberate prompt structure. The default tendency — "load the data and run the analysis" — collapses inspection and computation into a single step. Breaking them apart is a discipline, enforced through the prompt.

**Before (collapsed prompt):**

```
Load the BraTS FLAIR slices and run the segmentation algorithm.
```

This prompt grants Claude permission to skip past the data entirely. It will. It will load, threshold, and report a Dice score, and you will have no record of what the data actually looked like.

**After (inspection-first prompt):**

```
Before running any algorithm, inspect the loaded FLAIR data. Report:
- Array shape and dtype for each slice
- Intensity min, max, mean, and any values outside [0, 1] or [0, 4095] depending on normalization
- Whether the tumour masks are binary (0/1 only)
- Any slices where the mask is empty or nearly empty
- Anything that looks anomalous or that you would flag before trusting a model's output on this data

Do not run the segmentation yet. Write your findings to reports/data_notes.md.
```

The difference is not cosmetic. The second prompt creates a checkpoint. Nothing runs until the inspection is complete and reviewed.

---

## The Clinical Scenario in This Course

In this module, students receive ten FLAIR MRI slices from the BraTS dataset. The task is not to segment tumour — not yet. The task is to understand what you are about to model.

Students run two make targets:

- `make fetch-sample` — downloads the ten teaching slices from the course data store and places them in the expected directory structure
- `make visualize` — runs the visualization script, which overlays the tumour mask on the FLAIR image for each slice and saves the figures to `outputs/figures/sample_overlay.png`

These targets correspond to stages `stage_01_fetch_sample` and `stage_02_load_visualize` in the prompt sequence. The student's job is to prompt Claude to inspect the data at each stage and document findings, rather than treating the fetch and visualize steps as mechanical prerequisites to get through on the way to modeling.

Concretely: after running `make visualize`, the student should not immediately proceed to the segmentation module. They should have Claude examine the overlay figures and the underlying arrays, ask questions about intensity range and mask quality, and record what was found. This record is what makes the later experiment interpretable.

---

## Assignment

**Artifact to produce:** `reports/data_notes.md`

**Make targets:** `fetch-sample`, `visualize`

**What the artifact must contain:**

1. A description of the dataset: number of slices, image dimensions, modality, source
2. Intensity statistics for the FLAIR images: range, approximate distribution, any normalization that appears to have been applied
3. Mask quality notes: are all masks binary? Are there slices with very small or empty tumour regions? What fraction of voxels are tumour-positive across the ten slices?
4. Visual inspection notes: looking at the overlays in `outputs/figures/`, do the masks appear to align with visible hyperintensity? Any slices where the overlay looks misaligned or suspicious?
5. At least one flagged concern — something about the data that the student would want to verify or account for before modeling

The notes do not need to be long. They need to be honest and specific. "Data looks fine" is not an acceptable finding. "Slice 7 has a mask covering 0.3% of the image area, which is substantially smaller than the others — worth checking whether this is a genuine small tumour or a labeling edge case" is the kind of finding this module is designed to produce.

---

## Reflection Questions

After completing the module, students answer the following in their own words:

1. What did you find in the data that you would not have noticed if you had gone straight to modeling? Be specific about at least one finding.

2. The prompt principle for this module says "inspection is not overhead — it is part of the experiment." In your own research context, describe a case where skipping inspection either caused a problem or could have caused one.

3. What is the difference between having Claude produce a visualization and having Claude inspect the visualization? Why does the distinction matter?

---

## Transfer to Your Own Research

The prompt pattern in this module — defer computation, demand observation, document findings before proceeding — applies anywhere you work with clinical data for the first time.

In radiomics studies, it corresponds to checking feature distributions before fitting models: are your texture features normally distributed? Do some features show bimodal distributions that suggest acquisition differences across sites? In EHR-based studies, it corresponds to characterizing missingness before imputation: which variables are missing, at what rate, and does the missingness pattern look random or structured? In survival analysis, it corresponds to examining event rates and follow-up time distributions before selecting a model form.

The Claude capability being practiced here — ask Claude to read and describe before it computes — generalises directly. Any dataset you receive from a collaborator, download from a public repository, or extract from a clinical system deserves this step. The question to ask before every new analysis: "Claude, what do you actually see in this data before we do anything with it?"

---

## Success Criteria

Strong work in this module looks like:

- `reports/data_notes.md` exists, is specific, and contains at least one non-obvious finding
- The student prompted Claude to inspect data before running algorithms, not after
- The overlay figures in `outputs/figures/` were examined and commented on, not just generated
- At least one concern was flagged that would be worth addressing before the segmentation module
- The reflection answers are substantive and specific, not generic restatements of the module premise

Weak work looks like: a data notes file that lists dimensions and dtype and nothing else; reflection answers that paraphrase the module text; overlay figures that were generated but not examined. The point of this module is not to complete a checklist. It is to develop the habit of looking before acting — a habit that distinguishes careful clinical AI research from fast, fragile pipelines.
