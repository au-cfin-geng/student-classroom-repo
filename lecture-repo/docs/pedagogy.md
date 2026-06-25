# Pedagogical Model — Clinical Claude

## The Four-Layer Model

The Clinical Claude course is organized around four progressive layers of competency. Each layer builds on the previous, and the course design refuses to let students skip ahead.

**Layer 1 — Operational.** Students learn to work in a structured research repository: understanding directory conventions, running make targets, reading pipeline outputs, and interpreting committed artifacts. This is not trivial. Most clinical researchers arrive with habits shaped by ad-hoc scripts and email chains. The operational layer forces discipline before creativity.

**Layer 2 — Prompt Craft.** Students learn that prompts are specifications, not requests. They practice the difference between a vague instruction ("analyze this") and a precise one (role, context, constraint, output format, success criterion). Each module isolates one prompt principle — role assignment, few-shot examples, chain-of-thought elicitation, structured output, self-critique — and students see the causal relationship between prompt structure and output quality on a single fixed clinical problem.

**Layer 3 — Research Reasoning.** Students learn to use Claude as a reasoning partner, not a search engine. They form hypotheses about why the Dice coefficient behaves as it does, generate competing explanations, and use Claude to stress-test their logic. The course teaches that a good AI-assisted workflow produces arguments, not just numbers.

**Layer 4 — Translation.** Students learn to communicate findings to audiences who were not in the room: regulatory reviewers, clinical collaborators, grant committees. This layer exposes the gap between technical correctness and communicative adequacy. A result that is correct but untranslatable has failed as research.

---

## The "Student as Junior Investigator" Positioning

The course frames students as junior investigators, not programmers. This distinction is load-bearing.

If students believe they are learning to code, they will evaluate their work by whether the script runs. If they believe they are conducting a constrained investigation, they evaluate their work by whether the conclusion is defensible. These are different cognitive stances. The second one is what clinical AI research actually requires.

The brain tumour segmentation problem is deliberately simple. A first-year medical student can understand intensity thresholding. The simplicity is a feature: it removes the excuse of technical confusion and forces students to engage with the harder problems — measurement validity, failure analysis, communicative framing. The Dice coefficient is a number that demands interpretation, not just computation.

---

## The "Artifact over Chat" Principle

Every module produces a committed file. Grades are assessed on what exists in the repository, not on what was discussed in a session. This is not merely an assessment convenience. It teaches a critical professional habit: in research, only what is written down exists.

Chat is ephemeral and unaccountable. A committed artifact is reviewable, versioned, and falsifiable. The discipline of writing a file — not just generating a response — forces students to make a decision about what is worth preserving. That decision is itself a form of judgment.

Instructors should enforce this strictly. A student who describes their analysis verbally but has not committed a file has not completed the module.

---

## The Tension Between Scaffold and Authenticity

The course provides a great deal of scaffold: a fixed dataset, pre-written make targets, numbered prompt stages, required output formats. This creates a genuine tension. Over-scaffolding produces students who can follow instructions but cannot transfer. Under-scaffolding produces students who are lost and learn only frustration.

The resolution is this: the scaffold controls the *logistics* of the task, not the *reasoning* about it. The make target runs the script. The prompt stage specifies the format. But the hypothesis, the interpretation, and the translation are entirely the student's responsibility. No correct answer is provided. No model output is given to compare against. The student's judgment is the only thing being evaluated in those sections.

---

## The Five Core Tensions and How Each is Resolved

**Structure vs. freedom.** Resolved by fixing the technical substrate (dataset, algorithm, metrics) while leaving the interpretive substrate open. Students cannot choose a different problem; they must choose their own analysis.

**Hidden scaffold vs. authenticity.** Resolved by making the scaffold visible. Students see the make targets, the prompt stages, the directory structure. Nothing is magic. The course teaches that good research infrastructure is designed, not accidental.

**Monitoring vs. overload.** Resolved by keeping the feedback loop tight. Each module has one make target and one committed artifact. Instructors do not review process; they review outputs. This keeps cognitive load manageable for both parties.

**Best practices vs. boredom.** Resolved by making best practices consequential. A poorly structured prompt produces a worse analysis. A vague hypothesis produces a weaker argument. Students see the cost of cutting corners on the same problem they've been working on since Module 0.

**Serious course vs. playful engagement.** Resolved by trusting the clinical problem. Brain tumour segmentation is not playful. It is serious. Students who engage honestly with the material do not need manufactured enthusiasm.

---

## What Instructors Must Not Do

Three instructor behaviors undermine the course design and must be avoided.

**Do not let students look up the Dice score for intensity thresholding on brain MRI.** The point of the module is not the number; it is the process of obtaining and interpreting the number. A student who knows the answer before running the pipeline has bypassed the learning.

**Do not answer the hypothesis question before students form one.** Instructors who tell students what to expect from the segmentation results short-circuit the reasoning layer entirely. The hypothesis must be the student's own, formed before seeing the output.

**Do not allow scripts to be run manually instead of through the prompt pipeline.** The prompt stages exist because the act of specifying what Claude should do — and reading what it produces — is itself the curriculum. Running `python scripts/evaluate.py` directly skips the instructional content. The make target enforces the pipeline for a reason.

---

## A Note on Transfer

The clinical problem in this course is fixed. The principles are not. A student who completes this course should be able to apply structured prompt craft, research reasoning, and translation discipline to any clinical AI problem they encounter in their own work. The final module makes this transfer explicit. Instructors should assess not only whether students completed the course modules, but whether they can articulate which principles apply to a problem they have not seen before.
