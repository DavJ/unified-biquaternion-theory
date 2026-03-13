<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Repository Culture

**Last Updated:** 2026-03-12  
**Author:** Ing. David Jaroš  
**Version:** v1.0 (root_detox_phase1)

---

## 1. One Source of Truth

The canonical, mainline theory lives exclusively in **`core/`**.

- `core/` is the single authoritative tree for the Unified Biquaternion Theory (UBT).
- All other directories are secondary, archived, experimental, or speculative.
- Do **not** create new parallel top-level directories that duplicate or shadow `core/`.

---

## 2. No New Parallel Core Directories

The following root-level directories are **permanently forbidden** as new top-level additions:

- `canonical/`, `core_ubt/`, `ubt/`, `ubt_core/`, `strict_ubt/` — these have been merged into `core/`
- `unified_biquaternion_theory/` — historical; now archived in `core/unified_biquaternion_theory/`

If you need a new theory subtree, create it **inside** `core/` (e.g., `core/my_extension/`), not at the repository root.

---

## 3. Root Hygiene Rules

The repository root **must** contain only:

| Entry | Purpose |
|-------|---------|
| `README.md` | Project overview |
| `DERIVATION_INDEX.md` | Index of all derivations |
| `CURRENT_STATUS.md` | Current development status |
| `CHANGELOG.md` | Version history |
| `CITATION.cff` | Citation metadata |
| `LICENSE.md` | License information |
| `CONTRIBUTING.md` | Contribution guidelines |
| `CODE_OF_CONDUCT.md` | Community standards |
| `core/` | Canonical theory tree |
| `research_tracks/` | Non-mainline research branches |
| `speculative_extensions/` | Ontology-heavy / speculative content |
| `experiments/` | Numerical experiments and computations |
| `archive/` | Deprecated, historical, or superseded content |
| `docs/` | Process documentation, reports, meta files |
| `.github/` | CI/CD and GitHub configuration |
| `tests/` | Test suite |
| `tools/` | Repository maintenance tools |
| `scripts/` | Utility scripts |
| `DATA/` | Observational and experimental data |

**No new top-level files or directories** should be added to the root without explicit approval. All new content goes into the appropriate subdirectory.

---

## 4. Where Speculative Content Goes

Speculative content belongs in **`speculative_extensions/`**:

- Content that is not yet physically testable
- Ontology-heavy material (consciousness models, psychons, CTCs)
- Extensions to UBT that have not been validated
- Philosophical or interpretational appendices

Speculative content must **not** appear in `core/`.

---

## 5. Where Experiments Go

Computational experiments and numerical studies belong in **`experiments/`**:

- Python scripts for physics computations
- Numerical simulations
- Parameter fitting and optimization runs
- Calibration scripts

---

## 6. Where Research Tracks Go

Non-mainline theory branches and exploratory research belong in **`research_tracks/`**:

- Alternative theoretical approaches (THEORY_COMPARISONS)
- Exploratory mathematical investigations
- Research-phase-lock snapshots
- Information-theoretic probes
- Comparison with other theories

---

## 7. File Naming and Structure

- Use ALL_CAPS_WITH_UNDERSCORES for top-level policy/status documents (e.g., `CURRENT_STATUS.md`)
- Use lowercase with underscores for theory files and scripts
- Avoid creating report/summary files at the root; they go in `docs/`
- Historical snapshots and superseded content go in `archive/`

---

## 8. Pull Request Guidelines

Before opening a PR:

1. Check that no new files or directories are being added to the root
2. Ensure new theory content goes into `core/` or an appropriate subdirectory
3. Run the test suite: `pytest tests/`
4. Verify CI passes

---

*This document was created as part of the `root_detox_phase1` reorganization.*
