all: main.pdf indices_torsion_anticommutator_rot_student_paper_cs.pdf

main.pdf: main.tex chapters/*.tex appendices/*.tex frontmatter/*.tex
	TEXINPUTS=../../tex: latexmk -pdf -halt-on-error -interaction=nonstopmode main.tex

indices_torsion_anticommutator_rot_student_paper_cs.pdf: \
	indices_torsion_anticommutator_rot_student_paper_cs.tex \
	student_papers/indices_torsion_anticommutator_rot_cs.tex
	TEXINPUTS=../../tex: latexmk -pdf -halt-on-error -interaction=nonstopmode \
		indices_torsion_anticommutator_rot_student_paper_cs.tex

clean:
	latexmk -C
