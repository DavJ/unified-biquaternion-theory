# Repository Structure Guide

**Path**: `docs/repo_structure.md`  
**Date**: 2026-03-11  
**Purpose**: Navigation guide to the UBT repository after the 2026-03 archive cleanup.

---

## Root Directory Layout

The repository root contains a large number of files.  This guide explains the main
directories and how to navigate them.  Legacy clutter has been moved to `ARCHIVE/`
(see Section 4).

```
/
├── README.md                 # Main entry point
├── DERIVATION_INDEX.md       # Index of all derivation files
├── CURRENT_STATUS.md         # Summary of theory status
├── FITTED_PARAMETERS.md      # Parameters that are fitted, not derived
├── RESEARCH_PRIORITIES.md    # Current research focus areas
├── docs/                     # Documentation (this directory)
├── ARCHIVE/                  # Archived legacy and generated content
├── AUDITS/                   # Audit reports and gap backlogs
├── THEORY/                   # Core theory documents
├── THEORY_COMPARISONS/       # Comparison sandboxes (twistor, su3, etc.)
├── canonical/                # Canonical (authoritative) UBT definitions
├── consolidation_project/    # Consolidated UBT document project
├── speculative_extensions/   # Speculative extensions (consciousness, CTCs)
├── tests/                    # Root-level test suite
├── tools/                    # Repository audit and utility tools
├── unified_biquaternion_theory/  # Original UBT documents (historical)
└── ...                       # See below for remaining directories
```

---

## 1. Primary Theory Documents

### 1.1 Canonical Definitions (`canonical/`)

The `canonical/` directory contains the authoritative mathematical definitions for UBT.
All other documents should be consistent with these.

| Subdirectory | Content |
|---|---|
| `canonical/geometry/` | Metric, curvature, connection, GR recovery |
| `canonical/fields/` | Biquaternion field definition, AXIOM B |
| `canonical/algebra/` | Biquaternion algebra, generators |
| `canonical/interactions/` | Gauge fields, SM embedding |

Key files:
- `canonical/geometry/metric.tex` — canonical UBT metric definition
- `canonical/geometry/curvature.tex` — curvature tensors (derived quantities)
- `canonical/geometry/gr_as_limit.tex` — GR recovery in real limit
- `canonical/geometry/gr_completion_attempt.tex` — GR recovery status

### 1.2 Consolidation Project (`consolidation_project/`)

A consolidated, structured version of the UBT derivation chain.

| Subdirectory | Content |
|---|---|
| `GR_closure/` | Stepwise GR recovery derivation |
| `T_munu_derivation/` | Stress-energy tensor derivation |
| `B_derivation/` | Magnetic field / gauge structure derivation |
| `FPE_verification/` | Fokker–Planck equation checks |
| `scripts/` | Computation scripts |

Key files in `GR_closure/`:
- `step1_metric_unification.tex` — emergent metric from Θ
- `step2_theta_only_closure.tex` — Θ-only variational argument (on-shell, injectivity assumption required)
- `step3_signature_theorem.tex` — Lorentzian signature derivation
- `step4_offshell_Tmunu.tex` — off-shell T_μν properties

**Note**: The `GR_closure/step2_theta_only_closure.tex` result is conditional on an
injectivity assumption.  See `AUDITS/followup_gap_backlog_2026_03.md` GAP-01.

### 1.3 Original UBT Documents (`unified_biquaternion_theory/`)

The original research documents by David Jaroš.  These are the primary source;
the consolidation_project provides a structured reorganization.

---

## 2. Theory Comparisons (`THEORY_COMPARISONS/`)

Sandboxes comparing UBT to other frameworks.

| Sandbox | Content | Status |
|---|---|---|
| `penrose_twistor/` | UBT ↔ Penrose twistor theory | Active; flat-space bridge proved |
| `su3_qubit_mapping/` | su(3) → qubit homomorphism | Active |
| `dimensional_economy/` | Dimensional reduction sandbox | Active |
| `multi_criteria_v56/` | Multi-criteria optimization | Active |

### Penrose Twistor Sandbox (`THEORY_COMPARISONS/penrose_twistor/`)

Key files (as of 2026-03-11):
- `STATUS.md` — claim register stratified by evidence level
- `ubt_twistor_bridge_note.md` — technical bridge note
- `tau_phase_mapping.md` — analysis of UBT phase ψ in twistor geometry
- `curved_bridge_todo.md` — plan for curved spacetime extension
- `twistor_core/` — core implementation modules
- `experiments/` — experiment scripts (e01–e08)
- `tests/` — test suite (99 tests, all passing)
- `reports/` — experiment output summaries

---

## 3. Audit and Documentation (`AUDITS/`, `docs/`)

### Audits (`AUDITS/`)

| File | Content |
|---|---|
| `followup_gap_backlog_2026_03.md` | Gap backlog from 2026-03 audit |
| `claim_evidence_matrix.md` | Claims vs evidence matrix |
| `copilot_repo_verification_and_gap_report.md` | Copilot gap report |
| `repository_claim_map.md` | Map of claims across repo |

### Documentation (`docs/`)

| File | Content |
|---|---|
| `status_legend.md` | Canonical status label definitions |
| `repo_structure.md` | This file |
| `pdfs/` | Compiled PDF outputs |

---

## 4. Archive (`ARCHIVE/`)

The `ARCHIVE/` directory contains content that was moved from the root to reduce
clutter.  **No scientific content was deleted**; all content is preserved.

### Archive Structure

```
ARCHIVE/
├── README.md                           # Archive overview
├── archive_manifest.tsv                # Every moved file with SHA256
├── archive_move_log.md                 # Rationale for each move
├── legacy_variants/                    # Legacy UBT variant directories
│   ├── ubt_with_chronofactor/
│   ├── ubt_no_chronofactor/
│   └── ubt_compare/
├── generated_outputs/                  # Auto-generated test/scan outputs
│   ├── test_output/
│   └── scans/
├── patches_and_dropins/                # Patch files and drop-in guides
│   ├── README_DROPIN.txt
│   ├── README_SPECTRAL_PARITY_SCAN.txt
│   ├── integration_guide.txt
│   ├── patch_*.patch
│   └── ...
└── duplicate_or_snapshot_roots/        # Snapshot directories
    ├── ubt_audit_pack_v2/
    └── ...
```

### How to Access Archived Content

All archived content is fully accessible at its `ARCHIVE/` path.  The manifest
`ARCHIVE/archive_manifest.tsv` lists every file with its original path, new path,
SHA256 hash, and reason for archiving.

---

## 5. Status Summary Files

These files provide theory status summaries at different levels:

| File | Scope | Notes |
|---|---|---|
| `CURRENT_STATUS.md` | Overall theory status | Last updated Nov 2025 |
| `FITTED_PARAMETERS.md` | Which parameters are fitted | Maintained manually |
| `RESEARCH_PRIORITIES.md` | Current research priorities | — |
| `docs/status_legend.md` | **Status label definitions** | Authoritative reference |
| `AUDITS/followup_gap_backlog_2026_03.md` | **Known gaps** | Updated 2026-03-11 |
| `reports/gr_recovery_final_status.md` | GR recovery chain status | — |
| `THEORY_COMPARISONS/penrose_twistor/STATUS.md` | Twistor bridge status | Updated 2026-03-11 |

---

## 6. Test Suites

| Location | Coverage | Run command |
|---|---|---|
| `tests/` | Core UBT: α, GR, manifolds, provenance | `pytest -q tests/` |
| `THEORY_COMPARISONS/penrose_twistor/tests/` | Twistor bridge (99 tests) | `pytest -q THEORY_COMPARISONS/penrose_twistor/tests/` |
| `THEORY_COMPARISONS/su3_qubit_mapping/tests/` | su(3) qubit mapping | `pytest -q THEORY_COMPARISONS/su3_qubit_mapping/tests/` |

**Dependencies**: `sympy` is required for twistor tests (`pip install sympy`).

---

## 7. Navigation by Topic

### To understand the GR recovery chain:
1. `canonical/geometry/gr_as_limit.tex` — overview
2. `consolidation_project/GR_closure/step1_metric_unification.tex`
3. `consolidation_project/GR_closure/step2_theta_only_closure.tex`
4. `consolidation_project/T_munu_derivation/step3_einstein_with_matter.tex`
5. `reports/gr_recovery_final_status.md` — current status

### To understand the twistor bridge:
1. `THEORY_COMPARISONS/penrose_twistor/STATUS.md` — claim register
2. `THEORY_COMPARISONS/penrose_twistor/ubt_twistor_bridge_note.md` — technical note
3. `THEORY_COMPARISONS/penrose_twistor/twistor_core/` — implementation

### To understand the fine-structure constant derivation:
1. `DERIVATION_INDEX.md` — index of α derivation files
2. `alpha_core_repro/` — α computation scripts
3. `FITTED_PARAMETERS.md` — which parameters are fitted

### To understand known gaps and open problems:
1. `AUDITS/followup_gap_backlog_2026_03.md` — gap backlog
2. `docs/status_legend.md` — status label definitions
3. `reports/gr_recovery_final_status.md` — GR-specific gaps
