# Canonical UBT Directory

This directory contains the **current-best, internally consistent, low-speculation** version of Unified Biquaternion Theory: what the theory currently treats as correct, preferably proved, reproduced, or clearly established as the canonical mainline.

## Purpose

`core/canonical/` is the **single reference formulation** of UBT for resolving conflicts and duplications.  
It is **stricter** than the historical or conceptual scope of the repository:

- Not all historical UBT material belongs here.
- Conceptual-only, unformalized, or speculative tracks do **not** belong here.
- Only current-best and sufficiently established material stays.
- **Speculative extensions** (including consciousness / psychons, universe-as-atom, fingerprint/parity side-tracks) are **not** part of canonical UBT — they live in `speculative_extensions/` and `research_tracks/`.

See `core/canonical/SCOPE.md` for the full inclusion/exclusion policy.

## Structure

```
core/canonical/
├── CANONICAL_DEFINITIONS.md    # Master definitions document
├── SCOPE.md                    # Inclusion / exclusion policy
├── README.md                   # This file
├── UBT_canonical_main.tex      # Main canonical document
├── explanation_of_nabla.tex    # Structure of covariant derivative ∇
├── algebra/                    # Biquaternion algebra foundations
│   ├── algebra_summary_table.tex
│   └── involutions_Z2xZ2xZ2.tex
├── bridges/                    # Navigation bridges (cross-references only)
│   ├── GR_chain_bridge.tex     # GR recovery chain Θ→g→Γ→R→Einstein
│   ├── QED_limit_bridge.tex    # QED limit, running α, B_base gap
│   └── gauge_emergence_bridge.tex  # SU(3)×SU(2)_L×U(1)_Y status
├── fields/                     # Canonical field definitions
│   ├── theta_field.tex         # Θ(q,T_B) biquaternion field
│   ├── biquaternion_time.tex   # T_B = t + iψ + jχ + kξ definition (canonical)
│   └── biquaternion_algebra.tex # Mathematical foundations
├── geometry/                   # Canonical geometric structures
│   ├── metric.tex              # g_μν canonical metric
│   ├── connection.tex          # Γ^λ_μν Levi-Civita connection
│   ├── curvature.tex           # Riemann tensor, GR equivalence
│   ├── gr_as_limit.tex         # GR recovery theorem (constant-phase limit)
│   └── stress_energy.tex       # T_μν canonical form
├── interactions/               # Canonical interaction Lagrangians
│   ├── qed.tex                 # QED complete
│   ├── qcd.tex                 # QCD complete
│   └── sm_gauge.tex            # Full SM gauge structure
└── appendices/                 # Canonical appendices
    └── symbol_dictionary.tex   # Symbol standardization
```

## What is NOT in core/canonical/

The following content has been intentionally moved out:

|  Removed from core/canonical/ | Moved to |
|--------------------------|----------|
| `consciousness/psychons.tex` | `speculative_extensions/consciousness/` |
| `UBT_coding_fingerprint.tex` | `research_tracks/fingerprints/` |
| `UBT_spectral_parity_test.tex` | `research_tracks/fingerprints/` |
| `appendix_universe_as_atom.tex` | `speculative_extensions/cosmology_or_metaphysics/` |

Consciousness claims, dark-matter/dark-energy interpretive assertions beyond proved status, fingerprint/parity side-tracks, and universe-as-atom cosmological speculation are **not** part of canonical UBT.

## Bridges Directory

The `bridges/` subdirectory contains **navigation bridge files** — cross-reference-only documents that help an external reviewer traverse the repository without reading multiple scattered files. They contain no new derivations.

| Bridge file | Purpose |
|---|---|
| `GR_chain_bridge.tex` | Locates each step of the GR recovery chain (Θ→g→Γ→R→Einstein) with proof-status labels |
| `QED_limit_bridge.tex` | Collects QED limit claims, running coupling derivation, and marks the B_base open problem explicitly |
| `gauge_emergence_bridge.tex` | Lists each gauge group component (SU(3), SU(2)_L, U(1)_Y) with proved / semi-empirical / open labels |

**When to use bridges vs. primary files:**
- Use **primary canonical files** (geometry/, interactions/, fields/) when you need the actual mathematical definition or derivation.
- Use **bridge files** when you need to understand which claims are proved, which are open, and where to find the proof.

## Principles

### 1. Single Definition Rule
Each concept has **exactly one** canonical definition in this directory. All other documents must reference or include from here.

### 2. Conflict Resolution
When multiple versions of a definition exist in the repository:
- The `core/canonical/` version is authoritative
- Conflicting versions should be marked as deprecated
- Legacy versions remain in `unified_biquaternion_theory/` (read-only)

### 3. Symbol Standardization
All symbols follow the dictionary in `CANONICAL_DEFINITIONS.md`:
- `α` = fine structure constant ONLY
- `ψ` = scalar imaginary time component ONLY  
- `χ, ξ` = vector imaginary time components ONLY
- `T_B` = biquaternion time (canonical)
- `τ` = complex time (isotropic limit/simplification)
- `q` = biquaternion coordinate ONLY
- etc.

### 4. Version Control
- All canonical files include version headers
- Changes require justification and documentation
- Backwards-incompatible changes trigger version increment

## Usage

### For Authors
When writing new UBT content:
1. Check `CANONICAL_DEFINITIONS.md` first
2. Use `\input{canonical/fields/theta_field.tex}` in LaTeX
3. Do NOT redefine canonical symbols
4. Report conflicts as issues
5. **Note**: Biquaternion time T_B is canonical; complex time τ is the isotropic limit

### For Consolidation
When consolidating existing content:
1. Compare against canonical definitions
2. Rewrite using canonical notation
3. Remove duplicate definitions
4. Update cross-references

### For Reviewers
When reviewing UBT documents:
1. Verify consistency with canonical definitions
2. Check symbol usage against dictionary
3. Ensure proper citations to canonical sources
4. Flag any redefinitions

## Status

### Canonical Tightening: ✅ Complete
- `consciousness/` moved to `speculative_extensions/consciousness/`
- Fingerprint/parity files moved to `research_tracks/fingerprints/`
- `appendix_universe_as_atom.tex` moved to `speculative_extensions/cosmology_or_metaphysics/`
- CANONICAL_DEFINITIONS.md audited; speculative claims downgraded or relocated

### Core Definitions: ✅ Complete
- Theta field Θ(q,T_B)
- Biquaternion time T_B = t + iψ + jχ + kξ (canonical)
- Metric g_μν
- Connection Γ^λ_μν
- Stress-energy T_μν
- QED Lagrangian
- QCD Lagrangian
- SM gauge structure
- Biquaternion algebra foundations
- Curvature tensors
- GR limit theorem

### Ongoing
- Electron mass unification (open)
- Global symbol unification pass

## Related Documents

- `core/canonical/SCOPE.md` - Inclusion / exclusion policy for this directory
- `core/canonical/CANONICAL_DEFINITIONS.md` - Master definitions document
- `consolidation_project/metadata/todos.md` - Consolidation task list
- `DERIVATION_INDEX.md` - Root derivation status map
- `speculative_extensions/` - Speculative content (consciousness, cosmological speculation)
- `research_tracks/` - Side-tracks (fingerprints, parity tests)

## Notes

### DO NOT MODIFY
Files in `unified_biquaternion_theory/` are original research documents and should NOT be modified. They are preserved for historical reference.

### Consolidation Source
Most consolidated content comes from `consolidation_project/` which contains partial consolidations. The `core/canonical/` directory represents the final, authoritative versions.

---

**Last Updated**: 2026-03-12  
**Status**: Canonical-tightened — speculative extensions removed
