# ARCHIVE — Preserved Legacy & Generated Content

This directory preserves **all content** that was removed from the canonical root during
the repository pruning task `repo_prune_with_full_archive_preservation` (2026-03-11).

**Nothing has been deleted.** Every file is intact and traceable via `archive_manifest.tsv`.

---

## Subdirectory Index

| Directory | Content | Reason archived |
|-----------|---------|-----------------|
| `legacy_variants/` | Old parallel theory trees (`ubt_with_chronofactor/`, `ubt_no_chronofactor/`, `ubt_compare/`) | Legacy/alternate-branch roots; not the canonical theory location |
| `generated_outputs/` | `test_output/`, `scans/` | Generated artefacts; not source content |
| `duplicate_or_snapshot_roots/` | `ubt_audit_pack_v2/`, `DOCS/`, `data/`, `report/` | Duplicate-capitalization trees or audit bundles |
| `patches_and_dropins/` | `.patch` files, `README_DROPIN*.txt`, `integration_guide*.txt` | Helper / patch clutter at repo root |
| `top_level_reports/` | (reserved for future use) | — |
| `migration_stubs/` | (reserved for future use) | — |

---

## How to find old content

1. Open `archive_manifest.tsv` — every moved file is listed with its old path, new path,
   SHA-256 hash, byte size, and reason.
2. Or use `git log --follow -- <old_path>` to trace the full history of any file.
3. Or look at `archive_move_log.md` for a human-readable narrative of every move.

---

## Canonical root directories (not archived)

The following directories remain at the repository root and constitute the **current
canonical content**:

```
.github/          canonical/         consolidation_project/
THEORY/           THEORY_COMPARISONS/ docs/
DATA/             tests/             validation/
reports/          copilot/           tools/
scripts/          papers/            publication/
forensic_fingerprint/  FINGERPRINTS/  HUBBLE_LATENCY/
research_tracks/  experiments/       computations/
```

Key root files: `README.md`, `DERIVATION_INDEX.md`, `FITTED_PARAMETERS.md`,
`CURRENT_STATUS.md`, `CHANGELOG.md`, `ROADMAP.md`, `REPO_GOVERNANCE.md`,
`CONTRIBUTING.md`, `CITATION.cff`, `LICENSE.md`, `requirements.txt`,
`pytest.ini`, `references.bib`, `Makefile`.

---

*Archive created by GitHub Copilot agent — task `repo_prune_with_full_archive_preservation`.*
