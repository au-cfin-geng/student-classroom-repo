"""
Grade lab submissions: structure and completion checks only.

Usage:
  python lecture-repo/scripts/grade_submissions.py
  python lecture-repo/scripts/grade_submissions.py --mode progress
  python lecture-repo/scripts/grade_submissions.py --mode strict
  python lecture-repo/scripts/grade_submissions.py --mode strict --required Lab00 Lab01 Lab03

Modes:
  progress (default via make progress)
    - Shows current state of all labs
    - Exit code 0 always — safe for fresh clone and dashboard
    - States: Not started / In progress / Ready / Broken
    - Suitable for: during-course feedback, GitHub Actions on push

  strict (default via make grade)
    - Fails if any submitted lab is Broken (claims ready but evidence missing)
    - Optionally fails if --required labs are not submitted / incomplete
    - Exit code 1 on failure, 0 otherwise
    - Suitable for: final grading, instructor review

States:
  Not started — submission folder has only README / .gitkeep; no package run yet
  In progress — package has been run (status.json or evidence_manifest.json present)
               but not all structure is complete or ready_for_review=false
  Ready       — all structure present, ready_for_review=true, evidence on disk
  Broken      — claims ready_for_review=true but evidence or structure missing

Writes:
  - Terminal summary
  - lecture-repo/outputs/grading/grading_report.json
  - COURSE_PROGRESS.md at repo root
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]

VALID_LABS = ["Lab00", "Lab01", "Lab02", "Lab03", "Lab04", "Lab05", "Capstone"]

_LAB_HEADINGS = [
    "## Clinical problem",
    "## Agentic / Claude concept",
    "## What was produced",
    "## Human verification",
    "## Limitations",
    "## Ready for review",
]

_CAPSTONE_HEADINGS = [
    "## Research problem",
    "## Agentic workflow used",
    "## Evidence and artifacts",
    "## Human verification",
    "## Limitations",
    "## Showcase summary",
    "## Ready for review",
]

_REQUIRED_TITLE = {lab: f"# {lab} Submission" for lab in VALID_LABS if lab != "Capstone"}
_REQUIRED_TITLE["Capstone"] = "# Capstone Submission"


def _submission_dir(lab_id: str) -> Path:
    return BASE / f"{lab_id}Submission"


def _has_meaningful_content(sub_dir: Path) -> bool:
    """Return True if the submission folder contains more than README / .gitkeep."""
    for f in sub_dir.iterdir():
        if f.name not in ("README.md", ".gitkeep", ".DS_Store"):
            return True
    return False


def _check_headings(lab_id: str, text: str) -> list:
    headings = _CAPSTONE_HEADINGS if lab_id == "Capstone" else _LAB_HEADINGS
    return [h for h in headings if h not in text]


def _grade_one(lab_id: str) -> dict:
    sub_dir = _submission_dir(lab_id)
    result = {
        "lab": lab_id,
        "submission_folder": f"{lab_id}Submission/",
        "work_folder": f"{lab_id}/work/",
        "dir_exists": sub_dir.exists(),
        "submission_md": False,
        "status_json": False,
        "manifest_json": False,
        "missing_headings": [],
        "missing_evidence": [],
        "claims_ready": False,
        "structural_pass": False,
        "grade": "Not started",
        "notes": [],
    }

    if not sub_dir.exists():
        return result

    # Folder exists but contains only README / .gitkeep — no package run yet.
    if not _has_meaningful_content(sub_dir):
        result["notes"].append("Use the Finish Lab prompt in Claude Code to package this lab")
        return result

    # Meaningful content is present — inspect it.
    sub_path = sub_dir / "submission.md"
    if sub_path.exists():
        result["submission_md"] = True
        text = sub_path.read_text(encoding="utf-8")
        if _REQUIRED_TITLE[lab_id] not in text:
            result["notes"].append(f"Missing title: '{_REQUIRED_TITLE[lab_id]}'")
        result["missing_headings"] = _check_headings(lab_id, text)
    else:
        result["notes"].append("submission.md missing — paste finish_lab.md into Claude Code")

    status_path = sub_dir / "status.json"
    if status_path.exists():
        try:
            s = json.loads(status_path.read_text(encoding="utf-8"))
            result["status_json"] = True
            result["claims_ready"] = bool(s.get("ready_for_review", False))
        except Exception as exc:
            result["notes"].append(f"status.json parse error: {exc}")

    manifest_path = sub_dir / "evidence_manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            result["manifest_json"] = True
            if result["claims_ready"]:
                for entry in manifest.get("evidence", []):
                    if entry.get("required") and not (BASE / entry["path"]).exists():
                        result["missing_evidence"].append(entry["path"])
        except Exception as exc:
            result["notes"].append(f"evidence_manifest.json parse error: {exc}")

    has_content = result["submission_md"] and not result["missing_headings"]
    has_meta = result["status_json"] and result["manifest_json"]
    no_missing = not result["missing_evidence"]

    if result["claims_ready"] and not no_missing:
        result["grade"] = "Broken"
        result["notes"].append(
            f"Claims ready but {len(result['missing_evidence'])} evidence file(s) missing"
        )
    elif has_content and has_meta and no_missing and result["claims_ready"]:
        result["structural_pass"] = True
        result["grade"] = "Ready"
    elif result["dir_exists"]:
        result["grade"] = "In progress"

    return result


def _print_summary(results: list, mode: str = "progress") -> None:
    by_lab = {r["lab"]: r for r in results}
    rows = []
    for lab in VALID_LABS:
        r = by_lab.get(lab)
        if r is None:
            rows.append((lab, "Not started", ""))
        else:
            notes_parts = list(r["notes"])
            if r["missing_headings"]:
                notes_parts.insert(0, f"Missing headings: {r['missing_headings']}")
            rows.append((lab, r["grade"], "; ".join(notes_parts)))

    not_started = sum(1 for _, g, _ in rows if g == "Not started")
    in_progress = sum(1 for _, g, _ in rows if g == "In progress")
    ready = sum(1 for _, g, _ in rows if g == "Ready")
    broken = sum(1 for _, g, _ in rows if g == "Broken")

    label = "Progress Report" if mode == "progress" else "Grading Report"
    print("\n═══════════════════════════════════════════════════")
    print(f"  {label}")
    print(f"  {date.today().isoformat()}")
    print("═══════════════════════════════════════════════════")
    print(f"  {'Lab':<12} {'Status':<14} Notes")
    print(f"  {'-'*12} {'-'*14} {'-'*40}")
    for lab, grade, notes in rows:
        print(f"  {lab:<12} {grade:<14} {notes}")

    if mode == "progress":
        print(f"\n  {ready} ready · {in_progress} in progress · "
              f"{not_started} not started · {broken} broken")
        if not_started == len(VALID_LABS):
            print("  → Use the Finish Lab prompt after completing each lab.")
    else:
        # Strict mode — be reassuring when nothing is broken
        if broken == 0 and ready == 0:
            print(f"\n  No ready_for_review submissions to check.")
            print(f"  {not_started} not started · {in_progress} in progress")
            print("  Nothing failed.")
        elif broken == 0:
            print(f"\n  {ready} ready · {broken} broken · {not_started} not started")
            print("  All ready submissions pass structural check.")
        else:
            print(f"\n  {ready} ready · {broken} broken — see failures above")
    print("═══════════════════════════════════════════════════\n")


def _write_report(results: list) -> None:
    out_dir = BASE / "lecture-repo" / "outputs" / "grading"
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "graded_at": date.today().isoformat(),
        "total": len(results),
        "ready": sum(1 for r in results if r["grade"] == "Ready"),
        "broken": sum(1 for r in results if r["grade"] == "Broken"),
        "not_started": sum(1 for r in results if r["grade"] == "Not started"),
        "in_progress": sum(1 for r in results if r["grade"] == "In progress"),
        "results": results,
    }
    out_path = out_dir / "grading_report.json"
    out_path.write_text(json.dumps(report, indent=2))
    print(f"Report: {out_path.relative_to(BASE)}")


def _update_progress(results: list) -> None:
    by_lab = {r["lab"]: r for r in results}
    lines = [
        "# Course Progress\n",
        f"_Updated: {date.today().isoformat()}_\n\n",
        "| Lab | Work Folder | Submission Folder | Status | Notes |\n",
        "|-----|-------------|-------------------|--------|-------|\n",
    ]
    for lab_id in VALID_LABS:
        r = by_lab.get(lab_id)
        sub_folder = f"{lab_id}Submission/"
        work_folder = f"{lab_id}/work/"
        if r is None:
            lines.append(f"| {lab_id} | {work_folder} | {sub_folder} | Not started | |\n")
        else:
            notes = "; ".join(r["notes"]) if r["notes"] else ""
            lines.append(f"| {lab_id} | {work_folder} | {sub_folder} | {r['grade']} | {notes} |\n")
    progress_path = BASE / "COURSE_PROGRESS.md"
    progress_path.write_text("".join(lines))
    print(f"Progress: {progress_path.relative_to(BASE)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Grade lab submissions")
    parser.add_argument(
        "--mode",
        choices=["progress", "strict"],
        default="progress",
        help="progress: always exit 0. strict: exit 1 if broken submissions found.",
    )
    parser.add_argument(
        "--required",
        nargs="*",
        metavar="LAB",
        help="(strict only) Labs that must be submitted. E.g. --required Lab00 Lab01 Lab03",
    )
    args = parser.parse_args()

    results = [_grade_one(lab_id) for lab_id in VALID_LABS]
    _print_summary(results, mode=args.mode)
    _write_report(results)
    _update_progress(results)

    if args.mode == "strict":
        failures = []
        for r in results:
            if r["grade"] == "Broken":
                failures.append(
                    f"{r['lab']}: claims ready_for_review but "
                    f"evidence missing: {r['missing_evidence']}"
                )
        if args.required:
            for lab_id in args.required:
                r = next((x for x in results if x["lab"] == lab_id), None)
                if r is None or r["grade"] in ("Not started",):
                    failures.append(f"{lab_id}: required but not submitted")
                elif r["grade"] == "Broken":
                    failures.append(
                        f"{lab_id}: required but broken — {'; '.join(r['notes'])}"
                    )
                elif r["grade"] != "Ready":
                    failures.append(
                        f"{lab_id}: required but not complete — {'; '.join(r['notes'])}"
                    )
        if failures:
            print("Strict mode failures:")
            for f in failures:
                print(f"  ✗ {f}")
            sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
