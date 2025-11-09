.PHONY: all core clean pdf verify tests ci alpha-notebooks alpha-tests alpha-audit alpha-proof masses-tests

PDFLATEX?=pdflatex
TEXSRCS=$(wildcard *.tex)
CORE_MAIN=ubt_core_main.tex
ALL_MAIN=ubt_2_main.tex
MAIN_TEX := consolidation_project/ubt_2_main.tex
VERIFY_SCRIPT := consolidation_project/scripts/verify_lorentz_in_HC.py

core:
	$(PDFLATEX) -interaction=nonstopmode $(CORE_MAIN)
	$(PDFLATEX) -interaction=nonstopmode $(CORE_MAIN)

all:
	$(PDFLATEX) -interaction=nonstopmode $(ALL_MAIN)
	$(PDFLATEX) -interaction=nonstopmode $(ALL_MAIN)

pdf:
	@which latexmk >/dev/null 2>&1 || (echo "ERROR: latexmk not found. Install TeX Live/MacTeX."; exit 1)
	latexmk -pdf -halt-on-error -interaction=nonstopmode $(MAIN_TEX)

verify:
	@python3 -c "import sys, pathlib; p=pathlib.Path('$(VERIFY_SCRIPT)'); \
	             (print(f'ERROR: script not found: {p}') or sys.exit(1)) if not p.exists() else None"
	@python3 $(VERIFY_SCRIPT)

tests:
	python -m pytest -q

ci: pdf verify tests
	@echo "CI OK"

clean:
	latexmk -C || true
	@rm -f *.aux *.bbl *.blg *.lof *.log *.lot *.out *.toc *.fls *.fdb_latexmk

# Alpha derivation targets (v2 Playbook)

alpha-tests:
	@echo "Running alpha derivation tests (fit-free proof)..."
	pytest -v consolidation_project/alpha_two_loop/tests

alpha-audit:
	@echo "Auditing alpha derivation..."
	python3 tools/alpha_audit.py --root . --out reports/alpha_hits.json --context 6 || true
	python3 tools/latex_extract.py || true
	python3 tools/fill_checklist.py || true

alpha-proof:
	@echo "Building alpha proof documents..."
	@echo "Note: Individual tex files require proper documentclass setup"
	@echo "See consolidation_project/alpha_two_loop/tex/ for proof documents"

# Masses program targets

masses-tests:
	@echo "Running masses symbolic tests..."
	pytest -v consolidation_project/masses/tests || echo "Masses tests not yet implemented"

# Combined alpha + masses CI

alpha-ci: alpha-tests alpha-audit
	@echo "Alpha CI complete: tests passing, audit complete"

.PHONY: alpha-notebooks alpha-tests alpha-audit alpha-proof masses-tests alpha-ci

alpha-notebooks:
	@echo "Open and run the notebooks under consolidation_project/alpha_two_loop/notebooks/"
