PDFLATEX?=pdflatex
TEXSRCS=$(wildcard *.tex)
CORE_MAIN=ubt_core_main.tex
ALL_MAIN=ubt_2_main.tex

.PHONY: all core clean pdf verify ci
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

ci: pdf verify
	@echo "CI OK"

clean:
	latexmk -C || true
	@rm -f *.aux *.bbl *.blg *.lof *.log *.lot *.out *.toc *.fls *.fdb_latexmk
