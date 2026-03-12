<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# canonical/ — Scope and Inclusion Policy

This document defines precisely what belongs in `canonical/` and what must be kept outside it.

## Definition of canonical/

`canonical/` contains the **current-best, internally consistent, low-speculation** formulation of
Unified Biquaternion Theory (UBT): material that the theory currently treats as correct, and that is
preferably proved, reproduced, or clearly established as the canonical mainline.

`canonical/` is **stricter** than the full historical or conceptual scope of the repository.
It is the reference formulation — not an archive, not a brainstorming space, not a side-track.

## Inclusion rules

Material stays in `canonical/` only if it is:

1. **Current-best mainline** — reflects the current state of the theory, not superseded variants.
2. **Internally consistent** — does not contradict root `README.md` or root `DERIVATION_INDEX.md`.
3. **Proved, reproduced, or clearly established** on the stated admissible sector.
4. **Canonical definitions** needed by the mainline theory.

Some non-proved material is allowed **only if**:
- It is indispensable for the current mainline formulation, **and**
- Its status is explicitly labeled as **conditional / assumed / open**.

## Exclusion rules

The following categories must be moved out of `canonical/`:

| Category | Destination |
|----------|-------------|
| Conceptual design only (no formalization) | `research_tracks/` or `speculative_extensions/` |
| Lacks mathematical formalization | `research_tracks/` |
| Speculative ontology | `speculative_extensions/` |
| Fingerprint / parity side-tracks | `research_tracks/fingerprints/` |
| Universe-as-atom side-track | `speculative_extensions/cosmology_or_metaphysics/` |
| Consciousness-first interpretation | `speculative_extensions/consciousness/` |
| Claims conflicting with root `README.md` or `DERIVATION_INDEX.md` | `ARCHIVE/` or `speculative_extensions/` |

## Consciousness claims policy

**Consciousness is not part of canonical UBT.**

- Do not put strong claims about consciousness in `canonical/`.
- Psychon content, theta-resonator design, and related interpretive material live in
  `speculative_extensions/consciousness/`.
- `canonical/CANONICAL_DEFINITIONS.md` does not assert consciousness as part of core UBT.
- The imaginary time components (ψ, χ, ξ) are canonical mathematical degrees of freedom;
  their possible physical interpretation as a "consciousness substrate" is speculative and
  lives outside `canonical/`.

## Required content (must stay in canonical/)

| Path | Role |
|------|------|
| `algebra/` | Biquaternion algebra foundations |
| `fields/` | Field definitions |
| `geometry/` | Geometric structures |
| `interactions/` | Interaction Lagrangians |
| `appendices/` | Canonical appendices |
| `bridges/` | Cross-reference navigation |
| `CANONICAL_DEFINITIONS.md` | Master definitions |
| `UBT_canonical_main.tex` | Main canonical document |
| `README.md` | Directory overview |
| `SCOPE.md` | This file |

## Moved-out content record

| File (former canonical/ path) | Current location | Reason |
|-------------------------------|-----------------|--------|
| `consciousness/psychons.tex` | `speculative_extensions/consciousness/psychons.tex` | Speculative consciousness content |
| `UBT_coding_fingerprint.tex` | `research_tracks/fingerprints/UBT_coding_fingerprint.tex` | Fingerprint side-track |
| `UBT_spectral_parity_test.tex` | `research_tracks/fingerprints/UBT_spectral_parity_test.tex` | Parity test side-track |
| `appendix_universe_as_atom.tex` | `speculative_extensions/cosmology_or_metaphysics/appendix_universe_as_atom.tex` | Universe-as-atom speculation |

All moves preserve full git history.

---

**Last Updated**: 2026-03-12
