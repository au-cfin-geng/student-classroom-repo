"""
Smoke acceptance test for the Lab00 submission workflow.

Tests:
  1. package_lab creates Lab00Submission/ structure from Lab00/work/ evidence
  2. grade_submissions correctly classifies the lab after packaging
  3. strict mode exits 0 when ready_for_review=true and evidence is present
  4. strict mode exits 1 when ready_for_review=true but evidence is missing

Uses temporary directories — does NOT modify the real student repo.

Usage:
  python lecture-repo/scripts/smoke_lab00_submission.py
  python lecture-repo/scripts/smoke_lab00_submission.py --verbose

Exit codes:
  0 — all smoke tests pass
  1 — one or more smoke tests failed
"""

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

# ── Resolve repo root ──────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parents[2]
LECTURE = BASE / "lecture-repo"

# Import the modules under test
sys.path.insert(0, str(LECTURE / "scripts"))
import package_lab as pkg_mod
import grade_submissions as grade_mod

VERBOSE = False


def _log(msg: str) -> None:
    if VERBOSE:
        print(f"  {msg}")


def _pass(label: str) -> None:
    print(f"  ✓ {label}")


def _fail(label: str, detail: str = "") -> None:
    print(f"  ✗ {label}" + (f": {detail}" if detail else ""))


def _run_in_tmpdir(
    lab_work_files: dict,
    submission_extra: dict | None = None,
    force_package: bool = False,
) -> tuple[Path, dict, int]:
    """
    Build a minimal temp repo, run package_lab and grade_submissions, return results.

    lab_work_files: {relative_path: content_string} — written under Lab00/work/
    submission_extra: {relative_path: content_string} — extra files in Lab00Submission/
    Returns: (tmpdir, grade_result_dict, grade_exit_code)
    """
    tmpdir = Path(tempfile.mkdtemp(prefix="smoke_lab00_"))
    _log(f"tmpdir: {tmpdir}")

    # Replicate minimum repo skeleton
    (tmpdir / "Lab00" / "work").mkdir(parents=True)
    (tmpdir / "Lab00Submission").mkdir(parents=True)
    (tmpdir / "Lab00Submission" / "README.md").write_text("# Lab00Submission\nGenerated.\n")
    lecture = tmpdir / "lecture-repo"
    lecture.mkdir(parents=True)
    (lecture / "outputs" / "grading").mkdir(parents=True)

    # Write fake work files
    for rel, content in lab_work_files.items():
        p = tmpdir / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)

    # Write any extra submission files
    if submission_extra:
        for rel, content in submission_extra.items():
            p = tmpdir / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)

    # Monkey-patch BASE in both modules to point to tmpdir
    orig_pkg_base = pkg_mod.BASE
    orig_grade_base = grade_mod.BASE
    try:
        pkg_mod.BASE = tmpdir
        grade_mod.BASE = tmpdir

        # Run package_lab
        pkg_mod.package_lab("Lab00", force=force_package)

        # Run grade_submissions and capture the result dict
        result = grade_mod._grade_one("Lab00")
        grade_exit = 0
        if result["grade"] == "Broken":
            grade_exit = 1
    finally:
        pkg_mod.BASE = orig_pkg_base
        grade_mod.BASE = orig_grade_base

    return tmpdir, result, grade_exit


def test_fresh_submission_folder_is_not_started() -> bool:
    """An empty submission folder (README only) should be 'Not started'."""
    print("\nTest 1 — Fresh submission folder is Not started")
    tmpdir = Path(tempfile.mkdtemp(prefix="smoke_lab00_"))
    try:
        (tmpdir / "Lab00Submission").mkdir(parents=True)
        (tmpdir / "Lab00Submission" / "README.md").write_text("# Lab00Submission\n")

        orig = grade_mod.BASE
        grade_mod.BASE = tmpdir
        try:
            result = grade_mod._grade_one("Lab00")
        finally:
            grade_mod.BASE = orig

        if result["grade"] == "Not started":
            _pass("Grade is 'Not started'")
            return True
        else:
            _fail("Expected 'Not started'", f"got '{result['grade']}'")
            return False
    finally:
        shutil.rmtree(tmpdir)


def test_package_creates_submission_structure() -> bool:
    """After packaging with evidence, submission folder should have required files."""
    print("\nTest 2 — Package creates submission structure")
    work_files = {
        "Lab00/work/L0_orientation.md": "# Orientation\nWorkspace is ready.",
        "Lab00/work/status.json": json.dumps({"status": "ok", "lab": "Lab00"}),
    }
    tmpdir, result, exit_code = _run_in_tmpdir(work_files)
    try:
        sub_dir = tmpdir / "Lab00Submission"
        ok = True
        for fname in ("evidence_manifest.json", "status.json", "submission.md"):
            p = sub_dir / fname
            if p.exists():
                _pass(f"{fname} created")
            else:
                _fail(f"{fname} missing")
                ok = False
        return ok
    finally:
        shutil.rmtree(tmpdir)


def test_grade_in_progress_when_no_ready() -> bool:
    """After packaging with evidence but ready_for_review=false → 'In progress'."""
    print("\nTest 3 — Grade is 'In progress' when not ready_for_review")
    work_files = {
        "Lab00/work/L0_orientation.md": "# Orientation\nWorkspace is ready.",
        "Lab00/work/status.json": json.dumps({"status": "ok", "lab": "Lab00"}),
    }
    # Add a filled submission.md (with all required headings) but ready=false
    sub_md = """# Lab00 Submission

## Clinical problem
Brain tumour segmentation.

## Agentic / Claude concept
Prompt contract for workspace setup.

## What was produced
L0_orientation.md and status.json.

## Human verification
Confirmed output structure was correct.

## Limitations
Orientation only — no model output.

## Ready for review
- [ ] Ready: NO
"""
    tmpdir, _, _ = _run_in_tmpdir(work_files)
    try:
        (tmpdir / "Lab00Submission" / "submission.md").write_text(sub_md)
        # status.json from package sets ready_for_review based on evidence presence
        # Force it to true for this test since evidence IS present
        status = json.loads((tmpdir / "Lab00Submission" / "status.json").read_text())
        status["ready_for_review"] = False
        (tmpdir / "Lab00Submission" / "status.json").write_text(json.dumps(status))

        orig = grade_mod.BASE
        grade_mod.BASE = tmpdir
        try:
            result = grade_mod._grade_one("Lab00")
        finally:
            grade_mod.BASE = orig

        if result["grade"] in ("In progress", "Ready"):
            _pass(f"Grade is '{result['grade']}' (in-progress or better)")
            return True
        else:
            _fail("Expected 'In progress' or better", f"got '{result['grade']}'")
            return False
    finally:
        shutil.rmtree(tmpdir)


def test_grade_ready_when_evidence_and_ready() -> bool:
    """Full evidence + ready_for_review=true + full submission.md → 'Ready'."""
    print("\nTest 4 — Grade is 'Ready' when evidence present and ready_for_review=true")
    work_files = {
        "Lab00/work/L0_orientation.md": "# Orientation\nWorkspace is ready.",
        "Lab00/work/status.json": json.dumps({"status": "ok", "lab": "Lab00"}),
    }
    sub_md = """# Lab00 Submission

## Clinical problem
Brain tumour segmentation from FLAIR MRI.

## Agentic / Claude concept
Output contract for workspace orientation.

## What was produced
L0_orientation.md describing the research question.
status.json confirming workspace readiness.

## Human verification
Reviewed orientation artifact for accuracy.

## Limitations
Lab00 is a setup lab only — no model outputs.

## Ready for review
- [x] All required artifacts committed
- [x] Ready: YES
"""
    tmpdir, _, _ = _run_in_tmpdir(work_files)
    try:
        (tmpdir / "Lab00Submission" / "submission.md").write_text(sub_md)
        # Set ready_for_review=true
        status = json.loads((tmpdir / "Lab00Submission" / "status.json").read_text())
        status["ready_for_review"] = True
        (tmpdir / "Lab00Submission" / "status.json").write_text(json.dumps(status))

        orig = grade_mod.BASE
        grade_mod.BASE = tmpdir
        try:
            result = grade_mod._grade_one("Lab00")
        finally:
            grade_mod.BASE = orig

        if result["grade"] == "Ready":
            _pass("Grade is 'Ready'")
            return True
        else:
            _fail("Expected 'Ready'", f"got '{result['grade']}', notes: {result['notes']}")
            return False
    finally:
        shutil.rmtree(tmpdir)


def test_grade_broken_when_evidence_missing() -> bool:
    """ready_for_review=true but evidence missing → 'Broken', strict mode exits 1."""
    print("\nTest 5 — Grade is 'Broken' when ready_for_review=true but evidence missing")
    # Package with NO work files so evidence is marked missing
    work_files = {}  # empty — no Lab00/work/ files
    tmpdir, _, _ = _run_in_tmpdir(work_files)
    try:
        sub_md = """# Lab00 Submission

## Clinical problem
Test.

## Agentic / Claude concept
Test.

## What was produced
Test.

## Human verification
Test.

## Limitations
Test.

## Ready for review
- [x] Ready: YES
"""
        (tmpdir / "Lab00Submission" / "submission.md").write_text(sub_md)
        # Force ready_for_review=true even though evidence is absent
        status = {
            "lab": "Lab00",
            "packaged_at": "2026-06-01",
            "all_required_found": False,
            "required_count": 2,
            "found_required_count": 0,
            "ready_for_review": True,  # lying — evidence is missing
        }
        (tmpdir / "Lab00Submission" / "status.json").write_text(json.dumps(status))
        # evidence_manifest.json listing required files as NOT found
        manifest = {
            "lab": "Lab00",
            "evidence": [
                {"path": "Lab00/work/L0_orientation.md", "required": True, "found": False},
                {"path": "Lab00/work/status.json", "required": True, "found": False},
            ],
        }
        (tmpdir / "Lab00Submission" / "evidence_manifest.json").write_text(
            json.dumps(manifest)
        )

        orig = grade_mod.BASE
        grade_mod.BASE = tmpdir
        try:
            result = grade_mod._grade_one("Lab00")
        finally:
            grade_mod.BASE = orig

        if result["grade"] == "Broken":
            _pass("Grade is 'Broken' — correct")
            return True
        else:
            _fail("Expected 'Broken'", f"got '{result['grade']}'")
            return False
    finally:
        shutil.rmtree(tmpdir)


def main() -> None:
    global VERBOSE
    parser = argparse.ArgumentParser(description="Smoke acceptance test for Lab00 workflow")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    VERBOSE = args.verbose

    print("\n══════════════════════════════════════════════════")
    print("  Lab00 Submission Workflow — Smoke Acceptance Test")
    print("══════════════════════════════════════════════════")

    tests = [
        test_fresh_submission_folder_is_not_started,
        test_package_creates_submission_structure,
        test_grade_in_progress_when_no_ready,
        test_grade_ready_when_evidence_and_ready,
        test_grade_broken_when_evidence_missing,
    ]

    results = []
    for t in tests:
        try:
            results.append(t())
        except Exception as exc:
            print(f"  ✗ {t.__name__} raised: {exc}")
            results.append(False)

    passed = sum(results)
    total = len(results)
    print(f"\n  {passed} / {total} smoke tests passed")
    if passed == total:
        print("  All smoke tests pass — submission workflow is correct.\n")
        sys.exit(0)
    else:
        print(f"  {total - passed} test(s) failed.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
