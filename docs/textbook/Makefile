REPO_ROOT := $(abspath ../..)
BUILD_ROOT := $(REPO_ROOT)/build/textbook
WORK_ROOT := $(BUILD_ROOT)/work
PUBLIC_ROOT := $(BUILD_ROOT)/public
PUBLISH_ROOT := $(REPO_ROOT)/docs/pdfs
TEXINPUTS_ENV := TEXINPUTS=$(REPO_ROOT)/tex//:

TEXTBOOK_PDF := $(PUBLIC_ROOT)/UBT_Textbook.pdf
PUBLISHED_TEXTBOOK_PDF := $(PUBLISH_ROOT)/UBT_Textbook.pdf

.PHONY: all build publish verify clean list

all: build

build: $(TEXTBOOK_PDF)

$(TEXTBOOK_PDF): main.tex chapters/*.tex appendices/*.tex frontmatter/*.tex
	mkdir -p $(WORK_ROOT)/main $(PUBLIC_ROOT)
	$(TEXINPUTS_ENV) latexmk -pdf -halt-on-error -interaction=nonstopmode \
		-file-line-error -outdir=$(WORK_ROOT)/main main.tex
	cp $(WORK_ROOT)/main/main.pdf $@

publish: build
	mkdir -p $(PUBLISH_ROOT)
	cp $(TEXTBOOK_PDF) $(PUBLISHED_TEXTBOOK_PDF)

verify: build
	@test -s $(TEXTBOOK_PDF)
	@printf '%s\n' 'Official textbook PDF is present:'
	@ls -lh $(TEXTBOOK_PDF)

list:
	@printf '%s\n' $(TEXTBOOK_PDF)

clean:
	rm -rf $(BUILD_ROOT)
	latexmk -C main.tex || true
