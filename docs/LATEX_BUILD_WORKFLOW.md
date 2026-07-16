# Repository-wide LaTeX build workflow

The repository does not rely on a contributor manually compiling selected PDF
files. The canonical workflow is `.github/workflows/latex_build.yml`.

## Behaviour

1. `tools/latex_audit.py` discovers every active `.tex` file containing an
   uncommented `\documentclass` declaration.
2. Every root is compiled in an isolated output directory. Engine magic comments
   and packages are detected automatically; exceptional roots whose included
   files require another engine are listed in
   `.github/latex_engine_overrides.tsv`. A failed document,
   timeout, missing citation, or absent input file is recorded and the queue
   continues with the next root.
3. At the start of every run, `reports/latex_build/` is deleted completely and
   recreated. Therefore the tracked report never mixes different runs.
4. Successful PDFs are uploaded as one GitHub Actions artifact.
5. A small curated set listed in `.github/latex_publish_map.tsv` is copied into
   `docs/pdfs/` and committed on successful completion of the workflow job.
6. Failure logs and the summary are committed to `reports/latex_build/` on
   pushes to `master`.

Document failures do **not** fail the workflow. Missing build infrastructure
(for example no `latexmk`) still fails, because no meaningful audit could be
produced.

## Report layout

```text
reports/latex_build/
├── summary.md
├── results.json
├── roots.txt
├── failures.txt
└── logs/
    └── <one text log per failed or timed-out root>
```

The directory is generated data. Do not add hand-written notes there.

## Local use

```bash
python3 tools/latex_audit.py --jobs 4 --timeout 180
```

Compile only selected roots:

```bash
python3 tools/latex_audit.py \
  --include 'papers/*.tex' \
  --include 'canonical/gr_closure/*.tex'
```

A manual deep workflow includes `ARCHIVE/archive_legacy/` and
`research_tracks/legacy_theory_variants/`. It is intentionally not run on every
push because those trees contain superseded snapshots and many expected
failures.

Use `--strict` only for a release gate after the audit report has identified a
controlled set of roots that are required to pass. Do not make the repository-
wide discovery build fail-fast again.
