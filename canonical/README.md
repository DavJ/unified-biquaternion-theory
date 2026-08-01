<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# canonical/ — Canonical UBT Physics

This directory contains the **current-best, internally consistent, low-speculation** version of Unified Biquaternion Theory: what the theory currently treats as correct, preferably proved, reproduced, or clearly established as the canonical mainline.

## Purpose

`canonical/` is the **single reference formulation** of UBT for resolving conflicts and duplications.  
It is **stricter** than the historical or conceptual scope of the repository:

- Not all historical UBT material belongs here.
- Conceptual-only, unformalized, or speculative tracks do **not** belong here.
- Only current-best and sufficiently established material stays.
- **Speculative extensions** (including consciousness / psychons, universe-as-atom, fingerprint/parity side-tracks) are **not** part of canonical UBT — they live in `speculative_extensions/` and `research_tracks/`.

See `canonical/SCOPE.md` for the full inclusion/exclusion policy.

## Confidence Labels

Results in this directory are classified by the following confidence levels:

| Label | Meaning |
|-------|---------|
| **Strong** | Rigorous derivation; zero free parameters |
| **Strong Partial** | Structural derivation substantially complete; ≤1 open sub-gap |
| **Candidate** | Proposed mechanism with supporting evidence; ≥1 gap unresolved |
| **Experimental** | Hypothesis supported by numerical/observational tests; no algebraic proof |
| **Open** | No complete derivation known; active problem |
| **Deprecated** | Approach proved to fail or superseded; preserved for reference |

## Structure

```
canonical/
├── CANONICAL_DEFINITIONS.md    # Master definitions document
├── SCOPE.md                    # Inclusion / exclusion policy
├── README.md                   # This file
├── AXIOMS.md                   # UBT axioms
├── UBT_canonical_main.tex      # Main canonical document (start here)
├── core_assumptions.tex        # Core assumptions
├── explanation_of_nabla.tex    # Structure of covariant derivative ∇
├── algebra/                    # Biquaternion algebra foundations
│   ├── algebra_summary_table.tex
│   └── involutions_Z2xZ2xZ2.tex
├── bridges/                    # Navigation bridges (cross-references only)
│   ├── GR_chain_bridge.tex     # GR recovery chain Θ→g→Γ→R→Einstein
│   ├── QED_limit_bridge.tex    # QED limit, running α, B_base gap
│   └── gauge_emergence_bridge.tex  # SU(3)×SU(2)_L×U(1)_Y status
├── fields/                     # Canonical field definitions
│   ├── theta_field.tex         # Θ(q,τ) biquaternion field
│   ├── biquaternion_time.tex   # τ = t + iψ definition (canonical); T_B deprecated
│   └── biquaternion_algebra.tex # Mathematical foundations
├── geometry/                   # Canonical geometric structures
│   ├── metric.tex              # g_μν canonical metric
│   ├── connection.tex          # Γ^λ_μν Levi-Civita connection
│   ├── curvature.tex           # Riemann tensor, GR equivalence
│   ├── gr_as_limit.tex         # GR recovery theorem (constant-phase limit)
│   └── stress_energy.tex       # T_μν canonical form
├── gr_limit/                   # Full GR recovery derivation
│   └── GR_limit_of_UBT.tex
├── interactions/               # Canonical interaction Lagrangians
│   ├── qed.tex                 # QED complete
│   ├── qcd.tex                 # QCD complete
│   └── sm_gauge.tex            # Full SM gauge structure
└── appendices/                 # Canonical appendices
    └── symbol_dictionary.tex   # Symbol standardization
```

## What is NOT in canonical/

The following content has been intentionally moved out:

| Removed from canonical/ | Moved to |
|---|---|
| `consciousness/psychons.tex` | `speculative_extensions/consciousness/` |
| `UBT_coding_fingerprint.tex` | `research_tracks/fingerprints/` |
| `UBT_spectral_parity_test.tex` | `research_tracks/fingerprints/` |
| `appendix_universe_as_atom.tex` | `speculative_extensions/cosmology_or_metaphysics/` |
| `CONSOLIDATION_ROADMAP.md` | `docs/` |
| `IMPLEMENTATION_CHECKLIST.md` | `docs/` |
| `NABLA_APPENDIX_VERIFICATION.md` | `docs/` |
| `PHASE_1_COMPLETE_SUMMARY.md` | `docs/` |

Consciousness claims, dark-matter/dark-energy interpretive assertions beyond proved status, fingerprint/parity side-tracks, universe-as-atom cosmological speculation, and process/governance documents are **not** part of canonical UBT physics.

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
- `τ` = complex time (canonical)
- `T_B` = biquaternion time (deprecated/historical extension)
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
5. **Note**: Complex time τ=t+iψ is canonical; biquaternion time T_B is a deprecated/historical extension.

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

**Overall confidence: Strong Partial** — core field equations, GR recovery chain, and QED/QCD Lagrangians are substantially proved; fine structure constant derivation and lepton mass sector remain open.

### Canonical Tightening: ✅ Complete
- `consciousness/` moved to `speculative_extensions/consciousness/`
- Fingerprint/parity files moved to `research_tracks/fingerprints/`
- `appendix_universe_as_atom.tex` moved to `speculative_extensions/cosmology_or_metaphysics/`
- CANONICAL_DEFINITIONS.md audited; speculative claims downgraded or relocated

### Core Definitions: ✅ Complete
- Theta field Θ(q,τ) — **Strong**
- Complex time τ = t + iψ (canonical) — **Strong**
- Metric g_μν — **Strong**
- Connection Γ^λ_μν — **Strong**
- Stress-energy T_μν — **Strong**
- QED Lagrangian — **Strong**
- QCD Lagrangian — **Strong**
- SM gauge structure (SU(3)×SU(2)_L×U(1)_Y emergence) — **Strong Partial**
- Biquaternion algebra foundations — **Strong**
- Curvature tensors — **Strong**
- GR limit theorem — **Strong Partial**

### Open
- Fine structure constant α — **Open** (B_base gap unresolved; see DERIVATION_INDEX.md)
- Electron / lepton mass spectrum — **Open**
- Global symbol unification pass

## Related Documents

- `canonical/SCOPE.md` - Inclusion / exclusion policy for this directory
- `canonical/CANONICAL_DEFINITIONS.md` - Master definitions document
- `DERIVATION_INDEX.md` - Root derivation status map (with confidence labels)
- `research_tracks/README.md` - Index of all research tracks with confidence labels
- `speculative_extensions/` - Speculative content (consciousness, cosmological speculation)
- `research_tracks/` - Side-tracks (fingerprints, parity tests)
- `docs/REPOSITORY_STRUCTURE.md` - Full repository structure guide

## Notes

### DO NOT MODIFY
Files in `unified_biquaternion_theory/` are original research documents and should NOT be modified. They are preserved for historical reference.

### Consolidation Source
Most consolidated content comes from `consolidation_project/` which contains partial consolidations. The `canonical/` directory represents the final, authoritative versions.

---

**Last Updated**: 2026-04-27  
**Status**: Canonical-tightened — speculative extensions removed; content lives directly in `canonical/`
