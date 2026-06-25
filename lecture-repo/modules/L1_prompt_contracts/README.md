# L1 — Prompt Contracts

**Concept:** Inputs, permissions, output schema — reproducible structured prompts
**Time:** 35 minutes · Day 1
**Prompt file:** `prompts/stage_02_load_visualize.md`
**Required artifacts:** `outputs/status/lab_01_prompt_contract.json`, `reports/lab_01_prompt_contract.md`

---

## 1. Overview

A prompt that produces different outputs on different runs is not a scientific instrument — it is a conversation. Clinical research demands reproducibility: the same protocol applied to the same data should yield outputs in the same format, at the same paths, with the same schema. Yet the default human instinct when working with a language model is to ask loosely, invite interpretation, and accept whatever emerges. That instinct is appropriate for brainstorming; it is fatal for research.

This lab introduces the **prompt contract** as the fundamental unit of reproducibility in agentic clinical AI research. A prompt contract has three mandatory components: a declared set of allowed inputs, an explicit permissions boundary (what Claude may and may not do), and a binding output schema specifying file paths, required fields, and data types. When all three components are present, the prompt functions like a laboratory protocol — any investigator, running it against the same data in a fresh session, should produce structurally identical results. When any component is absent, the prompt functions like a verbal instruction: dependent on context, mood, and interpretation.

---

## 2. Learning Objectives

- Distinguish between a conversational prompt and a prompt contract, and articulate why the distinction matters for research reproducibility.
- Write a prompt that explicitly declares input scope, permission constraints, and a verifiable output schema.
- Verify that a prompt contract produces structurally identical outputs across independent sessions.
- Recognize the categories of research workflow — data characterization, pre-processing audit, summary generation — where prompt contracts are most critical.

---

## 3. Clinical Bottleneck

Clinical data provenance depends on knowing exactly what happened to the data at each step of a study. When a team member reports that they "asked Claude to analyze the MRI data and got a summary," the clinical record contains no auditable information. Which files were read? Which were written? Was any preprocessing applied? Did the analysis branch on a condition that may not recur? None of these questions can be answered from a conversational exchange.

The downstream consequences are significant. Multi-site studies require that data characterization steps be performed identically at every site. Grant reports cite summary statistics that must be reproducible by reviewers. Regulatory submissions require evidence that analytical procedures were applied consistently. A pipeline stage that behaves differently depending on how a question is phrased has no place in any of these contexts.

The specific bottleneck this lab addresses is the **first contact with a new dataset** — the data characterization step that precedes any modeling or analysis. Before a single model is trained or a single metric is computed, a research team needs to know what is in the dataset: file count, image dimensions, intensity range, modality, and preliminary quality signals. When this step is performed with a loose prompt, the resulting notes vary by investigator and session. When it is performed with a prompt contract, the output is a structured JSON file that can be tested, versioned, and cited.

---

## 4. Agentic Concept: The Prompt Contract

A prompt contract is a prompt that has been explicitly structured around three binding specifications.

**Input declaration** names exactly which files, directories, or variables Claude is permitted to read. This matters because a model given broad access to a repository may draw on files the investigator did not intend as inputs — configuration files, prior outputs, or cached state from previous sessions. By naming the allowed inputs explicitly, the investigator ensures that the analysis is grounded in the same evidence base every time.

**Permission constraints** state what actions Claude may and may not take during the session. The minimum useful constraint for a data characterization step is a read-only boundary: Claude may inspect files but may not write to, move, or delete data files. More complex pipelines may require additional permissions — for example, permission to run a specific script but not to modify it. Explicit permission constraints serve two purposes: they prevent unintended side effects, and they make the boundary of Claude's agency legible to anyone reviewing the session record.

**Output schema** specifies the exact file path, required keys, and expected data types of every output Claude must produce. A schema is not a suggestion. It is a contract between the prompt author and any downstream consumer of the output — including automated tests, dashboard visualizations, and other agents in a multi-step pipeline. When the output schema is fully specified, the prompt becomes testable: a single assertion can verify that all required keys are present and correctly typed.

Together, the three components transform a prompt from a communication act into a research protocol. The protocol can be stored in a file, version-controlled, reviewed by collaborators, and executed by any agent — human or automated — that has access to the same data.

---

## 5. Before / After

**Before — conversational prompt:**

```
Look at the MRI data and tell me what you see.
```

Claude reads whatever files seem relevant, produces a narrative summary in whatever format feels natural, possibly writes a file, possibly does not. The output structure varies between sessions. There is no way to assert that the output is correct, because correct has not been defined. Running this prompt in a new session three months later may produce an output in a completely different format, with different fields, at a different path — or no file at all.

**After — prompt contract:**

```
You are a medical data characterisation agent. Read data/sample/ and inspect the first NIfTI file you find.

Do NOT modify, move, or delete any files in data/.

Write your findings to outputs/status/lab_01_prompt_contract.json with EXACTLY these keys:
  file_count: int
  shape: list[int]
  voxel_range: list[float]   # [min, max]
  modality_guess: str
  quality_flags: list[str]

Then write a one-paragraph clinical data memo to reports/lab_01_prompt_contract.md. The memo must include: modality, image dimensions, intensity range, and at least one quality observation.
```

The second prompt produces the same output schema in every session. The output can be tested automatically. The `Do NOT modify` constraint creates a read-only audit boundary. Any team member running this prompt against the same data produces an output that is structurally identical to any other team member's output — even if the narrative wording of the memo differs, the JSON fields and types will match.

---

## 6. Assignment

1. Open `prompts/stage_02_load_visualize.md` and read the full prompt before running anything. Identify which of the three contract components are present: input declaration, permission constraints, and output schema.
2. Run the prompt in Claude Code. After it completes, open `outputs/status/lab_01_prompt_contract.json` and verify that all five required keys are present with the correct types.
3. Open a new Claude Code session and run the same prompt a second time. Compare the two JSON outputs. Are the keys identical? Are the values consistent with the same underlying data?
4. Edit `reports/lab_01_prompt_contract.md` to add a brief annotation — one paragraph — describing what the contract enforced and what would have been different without the output schema specification.
5. Answer the three reflection questions in your own words, either in the report or in a separate notes document.

---

## 7. Required Artifacts

| Path | Required content |
|------|-----------------|
| `outputs/status/lab_01_prompt_contract.json` | All five keys present: `file_count` (int), `shape` (list of int), `voxel_range` (list of float with min and max), `modality_guess` (str), `quality_flags` (list of str) |
| `reports/lab_01_prompt_contract.md` | Clinical data memo: modality, dimensions, intensity range, at least one quality observation, and a student annotation describing what the contract enforced |

Both files must be present and non-empty. The JSON file must parse without errors. Automated grading tests check key presence and type; they do not check the specific values, which depend on the dataset.

---

## 8. Reflection Questions

1. A function signature in software engineering specifies inputs, return type, and — in typed languages — constraints on both. In what ways is a prompt contract analogous to a function signature, and in what ways does the analogy break down?
2. Remove the output schema from the prompt and run it a third time. What changes in the output? What does this tell you about where reproducibility actually comes from in an agentic workflow?
3. Identify a step in your own research — not in this course — where a loose prompt might be appropriate and where a prompt contract would be required. What is the criterion that determines which mode is correct for a given step?

---

## 9. Success Criteria

Excellent work at this lab demonstrates the following:

- `outputs/status/lab_01_prompt_contract.json` exists, parses correctly, and contains all five required keys with the specified types.
- The student can verify, from two independent sessions, that the output schema is structurally identical even if narrative content differs.
- `reports/lab_01_prompt_contract.md` contains a clinical data memo that would be meaningful to a collaborator who has not seen the dataset.
- The student annotation in the report demonstrates genuine understanding of what the permission constraint and output schema each contribute — not just that they are present, but what failure mode each one prevents.
- Reflection answers are specific and grounded in the lab experience, not generic statements about AI reproducibility.

Work that simply produces the required files without demonstrating understanding of the contract mechanism does not meet the standard for this lab.

---

## 10. Instructor Notes

**Facilitating the before/after comparison.** The most effective facilitation move for this lab is to have students run the loose prompt first and record what they get, then run the contract prompt and compare. The contrast is more instructive than any explanation. Reserve five minutes at the end of the lab for a group comparison: ask two or three students to share their `lab_01_prompt_contract.json` files. The structural identity across outputs — despite different machines, different session states, and different Claude responses — is the concrete demonstration of what a contract buys.

**Common student errors.** The most common error is treating the output schema as a suggestion rather than a constraint. Students often add extra keys or omit `quality_flags` when no obvious quality issue is present (an empty list is a valid value; the key must still exist). A second common error is conflating the permission constraint with a safety feature. The `Do NOT modify` instruction is not primarily about preventing harm — it is about making the audit boundary explicit. Emphasize this distinction.

**Connecting to research practice.** Students with wet lab backgrounds will recognize the prompt contract as analogous to a standard operating procedure (SOP): a written protocol that specifies inputs, permitted actions, and expected outputs so that any trained operator produces a comparable result. Students with computational backgrounds may find the function signature analogy more useful. Both framings are correct. The key distinction to emphasize is that the contract lives in the prompt — it is not enforced by a runtime system — which means the investigator bears responsibility for writing it precisely.

**Timing.** The lab is designed for 35 minutes: 10 minutes to read and understand the prompt, 10 minutes to run and verify, 10 minutes for the second session comparison, and 5 minutes for reflection. If time is short, the second session run can be assigned as independent work before the debrief. The group comparison of JSON outputs is high-value and should not be cut.

**Extension for advanced students.** Ask students to write a prompt contract for a step in their own research — outside this course — and to identify what output schema they would need to make that step auditable. This transfer exercise is the most reliable indicator of whether the concept has been genuinely internalized.
