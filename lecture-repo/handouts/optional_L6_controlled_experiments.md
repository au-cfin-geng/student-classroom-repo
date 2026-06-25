# L6 (Extension): Controlled Experiments

**Course:** Agentic Clinical Research Studio
**Session type:** Optional extension lab
**Estimated time:** 90 minutes
**Prerequisites:** Completion of L1-L5

---

## 1. Opening Story

Priya is a third-year PhD student in medical imaging, eight months from her thesis submission. She has been working on a deep learning pipeline to automatically segment glioblastoma on post-contrast MRI scans. Over six weeks she has run perhaps forty training runs, tweaking things as she goes: adjusting the learning rate here, swapping a loss function there, changing the data augmentation settings after reading a new preprint, and at one point rewriting the preprocessing step because she noticed the intensity normalisation looked wrong.

Her latest model reaches a Dice score of 0.78 on the held-out test set. When she started six weeks ago the baseline was 0.71. That is a real and meaningful improvement. Her supervisor is pleased. Her progress report says the model improved by seven Dice points.

Two weeks later, her supervisor asks a pointed question during the group meeting: which of those changes actually drove the improvement? Priya opens her experiment log, which is a single spreadsheet with inconsistent column names and several rows where she noted only "tried new config." She cannot answer the question. She cannot tell whether the gain came from fixing normalisation, from the loss function change, from the augmentation strategy, or from some combination. For her thesis methods chapter, and certainly for any eventual publication, this is a serious problem. She has results. She does not have findings.

---

## 2. The Old Workflow

Without agentic AI, a researcher approaching an experimental comparison would typically:

- Run a "baseline" model once, record the number informally in a notebook or spreadsheet
- Make several changes simultaneously between runs because it feels more efficient
- Note the new result and compare it to the earlier number, attributing the change to whichever modification felt most important
- Repeat this process over weeks, accumulating a log where many runs have undocumented settings
- Realise at paper-writing time that intermediate runs cannot be compared because their conditions differed in multiple ways
- Re-run selected experiments from scratch to produce a clean-looking ablation table, often with subtle differences from the original runs due to non-determinism or code changes
- Write up results in which the ablation table and the narrative describe different experiments

---

## 3. The Agentic Workflow

With an agentic AI assistant and the discipline introduced in this lab, the same researcher would:

- Document a frozen baseline: specific code version, data split, random seed, hyperparameters, and evaluation metric — before any changes are made
- Write an experiment prompt to the agent that names exactly one variable to change and explicitly freezes all others: "Change ONLY the loss function from cross-entropy to Dice loss. Do not alter the learning rate, augmentation pipeline, preprocessing, or architecture."
- Have the agent run the controlled experiment, record results in a structured log alongside the baseline, and return a plain-language comparison
- Review the before/after metrics, including cases where the change made no difference or made things worse
- Commit that result as a named, versioned experiment before moving to the next variable
- Build an ablation table incrementally, one row at a time, where every row corresponds to an interpretable and reproducible change
- Write a methods section in which every claim maps to a specific, traceable experiment

---

## 4. Core Concept

A controlled experiment isolates one variable. This is not a new idea — it is the foundational logic of scientific inference. What changes in the context of computational AI research is that the temptation to change multiple things at once is unusually strong, and the tools that make changes easy (version control, config files, automated retraining) also make it easy to lose track of what changed between runs.

The discipline of controlled experimentation in AI research means three things in practice. First, you must establish and document a genuine baseline before you begin varying anything. The baseline is not just a number; it is a complete and frozen description of the system that produced that number. If you cannot recreate your baseline from your documentation alone, you do not have a baseline. Second, each experimental run must change exactly one thing relative to the previous run or relative to the documented baseline. The constraint "change ONLY X" should be written explicitly — not assumed. When you ask an AI agent to run an experiment, that constraint must appear in the prompt. Agents are good at following explicit instructions and poor at inferring unstated ones.

Third, you must record and report all results, including results where your intervention had no effect or made things worse. Negative results are scientifically valid. They are also methodologically essential: if you only report the runs that improved performance, your ablation table is not an ablation table — it is a selection of successes that cannot support a causal claim. A reader cannot tell whether your design choices improved the system or whether you simply ran enough variants that some happened to be better by chance.

For medical AI, the stakes of interpretable experiments are higher than in most fields. A model that reaches clinical deployment on the basis of an uninterpretable development process is a model whose behaviour in distribution shift cannot be predicted or explained. Understanding which components drive performance is not academic rigour for its own sake; it is a prerequisite for safe, auditable clinical AI.

---

## 5. Clinical Example

Suppose you are developing an automated MRI analysis pipeline to distinguish low-grade from high-grade glioma using radiomics features extracted from pre-operative scans. Your current pipeline has a held-out AUC of 0.81. You want to improve it.

You have identified four candidate changes: (a) add a new set of texture features from the peritumoral region, (b) switch from a random forest to a gradient boosting classifier, (c) apply z-score normalisation per patient rather than per cohort, and (d) remove scanner-site as a feature due to concerns about data leakage.

If you implement all four changes at once and reach AUC 0.85, you know the combination helped. You do not know whether any single change drove the improvement, whether any of the changes was harmful and masked by the others, or whether removing the scanner-site feature (the ethically motivated change) cost you performance that was then recovered by one of the others.

A controlled experiment answers these questions one at a time. You start with your frozen baseline. You add peritumoral features only; AUC moves to 0.83. You then switch the classifier with everything else held constant; AUC stays at 0.83. You apply per-patient normalisation; AUC moves to 0.86. You then remove scanner-site; AUC drops to 0.84. Now you have an interpretable picture. The normalisation change drove most of the gain. The classifier change had no measurable effect. Removing the leakage-prone feature costs two points of AUC — a cost you can report honestly and defend ethically. That is a finding. You can write it, defend it, and clinicians can act on it.

---

## 6. In-Class Activity

**Duration:** 15-20 minutes
**Format:** Pairs or small groups of 2-3

**Setup:** Each group will design a mini controlled experiment for a hypothetical AI pipeline. You do not need to run code; this is a design exercise.

**Scenario:** You are working on a clinical NLP pipeline that extracts diagnosis codes from discharge summaries. Your current baseline F1 score on a 200-note test set is 0.74. You want to improve it. You have the following list of candidate changes:

- Swap from a rule-based extraction system to a prompted LLM
- Pre-process notes to remove boilerplate headers
- Expand the synonym dictionary for cardiovascular terms
- Change the evaluation metric from exact match to partial match

**Step 1 (5 minutes):** As a group, identify the single most interpretable experiment you would run first. Write down: (a) exactly what changes, (b) exactly what stays the same, and (c) what the prompt instruction to your AI agent would be, using the phrase "change ONLY."

**Step 2 (5 minutes):** Now identify one change in the list that is not an experiment variable — it is a change to the evaluation criteria. What is the problem with running this change as if it were a normal experiment? Discuss what you would need to do before changing the metric.

**Step 3 (5 minutes):** Consider a result in which your first experiment makes no difference — F1 stays at 0.74. Write a two-sentence honest interpretation of that result. What does it tell you? What does it not tell you?

**Debrief:** Groups share their Step 1 prompt and their Step 3 interpretation. The facilitator highlights cases where the "change ONLY" constraint was well-specified and cases where it was ambiguous.

---

## 7. Artifact Contract

The following files constitute a passing artifact for this lab. All files should be placed in `outputs/L6/`.

| File | Format | Passing standard |
|------|--------|-----------------|
| `baseline.json` | JSON | Contains: model or pipeline version identifier, all key configuration parameters, evaluation metric name and value, data split description, random seed if applicable, and date run |
| `experiment_log.md` | Markdown table | One row per run. Columns: run ID, change from baseline (one item only), result, comparison to baseline (delta), and pass/fail flag for the "single variable" constraint |
| `controlled_prompt.txt` | Plain text | The exact prompt used to instruct the agent for at least one experimental run. Must contain the phrase "change ONLY" and must explicitly name at least two things that are held constant |
| `interpretation.md` | Markdown | 200-400 words. Interprets all results including any null or negative results. Does not attribute combined improvements to single changes. States explicitly what remains unresolved |

A submission fails if: the experiment log contains any run where more than one variable changed; the interpretation omits negative or null results; the baseline file is incomplete or was created after the experimental runs.

---

## 8. Common Failure Modes

**Changing the baseline retroactively.** After a run improves performance, researchers sometimes update the baseline documentation to match the new configuration "for clarity." This destroys the comparison. Your baseline documentation must be written and committed before any experimental run, and it must not be changed afterwards. If you discover the baseline was wrong or incomplete, document a new clean baseline as a separate named entry and restart the comparison from there.

**Treating metric changes as experimental results.** Switching from exact-match to partial-match F1 is not an experiment — it is a redefinition of what you are measuring. It cannot produce a meaningful before/after comparison because the before and after are measuring different things. Any change to the evaluation procedure requires a fresh baseline measured under the new procedure before any variable experiments begin.

**Conflating "no effect" with "failure."** When an intervention produces no measurable change, researchers sometimes discard that run and quietly try something else. A null result is data. It tells you that the variable you changed does not matter — at least not in isolation, at least on this dataset. Record it. A paper that reports a null result for one ablation and a positive result for another is more credible, not less, than a paper where every row of the ablation table shows an improvement.

**Under-specified "change ONLY" constraints.** Telling an agent to "change only the loss function" is ambiguous if the learning rate schedule interacts with the loss function and the agent adjusts it as a side effect. Effective controlled prompts name not just the one thing that changes but the specific things that must not change. The more dependencies exist in your pipeline, the more explicit this list must be.

**Ignoring non-determinism.** Many AI training procedures have stochastic elements. A difference of 0.002 AUC between two runs may be smaller than run-to-run variance. Before interpreting any result as meaningful, establish whether your experimental setup is deterministic (fixed seed, deterministic operations) or stochastic, and if stochastic, whether you have enough replications to distinguish signal from noise. A single run comparison is only interpretable if you have evidence that the variance is small relative to the difference you observe.

---

## 9. Responsible Use

Controlled experimental discipline is not merely a methodological nicety; it is a form of scientific integrity. When a medical AI model reaches deployment, clinicians and regulators will ask: what is this system's performance on the relevant population, and why does it perform as well as it does? If the answer to the second question is "we are not sure which design choices mattered," then the model's behaviour in novel settings — new scanners, different patient demographics, updated clinical workflows — cannot be reliably predicted. Interpretable development is not a research luxury; it is a prerequisite for trustworthy clinical translation.

There is a specific concern around publication and reporting. In computational medicine, there is strong incentive to report clean, improving ablation tables. If your workflow allows you to run many variants and select only the ones that improved performance, you are engaging in a form of selective reporting that inflates apparent performance and misleads readers about which design choices are important. Pre-registration of your experimental plan — naming in advance which variables you will test and in which order — is one way to mitigate this, particularly for clinical studies. Even without formal pre-registration, maintaining a complete and honest experiment log, including all null and negative results, fulfils the same purpose and should be considered a minimum standard of practice.

Finally, be explicit with your AI agent about the constraints of the task. Agents will follow the instructions you give them. If your prompt does not specify what must not change, the agent will not protect it. The responsibility for experimental design remains with you. The agent executes; you design, interpret, and are accountable. No agentic tool changes the fact that your name is on the paper.

---

## 10. Further Learning

This section lists categories of literature to search and resources to verify before releasing this handout. No paper titles, author names, or DOIs are provided here, as these have not been independently verified.

**Literature to search:**

- Search "ablation study clinical AI" and "ablation study medical imaging" in PubMed and Google Scholar for examples of well-structured and poorly-structured ablation reporting in medical AI papers
- Search "reproducibility machine learning" and "reproducibility deep learning medical imaging" for literature on the reproducibility crisis in computational medicine and recommended practices
- Search "controlled experiment AI safety" for emerging governance literature on the relationship between experimental interpretability and AI safety in clinical contexts
- Search "negative results machine learning" for discussion of publication bias and the scientific value of null results in AI research
- Search "pre-registration AI clinical study" for guidance on adapting clinical trial pre-registration concepts to AI model development

**Course materials to reference:**

- This lab extends concepts introduced in the core L1-L5 sequence of the Agentic Clinical Research Studio course
- Foundational prompt construction skills are covered in Claude Code 101 (Anthropic)
- Anthropic's published documentation on effective prompting, particularly sections on specificity and constraint specification, are directly relevant to writing controlled experiment prompts

**Standards and guidelines to check for current versions:**

- TRIPOD-AI and TRIPOD+AI reporting guidelines for clinical prediction model studies (check for current version at the EQUATOR Network)
- CLAIM checklist for AI in medical imaging (check for current version)
- CONSORT-AI extension for trials involving AI (check for current version at the EQUATOR Network)
- Any institutional or journal-specific data and code availability requirements relevant to your field

**Internal review note:** Before releasing this handout, verify that the Dice score ranges cited in Section 5 are plausible for the described task on standard benchmarks, and confirm that no specific tooling recommendations (libraries, platforms) need updating for the current course environment.
