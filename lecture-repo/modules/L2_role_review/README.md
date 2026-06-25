# L2 — Role-Based Review

**Concept:** Switching from builder to critic  
**Time:** 40 min · Day 1  
**Prompt file:** `prompts/stage_07_challenge_plan.md`

---

## Why this lab exists

The person who built something is the worst person to review it. They know what they intended — so they see the intended behaviour rather than the actual behaviour. They are mentally committed to the design decisions they made — so they resist evidence that those decisions were wrong.

Claude has the same limitation. If you only ever ask Claude to build — to write code, to produce analysis, to train models — it adopts the builder's perspective. It is optimistic about your work because you framed the task as a building task.

Role switching fixes this. You tell Claude to adopt a specific, adversarial identity: a peer reviewer, a skeptical statistician, a clinical deployment engineer. That identity changes what Claude looks for. The output shifts from "here is what your model does" to "here is what your model fails to do."

The critical skill is writing a role prompt sharp enough to produce actionable criticism rather than generic hedging. "Act as a reviewer" produces platitudes. "You are a biostatistician preparing a protocol review for a clinical trial application. Assume the current method is insufficient until proven otherwise. Identify exactly three specific experiments the authors must run, with named metrics and threshold values." — that produces something you can act on.

---

## The clinical problem this addresses

In medical AI research, the consequence of blind spots is not just a lower Dice score — it is a method deployed before it is ready, in a clinical environment, on patients. Systematic adversarial review before advancement is not optional. This lab teaches you to build that review into your Claude workflow.

---

## Before / After

**Before:**
```
What do you think of my brain segmentation model? Is it good enough?
```

Claude gives a balanced assessment — noting some strengths, some limitations. It is optimistic because you framed the question as "is it good enough?" which invites a yes/no answer weighted toward yes.

**After:**
```
You are a clinical deployment engineer reviewing a brain tumour segmentation prototype
for potential use in a research pipeline. This is a Stage 1 feasibility review.

Assume nothing is validated. Read outputs/metrics/val_metrics.json and reports/train_notes.md.

Identify:
  1. What claims the current results support
  2. What claims they do NOT support
  3. Three additional experiments required before this method could appear in a publication

Write your review to reports/lab_02_role_review.md.

Be specific — no generic 'more data needed' statements.
Name each experiment, the metric it measures, and the threshold that would satisfy it.
Write status to outputs/status/lab_02_role_review.json with key: status='ok'.
```

The second prompt gives Claude a specific adversarial identity, a clear asymmetry (assume insufficient), and a concrete deliverable format. The "no generic statements" constraint forces specificity.

---

## Clinical scenario

You have trained a baseline segmentation model. Dice is 0.58 on the teaching set. Your supervisor asks: "Is this ready for the next stage?" 

How do you get an honest answer? You are not in a position to review your own work objectively — you spent the last two days building it.

---

## Assignment

1. Complete L5 (Agentic Coding) first to have `val_metrics.json` and `reports/train_notes.md`.
   (Or use the stub files in `reports/` if the pipeline hasn't run yet.)
2. Paste the lab prompt into Claude Code.
3. Read the review Claude produces. Do you agree with all three required experiments?
4. Write your own assessment in `reports/lab_02_role_review.md`: which criticism is most important, and why?
5. Answer the reflection questions.

---

## Required artifacts

| Path | Required key |
|------|-------------|
| `outputs/status/lab_02_role_review.json` | `status: "ok"` |
| `reports/lab_02_role_review.md` | Role-based critique with three specific experiments |

---

## Reflection questions

1. What did the role-switched Claude notice that you hadn't noticed yourself?
2. How does the specificity of the role description affect the quality of the critique?
3. When would you NOT want Claude in critic mode? Name a specific case where builder mode is more appropriate.

---

## The principle generalises

Role switching is not limited to criticism. Other useful roles:

| Role | Use case |
|------|---------|
| Clinician with no ML background | Checking whether technical claims translate honestly |
| Patient | Whether plain language explanations are actually plain |
| Grant reviewer | Whether the proposed contribution is overstated |
| Reproducibility auditor | Whether another lab could reproduce your result from your methods section |
| Ethics reviewer | Whether the proposed deployment has adequate safeguards |

Each role shifts what Claude attends to. The skill is choosing the right role for the blind spot you most need to address.

---

## Success criteria

- `outputs/status/lab_02_role_review.json` exists with `status: ok`
- `reports/lab_02_role_review.md` contains a critique with three specific, named experiments (not generic suggestions)
- You can articulate what the role constraint changed compared to a generic "review this" prompt
