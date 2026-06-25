"""
Structural tests — verify the repository skeleton is intact.

Run from the repo root: pytest -q lecture-repo/tests/test_preflight.py
"""

from pathlib import Path
import json

LECTURE = Path("lecture-repo")


def test_readme_exists_and_nontrivial():
    p = Path("README.md")
    assert p.exists(), "README.md is missing"
    assert len(p.read_text(encoding="utf-8")) > 200, "README.md is too short"


def test_assignment_exists():
    assert Path("ASSIGNMENT.md").exists(), "ASSIGNMENT.md is missing"


def test_claude_md_exists_and_nontrivial():
    p = Path("CLAUDE.md")
    assert p.exists(), "CLAUDE.md is missing"
    assert len(p.read_text(encoding="utf-8")) > 200, "CLAUDE.md is too short"


def test_makefile_exists():
    assert Path("Makefile").exists(), "Makefile is missing"


def test_requirements_txt_exists():
    assert (LECTURE / "requirements.txt").exists(), "lecture-repo/requirements.txt is missing"


def test_artifacts_schema_exists():
    p = LECTURE / "artifacts" / "schema.json"
    assert p.exists(), "lecture-repo/artifacts/schema.json is missing"
    data = json.loads(p.read_text(encoding="utf-8"))
    assert "required_outputs" in data, "schema.json must have a 'required_outputs' key"


def test_teaching_pack_cfg_exists():
    assert (LECTURE / "data" / "teaching_pack.cfg").exists(), (
        "lecture-repo/data/teaching_pack.cfg is missing."
    )


def test_teaching_pack_cfg_example_exists():
    assert (LECTURE / "data" / "teaching_pack.cfg.example").exists(), (
        "lecture-repo/data/teaching_pack.cfg.example is missing."
    )


def test_all_stage_prompts_exist():
    expected = [
        "stage_00_bootstrap.md",
        "stage_01_fetch_sample.md",
        "stage_02_load_visualize.md",
        "stage_03_train_baseline.md",
        "stage_04_error_analysis.md",
        "stage_05_model_swap.md",
        "stage_06_pack_report.md",
        "stage_07_challenge_plan.md",
        "stage_08_adapt_pipeline.md",
        "stage_09_translation_memo.md",
    ]
    for name in expected:
        assert (LECTURE / "prompts" / name).exists(), f"Missing prompt: lecture-repo/prompts/{name}"


def test_all_stage_scripts_exist():
    expected = [
        "bootstrap.py",
        "fetch_data.py",
        "inspect_data.py",
        "data_utils.py",
        "visualize_sample.py",
        "run_train.py",
        "error_analysis.py",
        "model_swap.py",
        "pack_report.py",
        "challenge_plan.py",
        "adapt_pipeline.py",
        "translation_memo.py",
    ]
    for name in expected:
        assert (LECTURE / "scripts" / name).exists(), f"Missing script: lecture-repo/scripts/{name}"


def test_lab_working_folders_exist():
    for lab in ["Lab00", "Lab01", "Lab02", "Lab03", "Lab04", "Lab05", "Capstone"]:
        assert Path(lab).exists(), f"Missing lab working folder: {lab}/"
        assert (Path(lab) / "work").exists(), f"Missing work dir: {lab}/work/"


def test_lab_submission_folders_exist():
    for lab in ["Lab00", "Lab01", "Lab02", "Lab03", "Lab04", "Lab05", "Capstone"]:
        assert Path(f"{lab}Submission").exists(), f"Missing submission folder: {lab}Submission/"


def test_package_and_grade_scripts_exist():
    assert (LECTURE / "scripts" / "package_lab.py").exists()
    assert (LECTURE / "scripts" / "grade_submissions.py").exists()
