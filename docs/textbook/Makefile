all: main.pdf
main.pdf: main.tex chapters/*.tex appendices/*.tex frontmatter/*.tex
	latexmk -pdf -halt-on-error -interaction=nonstopmode main.tex
clean:
	latexmk -C
