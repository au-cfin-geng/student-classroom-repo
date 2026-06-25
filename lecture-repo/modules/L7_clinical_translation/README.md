# L7 — Clinical Translation

**Concept:** Audience-aware writing with honesty constraints  
**Time:** 40 min · Day 2  
**Prompt file:** `prompts/stage_09_translation_memo.md`

---

## Why this lab exists

A research result is not a single document. It is a set of claims that must be calibrated differently for different audiences. The same Dice coefficient of 0.58 means something different to:

- A machine learning engineer (is this above the literature baseline for intensity-threshold methods?)
- A radiologist (how does this compare to a junior resident's performance on the same task?)
- A hospital administrator (can this replace or support our current workflow?)
- A grant reviewer (does this justify the proposed next phase of funding?)
- A patient (will this help detect my tumour?)

Claude can translate fluently across these registers. The problem is that without explicit constraints, Claude tends toward optimistic framing. Claude is helpful — and "helpful" in a translation context often means smoothing over uncertainty and emphasising positive findings. A clinical AI memo written by Claude without honesty constraints will typically read as more confident than the underlying evidence warrants.

The solution is the **honesty constraint list**: explicit statements of what the text must NOT say. These constraints override Claude's default helpful optimism. "Do not claim clinical deployment readiness. Do not omit the failure cases. Do not compare to other methods without citations." — these constraints are what separate a responsible clinical AI communication from a marketing document.

---

## The clinical problem this addresses

A clinical AI research team shares a "promising preliminary results" memo with a hospital partner. The memo, written with Claude, glosses over the failure cases and frames a Dice of 0.58 as "strong performance." The hospital invests three months in a deployment study. The failure cases emerge in the real-world data and the partnership collapses. The problem was not the Dice score — it was the translation.

This failure is common. It is preventable with explicit honesty constraints in the writing prompt.

---

## Before / After

**Before:**
```
Write a summary of my brain tumour segmentation results for a clinical collaborator.
```

Claude writes a fluent, optimistic summary. It mentions the Dice score and notes "limitations," but the framing treats the prototype as more ready than it is. A radiologist reading this memo might develop false expectations about what the system can do.

**After:**
```
You are a clinical AI research communicator.

Write a clinical collaborator briefing about this brain tumour segmentation study.
Audience: radiologist with no ML background, considering a research collaboration.
Tone: honest, specific, measured. Length: approximately 400 words.

You MUST include:
  - What the method is (plain English, no jargon)
  - The exact Dice coefficient (from outputs/metrics/val_metrics.json)
  - The specific failure cases identified (from reports/error_analysis.md)
  - What additional validation would be required before clinical consideration

You MUST NOT:
  - Claim the method is ready for clinical use
  - Compare to other methods without citing them
  - Omit the failure cases
  - Use ML jargon without explaining it
  - Round the Dice score above its actual value

Write to reports/lab_07_clinical_translation.md.
Write status to outputs/status/lab_07_clinical_translation.json.
```

The second prompt specifies the audience precisely, sets a length that forces prioritisation, and includes both a MUST list and a MUST NOT list. The MUST NOT list is the critical addition — it is the honesty constraint.

---

## Clinical scenario

Your supervisor is meeting a clinical radiologist next week. She asks you to prepare a one-page briefing on your brain tumour segmentation work. The radiologist has no ML background and is evaluating whether to participate in a follow-up study.

How do you write something that honestly represents what you have — not overselling the prototype, not underselling the work, not burying the failure cases in qualifications the radiologist won't notice?

---

## Assignment

1. Have `outputs/metrics/val_metrics.json` and `reports/error_analysis.md` available.
   (From L5/L6 or legacy pipeline. Use stubs if needed.)
2. Paste the lab prompt into Claude Code.
3. Read Claude's output critically:
   - Did it include the exact Dice coefficient?
   - Did it name the specific failure cases, or use vague language like "some limitations"?
   - Did it claim or imply clinical readiness?
4. If Claude violated any MUST NOT constraints, add those violations to your reflection.
5. Write your final assessment: would you be comfortable sharing this memo with an actual clinical collaborator?

---

## Required artifacts

| Path | Contents |
|------|---------|
| `reports/lab_07_clinical_translation.md` | Clinical collaborator briefing (~400 words, audience-appropriate) |
| `outputs/status/lab_07_clinical_translation.json` | `status: "ok"` |

---

## Reflection questions

1. Did Claude violate any of the MUST NOT constraints on the first run? Which ones?
2. Why does a radiologist need a different document than an ML engineer, even if the facts are identical?
3. Name a communication failure in clinical AI research that could have been prevented by an honesty constraint in the writing prompt.

---

## The four-audience exercise (extension)

Write the same result for four audiences using four separate prompts:
1. ML conference abstract
2. Clinical collaborator briefing (this lab)
3. Grant committee summary
4. Patient-facing plain language explanation

Compare what stays constant (the Dice score, the failure cases) and what changes (the framing, the emphasis, the language level). This exercise reveals how much of research communication is legitimate contextualisation versus problematic spin.

---

## Success criteria

- `reports/lab_07_clinical_translation.md` names the exact Dice coefficient and describes specific failure cases
- The document does not claim clinical deployment readiness
- You can identify which part of the prompt — MUST or MUST NOT — most changed Claude's output
- You would be comfortable showing the memo to a clinical collaborator
