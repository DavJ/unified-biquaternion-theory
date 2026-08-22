REPO_ROOT := $(abspath ../..)
BUILD_ROOT := $(REPO_ROOT)/build/textbook
WORK_ROOT := $(BUILD_ROOT)/work
PUBLIC_ROOT := $(BUILD_ROOT)/public
PUBLISH_ROOT := $(REPO_ROOT)/docs/pdfs
TEXINPUTS_ENV := TEXINPUTS=$(REPO_ROOT)/tex//:

TEXTBOOK_CS_PDF := $(PUBLIC_ROOT)/UBT_Textbook_CS.pdf
TEXTBOOK_EN_PDF := $(PUBLIC_ROOT)/UBT_Textbook_EN.pdf
TEXTBOOK_PDFS := $(TEXTBOOK_CS_PDF) $(TEXTBOOK_EN_PDF)

.PHONY: all build publish verify clean list

all: build

build: $(TEXTBOOK_PDFS)

$(TEXTBOOK_CS_PDF): main.tex main.cs.tex chapters/*.cs.tex appendices/*.cs.tex frontmatter/*.cs.tex
	mkdir -p $(WORK_ROOT)/cs $(PUBLIC_ROOT)
	$(TEXINPUTS_ENV) latexmk -pdf -halt-on-error -interaction=nonstopmode \
		-file-line-error -outdir=$(WORK_ROOT)/cs main.cs.tex
	cp $(WORK_ROOT)/cs/main.cs.pdf $@

$(TEXTBOOK_EN_PDF): main.tex main.en.tex chapters/*.en.tex appendices/*.en.tex frontmatter/*.en.tex
	mkdir -p $(WORK_ROOT)/en $(PUBLIC_ROOT)
	$(TEXINPUTS_ENV) latexmk -pdf -halt-on-error -interaction=nonstopmode \
		-file-line-error -outdir=$(WORK_ROOT)/en main.en.tex
	cp $(WORK_ROOT)/en/main.en.pdf $@

publish: build
	mkdir -p $(PUBLISH_ROOT)
	cp $(TEXTBOOK_CS_PDF) $(PUBLISH_ROOT)/UBT_Textbook_CS.pdf
	cp $(TEXTBOOK_EN_PDF) $(PUBLISH_ROOT)/UBT_Textbook_EN.pdf

verify: build
	@test -s $(TEXTBOOK_CS_PDF)
	@test -s $(TEXTBOOK_EN_PDF)
	@test "$$(find $(PUBLIC_ROOT) -maxdepth 1 -type f -name 'UBT_Textbook_*.pdf' | wc -l | tr -d ' ')" = 2
	@printf '%s\n' 'Official bilingual textbook PDFs are present:'
	@ls -lh $(TEXTBOOK_PDFS)

list:
	@printf '%s\n' $(TEXTBOOK_PDFS)

clean:
	rm -rf $(BUILD_ROOT)
	latexmk -C main.cs.tex main.en.tex || true
