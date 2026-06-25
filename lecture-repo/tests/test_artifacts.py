"""
Artifact tests for the LabXX/work/ structure.

These tests verify:
  1. Lab working folders and submission folders exist with correct structure
  2. For any lab that has been submitted, submission.md has the required headings
  3. For any lab that declares ready_for_review=true, required evidence files exist

Tests pass on a fresh student clone (no work done yet).
Tests fail only if a lab claims completion but is missing evidence.
"""
import json
from pathlib import Path
import pytest

BASE = Path(__file__).resolve().parents[2]

LABS = ["Lab00", "Lab01", "Lab02", "Lab03", "Lab04", "Lab05", "Capstone"]

REQUIRED_EVIDENCE = {
    "Lab00":    ["Lab00/work/L0_orientation.md", "Lab00/work/status.json"],
    "Lab01":    ["Lab01/work/L1_prompt_contract.md", "Lab01/work/status.json"],
    "Lab02":    ["Lab02/work/L2_multi_stakeholder_review.md", "Lab02/work/status.json"],
    "Lab03":    ["Lab03/work/L3_literature_search_skill.md",
                 "Lab03/work/L3_literature_search.md", "Lab03/work/status.json"],
    "Lab04":    ["Lab04/work/L4_tool_mcp_workflow.md", "Lab04/work/status.json"],
    "Lab05":    ["Lab05/work/L5_subagent_workflow.md",
                 "Lab05/work/L5_subagent_workflow_report.md", "Lab05/work/status.json"],
    "Capstone": ["Capstone/work/capstone_report.md",
                 "Capstone/work/showcase.md", "Capstone/work/status.json"],
}

SUBMISSION_HEADINGS = [
    "## Clinical problem",
    "## Agentic",
    "## What was produced",
    "## Human verification",
    "## Limitations",
]


# ─── Structure tests (always run, always pass on fresh clone) ─────────────────

@pytest.mark.parametrize("lab", LABS)
def test_lab_work_folder_exists(lab):
    d = BASE / lab / "work"
    assert d.exists(), f"{lab}/work/ folder missing"


@pytest.mark.parametrize("lab", LABS)
def test_submission_folder_exists(lab):
    sub = f"{lab}Submission"
    d = BASE / sub
    assert d.exists(), f"{sub}/ folder missing"


@pytest.mark.parametrize("lab", LABS)
def test_submission_readme_exists(lab):
    sub = f"{lab}Submission"
    readme = BASE / sub / "README.md"
    assert readme.exists(), f"{sub}/README.md missing"


# ─── Conditional tests (skip if lab not yet submitted) ───────────────────────

def _submission_md(lab: str) -> Path:
    return BASE / f"{lab}Submission" / "submission.md"


def _status_json(lab: str) -> dict | None:
    p = BASE / f"{lab}Submission" / "status.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None


@pytest.mark.parametrize("lab", LABS)
def test_submission_md_headings(lab):
    sub_md = _submission_md(lab)
    if not sub_md.exists():
        pytest.skip(f"{lab} not yet submitted")
    text = sub_md.read_text()
    for heading in SUBMISSION_HEADINGS:
        assert heading in text, (
            f"{lab}Submission/submission.md missing heading: {heading}"
        )


@pytest.mark.parametrize("lab", LABS)
def test_status_json_valid(lab):
    p = BASE / f"{lab}Submission" / "status.json"
    if not p.exists():
        pytest.skip(f"{lab} not yet submitted")
    try:
        data = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        pytest.fail(f"{lab}Submission/status.json is not valid JSON: {e}")
    assert "status" in data, f"{lab}Submission/status.json missing 'status' key"


@pytest.mark.parametrize("lab", LABS)
def test_ready_for_review_has_evidence(lab):
    """If submission claims ready_for_review=true, all evidence files must exist."""
    status = _status_json(lab)
    if status is None:
        pytest.skip(f"{lab} not yet submitted")
    if not status.get("ready_for_review"):
        pytest.skip(f"{lab} not marked ready_for_review")
    missing = [p for p in REQUIRED_EVIDENCE[lab] if not (BASE / p).exists()]
    assert not missing, (
        f"{lab} claims ready_for_review but evidence missing: {missing}"
    )
