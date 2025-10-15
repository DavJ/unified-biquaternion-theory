# Complex-Time Theta Transform — LaTeX Paper

## Files
- `main.tex` — full article
- `style/preamble.tex` — packages and macros
- `refs.bib` — bibliography entries (add your UBT/CCT details)
- `figures/` — place figures here

## Build
Use `pdflatex` + `bibtex` (or `latexmk`):

```bash
latexmk -pdf main.tex
# or:
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The paper defines the complex-time theta transform with Gaussian window, quadratic phase and imaginary-time shift, and motivates its physical and predictive interpretation.