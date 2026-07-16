# Patch notes — v10.2.1 tetrad audit and resilient LaTeX workflow

**Baseline:** GitHub release `v10.2.0`, commit `89f225951444760e60e12ee0d8afc604605eb077`.

## Scientific governance

- Froze the covariant-tetrad architecture for the v10.x line.
- Added the mandatory **architecture-before-repair** rule: before adding modes,
  fields, fibers, projections, or embeddings, determine whether the obstruction
  is an artefact of the formulation.
- Added explicit review language preventing autonomous framework pivots by
  Copilot or other agents.
- Added `reviews/tetrad_architecture_audit_2026-07-16.md`, separating standard
  Cartan/tetrad geometry from UBT-specific results and checking the exact scope
  of the one-sided no-go and two-sided identity.
- Added `canonical/gr_closure/HISTORICAL_FIBER_ROUTE_STATUS.md`. The fiber route
  is archived as mathematically consistent but weakly selective, not as
  disproved.
- Clarified that the two-sided derivative is a minimal demonstrated escape from
  the one-sided obstruction, not a proved unique possibility.
- Added standard references for the tetrad postulate, Levi-Civita spin
  connection, torsion, and contorsion.

## PDF and LaTeX automation

- Replaced the fail-fast canonical-only workflow with a repository-wide batch
  compiler.
- `tools/latex_audit.py` automatically discovers every active standalone TeX
  root, compiles each in isolation, continues after failure, and writes one
  clean report directory.
- `reports/latex_build/` is deleted completely at the start of each run and
  regenerated with `summary.md`, `results.json`, `roots.txt`, `failures.txt`,
  and one text log for each failed or timed-out root.
- Every successful PDF is uploaded as one GitHub Actions artifact.
- A curated publication map automatically refreshes the canonical, GR,
  connection, integrability, rank, and student PDFs under `docs/pdfs/`.
- The report and curated PDFs are committed by the workflow on `master` using a
  `[skip ci]` commit and a rebase-before-push guard.
- A manual deep workflow attempts archived/legacy roots without blocking on
  individual failures.

## Status

No new fundamental physics gap is claimed closed in this patch. The central
results and open ledger from v10.2.0 remain unchanged:

- `GAP-10T-DYN`: OPEN;
- `GAP-10I-CURVED`: OPEN;
- `GAP-10D`: OPEN.
