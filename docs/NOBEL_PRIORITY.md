<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT Nobel Priority Analysis

> **Author**: Ing. David Jaroš  
> **Purpose**: Evaluate the research fronts of UBT by novelty, mathematical robustness, parameter freedom, experimental impact, and falsifiability.

---

## Preamble

This document evaluates the main research fronts of the Unified Biquaternion Theory
for scientific priority and impact. Assessments are based on the current state of
derivations in the repository.

Each claim is rated 1–5 on five dimensions:

| Dimension | Meaning |
|---|---|
| **Novelty** | How original is the approach relative to existing literature? |
| **Math Robustness** | How tight is the mathematical derivation? |
| **Param Freedom** | How many free parameters remain? (5 = zero, 1 = many) |
| **Experimental Impact** | How measurable/testable is the prediction? |
| **Falsifiability** | How clearly can the claim be experimentally refuted? |

---

## Research Front 1: Fine Structure Constant α

**Claim**: α⁻¹ = 137.036 derived from complex-time compactification + two-loop QED correction.

| Dimension | Score | Comment |
|---|---|---|
| Novelty | 5/5 | No other theory derives α from first principles without assuming it |
| Math Robustness | 3/5 | Bare n=137 semi-empirical; B coefficient ~90% derived; R factor unfixed |
| Param Freedom | 3/5 | 1 unfixed parameter (R ≈ 1.114 for B coefficient) |
| Experimental Impact | 5/5 | α is the most precisely measured fundamental constant |
| Falsifiability | 5/5 | Any deviation from 137.036 (to ppm) is a falsification |

**Total**: 21/25

**Key references**:  
- [`docs/PROOFKIT_ALPHA.md`](PROOFKIT_ALPHA.md)  
- [`STATUS_ALPHA.md`](../STATUS_ALPHA.md)  
- [`unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex`](../unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex)

**Priority assessment**: **HIGHEST PRIORITY** — if the B coefficient is fully derived from first principles, this becomes the first-ever parameter-free derivation of a fundamental coupling constant. This would be a landmark result regardless of broader unification claims.

**Bottleneck**: The R ≈ 1.114 correction factor needs a rigorous derivation from the biquaternionic renormalisation group flow.

---

## Research Front 2: Gauge Coupling Relations

**Claim**: SU(3)×SU(2)×U(1) emerges from Aut(ℂ⊗ℍ⊗𝕆).

| Dimension | Score | Comment |
|---|---|---|
| Novelty | 4/5 | Geometric gauge emergence is known (Kaluza-Klein, strings) but biquaternionic route is novel |
| Math Robustness | 3/5 | U(1) proven; SU(2) semi-empirical; SU(3) via octonionic extension (sketch) |
| Param Freedom | 4/5 | Gauge group structure has no free parameters; coupling values still semi-empirical |
| Experimental Impact | 4/5 | SM gauge group is confirmed experimentally |
| Falsifiability | 3/5 | Gauge group confirmation is binary; coupling predictions needed for quantitative tests |

**Total**: 18/25

**Key references**:  
- [`docs/PROOFKIT_GAUGE.md`](PROOFKIT_GAUGE.md)  
- [`Appendix_G_Emergent_SU3.tex`](../Appendix_G_Emergent_SU3.tex)  
- [`QED_SM_FROM_UBT_ANALYSIS.md`](../QED_SM_FROM_UBT_ANALYSIS.md)

**Priority assessment**: **HIGH PRIORITY** — the geometric derivation of the SM gauge group from a single algebraic structure is a compelling unification claim. The completeness of the SU(3) derivation is the main gap.

**Bottleneck**: Non-associativity of the octonionic extension (ℂ⊗𝕆) needs rigorous treatment.

---

## Research Front 3: Hubble Tension

**Claim**: The ~8% H₀ discrepancy arises from effective metric latency δ ≈ 0.078 in the ψ-sector.

| Dimension | Score | Comment |
|---|---|---|
| Novelty | 4/5 | Metric latency as Hubble tension cause is not in mainstream literature |
| Math Robustness | 2/5 | F=256, N=16 derivation is heuristic; parameters not fully derived |
| Param Freedom | 2/5 | Several parameters estimated (b, k, η, N); only F=256 from UBT structure |
| Experimental Impact | 5/5 | Hubble tension is one of the highest-profile open problems in cosmology |
| Falsifiability | 4/5 | Predicts δ constant in z; testable with next-generation distance ladder surveys |

**Total**: 17/25

**Key references**:  
- [`docs/PROOFKIT_HUBBLE.md`](PROOFKIT_HUBBLE.md)  
- [`speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex`](../speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex)  
- [`scripts/reproduce_hubble_prediction.py`](../scripts/reproduce_hubble_prediction.py)

**Priority assessment**: **MEDIUM-HIGH** — the highest-profile current cosmological tension, but the UBT derivation has the most parameters and is the least rigorous. Compelling as a **fingerprint hypothesis** for observational testing.

**Bottleneck**: The information-theoretic framing (F, N, O) needs to be derived from UBT geometry, not estimated.

---

## Research Front 4: CMB Predictions

**Claim**: UBT predicts calculable corrections to CMB acoustic peaks and baryon density Ω_b.

| Dimension | Score | Comment |
|---|---|---|
| Novelty | 3/5 | CMB beyond-ΛCDM predictions are an active research area |
| Math Robustness | 2/5 | Currently sketch-level; full derivation not in repository |
| Param Freedom | 2/5 | Multiple cosmological parameters not yet derived |
| Experimental Impact | 5/5 | CMB is the gold standard for cosmological tests |
| Falsifiability | 4/5 | Planck 2018 and future CMB-S4 data can test specific predictions |

**Total**: 16/25

**Key references**:  
- [`consolidation_project/appendix_CERN_BSM_predictions.tex`](../consolidation_project/appendix_CERN_BSM_predictions.tex)  
- [`STATUS_OBSERVATIONAL.md`](../STATUS_OBSERVATIONAL.md)

**Priority assessment**: **MEDIUM** — high experimental potential but derivations need significant development before predictions are specific enough to test.

**Bottleneck**: Need to derive UBT perturbation theory for CMB fluctuations.

---

## Overall Priority Ranking

| Rank | Research Front | Total Score | Recommendation |
|---|---|---|---|
| 1 | Fine structure constant α | 21/25 | **Highest priority** — close the B coefficient gap |
| 2 | Gauge coupling relations | 18/25 | **High priority** — formalise SU(3) octonionic proof |
| 3 | Hubble tension | 17/25 | **Medium-high** — submit as testable fingerprint hypothesis |
| 4 | CMB predictions | 16/25 | **Medium** — develop perturbation theory first |

---

## Strategic Recommendation

The most impactful path to external recognition:

1. **Paper 1A (Mathematics)**: Prove the SU(3) gauge group emergence rigorously
   from the biquaternionic/octonionic automorphism structure.

2. **Paper 1B (Fine structure constant)**: Complete the B coefficient derivation;
   publish the first parameter-free derivation of α.

3. **Paper 2 (Hubble tension fingerprint)**: Submit the metric latency hypothesis
   as a falsifiable cosmological prediction, framed as a hypothesis (not a "proof").

4. **Paper 3 (CMB)**: Follow up with full CMB perturbation theory after Papers 1A/1B.

---

## Priority Claim

The Unified Biquaternion Theory was first published by Ing. David Jaroš on GitHub
on 23 June 2025. All derivations and commit timestamps are verifiable in the
repository history.

See [`PRIORITY.md`](../PRIORITY.md) for the formal priority statement.

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
