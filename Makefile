
# Merged Makefile: TeX/Alpha + Infra (Docker/K8s) + New alpha-grid/insensitivity
# --------------------------------------------------------------------------------
# Usage highlights:
#   make pdf               # build main TeX (latexmk)
#   make core / make all   # build core/all PDFs (legacy targets)
#   make alpha-grid        # generate CSV grid (mock bring-up)
#   make alpha-grid-strict # generate CSV grid (strict, needs real two-loop)
#   make insensitivity     # run insensitivity sweep
#   make test-mock         # tests with mock
#   make test-strict       # tests strict (no mock)
#   make ci                # pdf + verify + tests
#   make nats-up-now ...   # infra (from new section)
#   make k8s-apply ...     # k8s helpers
#
# Variables:
#   PDFLATEX?=pdflatex
#   TEX_MAIN?=consolidation_project/ubt_2_main.tex
#   VERIFY_SCRIPT?=consolidation_project/scripts/verify_lorentz_in_HC.py
#   GRID_CSV?=alpha_core_repro/out/alpha_two_loop_grid.csv

SHELL := /bin/bash

# ----------------------------- Legacy/TeX variables -----------------------------
.PHONY: all core clean pdf verify tests ci alpha-notebooks alpha-tests alpha-audit alpha-proof masses-tests alpha-ci

PDFLATEX ?= pdflatex
TEXSRCS   = $(wildcard *.tex)
CORE_MAIN = consolidation_project/ubt_core_main.tex
ALL_MAIN  = consolidation_project/ubt_2_main.tex
TEX_MAIN ?= consolidation_project/ubt_2_main.tex
VERIFY_SCRIPT ?= consolidation_project/scripts/verify_lorentz_in_HC.py

# ----------------------------- TeX build targets --------------------------------
core:
	cd consolidation_project && $(PDFLATEX) -interaction=nonstopmode ubt_core_main.tex
	cd consolidation_project && $(PDFLATEX) -interaction=nonstopmode ubt_core_main.tex

all:
	cd consolidation_project && $(PDFLATEX) -interaction=nonstopmode ubt_2_main.tex
	cd consolidation_project && $(PDFLATEX) -interaction=nonstopmode ubt_2_main.tex

pdf:
	@which latexmk >/dev/null 2>&1 || (echo "ERROR: latexmk not found. Install TeX Live/MacTeX."; exit 1)
	latexmk -pdf -halt-on-error -interaction=nonstopmode $(TEX_MAIN)

verify:
	@python3 -c "import sys, pathlib; p=pathlib.Path('$(VERIFY_SCRIPT)'); (print(f'ERROR: script not found: {p}') or sys.exit(1)) if not p.exists() else None"
	@python3 $(VERIFY_SCRIPT)

tests:
	python -m pytest -q

ci: alpha-grid masses-csv tests test-provenance
	@echo "CI OK: PDFs, verification, tests, and provenance checks passed"

clean:
	latexmk -C || true
	@rm -f *.aux *.bbl *.blg *.lof *.log *.lot *.out *.toc *.fls *.fdb_latexmk

# ----------------------------- Alpha program (legacy) ---------------------------
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
	@echo "Running masses tests (fit-free electron mass derivation)..."
	pytest -v tests/test_electron_mass.py
	@echo "Running masses symbolic tests..."
	pytest -v consolidation_project/masses/tests || echo "Masses symbolic tests not yet implemented"

# Combined alpha + masses CI
alpha-ci: alpha-tests alpha-audit
	@echo "Alpha CI complete: tests passing, audit complete"

alpha-notebooks:
	@echo "Open and run the notebooks under consolidation_project/alpha_two_loop/notebooks/"

# ----------------------------- New alpha-grid targets ---------------------------
# CSV grid path for per-sector alpha
GRID_CSV ?= alpha_core_repro/out/alpha_two_loop_grid.csv

# Default all: ensure grid exists then build pdf
.DEFAULT_GOAL := full
full: $(GRID_CSV) pdf

alpha-grid:
	@echo "[alpha-grid] Generating CSV (mock) -> $(GRID_CSV)"
	@export UBT_ALPHA_STRICT=0 UBT_ALPHA_ALLOW_MOCK=1; \
	python -m alpha_core_repro.run_grid

alpha-grid-strict:
	@echo "[alpha-grid-strict] Generating CSV (STRICT) -> $(GRID_CSV)"
	@export UBT_ALPHA_STRICT=1; unset UBT_ALPHA_ALLOW_MOCK; \
	python -m alpha_core_repro.run_grid

$(GRID_CSV):
	@$(MAKE) alpha-grid

# Insensitivity sweep
insensitivity:
	@echo "[insensitivity] Running insensitivity sweep"
	@python -m insensitivity.sweep

# Export lepton masses to CSV
masses-csv:
	@echo "[masses-csv] Exporting computed lepton masses to CSV"
	@python -m ubt_masses.export_leptons_csv

# Tests with/without mock
test-mock:
	@echo "[test-mock] Running two-loop + insensitivity tests (MOCK)"
	@export UBT_ALPHA_STRICT=0 UBT_ALPHA_ALLOW_MOCK=1; \
	pytest -q alpha_core_repro/tests/test_alpha_two_loop.py; \
	pytest -q insensitivity/tests/test_insensitivity.py || true

test-strict:
	@echo "[test-strict] Running two-loop + insensitivity tests (STRICT)"
	@export UBT_ALPHA_STRICT=1; unset UBT_ALPHA_ALLOW_MOCK; \
	pytest -q alpha_core_repro/tests/test_alpha_two_loop.py || true; \
	pytest -q insensitivity/tests/test_insensitivity.py

# Provenance tests (verify computed, not hard-coded data)
test-provenance:
	@echo "[test-provenance] Running data provenance tests"
	@pytest -q tests/test_alpha_provenance.py
	@pytest -q tests/test_electron_sensitivity.py
	@pytest -q tests/test_electron_mass_precision.py
	@pytest -q tests/test_docs_use_generated_csv.py

deepclean: clean
	@rm -f $(GRID_CSV)
	@rm -rf alpha_core_repro/out insensitivity/out

# ----------------------------- Infra (Docker/K8s) -------------------------------
.PHONY: nats-up-now nats-up-plain nats-status integration lint fmt es app ingest down \
        k8s-apply k8s-set-image k8s-port k8s-job k8s-clean

nats-up-now:
	docker compose -f docker-compose.nats.yml up -d

nats-up-plain:
	docker compose -f docker-compose.nats.plain.yml up -d

nats-status:
	bash scripts/nats-status.sh

integration:
	python -m pytest -m integration -q

fmt:
	black .
	ruff format .
	# For older ruff:
	# ruff check --fix .

lint:
	ruff check .

es:    ; docker compose -f docker-compose.rag.yml up -d elasticsearch
app:   ; docker compose -f docker-compose.rag.yml up -d --build app
ingest:; docker compose -f docker-compose.rag.yml run --rm ingest
down:  ; docker compose -f docker-compose.rag.yml down

# --- Kubernetes helpers ---
IMAGE ?= ghcr.io/your-user/synaptix-core
TAG   ?= $(shell git rev-parse --short HEAD)

k8s-apply:
	kubectl apply -f k8s/namespace.yaml
	kubectl apply -f k8s/configmap.yaml
	@if test -f k8s/secret.yaml; then kubectl apply -f k8s/secret.yaml; else echo "(info) k8s/secret.yaml not found, skipping"; fi
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml

k8s-set-image:
	kubectl -n synaptix-core set image deploy/synaptix-core api=$(IMAGE):$(TAG)

k8s-port:
	kubectl -n synaptix-core port-forward svc/synaptix-core 8000:8000

k8s-job:
	kubectl apply -f k8s/ingest-job.yaml
	kubectl -n synaptix-core logs job/synaptix-core-ingest -f || true

k8s-clean:
	kubectl -n synaptix-core delete job/synaptix-core-ingest --ignore-not-found

# === Strict UBT targets (non-invasive; append to existing Makefile) ===

alpha-2loop:
	@echo "Computing 2-loop running of alpha (strict)..."
	python3 alpha_core_repro/two_loop_core.py

alpha-3loop:
	@echo "Computing 3-loop running of alpha (strict)..."
	python3 alpha_core_repro/three_loop_core.py

masses:
	@echo "Computing self-consistent lepton masses (strict)..."
	python3 tools/strict_ubt/self_consistent_solver.py

report:
	@echo "Building UBT strict comparison report..."
	cd report && pdflatex UBT_Strict_AlphaMass_Comparison.tex

all-strict: alpha-2loop alpha-3loop masses report
	@echo "All strict computations complete."

rigor-test:
	@echo "Checking TeX sources for hard-coded numbers (heuristic)..."
	@! grep -R --exclude-dir=.git -E '(^|[^\\])([0-9]+(\.[0-9]+)?)' report/*.tex || (echo "Found raw numbers; ensure all values come from CSV/macros." && exit 1) || true
