# Lab05 — Subagents & Workflow Orchestration

First confirm you are working from the repository root.
Then confirm the active lab folder is `Lab05/`.
All student-generated files for this lab should be written under `Lab05/work/` unless explicitly instructed.
Do not write into `lecture-repo/` except to read course materials.
If you are not in the correct repo, stop and tell me.

---

## Task

Study to review: [INSERT YOUR STUDY DESCRIPTION HERE]

--- SUBAGENT 1: LiteratureAgent ---
Role: systematic review specialist
Output: 3-5 bullets on gaps, prior work, positioning. Mark [VERIFIED] or [ESTIMATED].

--- SUBAGENT 2: MethodCriticAgent ---
Role: clinical trial methodologist
Output: top 2 methodological risks. One concrete fix for each.

--- SUBAGENT 3: ComplianceAgent ---
Role: clinical research compliance officer
Output: top 2 compliance concerns. Name applicable frameworks (GDPR, ICH-GCP).

--- DECISION MEMO ---
1. Summary of all three outputs
2. Top risk across all perspectives
3. Recommended next step (one specific action)
4. What remains unresolved

**Write to `Lab05/work/L5_subagent_workflow.md`** — the workflow design for reuse.
**Write to `Lab05/work/L5_subagent_workflow_report.md`** — the output for this run.
**Write to `Lab05/work/status.json`:** `{ "status": "ok", "lab": "Lab05" }`
