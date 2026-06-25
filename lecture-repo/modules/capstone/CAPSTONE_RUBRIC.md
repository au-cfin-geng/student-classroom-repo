# Capstone Rubric — Clinical Claude

**Total: 100 points**

The capstone is graded on process quality, scientific reasoning, and artifact-grounded judgment — not on Dice score. A capstone that produces a lower Dice than the M4 baseline but reasons about that result carefully and honestly scores higher than one that improves Dice without explanation.

---

## Dimension 1 — Research Question (15 points)

**What is being assessed:** Is the research question clear, specific, and clinically motivated?

| Score | Description |
|-------|-------------|
| 13–15 | Specific, falsifiable question with explicit clinical motivation. Names what would count as a meaningful result. |
| 9–12 | Clear question, but motivation is generic ("improve performance") or clinical relevance is not stated. |
| 5–8 | Vague question ("explore different approaches"). No clear success criterion. |
| 0–4 | No identifiable research question, or question is just "run the pipeline again." |

**Evidence to look for:** A written statement of the research question in the capstone report or `reports/challenge_plan.md`.

---

## Dimension 2 — Prompt Workflow Quality (15 points)

**What is being assessed:** Did the student use structured, well-specified prompts? Is there evidence of the seven Claude principles from M0–M6?

| Score | Description |
|-------|-------------|
| 13–15 | Prompts include explicit output contracts, role assignment, or inspection-before-action. Evidence of at least two distinct Claude principles applied. |
| 9–12 | Prompts are functional but generic. Output paths are specified but no explicit role switching or inspection pattern. |
| 5–8 | Prompts are vague. Outputs were produced but the prompts that generated them would not teach anything. |
| 0–4 | No evidence of structured prompting. Pipeline was likely run manually or by copying a prompt verbatim with no adaptation. |

**Evidence to look for:** Prompt transcript in `.lab_history/`, Layer B reflection in the report, or visible evidence of prompt patterns from the module guides.

---

## Dimension 3 — Artifact Quality (15 points)

**What is being assessed:** Are the required capstone artifacts present, valid, and non-trivial?

| Score | Description |
|-------|-------------|
| 13–15 | All required artifacts present. Figures are informative (not empty, not identical to M4 outputs). Metrics contain valid values with correct schema. |
| 9–12 | Required artifacts present but some are stub-level (minimal content, repeated from earlier modules). |
| 5–8 | Some artifacts missing or structurally invalid. |
| 0–4 | Fewer than half the required artifacts present. |

**Minimum capstone artifacts:**
- At least one new figure beyond M4's `model_swap_comparison.png`
- A metric file with before/after comparison
- A written report (`reports/adapt_pipeline.md` or student-named equivalent)

---

## Dimension 4 — Experimental Design (20 points)

**What is being assessed:** Was the capstone a controlled experiment? Was exactly one variable changed with a stated rationale?

| Score | Description |
|-------|-------------|
| 17–20 | One variable changed. Explicit before/after comparison with the same metric. Rationale tied to M3 failure hypothesis. Negative results honestly reported. |
| 12–16 | Controlled change, but rationale is weak or not tied to evidence from M3. |
| 7–11 | Multiple things changed simultaneously, making attribution impossible. Or: comparison made but baseline not preserved. |
| 0–6 | No controlled experiment. Student ran the pipeline with different parameters without any systematic comparison. |

**Key question for the instructor:** Can the student point to exactly one thing that changed and explain why it was expected to help, based on the M3 failure hypothesis?

---

## Dimension 5 — Failure Analysis and Limitation Honesty (20 points)

**What is being assessed:** Does the student accurately describe what went wrong, why, and what the limitations of their investigation are?

| Score | Description |
|-------|-------------|
| 17–20 | Specific failure cases identified with visual evidence. Failure hypothesis is falsifiable and tied to artifact evidence (specific slice indices, error patterns). Limitations are stated honestly and specifically. |
| 12–16 | Failure noted and described, but hypothesis is vague ("the model fails on hard cases"). Limitations stated but generic. |
| 7–11 | Failure acknowledged but not analyzed. Report says performance was poor without explaining how or why. |
| 0–6 | No failure analysis. Report implies the capstone was successful regardless of actual metrics. |

**Key question:** If the result was worse than the baseline, does the student explain why rather than hiding it?

---

## Dimension 6 — Clinical Translation Judgment (10 points)

**What is being assessed:** Does the student accurately place their capstone on the spectrum from toy pipeline to clinical contribution — without overclaiming?

| Score | Description |
|-------|-------------|
| 9–10 | Clear, honest statement of what the prototype can and cannot support clinically. Explicit gap between current results and clinical deployment readiness. Limitations named before conclusions. |
| 6–8 | Translation present but mild overclaiming ("promising results for clinical use"). |
| 3–5 | Generic clinical framing without specific evidence ("this could help clinicians"). |
| 0–2 | Clinical claims unsupported by the results, or no translation attempted. |

---

## Dimension 7 — Showcase Presentation (5 points)

**What is being assessed:** Can the student explain their work clearly in 5 minutes to a non-ML audience?

| Score | Description |
|-------|-------------|
| 5 | Shows the error analysis figure, states the failure hypothesis in plain language, names one honest limitation. Clear narrative from question to result. |
| 3–4 | Covers the key points but relies on jargon, or the limitation statement is superficial. |
| 1–2 | Presentation covers what was done but not why it matters or what failed. |
| 0 | Did not present, or presentation only discussed Dice score without failure analysis. |

**Hard requirement:** The showcase must include a failure analysis figure and a stated limitation. A presentation that only discusses Dice improvement scores 0–2 on this dimension regardless of result quality.

---

## Grading notes

**Do not penalize a lower Dice score** unless the student's explanation of it is absent or dishonest.

**Reward honest reporting of negative results.** A capstone that found no improvement but explains clearly why is better science than one that found improvement it cannot explain.

**Check the commit history.** A single commit at the deadline loses points on Dimension 2 (prompt workflow quality) and Dimension 4 (experimental design) because there is no evidence of iterative process.

**The translation memo is the hardest part.** Most first-draft memos overclaim. If the student's memo would embarrass a clinical collaborator who read it, ask them to revise before accepting.
