# Student Acceptance Test Protocol

Manual protocol for verifying the student experience works end-to-end.
Run this before distributing the repo to students.

---

## Environment

- Fresh clone of the repo (do not reuse a development clone)
- VS Code with Claude Code extension installed
- Python 3.11+ with `pip install -r lecture-repo/requirements.txt`

---

## Test 1 — Fresh clone

**Steps:**
1. Clone the repo to a new directory
2. `cd student-classroom-repo`
3. Run `make preflight`

**Expected:**
- All 15 preflight tests pass
- No errors
- Bootstrap prints "Bootstrap completed."

**Failure criteria:** Any test fails. Any Python import error.

---

## Test 2 — Student workspace

**Steps:**
1. Open VS Code: `code student-lab.code-workspace`
2. Inspect the Explorer panel

**Expected:**
- Visible: `Lab00/`, `Lab01/`, `Lab02/`, `Lab03/`, `Lab04/`, `Lab05/`, `Capstone/`
- Visible: `Lab00Submission/` through `CapstoneSubmission/`
- Visible: `START_HERE.md`, `CLAUDE.md`, `ASSIGNMENT.md`, `Makefile`
- Hidden: `lecture-repo/app/`, `lecture-repo/scripts/`, `lecture-repo/tests/`, `lecture-repo/data/`

**Failure criteria:** Any `lecture-repo/` internals visible to student. Any lab folder missing.

---

## Test 3 — Dashboard

**Steps:**
1. Run `make dashboard`
2. Navigate to http://localhost:8501
3. Click through: Welcome → How to Start → each Lab page → Progress → Resources

**Expected:**
- Dashboard loads without errors
- Each lab page shows the "How to finish this lab" callout with Claude-centric instructions
- "Finish this Lab" section says "You do not manually package submissions. Claude does that."
- Progress page shows all labs as "Not started"
- Resources page shows `lecture-repo/handouts/`, `lecture-repo/prompts/`, `lecture-repo/modules/` paths

**Failure criteria:** Dashboard crashes. Any page shows traceback. "How to finish" instructs student to manually run `make package`.

---

## Test 4 — Lab00 do_lab_prompt

**Steps:**
1. Open `Lab00/do_lab_prompt.md`
2. Copy the entire file contents
3. Paste into Claude Code
4. Observe Claude's actions

**Expected:**
- Claude confirms repo root (sees `START_HERE.md`, `CLAUDE.md`, `Makefile`, `Lab00/`)
- Claude confirms active lab folder is `Lab00/`
- Claude writes ONLY inside `Lab00/work/`
- Files created: `Lab00/work/L0_orientation.md`, `Lab00/work/status.json`
- Claude does NOT write into `lecture-repo/` or repo root

**Failure criteria:**
- Claude writes files outside `Lab00/work/`
- Claude writes into `lecture-repo/scripts/` or any infrastructure path
- Required files not created

---

## Test 5 — Finish Lab prompt for Lab00

**Steps:**
1. Open `lecture-repo/prompts/finish_lab.md`
2. Copy the entire file contents
3. Paste into Claude Code (fresh conversation or same conversation)
4. Tell Claude: "Lab00"

**Expected sequence:**
1. Claude asks for lab ID (or accepts "Lab00" from context)
2. Claude confirms repo root
3. Claude lists `Lab00/work/` contents
4. Claude reads `Lab00/work/L0_orientation.md` and `Lab00/work/status.json`
5. Claude runs `make package LAB=Lab00`
6. Claude reads `Lab00Submission/submission.md` scaffold
7. Claude **writes** `Lab00Submission/submission.md` with content derived from the evidence
8. Claude shows the student the filled submission.md
9. Claude asks: "Does this accurately reflect your lab work?"
10. After confirmation, Claude runs `make progress`
11. Claude shows `git status` output
12. Claude asks "Commit and push? (YES/NO)"
13. Student says YES
14. Claude runs `git add Lab00/work/ Lab00Submission/...` then `git commit`
15. Claude does NOT push without explicit request

**Failure criteria:**
- Claude skips reading the evidence files
- Claude writes placeholder text in submission.md instead of evidence-based content
- Claude commits without showing `git status` first
- Claude pushes without student approval
- `Lab00Submission/evidence_manifest.json` not created

---

## Test 6 — Progress check after Lab00

**Steps:**
1. Run `make progress`

**Expected output:**
```
Lab00     Pass/In progress   ...
Lab01     Not started        ...
...
1 ready · 0 in progress · 6 not started
```

Exit code: 0

**Failure criteria:** Exit code non-zero. Lab00 shows "Not started". Error traceback.

---

## Test 7 — Strict grade on partial completion

**Steps:**
1. Run `make grade`

**Expected:**
- Exit code 0 (no lab claims ready_for_review=true with broken evidence)
- OR: Lab00 shows "Pass" if ready_for_review=true was set

**Failure criteria:** Exit code 1 without a broken ready submission. Traceback.

---

## Test 8 — Git commit message

**After Test 5 commit:**

**Expected:**
- Commit message: `Complete Lab00 submission package` (or similar)
- Committed files include: `Lab00/work/L0_orientation.md`, `Lab00/work/status.json`, `Lab00Submission/submission.md`, `Lab00Submission/evidence_manifest.json`, `Lab00Submission/status.json`
- `COURSE_PROGRESS.md` at repo root updated

**Failure criteria:** Commit message is unclear. Submission files not committed. Files outside Lab00 committed unexpectedly.

---

## Test 9 — GitHub Actions (after push)

**Steps:**
1. `git push origin main`
2. Watch GitHub Actions at github.com/…/actions

**Expected:**
- `Grade Submissions` workflow triggers
- Progress mode step: exits 0
- Strict mode step: exits 0 (since evidence is present)
- Grading report artifact uploaded: `grading-report-<sha>/grading_report.json`
- No red failures

**Failure criteria:** Workflow fails on a correctly completed Lab00 push. Artifact not uploaded.

---

## Test 10 — Fresh clone does not fail GitHub Actions

**Steps:**
1. Push a fresh clone with no student work (only the base `.gitkeep` files)
2. Trigger `Grade Submissions` workflow (manually via workflow_dispatch or by changing a Lab file)

**Expected:**
- Progress mode: exits 0, shows "Not started" for all labs
- Strict mode: exits 0 (no lab claims ready but broken)

**Failure criteria:** GitHub Action fails on a fresh push. Exit code 1 when no labs submitted.

---

## Sign-off checklist

- [ ] Test 1 — preflight: 15 pass
- [ ] Test 2 — workspace: lecture-repo internals hidden
- [ ] Test 3 — dashboard: loads, Claude-centric finish instructions
- [ ] Test 4 — Lab00 do_lab_prompt: writes only in Lab00/work/
- [ ] Test 5 — Finish Lab prompt: Claude drafts submission, asks before commit
- [ ] Test 6 — make progress: exits 0, shows Lab00 complete
- [ ] Test 7 — make grade: exits 0
- [ ] Test 8 — commit message: clean, expected files
- [ ] Test 9 — GitHub Actions: passes after correct Lab00 submission
- [ ] Test 10 — GitHub Actions: passes on fresh clone

**Tested by:** _______________  **Date:** _______________
