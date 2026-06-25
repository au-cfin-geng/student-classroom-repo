LECTURE = lecture-repo

.PHONY: dashboard app preflight test check package finish progress grade help

help:
	@echo ""
	@echo "Agentic Clinical Research Studio"
	@echo ""
	@echo "Student commands:"
	@echo "  make dashboard          Start course dashboard"
	@echo "  make preflight          Structural check — no data required"
	@echo "  make progress           Show current lab progress (always succeeds)"
	@echo ""
	@echo "Lab completion (normally run by Claude via Finish Lab prompt):"
	@echo "  make package LAB=Lab03  Package Lab03 → Lab03Submission"
	@echo "  make finish  LAB=Lab03  Alias for package"
	@echo ""
	@echo "Instructor / CI commands:"
	@echo "  make test               Full test suite"
	@echo "  make grade              Strict grading — fails on broken ready submissions"
	@echo ""

dashboard app:
	python -m streamlit run $(LECTURE)/app/streamlit_app.py

preflight:
	python $(LECTURE)/scripts/bootstrap.py
	pytest -q $(LECTURE)/tests/test_preflight.py $(LECTURE)/tests/test_scripts_exist.py

test check:
	pytest -q $(LECTURE)/tests/

package:
	python $(LECTURE)/scripts/package_lab.py --lab $(LAB)

finish:
	python $(LECTURE)/scripts/package_lab.py --lab $(LAB)

progress:
	python $(LECTURE)/scripts/grade_submissions.py --mode progress

grade:
	python $(LECTURE)/scripts/grade_submissions.py --mode strict
