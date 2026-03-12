<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Repository Structure

This document describes the top-level architecture of the UBT repository.
It was established as part of the repository structure phase 2 reorganisation (2026-03-12).

---

## Top-Level Architecture

```
unified-biquaternion-theory/
│
├── core/                       ← Canonical, proved / established UBT physics
│   ├── canonical/              ← Current-best mainline (tightened, low-speculation)
│   │   ├── CANONICAL_DEFINITIONS.md
│   │   ├── SCOPE.md
│   │   ├── algebra/
│   │   ├── fields/
│   │   ├── geometry/
│   │   ├── interactions/
│   │   ├── bridges/
│   │   └── appendices/
│   ├── AXIOMS.md               ← Locked canonical axioms (AXIOM A, B, C, ...)
│   ├── core_assumptions.tex
│   └── gr_limit/               ← GR limit proof
│
├── extensions/                 ← Formal extensions (formalized but not canonical mainline)
│   └── [dark_sector/, holographic/, padic/, ...]
│
├── research_tracks/            ← Exploratory physics and mathematical tests
│   ├── associative_su3/
│   ├── fingerprints/           ← Coding fingerprint / parity side-tracks
│   ├── octonionic_completion/
│   └── three_generations/
│
├── speculative_extensions/     ← Conceptual / interpretative extensions (low formalization)
│   ├── consciousness/          ← Psychon / consciousness speculation
│   ├── cosmology_or_metaphysics/ ← Universe-as-atom and similar
│   ├── complex_consciousness/
│   ├── causality/
│   ├── invisibility/
│   └── [...]
│
├── experiments/                ← Numerical tests, parameter scans, simulation scripts
│   ├── constants_derivation/   ← Fine structure constant, mass ratio derivations
│   └── layer2_stability/       ← Layer 2 rigidity and stability scans
│
├── archive/                    ← Deprecated, obsolete, duplicate material (preserved)
│   ├── abandoned_tracks/
│   ├── deprecated/
│   └── historical_versions/
│
├── ARCHIVE/                    ← Legacy formulation variants (read-only)
│   └── legacy_variants/
│       ├── ubt_with_chronofactor/
│       ├── ubt_no_chronofactor/
│       └── ubt_compare/
│
├── consolidation_project/      ← Consolidated derivations and appendices
├── THEORY_COMPARISONS/         ← UBT vs other theories (sandboxed comparisons)
├── docs/                       ← Documentation, theory status maps, PDFs
├── tools/                      ← Repository audit and analysis tools
├── tests/                      ← Automated test suite
│
└── [root-level files]
    ├── README.md               ← Main entry point
    ├── DERIVATION_INDEX.md     ← Proof status of all major results
    ├── REPOSITORY_STRUCTURE.md ← This file
    └── ...
```

---

## Directory Roles

### `core/`

**Role**: The single authoritative home for proved and canonical UBT physics.

`core/` contains:
- `core/canonical/` — the current-best, tightened canonical mainline (see `core/canonical/SCOPE.md`)
- `core/AXIOMS.md` — locked canonical axioms (must not be redefined)
- `core/gr_limit/` — the GR limit proof

**Rules**:
- All content in `core/` must be internally consistent with `README.md` and `DERIVATION_INDEX.md`.
- `core/canonical/` follows the strict inclusion rules defined in `core/canonical/SCOPE.md`.
- Any change to `core/` requires Auditor approval (see `.github/CODEOWNERS`).

### `extensions/`

**Role**: Formal extensions of the UBT framework that are well-formalized but not yet canonical.

Extensions differ from `core/canonical/` in that they:
- Address new physical sectors (dark sector, holographic, p-adic, noncommutative, ...)
- Have some open questions or conditional assumptions
- Are not yet proved on the canonical admissible sector A_UBT

Extensions differ from `speculative_extensions/` in that they:
- Have mathematical formalization
- Do not assert speculative ontology (consciousness, simulation, etc.)

### `research_tracks/`

**Role**: Exploratory mathematical and physical tracks.

Research tracks are active investigations that are not yet ready for `core/` or `extensions/`.
They may involve:
- Testing novel algebraic structures (associative SU(3), octonionic completion)
- Investigating generation structure
- Fingerprint / parity forensics

**Subdirectories**:
| Path | Content |
|------|---------|
| `research_tracks/associative_su3/` | SU(3) derivation via associative algebra |
| `research_tracks/fingerprints/` | Coding fingerprint and spectral parity tests |
| `research_tracks/octonionic_completion/` | Octonionic extension track |
| `research_tracks/three_generations/` | Three-generation mechanism derivation |

### `speculative_extensions/`

**Role**: Conceptual or interpretative extensions — low formalization, speculative ontology.

Content here is explicitly **not** part of canonical UBT.  It includes:
- Consciousness / psychon models (`consciousness/`, `complex_consciousness/`)
- Universe-as-atom cosmological metaphysics (`cosmology_or_metaphysics/`)
- Causality extensions, invisibility models, etc.

**Key rule**: No content from `speculative_extensions/` should be cited as a proved result.

### `experiments/`

**Role**: Numerical tests, parameter scans, simulation scripts.

Experiments are executable code that test, verify, or explore UBT predictions.
They should reference the canonical equations they test.

**Subdirectories**:
| Path | Content |
|------|---------|
| `experiments/constants_derivation/` | Fine structure constant derivation |
| `experiments/layer2_stability/` | Layer 2 rigidity / stability scan |

### `archive/` and `ARCHIVE/`

**Role**: Deprecated, obsolete, or superseded material — preserved for reproducibility.

- `archive/` — deprecated tracks, historical status files, abandoned derivations
- `ARCHIVE/` — legacy UBT variants (with-chronofactor, no-chronofactor, comparison framework)

**Rule**: Files here are read-only. Do not cite them as current results.

---

## Proof-Status Conventions

UBT uses the following status labels throughout the repository (defined in `DERIVATION_INDEX.md`):

| Label | Meaning |
|-------|---------|
| ✅ Proved [L0] | Analytically proved with no free parameters |
| ✅ Proved [L1] | Proved with stated conditional assumptions |
| ⚡ Supported | Supported by numerical evidence |
| 🔭 Predicted | Testable prediction, not yet observed |
| 📐 Semi-empirical | Requires ≥1 fitted parameter |
| ❌ Open | Unsolved problem or dead end |
| 💀 Dead End | Approach shown to fail |

---

## Navigation Guide

| Question | Where to look |
|----------|---------------|
| What has UBT actually proved? | `DERIVATION_INDEX.md` |
| Current theory status? | `docs/THEORY_STATUS.md` |
| Canonical definitions? | `core/canonical/CANONICAL_DEFINITIONS.md` |
| Canonical axioms? | `core/AXIOMS.md` |
| GR recovery proof? | `core/gr_limit/GR_limit_of_UBT.tex` |
| QED from UBT? | `core/canonical/interactions/qed.tex` |
| Consciousness content? | `speculative_extensions/consciousness/` |
| Fingerprint tests? | `research_tracks/fingerprints/` |
| Numerical experiments? | `experiments/` |
| Legacy variants? | `ARCHIVE/legacy_variants/` |

---

## Governance

| Directory | Code Owner | Change Process |
|-----------|-----------|----------------|
| `core/` | @auditor | PR + Auditor review; `allow-core-change` label |
| `original_release_of_ubt/` | @auditor | PR + Auditor review |
| `unified_biquaternion_theory/` | @auditor | PR + Auditor review (historical, read-only) |
| `experiments/` | @experimentalist @auditor | PR with test output |
| `tools/` | @engineer @auditor | PR with test output |
| All other | Any contributor | PR with description |

See `.github/CODEOWNERS` for the authoritative ownership rules.

---

**Last Updated**: 2026-03-12  
**Status**: Phase 2 structure established
