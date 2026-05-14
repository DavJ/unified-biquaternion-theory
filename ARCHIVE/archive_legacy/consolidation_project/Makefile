PDFLATEX?=pdflatex
CORE_MAIN=ubt_core_main.tex
ALL_MAIN=ubt_2_main.tex

.PHONY: all core clean

all:
	$(PDFLATEX) -interaction=nonstopmode $(ALL_MAIN)
	$(PDFLATEX) -interaction=nonstopmode $(ALL_MAIN)

core:
	$(PDFLATEX) -interaction=nonstopmode $(CORE_MAIN)
	$(PDFLATEX) -interaction=nonstopmode $(CORE_MAIN)

clean:
	rm -f *.aux *.log *.out *.toc *.pdf *.bbl *.blg *.lof *.lot
