# Lab01 — Prompt Contracts

First confirm you are working from the repository root.
Then confirm the active lab folder is `Lab01/`.
All student-generated files for this lab should be written under `Lab01/work/` unless explicitly instructed.
Do not write into `lecture-repo/` except to read course materials.
If you are not in the correct repo, stop and tell me.

---

## Task

Demonstrate a prompt contract: explicit inputs, permissions, and output schema.

**Input:** Read `lecture-repo/data/sample/` — inspect the first available file.
**Permissions:** Read-only. Do NOT modify any data files.

**Task:** Characterise the imaging dataset.

**Write `Lab01/work/status.json`** with EXACTLY these keys:
```json
{ "file_count": int, "shape": [x,y,z], "voxel_range": [min,max],
  "modality_guess": str, "quality_flags": list_of_strings }
```

**Write `Lab01/work/L1_prompt_contract.md`:**
- One paragraph on data suitability for analysis
- Confidence level: HIGH / MEDIUM / LOW
- Assumptions stated explicitly

Do not fabricate values. If a value cannot be determined, write `null` and explain why.
