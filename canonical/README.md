# Canonical UBT Directory

This directory contains the **canonical (authoritative)** versions of all Unified Biquaternion Theory definitions, derivations, and formulations.

## Purpose

The `canonical/` directory serves as the **single source of truth** for UBT to resolve conflicts and duplications found across the repository.

## Structure

```
canonical/
├── CANONICAL_DEFINITIONS.md    # Master definitions document
├── explanation_of_nabla.tex    # Structure of covariant derivative ∇
├── bridges/                     # Navigation bridges (cross-references only)
│   ├── GR_chain_bridge.tex     # GR recovery chain Θ→g→Γ→R→Einstein
│   ├── QED_limit_bridge.tex    # QED limit, running α, B_base gap
│   └── gauge_emergence_bridge.tex  # SU(3)×SU(2)_L×U(1)_Y status
├── fields/                      # Canonical field definitions
│   ├── theta_field.tex         # Θ(q,T_B) biquaternion field
│   ├── biquaternion_time.tex   # T_B = t + iψ + jχ + kξ definition (canonical)
│   ├── biquaternion_algebra.tex # Mathematical foundations
│   └── electron_mass.tex       # Unified electron mass derivation
├── geometry/                    # Canonical geometric structures
│   ├── metric.tex              # g_μν canonical metric
│   ├── connection.tex          # Γ^λ_μν Levi-Civita connection (stub → curvature.tex)
│   ├── curvature.tex           # Riemann tensor, GR equivalence
│   ├── gr_as_limit.tex         # GR recovery theorem (constant-phase limit)
│   └── stress_energy.tex       # T_μν canonical form
├── interactions/                # Canonical interaction Lagrangians
│   ├── qed.tex                 # QED complete
│   ├── qcd.tex                 # QCD complete
│   └── sm_gauge.tex            # Full SM gauge structure
├── consciousness/               # Canonical consciousness theory
│   ├── psychons.tex            # Psychon definition
│   └── theta_resonator.tex     # Experimental design
└── appendices/                  # Canonical appendices
    └── symbol_dictionary.tex    # Symbol standardization
```

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
- The `canonical/` version is authoritative
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

### Phase 1: ✅ Complete
- Directory structure created
- Master definitions documented

### Phase 2: 🚧 In Progress
- Creating canonical .tex files:
  - [x] Theta field Θ(q,T_B)
  - [x] Biquaternion time T_B = t + iψ + jχ + kξ (canonical)
  - [x] Metric g_μν
  - [x] Connection Γ^λ_μν (stub)
  - [x] Stress-energy T_μν
  - [x] QED Lagrangian
  - [x] QCD Lagrangian
  - [x] SM gauge structure
  - [x] Biquaternion algebra foundations
  - [x] Curvature tensors
  - [x] GR limit theorem
  - [x] Psychon formalization
  - [ ] Electron mass unification
  - [ ] Theta-resonator design

### Phase 3: ⏳ Planned
- Consolidate appendices using canonical definitions
- Remove duplicate versions
- Update cross-references

### Phase 4: ⏳ Planned
- Global symbol unification
- Notation consistency enforcement
- Symbol dictionary validation

### Phase 5: ⏳ Planned
- Main article assembly
- 12-section structure
- Final compilation

## Conflict Tracking

Known conflicts resolved by canonical definitions:

| Conflict | Canonical Resolution | Status |
|----------|---------------------|---------|
| Complex time (3 versions) | τ = t + iψ (dynamic ψ) | ✅ Defined |
| Θ field dimension | C^(4×4) extendable to C^(8×8) | ✅ Defined |
| Metric g_μν (3 derivations) | Re Tr(∂_μΘ ∂_νΘ†) | ✅ Defined |
| T_μν (3 definitions) | Field-theoretic form | ✅ Defined |
| QED (inconsistent) | Canonical Lagrangian | ✅ Defined |
| QCD (3 versions) | Emergent SU(3) form | ✅ Defined |
| Electron mass (3 methods) | Unified method | 🚧 To consolidate |
| α notation (4 meanings) | Coupling constant only | ✅ Defined |
| ψ notation (4 uses) | Imaginary time only | ✅ Defined |
| Theta functions (2 normalizations) | Jacobi standard | ✅ Defined |

## Related Documents

- `COPILOT_INSTRUCTIONS_CONSOLIDATION.md` - Master consolidation instructions
- `consolidation_project/metadata/todos.md` - Consolidation task list
- `consolidation_project/metadata/consolidation_map.md` - File mapping

## Notes

### DO NOT MODIFY
Files in `unified_biquaternion_theory/` are original research documents and should NOT be modified. They are preserved for historical reference.

### Consolidation Source
Most consolidated content comes from `consolidation_project/` which contains partial consolidations. The `canonical/` directory represents the final, authoritative versions.

### Research Extensions
Speculative or experimental content (holography, p-adic extensions, etc.) will be organized into `research_extensions/` directory (Phase 6).

## Questions?

For questions about canonical definitions:
1. Check `CANONICAL_DEFINITIONS.md`
2. Review `consolidation_project/metadata/consolidation_map.md`
3. Consult repository maintainers

---

**Last Updated**: 2025-11-14  
**Phase**: 1 (Directory Restructuring)  
**Status**: Active Development
