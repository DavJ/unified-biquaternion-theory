<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Repository Layers

This document defines the authority hierarchy of the Unified Biquaternion Theory
(UBT) repository. Every file in the repository belongs to exactly one layer.

---

## Authority Model

### Primary Status Authority

**`DERIVATION_INDEX.md`** is the **golden source of truth** for:
- What derivations exist
- Current derivation status (PROVEN, PARTIAL, OPEN, etc.)
- Claim maturity and layer classification
- Theory coverage map

If any other document (README, topic index, test, secondary summary) disagrees
with `DERIVATION_INDEX.md` on a derivation status question, treat
`DERIVATION_INDEX.md` as authoritative until it is verified and corrected.

`DERIVATION_INDEX.md` is itself subject to audit; treat it as primary but not
infallible.

---

## Layer Definitions

### `canonical/`

**Authoritative theory text** — the current best internally consistent
formulation of UBT that the project stands behind.

Canonical content:
- Definitions of theory objects (biquaternion algebra, Θ field, complex time)
- Core algebraic structures
- Main derivations with complete proofs
- Appendices supporting canonical derivations
- Bridges between theory sectors

Canonical content must be:
- Internally consistent
- Mathematically defined
- Compatible with GR and Standard Model limits

**What does NOT belong in `canonical/`:**
- Conceptual designs without equations
- Philosophical interpretations
- Experimental probes
- Incomplete derivations
- Speculative ontologies

---

### `research_tracks/`

**Active research front** — promising, non-canonical research lines,
extensions, comparisons, and partial developments that may later be promoted
to canonical.

Research tracks contain:
- Active derivation attempts at open problems
- Theory comparisons with competing frameworks
- Numerical explorations of model parameters
- Partial results awaiting closure
- Historical variants of the theory under active revision

Content in `research_tracks/` is valuable and maintained, but not yet
authoritative enough for canonical status.

---

### `speculative_extensions/`

**Exploratory ideas** — conceptual or exploratory material not yet strong
enough for canonical or research track status.

Speculative content includes:
- Consciousness and psychon models (Complex Consciousness Theory)
- Closed timelike curve solutions
- Multiverse projections
- Preliminary ideas without mathematical closure

---

### `ARCHIVE/`

**Historical storage** — archived, superseded, incomplete, redundant, or
low-priority material kept for traceability.

`ARCHIVE/` is **excluded from canonical validation**. Tests and CI workflows
must not require archived files to pass.

The archive is organized as:
- `ARCHIVE/archive_legacy/` — material from the pre-refactor repository
  - `ARCHIVE/archive_legacy/ARCHIVE/legacy_variants/` — old code variants
    including `ubt_with_chronofactor/` (the original monorepo subpackage)
  - `ARCHIVE/archive_legacy/consolidation_project/` — superseded TeX documents
  - `ARCHIVE/archive_legacy/tex/` — lock-in files from earlier theory versions

---

### Supporting Directories

| Directory | Purpose |
|-----------|---------|
| `docs/` | Documentation, reports, governance files |
| `experiments/` | Numerical experiments, computations, shim scripts |
| `tools/` | Utility scripts for audit, validation, generation |
| `scripts/` | Shell and Python maintenance scripts |
| `tests/` | Pytest test suite (validates canonical layer) |
| `data/` | Generated CSV files (computed outputs) |
| `tex/` | Auto-generated TeX macro files |
| `canonical/` | Authoritative theory (see above) |
| `research_tracks/` | Active research front (see above) |
| `speculative_extensions/` | Exploratory ideas (see above) |
| `ARCHIVE/` | Historical storage (see above) |

---

## Promotion and Demotion Rules

### Promote to `canonical/` when:
- Content is part of the current intended theory backbone
- It is referenced by current canonical derivations or summaries
- It contains a stronger or clearer derivation than the current canonical version
- It is needed for a coherent canonical narrative
- It is not merely historical

### Promote to `research_tracks/` when:
- Content is valuable and actively maintained
- It supports ongoing development
- It is not yet authoritative enough for canonical
- It preserves an important concept users expect to find

### Move to `ARCHIVE/` when:
- Content is duplicated elsewhere in stronger form
- Content is obsolete after refactor
- Content is historically interesting but not part of the active theory line
- Content is weakly supported speculation unsuitable for canonical or research front
- Content confuses navigation more than it helps

---

## Validation Boundary

The test suite (`pytest tests/`) validates the **canonical layer only**:
- `canonical/` content
- `DERIVATION_INDEX.md` path references
- Selected root governance files
- Canonical topic indexes

`ARCHIVE/` is **explicitly excluded** from all canonical validation checks.
Test failures caused by missing archived files are configuration bugs, not
theory failures.

---

## Status Vocabulary

The following shared vocabulary is used across `DERIVATION_INDEX.md` and
canonical status documents:

| Term | Meaning |
|------|---------|
| **PROVEN / Proven** | Rigorous derivation exists; no free parameters |
| **STRONG / Strong** | Strong evidence; minor gaps documented |
| **PARTIAL / Partial** | Main argument present; sub-steps open |
| **OPEN** | No known proof; problem stated |
| **SPECULATIVE** | Extrapolates beyond current evidence |
| **DEAD END** | Approach proved to fail; documented for completeness |
| **CONJECTURE** | Proposed but not derived; hypothesis stated |

Layer labels:
- `[L0]` — pure biquaternionic geometry (no loop corrections)
- `[L1]` — one-loop result
- `[L2]` — higher-loop or non-perturbative

---

*This document is authoritative for repository structure.*
*For derivation status, see `DERIVATION_INDEX.md`.*
