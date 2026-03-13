<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT Theory Map — Derived from DERIVATION_INDEX.md

This document maps every major theory topic to its canonical entry point,
file-role classification, and derivation status as recorded in
[`DERIVATION_INDEX.md`](../DERIVATION_INDEX.md).

**Single source of truth**: `DERIVATION_INDEX.md`  
**Topic indexes**: `canonical/THEORY/topic_indexes/`  
**Last synced**: 2026-03-13

---

## File-Role Labels

| Label | Meaning | Physical location |
|-------|---------|-------------------|
| ⭐ **CANONICAL** | Single authoritative source; start here | `canonical/` |
| **supporting** | Valid derivation referenced by canonical source | `canonical/` or `ARCHIVE/consolidation_project/` |
| **heuristic** | Intuitive sketch; not a proof | `research_tracks/` |
| **sandbox** | Exploratory; outputs captured elsewhere | `research_tracks/` |
| **speculative** | Extrapolates beyond current evidence | `speculative_extensions/` |
| **historical** | Superseded; preserved for reference | `ARCHIVE/` |

---

## Topic 1 — Fine Structure Constant (α)

**Status**: PARTIALLY DERIVED — structural framework proved; B_base and R remain open  
**Topic index**: [`canonical/THEORY/topic_indexes/alpha_index.md`](../canonical/THEORY/topic_indexes/alpha_index.md)

| Result | Status | Canonical file |
|--------|--------|----------------|
| Complex time compactification | Proven [L0] | `STATUS_ALPHA.md §2` |
| Dirac quantisation condition | Proven [L0] | `STATUS_ALPHA.md §2` |
| V_eff(n) form | Proven [L1] | `STATUS_ALPHA.md §4` |
| Prime stability constraint | Proven [L0] | `STATUS_ALPHA.md §3` |
| N_eff = 12 | Proven [L0] | `STATUS_ALPHA.md §5` |
| B₀ = 8π | Proven [L1] | `STATUS_ALPHA.md §5` |
| B_base = N_eff^{3/2} = 41.57 | Motivated Conjecture | `STATUS_ALPHA.md §9` |
| R ≈ 1.114 | Open Hard Problem | `consolidation_project/alpha_derivation/r_factor_geometry.tex` |
| α⁻¹ = 137 (bare) | Semi-empirical | `STATUS_ALPHA.md` |
| α⁻¹ = 137.036 (full) | Semi-empirical | `STATUS_ALPHA.md` |

**⭐ Canonical source**: `STATUS_ALPHA.md`

---

## Topic 2 — Standard Model Gauge Group

**Status**: SU(3) and SU(2)_L × U(1)_Y proved; chirality gap C1 closed  
**Topic index**: [`canonical/THEORY/topic_indexes/SU3_index.md`](../canonical/THEORY/topic_indexes/SU3_index.md)

| Result | Status | Canonical file |
|--------|--------|----------------|
| SU(2)_L × U(1)_Y from ℂ⊗ℍ | Proven [L0] | `consolidation_project/appendix_E2_SM_geometry.tex` |
| U(1)_EM from ψ-cycle phase | Proven [L0] | `canonical/interactions/qed.tex` |
| SU(3)_c from involutions on ℂ⊗ℍ | Proved [L0] ⭐ | `consolidation_project/appendix_G_internal_color_symmetry.tex` |
| SU(3)_c from quantum superposition | Proved [L0] | `consolidation_project/SU3_derivation/step1_superposition_approach.tex` |
| SU(3)_c via i,j,k → r,g,b | **[HEURISTIC]** | `Appendix_G_Emergent_SU3.tex` |
| Color confinement (algebraic) | Conjectured with experimental support | `consolidation_project/confinement/algebraic_confinement.tex` |
| SU(2)_L chirality | Proved [L1] | `consolidation_project/chirality_derivation/` |

**⭐ Canonical source for SU(3)**: `consolidation_project/appendix_G_internal_color_symmetry.tex`

---

## Topic 3 — GR Recovery

**Status**: Steps 1–5 PROVED [L1]; Step 6 (off-shell closure) OPEN [L2]  
**Topic index**: [`canonical/THEORY/topic_indexes/GR_index.md`](../canonical/THEORY/topic_indexes/GR_index.md)

| Step | Result | Status | Canonical file |
|------|--------|--------|----------------|
| 1 | Metric g_μν from Θ | Proven [L1] | `canonical/geometry/metric.tex` |
| 1b | Derivative ≡ tetrad definitions | Proven [L0] | `consolidation_project/GR_closure/step1_metric_bridge.tex` |
| 2 | Non-degeneracy det(g) ≠ 0 | Proven [L0] | `consolidation_project/GR_closure/step2_nondegeneracy.tex` |
| 3 | Lorentzian signature (−,+,+,+) | Proven [L0] | `consolidation_project/GR_closure/step3_signature_theorem.tex` |
| 4 | Levi-Civita connection, curvature | Proven | `canonical/geometry/curvature.tex` |
| 5 | G_μν = 8πG T_μν (Hilbert variation) | Proven [L1] | `canonical/geometry/gr_as_limit.tex` |
| 6 | Off-shell Θ-only closure | OPEN [L2] | `canonical/geometry/gr_completion_attempt.tex` |

**⭐ Canonical navigation bridge**: `canonical/bridges/GR_chain_bridge.tex`

---

## Topic 4 — Hecke Operators & Twin Primes 137/139

**Status**: Strong numerical support (p=137); numerical observation (p=139); theory derivation OPEN  
**Topic index**: [`canonical/THEORY/topic_indexes/hecke_index.md`](../canonical/THEORY/topic_indexes/hecke_index.md)

| Result | Status | Canonical file |
|--------|--------|----------------|
| Hecke conjecture p=137 (Set A) | Strong Numerical Support | `reports/hecke_lepton/` |
| Hecke twin prime p=139 (Set B) | Numerical Observation | `reports/hecke_lepton/mirror_world_139.md` |
| Sets A and B algebraically independent | Verified | `reports/hecke_lepton/` |
| Weights k=2,4,6 from ψ-modes | Motivated Conjecture | `consolidation_project/hecke_bridge/motivation.tex §2` |
| Derivation of specific forms from ℂ⊗ℍ | OPEN | — |

**⭐ Canonical sources**: `reports/hecke_lepton/` + `consolidation_project/hecke_bridge/motivation.tex`

---

## Topic 5 — Mirror Sector

**Status**: Numerical observation; vacuum stability motivated conjecture  
**Topic index**: [`canonical/THEORY/topic_indexes/mirror_sector_index.md`](../canonical/THEORY/topic_indexes/mirror_sector_index.md)

| Result | Status | Canonical file |
|--------|--------|----------------|
| V_eff(137) < V_eff(139) | Numerical Observation | `consolidation_project/mirror_sector/vacuum_stability.tex` |
| n*=139 not local min of V_{B_137} | Proved Numerically | `consolidation_project/mirror_sector/vacuum_stability.tex` |
| n**=139 global min of B_{139} | Motivated Conjecture | `consolidation_project/mirror_sector/vacuum_stability.tex` |
| Mirror sector α'⁻¹ = 139 | Numerical Observation | `reports/hecke_lepton/mirror_world_139.md` |
| Mirror matter as dark matter | Conjecture | `consolidation_project/mirror_sector/README.md` |

**⭐ Canonical sources**: `consolidation_project/mirror_sector/README.md` + `reports/hecke_lepton/mirror_world_139.md`

---

## Topic 6 — Three Fermion Generations

**Status**: Generation mechanism proved; mass ratios not reproduced from first principles

| Result | Status | Canonical file |
|--------|--------|----------------|
| ψ-modes as independent fields | Proven [L0] | `research_tracks/three_generations/st3_complex_time_generations.tex §3` |
| Modes carry same SU(3) numbers | Proven [L0] | `research_tracks/three_generations/st3_complex_time_generations.tex §3` |
| ψ-parity forbids inter-generational mixing | Proven [L0] | `research_tracks/three_generations/st3_complex_time_generations.tex §4` |
| Mass ratios (KK / Hopfion) | Not reproduced | `research_tracks/three_generations/st3_complex_time_generations.tex §7` |

---

## Topic 7 — QM / GR / Statistical Mechanics Unification (FPE)

**Status**: Definitional equivalence proved [L0] in scalar sector

| Result | Status | Canonical file |
|--------|--------|----------------|
| FPE ↔ Euler–Lagrange equivalence | Proven [L0] | `consolidation_project/FPE_verification/step4_fpe_equivalence.tex` |
| Projection A: GR/KG from Re-sector | Proven [L0] | `consolidation_project/FPE_verification/step4_fpe_equivalence.tex §4` |
| Projection B: QM/Schrödinger from Im-sector | Sketch | `consolidation_project/FPE_verification/step4_fpe_equivalence.tex §4` |
| Projection C: FPE = statistical mechanics | Proven [L0] | `consolidation_project/FPE_verification/step4_fpe_equivalence.tex §4` |
| Born rule from FPE | Proved [L0] | `consolidation_project/FPE_verification/step7_born_rule.tex` |

---

## Topic 8 — QED Reproducibility at φ = const

**Status**: 3 results proved; 2 sketches; minimum criterion met

| Result | Status | Canonical file |
|--------|--------|----------------|
| U(1)_EM unbroken at φ=const | Proven [L0] | `consolidation_project/qed_phi_const/step1_u1_protection.tex` |
| δB(φ)=0 — α(μ) running unchanged | Proven [L1] | `consolidation_project/qed_phi_const/step3_beta_function.tex` |
| Schwinger term a_e=α/(2π) | Proven [L1] | `consolidation_project/qed_phi_const/step4_schwinger_term.tex` |

**⭐ Canonical directory**: `consolidation_project/qed_phi_const/`

---

## Topic 9 — Prime Attractor Theorem

**Status**: V_eff(n) minimum selects primes — proved [L1]

| Result | Status | Canonical file |
|--------|--------|----------------|
| Prime selection by V_eff(n) minimum | Proven [L1] | `STATUS_ALPHA.md §4` |
| Coupling type from ∇†∇Θ=κ𝒯 gives additive | Derived [L1] | `Appendix_H_Theta_Phase_Emergence.tex §H.7a` |
| Additive coupling gives no prime preference | Dead End | `Appendix_H_Theta_Phase_Emergence.tex §H.7a` |

---

## Topic 10 — φ-Universe Parameter and h_μν Vacuum

**Status**: φ proved physical for two-mode vacuum [L1]

| Result | Status | Canonical file |
|--------|--------|----------------|
| φ-projection theorem | Proven [L1] | `canonical/geometry/phase_projection.tex` |
| h_μν = 0 (single-mode) | Proven [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §1.2` |
| h_μν ≠ 0 (two-mode) | Proven [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §1.3` |
| r ≈ 4.66 for canonical two-mode vacuum | Proven [L1] | `tools/compute_h_munu_vacuum.py` |

---

## Open Hard Problems Summary

| Problem | Topic | Current best |
|---------|-------|--------------|
| B_base = N_eff^{3/2} derivation | α | 22 approaches tested; A2 (Hausdorff) best; 3/2 exponent not derived |
| R ≈ 1.114 correction factor | α | Best candidate 1+α(N_eff+π+1/4); 0.15% error; not derived |
| Lepton mass ratios from first principles | Generations | KK mismatch theorem forbids W2 formula; gap M1–M4 |
| Derivation of specific Hecke forms from ℂ⊗ℍ | Hecke | L-function of ℂ⊗ℍ/ℤ not identified |
| Off-shell Θ-only closure (GR Step 6) | GR | Global rank argument for J=δg/δΘ required |
| Unified 8π origin (single derivation) | GR/α | dim_ℝ(ℍ) = dim_ℂ(ℂ⊗ℍ) = 4 common; deeper link open |

---

## Repository Physical Layout (DERIVATION_INDEX labels)

```
canonical/           ⭐ CANONICAL + supporting derivations
  algebra/           — biquaternion algebra foundations
  fields/            — Θ field definition
  geometry/          — metric, curvature, GR recovery
  interactions/      — QED, electroweak
  bridges/           — navigation bridges between topics
  appendices/        — supporting appendices
  THEORY/            — canonical axioms, architecture, topic indexes
    topic_indexes/   — one entry point per topic (5 files)

research_tracks/     heuristic + sandbox exploration
  three_generations/ — fermion generations research
  automorphic/       — Hecke/automorphic forms
  legacy_theory_variants/ — older theory tree variants

speculative_extensions/  speculative extrapolations
  consciousness/     — complex consciousness theory
  cosmology/         — cosmological extensions

ARCHIVE/             historical + superseded
  archive_legacy/    — former archive/ root
```

---

*Generated from DERIVATION_INDEX.md. Do not edit theory status here — update DERIVATION_INDEX.md instead.*
