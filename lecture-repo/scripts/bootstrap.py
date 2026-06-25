from pathlib import Path
import json
import platform
import sys

base = Path(__file__).resolve().parents[2]

lecture = base / "lecture-repo"
for rel in ["outputs/figures", "outputs/metrics", "outputs/status", "reports", "data/sample"]:
    (lecture / rel).mkdir(parents=True, exist_ok=True)

info = {
    "python_version": sys.version.split()[0],
    "platform": platform.platform(),
    "status": "ok",
}

(lecture / "reports/env_check.md").write_text(
    "# Environment Check\n\nBootstrap completed successfully.\n",
    encoding="utf-8",
)
(lecture / "outputs/status/stage_00_bootstrap.json").write_text(
    json.dumps(info, indent=2), encoding="utf-8"
)
print("Bootstrap completed.")
