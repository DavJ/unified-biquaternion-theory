# Archive Move Log

**Task**: `repo_prune_with_full_archive_preservation`  
**Date**: 2026-03-11  
**Performed by**: GitHub Copilot agent  
**Hard rules**: `never_delete_files: true` — all content preserved; only paths changed.

---

## Phase 1 — Safe Moves (no reference update required)

These items had no inbound references from canonical root files.

| From (root) | To (ARCHIVE/) | Reason |
|-------------|--------------|--------|
| `ubt_audit_pack_v2/` | `duplicate_or_snapshot_roots/ubt_audit_pack_v2/` | Audit bundle snapshot, not canonical runtime/theory root |
| `test_output/` | `generated_outputs/test_output/` | Generated test output artefacts |
| `scans/` | `generated_outputs/scans/` | Generated scan CSVs and JSON artefacts |
| `README_DROPIN.txt` | `patches_and_dropins/README_DROPIN.txt` | Drop-in helper text, root clutter |
| `README_DROPIN_RS_SYNDROME.txt` | `patches_and_dropins/README_DROPIN_RS_SYNDROME.txt` | Drop-in helper text, root clutter |
| `README_SPECTRAL_PARITY_SCAN.txt` | `patches_and_dropins/README_SPECTRAL_PARITY_SCAN.txt` | Drop-in helper text, root clutter |
| `integration_guide.txt` | `patches_and_dropins/integration_guide.txt` | Auxiliary guide, root clutter |
| `integration_guide_m0.txt` | `patches_and_dropins/integration_guide_m0.txt` | Auxiliary guide, root clutter |
| `patch_healpy_compat.patch` | `patches_and_dropins/patch_healpy_compat.patch` | Patch artefact, root clutter |
| `patch_phase_shear_and_weighting.patch` | `patches_and_dropins/patch_phase_shear_and_weighting.patch` | Patch artefact, root clutter |
| `prime_gated.patch` | `patches_and_dropins/prime_gated.patch` | Patch artefact, root clutter |
| `radial-spectrum.patch` | `patches_and_dropins/radial-spectrum.patch` | Patch artefact, root clutter |
| `radial-spectrum.clean.patch` | `patches_and_dropins/radial-spectrum.clean.patch` | Patch artefact, root clutter |

---

## Phase 2 — Conditional Moves (references updated before move)

These items had inbound references from canonical files. All references were updated in
the same commit before the move was executed.

| From (root) | To (ARCHIVE/) | References updated |
|-------------|--------------|-------------------|
| `ubt_with_chronofactor/` | `legacy_variants/ubt_with_chronofactor/` | `README.md`, `docs/UBT_MAP.md`, `docs/PROOFKIT_ALPHA.md`, `THEORY/topic_indexes/hecke_index.md` |
| `ubt_no_chronofactor/` | `legacy_variants/ubt_no_chronofactor/` | `README.md` |
| `ubt_compare/` | `legacy_variants/ubt_compare/` | `README.md` |
| `DOCS/` | `duplicate_or_snapshot_roots/DOCS/` | `README.md`, `THEORY/README.md`, `copilot/tasks/UBT-TIME-FIX-001.md`, `copilot/tasks/UBT-TIME-DOC-001.md` |
| `data/` | `duplicate_or_snapshot_roots/data/` | None found |
| `report/` | `duplicate_or_snapshot_roots/report/` | `docs/predictions/UBT_cosmology_predictions.md` |

---

## Verification

- All moved files are listed with SHA-256 and byte size in `archive_manifest.tsv`
- Use `git log --follow -- <old_path>` to trace history of any moved file
- Scientific content is unchanged; only file paths were modified

---

## Items left at root (canonical_keep_at_root)

Per the task specification the following were intentionally **not** moved:

**Directories**: `.github/`, `canonical/`, `consolidation_project/`, `THEORY/`,
`THEORY_COMPARISONS/`, `docs/`, `DATA/`, `tests/`, `validation/`, `reports/`,
`copilot/`, `tools/`, `scripts/`, `papers/`, `publication/`, `forensic_fingerprint/`,
`FINGERPRINTS/`, `HUBBLE_LATENCY/`, `research_tracks/`, `experiments/`, `computations/`

**Files**: `README.md`, `DERIVATION_INDEX.md`, `FITTED_PARAMETERS.md`, `CURRENT_STATUS.md`,
`CHANGELOG.md`, `ROADMAP.md`, `REPO_GOVERNANCE.md`, `CONTRIBUTING.md`, `CITATION.cff`,
`LICENSE.md`, `requirements.txt`, `pytest.ini`, `references.bib`, `Makefile`
