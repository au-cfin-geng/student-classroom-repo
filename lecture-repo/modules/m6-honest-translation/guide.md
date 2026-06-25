# M6 — Honest Translation

## 1. Module Identity

Clinical AI research has a translation problem. Researchers produce numbers — Dice scores, sensitivity values, AUC curves — and then must communicate those numbers to audiences who lack the statistical vocabulary to interpret them. The usual result is compression: nuance gets stripped, caveats get dropped, and prototype performance gets restated as clinical capability. This is not fraud. It is what happens when the researcher has no explicit framework for translation fidelity.

This module addresses that problem through a specific Claude capability: multi-audience translation with honesty constraints. The core principle is that Claude will produce output shaped by the constraints you give it. A prompt that omits limitations will produce output that omits limitations. A prompt that requires limitations to precede benefits will produce output where limitations precede benefits. The honesty of the translation is a function of the honesty architecture of the prompt.

---

## 2. Before / After

**Old workflow — unconstrained translation:**

A researcher finishes a segmentation experiment. Dice = 0.72. They ask a colleague to help write a one-paragraph clinical summary. The colleague writes: "Our model achieves 72% accuracy in detecting brain tumours from FLAIR MRI, demonstrating strong potential for clinical integration." No one flags this as wrong. It sounds reasonable. It is not reasonable. The Dice coefficient is not accuracy. Detection is not segmentation. Seventy-two percent on ten teaching slices says nothing about clinical integration. The paragraph will appear in a grant proposal and be read by a clinician with no way to know what it actually means.

**Claude-assisted workflow — constrained translation:**

The researcher prompts Claude with explicit audience identification and an honesty constraint: "You are a clinical translator preparing a memo for a neurosurgery attending. You are bound by the following rule: you must state all limitations before stating any clinical implications. The metric is Dice coefficient (not accuracy). The dataset is ten teaching slices from BraTS, not a clinical cohort. Write the translation." Claude produces output that opens with the constraint architecture, names the prototype status explicitly, and does not use the word "accuracy" in place of Dice. The researcher reads it and finds it less exciting than the unconstrained version. That is the correct result.

---

## 3. The Prompt Principle

**Name the audience and give it an honesty constraint.**

A prompt that says "describe the clinical implications of this result" will produce clinical implications. A prompt that says "you are a clinical translator who is required to state limitations before benefits, writing for a neurosurgery attending who will make decisions based on this memo" will produce something structurally different — and safer.

The honesty constraint is not optional. It is not a nice-to-have. It is the mechanism by which you prevent the translation from drifting into overclaiming. Without it, Claude will optimise for a coherent, readable narrative, and coherent readable narratives about AI in medicine tend to overclaim.

**Before (unconstrained):**

```
Write a clinical summary of our brain tumour segmentation results for a medical audience. 
Dice score was 0.72.
```

**After (constrained):**

```
You are a clinical translator preparing a formal memo for a neurosurgery attending physician.

You are bound by the following honesty requirements:
1. State all limitations before stating any clinical implications
2. Explicitly distinguish prototype from deployment-ready system
3. Do not use the word "accuracy" in place of Dice coefficient
4. Include a specific gap analysis: what would need to be true for this to become a clinical tool

The experiment: intensity-threshold brain tumour segmentation on 10 teaching slices from BraTS (public dataset, not a clinical cohort). Dice coefficient = 0.72 on this dataset.

Write the translation memo. It should be direct and not promotional.
```

The second prompt constrains the output architecture before Claude writes a word. The limitations come first because the prompt requires it, not because Claude chose to include them.

---

## 4. The Clinical Scenario in This Course

At this point in the course, you have a complete pipeline: data ingested, algorithm implemented, metrics computed, figures generated, and a reviewer-mode critique of your methodology. Your Dice coefficient is on record. You now need to produce one written artifact that translates this work honestly for a clinical audience.

The scenario: a neurosurgery attending has asked you to summarise what your segmentation experiment found and whether it has any clinical relevance. They have ten minutes. They will read your memo once. They will not ask follow-up questions. What you write is what they will know.

This is not a hypothetical. Every clinical AI paper eventually produces a clinical audience encounter of exactly this structure. The attending reads the abstract. They read the conclusion. They form a judgment. Your job is to ensure that judgment is calibrated to what the work actually is: a teaching prototype on a small public dataset, with a specific quantitative result, and a specific gap between that result and clinical deployment.

You will use Claude as the translation engine, but you will architect the prompt. You will run `make translation-memo` and inspect the output. You will verify that the memo contains what it is required to contain. If it does not, you will revise the prompt until it does.

---

## 5. Assignment

**Artifact:** `reports/translation_memo.md`

**Make target:** `make translation-memo`

**Stage file:** `prompts/stage_09_translation_memo.md`

**Status output:** `outputs/status/stage_09_translation_memo.json`

The translation memo must contain all of the following. These are not suggestions — they are pass/fail criteria:

- **Clinical readiness status:** An explicit statement of whether this system is ready for clinical use. (It is not. The memo must say so.)
- **Stated limitations:** At minimum: dataset size (10 slices), dataset type (teaching set, not clinical cohort), algorithm type (intensity threshold, not learned), metric interpretation (Dice coefficient and what it does and does not measure).
- **Specific gap analysis:** A named list of what would need to be different for this prototype to move toward clinical deployment. This is not vague ("further validation needed") — it names specific gaps (prospective cohort, radiologist comparison, multi-site data, regulatory pathway).
- **Prototype-vs-deployment distinction:** An explicit sentence that distinguishes the current system (teaching prototype) from a deployment-ready clinical tool. This sentence must appear in the memo. It cannot be implied.

The memo should be 400-600 words. It should read like a professional clinical communication, not a promotional summary. If it sounds like a press release, the prompt needs revision.

---

## 6. Reflection Questions

Answer these in your own words after completing the module. There are no correct answers — these questions are designed to surface your reasoning.

1. When you read the translation memo Claude produced, what did you find yourself wanting to add back in — what caveats or qualifications felt like they were missing? What does that tell you about the default direction of drift in clinical AI communication?

2. The prompt principle for this module says the honesty constraint must be in the prompt. Why can't you rely on Claude to include limitations on its own, without explicit instruction? What would you need to believe about language models to think that was a safe assumption?

3. Consider the specific gap analysis in your memo. If you were a clinician reading it, what would you need to see addressed — in what kind of study, with what kind of evidence — before you would trust a system like this in your workflow? How does writing that gap analysis from the inside change how you think about what your research is actually doing?

---

## 7. Transfer to Your Own Research

The translation pattern in this module is not specific to brain tumour segmentation or Dice coefficients. Every quantitative clinical AI result eventually requires a translation encounter: a grant proposal, a conference abstract, a clinical collaborator email, a regulatory submission. In each case, the same failure mode is available — compression of nuance, substitution of familiar terms for precise ones, omission of limitations under time pressure.

The transferable skill is prompt architecture for constrained translation. Before you ask Claude to translate any research result for any clinical audience, establish:

- Who the audience is (role, background, decision-making context)
- What the honesty constraints are (what must be said, in what order, what words are prohibited)
- What the prototype-vs-deployment status is (explicit, not implied)
- What the gap analysis requires (specific, not vague)

This applies to radiology AI, pathology AI, risk prediction models, genomic screening tools — any context where a quantitative prototype result must be communicated to a clinical decision-maker. The pattern does not change. Only the domain-specific content changes.

If you work on AI that will ever touch a clinical environment, you will be asked to translate your results. Building the honesty constraint into the translation prompt is not additional work. It is the minimum responsible workflow.

---

## 8. Success Criteria

The following constitutes good work for this module:

- The memo opens with clinical readiness status and limitations — not with the Dice score or a claim about what the model "achieves"
- The word "accuracy" does not appear as a synonym for Dice coefficient
- The gap analysis contains at least three specific, named gaps — not generic statements about further validation
- The prototype-vs-deployment distinction appears as an explicit sentence, not as an implication
- The memo could be handed to a neurosurgery attending with no additional explanation and they would come away with a calibrated understanding of what this work is and is not
- The prompt in `stage_09_translation_memo.md` contains explicit honesty constraints, not just an instruction to "write a clinical summary"

If the memo reads like it is selling something, it is wrong. If it reads like it is hiding something, it is also wrong. Good clinical translation is the memo a careful, honest researcher would have written themselves — produced faster, and with a documented prompt that makes the translation architecture auditable.
