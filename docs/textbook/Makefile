REPO_ROOT := $(abspath ../..)
BUILD_ROOT := $(REPO_ROOT)/build/textbook
WORK_ROOT := $(BUILD_ROOT)/work
PUBLIC_ROOT := $(BUILD_ROOT)/public
PUBLISH_ROOT := $(REPO_ROOT)/docs/pdfs
TEXINPUTS_ENV := TEXINPUTS=$(REPO_ROOT)/tex//:

TEXTBOOK_PDF := $(PUBLIC_ROOT)/UBT_Textbook.pdf
COVARIANT_PDF := $(PUBLIC_ROOT)/UBT_Textbook_Supplement_Covariant_Tetrad.pdf
INDICES_PDF := $(PUBLIC_ROOT)/UBT_Textbook_Supplement_Indexy_Torze_Rot_CS.pdf
PUBLIC_PDFS := $(TEXTBOOK_PDF) $(COVARIANT_PDF) $(INDICES_PDF)

.PHONY: all build publish verify clean list

all: build

build: $(PUBLIC_PDFS)

$(TEXTBOOK_PDF): main.tex chapters/*.tex appendices/*.tex frontmatter/*.tex
	mkdir -p $(WORK_ROOT)/main $(PUBLIC_ROOT)
	$(TEXINPUTS_ENV) latexmk -pdf -halt-on-error -interaction=nonstopmode \
		-file-line-error -outdir=$(WORK_ROOT)/main main.tex
	cp $(WORK_ROOT)/main/main.pdf $@

$(COVARIANT_PDF): covariant_tetrad_student_paper.tex chapters/04_covariant_tetrad_geometry.tex
	mkdir -p $(WORK_ROOT)/covariant $(PUBLIC_ROOT)
	$(TEXINPUTS_ENV) latexmk -pdf -halt-on-error -interaction=nonstopmode \
		-file-line-error -outdir=$(WORK_ROOT)/covariant covariant_tetrad_student_paper.tex
	cp $(WORK_ROOT)/covariant/covariant_tetrad_student_paper.pdf $@

$(INDICES_PDF): indices_torsion_anticommutator_rot_student_paper_cs.tex \
	student_papers/indices_torsion_anticommutator_rot_cs.tex
	mkdir -p $(WORK_ROOT)/indices $(PUBLIC_ROOT)
	$(TEXINPUTS_ENV) latexmk -pdf -halt-on-error -interaction=nonstopmode \
		-file-line-error -outdir=$(WORK_ROOT)/indices \
		indices_torsion_anticommutator_rot_student_paper_cs.tex
	cp $(WORK_ROOT)/indices/indices_torsion_anticommutator_rot_student_paper_cs.pdf $@

publish: build
	mkdir -p $(PUBLISH_ROOT)
	cp $(PUBLIC_PDFS) $(PUBLISH_ROOT)/

verify: build
	@test -s $(TEXTBOOK_PDF)
	@test -s $(COVARIANT_PDF)
	@test -s $(INDICES_PDF)
	@printf '%s\n' 'Textbook PDF set is present:'
	@ls -lh $(PUBLIC_PDFS)

list:
	@printf '%s\n' $(PUBLIC_PDFS)

clean:
	rm -rf $(BUILD_ROOT)
	latexmk -C main.tex covariant_tetrad_student_paper.tex \
		indices_torsion_anticommutator_rot_student_paper_cs.tex || true
