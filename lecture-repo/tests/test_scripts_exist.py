"""
Script existence tests.
"""

from pathlib import Path

LECTURE = Path("lecture-repo")


def test_day1_scripts_exist():
    for name in [
        "bootstrap.py",
        "fetch_data.py",
        "visualize_sample.py",
        "run_train.py",
        "error_analysis.py",
        "model_swap.py",
        "pack_report.py",
    ]:
        assert (LECTURE / "scripts" / name).exists(), f"Missing: lecture-repo/scripts/{name}"


def test_day2_scripts_exist():
    for name in [
        "challenge_plan.py",
        "adapt_pipeline.py",
        "translation_memo.py",
    ]:
        assert (LECTURE / "scripts" / name).exists(), f"Missing: lecture-repo/scripts/{name}"
