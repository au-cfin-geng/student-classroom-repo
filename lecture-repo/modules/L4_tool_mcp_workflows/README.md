# L4 — Tool & MCP-Aware Research Workflows

**Concept:** Context engineering, permission design, minimal necessary access, audit trails
**Time:** 40 minutes · Day 1
**Audience:** Instructors and advanced students

---

## 1. Overview

This lab teaches the single most consequential skill in agentic clinical research: controlling exactly what information an AI agent accesses, in what order, through which tools, and with what authority to act. When clinical researchers connect an AI agent to external tools — whether a file system, a literature database, a hospital records API, or a project management system — they are not simply giving the agent more capability. They are granting it a permission surface that can produce irreversible side effects. A poorly scoped agent that reads the wrong files first will produce proposals anchored to the wrong evidence. An agent with write permissions when read permissions suffice will overwrite artifacts that took hours to produce. An agent with access to ten data sources when three are relevant will dilute its own reasoning. Context engineering is the discipline of composing that permission surface deliberately: what the agent sees, in what sequence, and with what rights to act. This lab exists because the default behavior of AI tools — read everything, do whatever seems helpful — is scientifically unsound in a clinical research context where every decision must be traceable to specific evidence.

---

## 2. Learning Objectives

- Specify a sequential context chain that enforces a logical dependency order across information sources
- Apply the principle of minimal necessary access by restricting tool permissions to exactly what the current task requires
- Design prompts that produce auditable, step-traceable outputs rather than plausible-sounding but ungrounded proposals
- Distinguish between tool access (what the agent may reach) and context (what the agent actually reads), and explain why the difference matters for research integrity

---

## 3. Clinical Bottleneck

A clinical AI researcher runs a baseline segmentation model, produces a quantitative error analysis, and asks the AI assistant to propose a targeted pipeline improvement. The assistant produces a technically coherent suggestion — increase data augmentation, adjust the learning rate schedule, swap the encoder backbone — but the suggestion is not grounded in the specific failure patterns documented in the error analysis. Three days of implementation follow. The improvement does not address the actual failure mode.

The root cause is not that the AI was wrong in a factual sense. It was wrong in an evidentiary sense: it proposed an action without being anchored to the specific evidence that should have constrained that proposal. This happens routinely when agents are given broad access to a project repository and allowed to read files in an unspecified order. The agent anchors its reasoning on whatever it reads first — often the code, not the evidence. By the time it reads the error analysis, its proposal is already framed.

In clinical research, an ungrounded proposal that sounds plausible is not a minor inefficiency. It is an error in scientific reasoning that can propagate into study design, resource allocation, and eventually into clinical evaluation. Context engineering is the method for preventing this class of error at the prompt level.

---

## 4. Agentic Concept: Context Engineering, Permission Design, and Audit Trails

### Context Engineering

Context engineering is the explicit composition of the information an agent receives: which sources, in what order, with what extraction instructions. It is distinct from prompt engineering (how you instruct the agent) and from tool use (which external systems the agent can reach). Context engineering answers the question: given that the agent can access many things, what should it actually read, and in what sequence?

In agentic systems, reading order matters because language models do not weight all context equally. Information encountered early in a session shapes the interpretive frame through which later information is processed. A researcher who provides the training script before the error analysis is effectively asking the agent to propose improvements from the perspective of a person who has not yet seen the failure evidence. Reversing the order — or enforcing a sequential chain where the agent must summarize each source before reading the next — changes the epistemic state of the agent at the moment of decision.

Effective context engineering for clinical research involves three design choices:
- **Source selection:** Which files, sections, or query results are evidentially relevant to this specific decision?
- **Extraction scope:** What portion of each source should the agent read? Reading an entire repository when only the preprocessing section of one script is relevant wastes context budget and introduces noise.
- **Dependency order:** In what sequence should sources be processed such that later reasoning is anchored to earlier evidence?

### Permission Design and Minimal Necessary Access

Every tool an agent has access to represents a potential for unintended action. In agentic research workflows, this principle has direct scientific consequences. An agent with write access to all scripts may helpfully refactor code during an analysis step, changing behavior in a way the researcher did not authorize and cannot easily trace. An agent connected to a live database may submit a query that triggers a billing event or a rate limit. An agent with access to a communication tool may send a draft to a collaborator before the researcher has reviewed it.

Minimal necessary access means specifying, in each prompt, exactly which tools the agent may use and which it may not. This is not a security concern in the traditional sense — it is a scientific reproducibility concern. A research workflow is reproducible only if the set of actions taken during a session is bounded and knowable. When an agent has unconstrained tool access, the set of possible actions is open-ended and the session cannot be reconstructed from its artifacts alone.

In practice, permission design in a prompt takes the form of explicit negations: "Do not modify any scripts. Do not run any code. Do not write to any path other than the two listed below." These constraints are not limitations on the agent's capability — they are the researcher's specification of what this particular research step requires.

### Audit Trails

An audit trail in agentic research is the chain of evidence connecting a conclusion to the specific inputs and reasoning steps that produced it. In a clinical AI context, audit trails serve three functions: they allow the researcher to verify that a proposal is grounded in the evidence it claims to use; they allow a collaborator or reviewer to reproduce the reasoning; and they allow the researcher to identify exactly where a flawed conclusion entered the workflow.

Structured status files, step-labeled outputs, and explicit source citations within reports are the practical mechanisms for maintaining audit trails in agentic sessions. A status file that records only `"status": "ok"` is not an audit trail. A status file that records which sources were read, what was extracted from each, and what decision was made on the basis of that extraction is the beginning of one.

---

## 5. Before / After

**Before — underspecified, ungoverned access:**
```
Claude, can you update my analysis script and run it on the data?
```

In this prompt, the agent determines its own reading order, selects its own context, and has implicit permission to modify scripts and execute code. The resulting proposal will be anchored to whatever the agent reads first. The researcher has no way to verify which evidence grounded the proposal, and the session cannot be reconstructed from its outputs.

**After — sequenced context chain with explicit permission boundaries:**
```
You are a clinical data pipeline engineer reviewing an evidence-grounded improvement proposal.
Work in this exact order and do not proceed to the next step until the current step is complete.

Step 1: Read scripts/run_train.py. Summarise only the preprocessing section (max 30 lines).
        Record this summary under the heading "Current Method" in your output.

Step 2: Read outputs/metrics/val_metrics.json. State the current Dice value exactly as recorded.
        Record this under the heading "Current Performance".

Step 3: Read reports/error_analysis.md (first 40 lines only). Identify the primary failure mode
        described. Record this under the heading "Identified Failure Mode" with a direct quote
        from the error analysis as supporting evidence.

Based ONLY on the evidence recorded in Steps 1–3, propose one specific modification to the
preprocessing step that targets the identified failure mode. The proposal must include:
  (a) What changes in the preprocessing pipeline
  (b) Why this change targets the specific failure mode (cite Step 3 evidence)
  (c) The expected measurable effect on the Dice coefficient
  (d) A falsification condition — what result would indicate the proposal was wrong

Write the complete proposal to reports/lab_04_tool_mcp_workflow.md.
Do not modify any scripts.
Do not run any code.
Do not write to any path other than reports/lab_04_tool_mcp_workflow.md
  and outputs/status/lab_04_tool_mcp_workflow.json.

Write a completion record to outputs/status/lab_04_tool_mcp_workflow.json with these fields:
  status, sources_read (list), primary_failure_mode (string), proposal_summary (string).
```

The second prompt enforces a context chain (summarize method → record metric → read failure evidence → propose), grants only read access to scripts and metrics, restricts write access to exactly two paths, and requires the output to contain the elements needed for an audit trail. The proposal can be evaluated against the evidence that was supposed to ground it.

---

## 6. Assignment

1. Verify that the prerequisite artifacts exist: `outputs/metrics/val_metrics.json` (with a `dice` key) and `reports/error_analysis.md`. If either is missing, run `make error-analysis` or use the stub files provided in `reports/stubs/`.

2. Read the "After" prompt in Section 5 of this guide. Do not paste it yet — read it carefully and identify: (a) the three sources being read, (b) the order constraint, (c) the permission boundaries, and (d) the four required proposal elements.

3. Paste the prompt into Claude Code. Watch the sequence of file reads as they occur. Note whether Claude follows the Step 1 / Step 2 / Step 3 sequence or reads files in a different order.

4. When the session completes, read `reports/lab_04_tool_mcp_workflow.md`. For each of the four required proposal elements, judge whether it is present and whether it is grounded in specific evidence from `reports/error_analysis.md` or whether it is generic.

5. Read `outputs/status/lab_04_tool_mcp_workflow.json`. Verify that the `sources_read` field lists exactly the three files specified in the prompt, that `primary_failure_mode` is a specific description and not a placeholder, and that `proposal_summary` is a precise, falsifiable statement.

6. Write a one-paragraph assessment at the end of `reports/lab_04_tool_mcp_workflow.md` under the heading "Researcher Assessment." Address: Did the context chain produce a more grounded proposal than you would expect from an unconstrained prompt? What would you change about the prompt design for your own research context?

---

## 7. Required Artifacts

| Path | Expected Content |
|------|-----------------|
| `reports/lab_04_tool_mcp_workflow.md` | Evidence-grounded modification proposal containing all four elements: (a) what changes, (b) why this targets the specific failure mode with cited evidence from the error analysis, (c) expected measurable effect on Dice, (d) a falsification condition. Concludes with a Researcher Assessment paragraph. |
| `outputs/status/lab_04_tool_mcp_workflow.json` | JSON object with keys: `status` ("ok"), `sources_read` (list of three file paths), `primary_failure_mode` (specific string, not a placeholder), `proposal_summary` (one-sentence falsifiable statement). |

---

## 8. Reflection Questions

1. In Step 3 of the assignment, did Claude follow the reading order you specified? If it deviated — reading files simultaneously or in a different sequence — what does that tell you about the reliability of order constraints in agentic prompts, and how would you redesign the prompt to enforce the dependency more strictly?

2. The "After" prompt forbids modifying scripts and running code. In a research session where you do need to run code, how would you redesign the permission structure so that write and execution access is granted only for a specific, bounded step — and revoked before the agent proceeds to interpretation?

3. The status file in this lab records `sources_read`, `primary_failure_mode`, and `proposal_summary`. If a collaborator reviewed this status file six months from now, what additional fields would they need to reconstruct the reasoning chain independently? What is the minimum viable audit trail for a clinical AI research decision?

---

## 9. Success Criteria

Excellent work in this lab meets the following standards:

- `reports/lab_04_tool_mcp_workflow.md` contains a proposal with all four required elements, and element (b) includes a direct quote or specific reference from `reports/error_analysis.md` — not a paraphrase of a generic failure type.
- The falsification condition in element (d) is genuinely falsifiable: it specifies a quantitative threshold or a specific observable result that would indicate the proposal was incorrect.
- `outputs/status/lab_04_tool_mcp_workflow.json` lists exactly the three specified source files in `sources_read`, contains a specific `primary_failure_mode` string that matches the evidence in the error analysis, and has a `proposal_summary` that a colleague could evaluate without reading the full report.
- The Researcher Assessment paragraph distinguishes between the quality of this constrained prompt and what an unconstrained prompt would likely have produced — and offers a specific, reasoned judgment rather than a generic reflection.
- The student can explain, without referring to notes, why reading order affects the evidentiary grounding of an AI-generated proposal in a clinical research context.

---

## 10. Instructor Notes

**Running this lab.** This lab works best when students have already completed the error analysis stage and have a real `reports/error_analysis.md` with specific failure patterns. If the class is running without GPU resources or the error analysis stage has not been completed, the stub files in `reports/stubs/` provide realistic synthetic error analysis content that produces meaningful proposals. Using stubs is acceptable — the pedagogical point is the prompt design pattern, not the specific clinical content.

**Common failure modes to watch for.** The most common student error is to paste the prompt and accept the first output without verifying the reading order. Claude Code will sometimes read files in parallel or in a different sequence than specified, particularly when the Step 1/2/3 labels are present but the dependency relationship between them is not made explicit in the prompt. If students report that the proposal seems generic, ask them to scroll up in the Claude Code session and count the file reads — they will often find that the error analysis was read first or that all three files were read simultaneously before any extraction step occurred.

**The permission boundary discussion.** The "do not modify / do not run" constraints generate productive discussion about what permissions are actually necessary for a given research step. A useful framing: ask students to list every irreversible action an unconstrained agent might take during this task. The list typically includes: modifying the training script, running training, overwriting the metrics file, writing to multiple reports. The exercise makes visible how much authority a permissive prompt silently grants.

**Connecting to MCP.** If students are using MCP servers — a PubMed connector, a project management API, a shared document store — the same design pattern applies directly. The only difference is that "read scripts/run_train.py" becomes "query the MCP server for the preprocessing method description" and "read outputs/metrics/val_metrics.json" becomes "query the metrics database for the current Dice value." The permission boundary concept becomes more consequential with MCP servers because many of them have write capabilities and rate limits that carry real costs. Instructors running MCP-enabled sessions should add a brief discussion of rate-limit and write-permission risks before students execute MCP-connected prompts.

**Audit trail extension.** For advanced students or second-day work, ask them to extend the status file schema to include a `reasoning_chain` field — a list of the three extraction results that fed into the proposal. This forces them to operationalize what an audit trail actually contains, and the resulting status files can be used in L6 (Evaluation) as a structured input for automated quality checks.

**Timing.** Most students complete the core assignment in 20–25 minutes. The remaining time should be used for the Researcher Assessment paragraph and the reflection questions. If time is short, reflection question 3 (minimum viable audit trail) is the highest-value discussion prompt and can be done as a five-minute group exercise at the end of the lab.
