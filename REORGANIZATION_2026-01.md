# Repository Reorganization - January 2026

## Purpose

This document describes the repository reorganization completed in January 2026 to transform the UBT repository into an audit-ready scientific framework with clear separation of:

1. Core theory
2. Derived fingerprints  
3. Court-grade forensic tests (including null results)
4. Documentation for readers vs auditors
5. Speculative notes
6. Hubble Latency solution as first-class module

## New Structure

The repository now follows this organization:

```
unified-biquaternion-theory/
├── THEORY/              # Core axioms, mathematics, architecture
├── FINGERPRINTS/        # Confirmed/candidate/null predictions
├── FORENSICS/           # Court-grade testing protocols
├── HUBBLE_LATENCY/      # Hubble tension interpretation (isolated)
├── DATA/                # Observational data with SHA-256 manifests
├── TOOLS/               # Data provenance, simulations, plotting
├── DOCS/                # Documentation for various audiences
└── SPECULATIVE/         # Non-core speculative extensions
```

## Key Principles

### 1. Null Results Are First-Class Outcomes

Planck CMB PR3 null result (p = 0.919) is preserved verbatim in `FINGERPRINTS/null_results/combined_verdict.md`. This demonstrates:
- Scientific integrity (no cherry-picking)
- Falsifiability (theory makes testable predictions)
- Resource allocation (shows where NOT to look)

### 2. Hubble Latency Isolated

The Hubble Latency module is now clearly isolated with conservative disclaimers:
- NOT dark energy
- NOT a new particle
- NOT a dynamical modification
- Architectural synchronization/clock-skew effect

See `HUBBLE_LATENCY/README.md`

### 3. Speculation Clearly Separated

All consciousness-related content, CTCs, and multiverse interpretations are in `SPECULATIVE/notes/`. Core UBT makes NO claims about these topics.

### 4. Court-Grade Reproducibility

All empirical tests include:
- Pre-registered protocols (`FORENSICS/protocols/`)
- SHA-256 manifests (`DATA/manifests/`)
- Exact reproduction commands
- Fail-fast validation

## Migration Guide

### For Finding Old Content

If you're looking for something from the old repository structure:

| Old Location | New Location |
|--------------|--------------|
| `appendix_hubble_latency.md` | `HUBBLE_LATENCY/appendix/` |
| `calibrate_hubble_latency.py` | `HUBBLE_LATENCY/calibration/` |
| `forensic_fingerprint/` | `FORENSICS/` |
| `forensic_fingerprint/run_real_data_cmb_comb.py` | `FORENSICS/cmb_comb/run_cmb_comb_court_grade.py` |
| `data/planck_pr3/` | `DATA/planck_pr3/` |
| `data/wmap/` | `DATA/wmap/` |
| `scripts/*.py` | `TOOLS/simulations/` |
| `tools/data_provenance/` | `TOOLS/data_provenance/` |
| `core/core_assumptions.tex` | `THEORY/axioms/` |
| `canonical/fields/` | `THEORY/math/fields/` |
| `canonical/geometry/` | `THEORY/architecture/geometry/` |
| `speculative_extensions/` | `SPECULATIVE/notes/` |
| CMB NULL verdict | `FINGERPRINTS/null_results/combined_verdict.md` |

### For External References

If you have papers, bookmarks, or scripts pointing to old paths, update as follows:

**Data files**: All data is now in `DATA/` with subdirectories for each survey
**Analysis scripts**: Simulation tools are in `TOOLS/simulations/`
**Protocols**: Testing protocols are in `FORENSICS/protocols/`
**Documentation**: High-level docs are in `DOCS/`, theory docs in `THEORY/`

## What Changed

### Added

- **THEORY/**: Centralized location for core axioms and mathematical framework
- **FINGERPRINTS/**: Organized predictions by empirical status (confirmed/candidate/null)
- **FORENSICS/**: Renamed and reorganized forensic testing framework
- **HUBBLE_LATENCY/**: Isolated module for Hubble tension interpretation
- **DOCS/**: User-facing documentation (overview, glossary, publication notes)
- **Comprehensive READMEs**: Every major directory has explanatory README.md

### Renamed

- `forensic_fingerprint/run_real_data_cmb_comb.py` → `FORENSICS/cmb_comb/run_cmb_comb_court_grade.py`
- Root `README.md` → Completely rewritten for clarity and audit-readiness

### Moved

- Core theory files → `THEORY/`
- Data files → `DATA/`
- Scripts → `TOOLS/simulations/`
- Provenance tools → `TOOLS/data_provenance/`
- Speculative content → `SPECULATIVE/`
- CMB null result → `FINGERPRINTS/null_results/`

### Preserved

- **ALL scientific content** - Nothing deleted
- **Git history** - All moves tracked in version control
- **Null results** - Planck CMB verdict preserved verbatim
- **Data integrity** - SHA-256 manifests still validate
- **Reproducibility** - All analysis scripts functional with new paths

## What Did NOT Change

### Unchanged Files

The following directories remain as-is for now (may be organized in future):

- `original_release_of_ubt/` - Historical archive
- `consolidation_project/` - LaTeX consolidation work
- `canonical/` - Canonical definitions (partially copied to THEORY/)
- `docs/` - Legacy documentation (lowercase, distinct from new DOCS/)
- `tools/` - Legacy tools (lowercase, distinct from new TOOLS/)
- Root `.md` files - Theory status, roadmaps, analyses (to be organized later)

These remain accessible but are not part of the new auditable structure.

## Next Steps

### Planned Future Work

1. **Migrate legacy docs/** content to **DOCS/** where appropriate
2. **Consolidate theory files** from multiple sources into **THEORY/**
3. **Update internal links** throughout repository to use new structure
4. **Create automated tests** to verify structure integrity
5. **Add GitHub Actions** to validate manifests on every commit

### For Contributors

When adding new content:

1. **Predictions** → Pre-register in `FORENSICS/protocols/`, test results go to `FINGERPRINTS/`
2. **Theory** → Core axioms and derivations go to `THEORY/`
3. **Data** → Raw data with manifests go to `DATA/`
4. **Tools** → Analysis scripts go to `TOOLS/simulations/`
5. **Speculation** → Non-core extensions go to `SPECULATIVE/`

See `CONTRIBUTING.md` for detailed guidelines.

## Validation Checklist

- [x] All new directories created
- [x] HUBBLE_LATENCY isolated with conservative README
- [x] Planck NULL verdict preserved in FINGERPRINTS/null_results/
- [x] Confirmed fingerprints documented (α, m_e)
- [x] FORENSICS protocols preserved with court-grade README
- [x] DATA organized with manifests
- [x] THEORY README created with assumptions/derivations/non-claims
- [x] DOCS created with overview, glossary, publication notes
- [x] SPECULATIVE separated with clear disclaimers
- [x] Top-level README rewritten (conservative, audit-ready)
- [x] No scientific content deleted
- [x] Git history preserves all moves

## Contact

Questions about the reorganization? See:
- Structure rationale: This file
- Content location: Migration guide above
- Contributing: `CONTRIBUTING.md`
- Issues: GitHub Issues

---

**Reorganization completed**: 2026-01-12
**Approved by**: Repository maintainers
**Philosophy**: Clarity, reproducibility, and auditability over compactness or creativity
