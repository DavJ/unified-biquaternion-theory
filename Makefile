\
.PHONY: all clean roots build

EXCLUDES ?= consolidation_project/old

roots:
	@EXCLUDES="$(EXCLUDES)" scripts/find-tex-roots.sh > .tex_roots

build: roots
	@while read -r f; do \
		echo "==> Building $$f"; \
		( cd "$$(dirname "$$f")" && latexmk -pdf -interaction=nonstopmode "$$(basename "$$f")" ); \
	done < .tex_roots

all: build

clean:
	@while read -r f; do \
		( cd "$$(dirname "$$f")" && latexmk -C "$$(basename "$$f")" || true ); \
	done < .tex_roots 2>/dev/null || true
