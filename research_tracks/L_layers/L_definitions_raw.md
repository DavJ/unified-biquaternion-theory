> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
>
> This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
> 4.0 International License (CC BY-NC-ND 4.0).

<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# L0 / L1 / L2 — Raw Definitions Extracted from Repository

**Task**: `ubt_L0_L1_L2_full_audit`  
**Date**: 2026-05-05  
**Mode**: deep_repo_analysis  
**Epistemic mode**: strict

---

## IMPORTANT: Two Distinct L-Labeling Systems Exist in This Repository

The repository uses the labels L0, L1, L2 (and [L0], [L1], [L2]) in **two
separate, incompatible classification systems**. These must not be conflated.

---

## System A: Architecture / Abstraction Hierarchy

**Source files**:
- `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`
- `docs/LAYER0_INVARIANT_EXTRACTION_README.md`
- `docs/INVARIANT_EXTRACTION_SUMMARY.md`
- `docs/architecture/LAYERS.md`
- `ARCHIVE/archive_legacy/ARCHIVE/legacy_variants/ubt_with_chronofactor/forensic_fingerprint/layer2_demote_heuristics.md`

These files define three abstraction layers describing the organization of the
UBT program. They use unbracketed notation "Layer 0", "Layer 1", "Layer 2"
(or "L0", "L1", "L2" without brackets).

---

### A.1 Layer 0

**file**: `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`  
**location**: §1.1 (Problem Statement), §2 (Layer-0 Structure)  
**type**: doc + formal mathematical definition

**snippet**:
```
Layer 0: Fundamental algebraic field Θ(q,τ) on complex manifold,
         minimal action S[Θ], continuous symmetries
```

**Formal definition (Definition 2.1 in tex)**:
```
The fundamental field Θ: B^4 × C → B ⊗ S ⊗ G is a smooth section
of the fiber bundle where:
  - B^4 = biquaternionic 4-manifold with coordinates q^μ ∈ B = C ⊗ H
  - C   = complex time manifold τ = t + iψ with t ∈ R, ψ ∈ R
  - B   = C ⊗ H = 8-dimensional biquaternion algebra
  - S   = spinor bundle Spin(3,1)
  - G   = gauge fiber SU(3) × SU(2) × U(1)
```

**Action (Definition 2.3 in tex)**:
```
S[Θ] = S_kin + S_pot + S_gauge

S_kin   = (1/2) ∫_{M×C} dμ G^{μν} Tr[(∇_μ Θ)† (∇_ν Θ)]
S_pot   = -∫_{M×C} dμ V(Θ),   V(Θ) = (λ/4)(⟨Θ,Θ⟩ - v²)²
S_gauge = -(1/4) ∫_{M×C} dμ Tr[F_{μν} F^{μν}]
```

**Layer-0 invariants (from docs/INVARIANT_EXTRACTION_SUMMARY.md)**:

| Invariant | Definition | Source |
|-----------|-----------|--------|
| Spectral Action | I_spec[Θ] = Tr[f(D²/Λ²)] | Heat kernel / Dirac operator |
| Topological Winding | I_wind[Θ] = n_wind ∈ ℤ | Homotopy class π₃(G/H) |
| Phase Winding | I_phase[Θ] = K_ψ ∈ ℤ | Complex time periodicity |
| Curvature Integral | I_curv[Θ] = ∫dμ R(q,τ) | Gauss-Bonnet / topological index |
| Action Functional | I_action[Θ] = S[Θ] | Stationary action principle |

**Key property**: All Layer-0 invariants are defined using only the
biquaternionic field Θ and its derivatives, the metric G_μν derived from Θ,
gauge fields A_μ, and integration measure dμ. **No discretization, numerical
procedures, or free parameters required.**

---

### A.2 Layer 1

**file**: `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`  
**location**: §1.1  
**type**: doc

**snippet**:
```
Layer 1: Emergent metric structure, classical GR/QFT limits
```

**file**: `docs/architecture/LAYERS.md`  
**location**: §Layer Definitions → Layer 1  
**type**: doc

**snippet**:
```
Layer 1: Geometry/Topology/Dynamics
What it is: Continuous symmetries, structural invariants, and dynamical laws

Examples:
- Biquaternionic field structure ℂ⊗ℍ
- Complex time manifold τ = t + iψ
- Field equation ∇†∇Θ = κ𝒯
- General Relativity recovery (ψ → 0 limit)
- Standard Model gauge group SU(3)×SU(2)×U(1) emergence from Aut(ℂ⊗ℍ)
- GR equivalence in real limit: R_μν - ½g_μν R = 8πG T_μν

Characteristics:
  ✅ Derived from axioms/symmetries
  ✅ Continuous parameters
  ✅ Independent of implementation details
  ✅ Testable via multiple observables
  ✅ Framework-level predictions
```

**Note**: In `docs/architecture/LAYERS.md`, "Layer 1" corresponds roughly
to what `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` calls "Layer 0" combined
with "Layer 1". The FORMAL_INVARIANT_EXTRACTION_LAYER0.tex document is more
fine-grained, separating the bare algebraic structure (Layer 0) from its
emergent metric/GR/QFT consequences (Layer 1). Both files are present in the
repository; their numbering schemes differ slightly.

---

### A.3 Layer 2

**file**: `ARCHIVE/archive_legacy/tex/FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`  
**location**: §1.1  
**type**: doc

**snippet**:
```
Layer 2: Discretized numerical procedures (prime-gated scans, CMB spectral
         tests, rigidity experiments, hit_rate and rarity_bits metrics)
```

**file**: `docs/architecture/LAYERS.md`  
**location**: §Layer Definitions → Layer 2  
**type**: doc

**snippet**:
```
Layer 2: Coding/Modulation/Protocol
What it is: Discrete choices, channel selections, implementation parameters

Examples:
- Winding number selection n=137 vs n=139 vs n=191
- OFDM channel indexing
- Prime gating patterns (which primes to use)
- RS(255,201) error correction code parameters
- GF(2⁸) finite field choice (256 states)
- Master Clock tick count (256-tick framing)
- Quantization grid discretization

Characteristics:
  ⚠️ Chosen to match observations or for engineering reasons
  ⚠️ Discrete/integer parameters
  ⚠️ Implementation-dependent
  ⚠️ Multiple valid choices possible
  ⚠️ Calibration parameters
```

**file**: `docs/INVARIANT_EXTRACTION_SUMMARY.md`  
**location**: §5 Additional Postulates in Layer-2  
**type**: doc

**snippet** — Layer-2 additional postulates:
```
L2.1 Winding numbers restricted to primes [101,199]  — Heuristic
L2.2 Physical winding number n=137 (matches α⁻¹)     — Empirical calibration
L2.3 RS(255,201) with GF(2⁸) error correction        — Engineering choice
L2.4 16 OFDM channels (2⁴ binary framing)             — Design parameter
L2.5 Fixed grid spacing (no adaptive refinement)      — Computational constraint
L2.6 Prime-gating pattern from discrete set           — Parametric scan choice
```

**file**: `research_tracks/gray_transport_layer/gray_vs_hamming_layer2.md`  
**location**: §1  
**type**: doc

**snippet** — Layer 2 sub-split:
```
L2S (State layer)     — Hamming (8,4,4) — State identity / state survival
L2T (Transport layer) — Gray adjacency  — Transition cost / path consistency
```

---

## System B: Perturbative Loop Order Labels

**Source files**:
- `docs/REPO_LAYERS.md` (authoritative status vocabulary)
- `ALPHA_PROGRESS_REPORT.md` (examples in derivation status)
- `research_tracks/T3_ALPHA/fallback_layer2_outline.md`

These files use bracketed notation `[L0]`, `[L1]`, `[L2]` as **derivation
status labels** in the context of perturbative quantum field theory loop
expansions.

---

### B.1 [L0]

**file**: `docs/REPO_LAYERS.md`  
**location**: §Status Vocabulary  
**type**: doc

**snippet**:
```
[L0] — pure biquaternionic geometry (no loop corrections)
```

**file**: `ALPHA_PROGRESS_REPORT.md`  
**location**: §2.1  
**type**: doc

**snippet**:
```
### 2.1 N_eff = 12 — [L0] PROVED

N_eff = N_phases × N_helicity × N_charge
      = dim_ℝ(Im ℍ) × 2 × 2
      = 3 × 2 × 2 = 12

Source: canonical/n_eff/step1_mode_decomposition.tex (Theorem 1.4)
Status: Zero-free-parameter algebraic theorem
```

**file**: `research_tracks/T3_ALPHA/fallback_layer2_outline.md`  
**location**: §Prerequisites  
**type**: doc

**snippets** (examples of [L0]-labelled results):
```
- [x] ℂ⊗ℍ ≅ Mat(2,ℂ) proved [L0]
- [x] ℤ₂×ℤ₂×ℤ₂ involutions and SU(3) proved [L0]
- [x] Qubit encoding of SU(3) proved [L0]
- [x] Gray code structure of involutions — proved [L0]
```

---

### B.2 [L1]

**file**: `docs/REPO_LAYERS.md`  
**location**: §Status Vocabulary  
**type**: doc

**snippet**:
```
[L1] — one-loop result
```

**file**: `ALPHA_PROGRESS_REPORT.md`  
**location**: §2.2  
**type**: doc

**snippet**:
```
### 2.2 B₀ = 8π (one-loop baseline) — [L1] PROVED

B₀ = 2π N_eff / 3 = 2π × 12 / 3 = 8π ≈ 25.133

Derived from the one-loop vacuum polarisation of N_eff = 12 charged modes
on the ψ-circle.
Source: canonical/n_eff/step2_vacuum_polarization.tex (Theorem 3.1)
```

Additional [L1]-labelled results in `ALPHA_PROGRESS_REPORT.md`:
```
2.3 V_eff(n) = n² − B·n·ln n          — [L1] PROVED (given B)
2.4 Stationarity condition for V_eff  — [L1] PROVED (given B)
2.5 Prime stability of n* = 137       — [L1] PROVED
2.6 Two-loop QED correction structure — [L1] PROVED
```

---

### B.3 [L2]

**file**: `docs/REPO_LAYERS.md`  
**location**: §Status Vocabulary  
**type**: doc

**snippet**:
```
[L2] — higher-loop or non-perturbative
```

No [L2]-labelled proved results were found in the repository at time of audit.
The label appears in `docs/REPO_LAYERS.md` as a defined category but no theorem
or derivation is currently tagged `[L2]` as proved.

---

## Additional L-related Terms Found

**file**: `docs/REPO_LAYERS.md`  
**location**: §Layer Definitions  
**type**: doc

**snippet** (repository directory layer definitions):
```
canonical/         — Authoritative theory text
research_tracks/   — Active research front
speculative_extensions/ — Exploratory ideas
ARCHIVE/           — Historical storage
```

Note: these are directory-level layers (repo structure), not the L0/L1/L2
physics/architecture layers described above.

---

## Search Terms Found

The following search terms from the task specification were located:

| Term | Occurrences (representative) |
|------|-------------------------------|
| `L0` | docs/REPO_LAYERS.md, ALPHA_PROGRESS_REPORT.md, T3_ALPHA/fallback_layer2_outline.md |
| `L1` | docs/REPO_LAYERS.md, ALPHA_PROGRESS_REPORT.md |
| `L2` | docs/REPO_LAYERS.md, docs/architecture/LAYERS.md, gray_transport_layer/ |
| `layer` | docs/architecture/LAYERS.md, FORMAL_INVARIANT_EXTRACTION_LAYER0.tex |
| `project` | Not a specialized L-layer term; refers to UBT project generally |
| `decode` | Not found as an L-layer term in any file |
| `transform` | Not found as a layer-specific term |

---

## What Is NOT Present in the Repository

- No Python function named `L0()`, `L1()`, or `L2()`
- No Python class named `L0`, `L1`, or `L2`
- No `transform()`, `encode()`, or `decode()` functions specific to the L-layer system
- No mathematical operator notation `L0: X → Y` defined as a function in code
- The term "decode" does not appear as an L-layer concept in any file

---

*Generated by ubt_L0_L1_L2_full_audit, Step 1.*
