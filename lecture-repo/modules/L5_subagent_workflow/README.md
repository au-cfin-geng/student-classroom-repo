# L5 — Subagents & Workflow Orchestration

**Concept:** Specialised subagents, handoff protocols, decision memos, human-in-the-loop  
**Time:** 60 min · Day 2  
**Prompt file:** `prompts/lab_05_subagent_workflow.md`

---

## Overview

Clinical research rarely fits within a single reasoning frame. A study protocol requires epidemiological thinking, statistical design, regulatory awareness, and clinical validity judgment — four distinct expert stances that cannot be usefully compressed into a single prompt. When a single Claude session attempts all of these simultaneously, the outputs tend toward plausible generalities rather than expert-level judgment in any one domain.

**Subagent orchestration** is the practice of decomposing a complex research task into discrete specialised roles, each scoped to a bounded decision, and then routing the outputs of one role as grounded inputs to the next. The researcher functions as the workflow architect: defining what each subagent is responsible for, specifying what it must receive and produce, and inserting human review checkpoints between stages where the stakes are high enough to warrant them.

This lab exists because the single-session, single-role pattern is the default behaviour students fall into — and it systematically produces outputs that look competent but lack the depth of genuine disciplinary judgment. Learning to orchestrate subagents with explicit handoff protocols and decision memos is the difference between using Claude as a search engine with good prose and using it as a structured research collaborator.

---

## Learning Objectives

- Design a multi-subagent workflow in which each agent has a bounded role, defined inputs, and a structured output document
- Write explicit handoff protocols that preserve research context across subagent transitions without loss of evidence grounding
- Produce a decision memo from each subagent transition that records what was decided, why, and what the next agent must know
- Insert a human-in-the-loop checkpoint at the highest-stakes decision point and describe what the researcher must evaluate before proceeding

---

## Clinical Bottleneck

A junior investigator is designing a protocol extension for a segmentation study. She asks Claude to review the study design, propose a statistical analysis plan, check for regulatory considerations, and flag clinical translation risks. Claude, operating as a single general assistant, produces a four-section document that is internally consistent but thin — the statistical section uses a generic sample-size formula, the regulatory section cites broad GDPR categories rather than the specific MDR classification at issue, and the clinical translation section echoes the introduction rather than adding new judgment.

The result is a document that passes a casual reading but would not survive a methods review from a biostatistician, a regulatory specialist, or a clinician. Each section lacks the depth that comes from a role with tightly scoped context and genuine disciplinary constraints.

The bottleneck is not Claude's capability — it is the absence of role scoping. When Claude is asked to be everything at once, it produces a competent average across disciplines rather than excellence within any one.

---

## Agentic Concept

A **subagent** is a Claude session (or a single, tightly scoped prompt) assigned a specific expert role, given a specific set of inputs, and required to produce a specific structured output. Subagents do not improvise their scope — their authority is bounded by the orchestrator's specification.

A **handoff protocol** is the structured document that carries information from one subagent to the next. It must include: (1) what the previous subagent decided and why, (2) the key evidence it relied on, (3) the open questions it could not resolve, and (4) the specific task the next subagent must perform. Without a handoff protocol, the second subagent starts from scratch — it has no access to the first agent's reasoning unless that reasoning is explicitly included in the input.

A **decision memo** is the output artifact of a subagent: a structured record of the decision reached, the evidence cited, the alternatives considered, and the conditions under which the decision would change. Decision memos serve two functions: they are inputs to the next subagent, and they are the permanent record of how each research decision was made. In a regulated clinical research environment, this audit trail is not optional.

A **human-in-the-loop checkpoint** is a deliberate pause in the workflow at which a researcher reviews a subagent's decision memo before it becomes input to the next subagent. Not every transition requires one — but at minimum, the checkpoint should be inserted before any decision that: (1) commits resources, (2) determines what data will be collected, or (3) shapes a regulatory filing. At those points, the researcher is not a passive consumer of Claude's output — they are the accountable reviewer who must be able to justify the decision independently.

The full pattern is:

> Orchestrator prompt → Subagent A (bounded role) → Decision Memo A → [Human checkpoint] → Subagent B (bounded role, receives Memo A) → Decision Memo B → ...

The orchestrator prompt does not perform research — it defines the workflow, assigns roles, and specifies handoff requirements. The work is done by the subagents, each of which receives only the context it needs.

---

## Before / After

**Before:**
```
Claude, review my study protocol and give me a complete assessment covering 
statistical design, regulatory requirements, and clinical translation risks.
```

Claude produces a multi-section document. Each section is plausible. No section is grounded in the specific context of the study in a way that a specialist reviewer would accept. The student submits the document without recognising that each section would require significant revision from an expert.

**After:**
```
You are a clinical research workflow orchestrator. You will coordinate three 
specialised subagents to produce a structured protocol assessment. Do not 
perform the assessment yourself — define the workflow, then execute each 
subagent role in sequence.

SUBAGENT 1 — Statistical Design Specialist
Role: Evaluate only the statistical design of the attached protocol.
Input: reports/study_protocol_draft.md (Methods section only)
Task: Assess primary endpoint definition, sample size rationale, and 
      proposed analysis plan. Identify the single most critical statistical 
      gap that would prevent publication in a methods journal.
Output: Write a decision memo to reports/lab_05_memo_statistics.md with 
        sections: Finding, Evidence, Open Questions, Handoff Requirement.

[HUMAN CHECKPOINT: Read reports/lab_05_memo_statistics.md. 
Do you agree with the critical gap identified? Amend before proceeding.]

SUBAGENT 2 — Regulatory Affairs Specialist
Role: Evaluate only the regulatory classification implications.
Input: reports/lab_05_memo_statistics.md + reports/study_protocol_draft.md 
       (Intended Use section only)
Task: Identify the MDR classification most likely to apply. State what 
      evidence is missing from the protocol to complete a conformity 
      assessment filing.
Output: Write a decision memo to reports/lab_05_memo_regulatory.md with 
        sections: Classification, Evidence, Gaps, Handoff Requirement.

SUBAGENT 3 — Clinical Translation Reviewer
Role: Evaluate only the clinical translation pathway.
Input: reports/lab_05_memo_statistics.md + reports/lab_05_memo_regulatory.md
Task: Given the statistical gap and the regulatory classification, identify 
      the single change to the study design that would most improve 
      deployability in a clinical workflow.
Output: Write a decision memo to reports/lab_05_memo_translation.md.

Write final status to outputs/status/lab_05_subagent_workflow.json.
```

The second prompt produces three focused decision memos, each grounded in the previous agent's output, with a researcher checkpoint inserted before the highest-stakes transition. Each memo is defensible independently, and the audit trail is complete.

---

## Assignment

1. Confirm that `reports/study_protocol_draft.md` exists, or use the stub in `reports/`. Review it briefly — you will need to evaluate Subagent 1's output against it.
2. Paste the lab prompt into Claude Code. Let Claude execute Subagent 1 and write `reports/lab_05_memo_statistics.md`.
3. Read `reports/lab_05_memo_statistics.md` before allowing the workflow to proceed. Ask yourself: Is the critical statistical gap identified genuinely the most important one? Would a biostatistics reviewer agree? If not, annotate the memo with your disagreement before proceeding.
4. Allow Claude to execute Subagents 2 and 3 in sequence, verifying that each memo references the previous one explicitly.
5. After all three memos are complete, read the full chain from Memo 1 through Memo 3. Does the clinical translation recommendation in Memo 3 follow logically from the constraints identified in Memos 1 and 2? Or does Memo 3 ignore those constraints?
6. Write a short synthesis section at the end of `reports/lab_05_subagent_workflow.md` assessing: whether the workflow produced better-scoped outputs than a single-session review would have, and what the human checkpoint changed.

---

## Required Artifacts

| Path | Expected Contents |
|------|------------------|
| `reports/lab_05_subagent_workflow.md` | Orchestrator workflow definition, per-agent scope summary, and synthesis assessment (including human checkpoint reflection) |
| `reports/lab_05_memo_statistics.md` | Subagent 1 decision memo: statistical gap, supporting evidence, open questions, handoff requirement |
| `reports/lab_05_memo_regulatory.md` | Subagent 2 decision memo: MDR classification, evidence basis, filing gaps, handoff requirement |
| `reports/lab_05_memo_translation.md` | Subagent 3 decision memo: single design change recommendation, grounded in constraints from Memos 1 and 2 |
| `outputs/status/lab_05_subagent_workflow.json` | `{"status": "ok", "memos_produced": 3, "checkpoint_reviewed": true}` |

---

## Reflection Questions

1. At the human checkpoint after Subagent 1, did you agree with the critical gap identified? If you amended the memo, what did you change — and what does that tell you about the limits of automated role-scoping?
2. Subagent 3 received the outputs of Subagents 1 and 2 as its inputs. Did Memo 3 reflect the constraints from both upstream memos, or did it produce a recommendation that could have been written without them? What does this tell you about the adequacy of the handoff protocol?
3. In your own research programme, identify one multi-stage decision process — grant design, ethics submission, model evaluation — that would benefit from subagent orchestration with human checkpoints. What roles would you define, and at which transitions would you insert human review?

---

## Success Criteria

Excellent work on this lab demonstrates four properties:

**Scope discipline.** Each decision memo is bounded to its assigned role. The statistical memo does not stray into regulatory territory; the regulatory memo does not pre-empt the clinical translation reviewer. Role boundaries are maintained because the prompts enforce them, not because Claude self-regulates.

**Handoff integrity.** Memo 3 explicitly references findings from Memos 1 and 2. The translation recommendation cannot be understood without the upstream constraints. The handoff protocol has preserved research context across subagent transitions.

**Genuine human review.** The synthesis section in `reports/lab_05_subagent_workflow.md` shows evidence that the student read the checkpoint memo critically — not just acknowledged it. If the student amended anything, the amendment is documented.

**Audit completeness.** The five required artifacts are present and internally consistent. A reviewer who had not been present in the session could reconstruct the full reasoning chain from the memo sequence alone.

---

## Instructor Notes

**Facilitating the human checkpoint moment.** The most instructive moment in this lab is when students reach the Subagent 1 checkpoint and have to decide whether they agree with the statistical gap identified. Many students will rubber-stamp the memo without genuine review. Push them: ask them to state the gap in their own words and whether they could defend it to a statistician. If they cannot, the checkpoint has not functioned.

**Common failure mode: scope drift.** Students often write orchestrator prompts that are too permissive — they tell Claude to "review the design" rather than "identify the single most critical statistical gap." The result is that Subagent 1 produces a broad commentary rather than a bounded judgment, and the handoff requirement is diffuse. When you see this, ask the student to rewrite the Subagent 1 task definition to be specific enough that two reviewers would agree on whether the task was completed.

**Distinguishing handoff from copy-paste.** A weak handoff protocol passes the previous memo verbatim to the next agent without specifying what the next agent must attend to. A strong handoff protocol extracts the specific constraint or finding that the next agent must incorporate. Ask students to check: does Subagent 3's prompt tell it which findings from Memos 1 and 2 are binding constraints, or does it just dump both memos into the context?

**On the "single most important" constraint.** Each subagent task in the model prompt asks for a single critical finding, gap, or recommendation. This is a deliberate discipline — it forces the subagent to make a priority judgment rather than produce a list. Lists are easy to produce and hard to act on. A single prioritised finding forces a defensible stance. Reinforce this with students who receive multi-finding memos: ask them to select one and justify why it is the most important.

**Time management.** This lab runs to 60 minutes if students read each memo carefully before proceeding. If students rush through the checkpoints, they will finish early but miss the lab's central lesson. Build in explicit reading time at each checkpoint — two to three minutes per memo is not excessive.

**Extension opportunity.** For advanced students who finish early: ask them to add a fourth subagent — an Adversarial Reviewer — whose role is to find the single most likely reason the protocol would be rejected at ethics review. The adversarial subagent receives all three previous memos and must produce a rejection argument grounded in them. This tests whether the workflow produces a robust design or a merely plausible one.
