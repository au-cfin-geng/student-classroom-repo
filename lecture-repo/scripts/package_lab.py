"""
Create a submission package for one lab.

Usage:
    python lecture-repo/scripts/package_lab.py --lab Lab03
    python lecture-repo/scripts/package_lab.py --lab Capstone
    python lecture-repo/scripts/package_lab.py --all
    python lecture-repo/scripts/package_lab.py --lab Lab03 --force

Or via root Makefile:
    make package LAB=Lab03

Creates:
    Lab03Submission/evidence_manifest.json
    Lab03Submission/status.json
    Lab03Submission/submission.md  (scaffold — never overwrites without --force)
    COURSE_PROGRESS.md             (updated at repo root)
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]

# ── Evidence definitions ───────────────────────────────────────────────────────
# primary: expected student work in LabXX/work/
# legacy:  old paths from pre-refactor structure (kept for backward compat)

EVIDENCE = {
    "Lab00": {
        "primary": [
            "Lab00/work/L0_orientation.md",
            "Lab00/work/status.json",
        ],
        "legacy": [
            "lecture-repo/reports/labs/L0_orientation.md",
            "lecture-repo/outputs/labs/L0/status.json",
            "lecture-repo/outputs/status/lab_00_agentic_studio.json",
        ],
    },
    "Lab01": {
        "primary": [
            "Lab01/work/L1_prompt_contract.md",
            "Lab01/work/status.json",
        ],
        "legacy": [
            "lecture-repo/reports/labs/L1_prompt_contract.md",
            "lecture-repo/outputs/labs/L1/status.json",
            "lecture-repo/outputs/status/lab_01_prompt_contract.json",
        ],
    },
    "Lab02": {
        "primary": [
            "Lab02/work/L2_multi_stakeholder_review.md",
            "Lab02/work/status.json",
        ],
        "legacy": [
            "lecture-repo/reports/labs/L2_multi_stakeholder_review.md",
            "lecture-repo/outputs/labs/L2/status.json",
            "lecture-repo/outputs/status/lab_02_multi_stakeholder_review.json",
        ],
    },
    "Lab03": {
        "primary": [
            "Lab03/work/L3_literature_search_skill.md",
            "Lab03/work/L3_literature_search.md",
            "Lab03/work/status.json",
        ],
        "legacy": [
            "lecture-repo/skills/L3_literature_search_skill.md",
            "lecture-repo/reports/labs/L3_literature_search.md",
            "lecture-repo/outputs/labs/L3/status.json",
        ],
    },
    "Lab04": {
        "primary": [
            "Lab04/work/L4_tool_mcp_workflow.md",
            "Lab04/work/status.json",
        ],
        "legacy": [
            "lecture-repo/reports/labs/L4_tool_mcp_workflow.md",
            "lecture-repo/outputs/labs/L4/status.json",
        ],
    },
    "Lab05": {
        "primary": [
            "Lab05/work/L5_subagent_workflow.md",
            "Lab05/work/L5_subagent_workflow_report.md",
            "Lab05/work/status.json",
        ],
        "legacy": [
            "lecture-repo/workflows/L5_subagent_workflow.md",
            "lecture-repo/reports/labs/L5_subagent_workflow.md",
            "lecture-repo/outputs/labs/L5/status.json",
        ],
    },
    "Capstone": {
        "primary": [
            "Capstone/work/capstone_report.md",
            "Capstone/work/showcase.md",
            "Capstone/work/status.json",
        ],
        "legacy": [
            "lecture-repo/reports/capstone/capstone_report.md",
            "lecture-repo/reports/capstone/showcase.md",
            "lecture-repo/outputs/capstone/status.json",
        ],
    },
}

VALID_LABS = list(EVIDENCE.keys())


def _submission_dir(lab_id):
    return BASE / f"{lab_id}Submission"


# ── Submission scaffold templates ──────────────────────────────────────────────

_LAB_TEMPLATE = """\
# {lab_id} Submission

_Fill in this submission after completing the lab. Then run:_
_`make package LAB={lab_id}` to update the evidence manifest._

## Clinical problem

_What clinical research problem did you investigate in this lab?_

## Agentic / Claude concept

_What agentic concept did you apply? What did the prompt pattern look like?_

## What was produced

_List the artifacts created in {lab_id}/work/. What does each contain?_

## Human verification

_What did you verify, judge, or correct in Claude's output?_

## Limitations

_What limitations or failure modes did you observe?_

## Ready for review

- [ ] All required artifacts are committed to git
- [ ] Reflection questions answered in your lab report
- [ ] Ready: YES / NO
"""

_CAPSTONE_TEMPLATE = """\
# Capstone Submission

_Fill in this submission after completing the capstone mini-project. Then run:_
_`make package LAB=Capstone` to update the evidence manifest._

## Research problem

_What clinical research problem did you investigate?_

## Agentic workflow used

_Which labs and concepts (Lab00–Lab05) did you integrate? Describe the workflow._

## Evidence and artifacts

_List your committed artifacts in Capstone/work/ and what each demonstrates._

## Human verification

_At which points did you review, judge, or correct Claude's output?_

## Limitations

_What limitations did you encounter? What would you do differently?_

## Showcase summary

_In 3–5 sentences: what did you build, what did you learn, and what is the next step?_

## Ready for review

- [ ] All required artifacts are committed to git
- [ ] Reflection questions answered
- [ ] Showcase summary written
- [ ] Ready: YES / NO
"""


def _submission_template(lab_id):
    if lab_id == "Capstone":
        return _CAPSTONE_TEMPLATE
    return _LAB_TEMPLATE.format(lab_id=lab_id)


# ── Core logic ─────────────────────────────────────────────────────────────────

def _scan_evidence(lab_id):
    spec = EVIDENCE[lab_id]
    entries = []
    for path_str in spec["primary"]:
        p = BASE / path_str
        entries.append({
            "path": path_str,
            "required": True,
            "found": p.exists(),
            "size_bytes": p.stat().st_size if p.exists() else None,
        })
    for path_str in spec["legacy"]:
        p = BASE / path_str
        if p.exists():
            entries.append({
                "path": path_str,
                "required": False,
                "found": True,
                "size_bytes": p.stat().st_size,
            })
    return entries


def package_lab(lab_id, force=False):
    print(f"\n── Packaging {lab_id} ──────────────────────────────────────────")

    sub_dir = _submission_dir(lab_id)
    sub_dir.mkdir(parents=True, exist_ok=True)

    evidence = _scan_evidence(lab_id)
    required = [e for e in evidence if e["required"]]
    found_required = [e for e in required if e["found"]]
    all_required_found = len(found_required) == len(required)

    for e in evidence:
        icon = "✓" if e["found"] else "○"
        tag = " [required]" if e["required"] else " [legacy]"
        print(f"  {icon} {e['path']}{tag}")

    manifest = {
        "lab": lab_id,
        "work_folder": f"{lab_id}/work/",
        "submission_folder": f"{lab_id}Submission/",
        "packaged_at": date.today().isoformat(),
        "evidence": evidence,
        "all_required_found": all_required_found,
        "any_found": any(e["found"] for e in evidence),
    }
    manifest_path = sub_dir / "evidence_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"  → {manifest_path.relative_to(BASE)}")

    status = {
        "lab": lab_id,
        "packaged_at": date.today().isoformat(),
        "all_required_found": all_required_found,
        "required_count": len(required),
        "found_required_count": len(found_required),
        "ready_for_review": all_required_found,
    }
    status_path = sub_dir / "status.json"
    status_path.write_text(json.dumps(status, indent=2))
    print(f"  → {status_path.relative_to(BASE)}")

    sub_path = sub_dir / "submission.md"
    if not sub_path.exists() or force:
        action = "Overwriting" if sub_path.exists() else "Creating"
        print(f"  → {action} {sub_path.relative_to(BASE)}")
        sub_path.write_text(_submission_template(lab_id))
    else:
        print(f"  ○ {sub_path.relative_to(BASE)} exists — skipping (--force to overwrite)")

    if all_required_found:
        print(f"  ✓ {lab_id}: ready for review")
    else:
        missing = [e["path"] for e in required if not e["found"]]
        print(f"  ✗ {lab_id}: {len(missing)} required artifact(s) missing:")
        for m in missing:
            print(f"      {m}")

    return 0


def _update_progress():
    lines = [
        "# Course Progress\n",
        f"_Updated: {date.today().isoformat()}_\n\n",
        "| Lab | Work Folder | Packaged | Ready for Review |\n",
        "|-----|-------------|---------|------------------|\n",
    ]
    for lab_id in VALID_LABS:
        status_path = _submission_dir(lab_id) / "status.json"
        if status_path.exists():
            try:
                s = json.loads(status_path.read_text())
                packaged = "✓"
                ready = "✓ Ready" if s.get("ready_for_review") else "○ Missing artifacts"
            except Exception:
                packaged = "?"
                ready = "?"
        else:
            packaged = "○"
            ready = "—"
        lines.append(f"| {lab_id} | {lab_id}/work/ | {packaged} | {ready} |\n")
    progress_path = BASE / "COURSE_PROGRESS.md"
    progress_path.write_text("".join(lines))
    print(f"\n  → Updated {progress_path.relative_to(BASE)}")


def main():
    parser = argparse.ArgumentParser(description="Package a lab submission")
    parser.add_argument("--lab", help=f"Lab to package: {', '.join(VALID_LABS)}")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite submission.md if it already exists")
    parser.add_argument("--all", dest="all_labs", action="store_true",
                        help="Package all labs")
    args = parser.parse_args()

    if args.all_labs:
        labs = VALID_LABS
    elif args.lab:
        # Accept both "Lab03" and "lab03" forms
        lab_id = args.lab
        if lab_id not in EVIDENCE:
            # Try capitalising the first letter(s)
            candidates = [k for k in EVIDENCE if k.lower() == lab_id.lower()]
            if candidates:
                lab_id = candidates[0]
            else:
                print(f"Error: unknown lab '{args.lab}'. Valid: {', '.join(VALID_LABS)}")
                sys.exit(1)
        labs = [lab_id]
    else:
        parser.print_help()
        sys.exit(1)

    for lab_id in labs:
        rc = package_lab(lab_id, force=args.force)
        if rc != 0:
            sys.exit(rc)

    _update_progress()
    print("\nDone.")


if __name__ == "__main__":
    main()
