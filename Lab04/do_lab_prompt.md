# Lab04 — Tool / MCP-Aware Workflow

First confirm you are working from the repository root.
Then confirm the active lab folder is `Lab04/`.
All student-generated files for this lab should be written under `Lab04/work/` unless explicitly instructed.
Do not write into `lecture-repo/` except to read course materials.
If you are not in the correct repo, stop and tell me.

---

## Task

Design a safe context workflow for: [INSERT YOUR SPECIFIC RESEARCH TASK]

**Write a specification to `Lab04/work/L4_tool_mcp_workflow.md`:**

1. Context inventory: what data does this task actually require?
   Format: Source | Type | Sensitivity (public/internal/restricted)

2. Allowed context: list each permitted source explicitly
3. Forbidden context: what must Claude NOT access? Why?
4. Write permissions: what may Claude create or modify?
5. Human approval gates: two to three review points, with risks of skipping
6. Audit trail: what record of actions, and who reviews it?
7. Risk analysis: three things that could go wrong
   Format: Risk | Probability (L/M/H) | Severity | Mitigation

**Write to `Lab04/work/status.json`:** `{ "status": "ok", "lab": "Lab04" }`
