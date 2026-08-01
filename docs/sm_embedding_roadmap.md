<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Standard Model Embedding Roadmap

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0

This document tracks the status of each element required for a complete derivation of the Standard
Model (SM) from the Unified Biquaternion Theory (UBT).

> **Important**: UBT provides proved derivations for SU(2)_L, U(1)_Y, U(1)_EM, N_eff = 12, and the
> three-generation mechanism. Full SM derivation (including SU(3)_c, mass ratios, and anomaly
> cancellation) remains open. See [`DERIVATION_INDEX.md`](../DERIVATION_INDEX.md) for the complete
> status index.

---

## Gauge Group Structure

| Element | Status | Notes |
|---------|--------|-------|
| U(1)_Y hypercharge quantization | **Open** | Why are hypercharges rational? Not derived from biquaternion structure. |
| SU(2)_L weak isospin | **Proved [L1]** | Generators T^a: M → (iσ^a/2)M from left action on ℂ⊗ₐℍ; commutation [T^a,T^b]=ε^{abc}T^c verified by direct computation. See `consolidation_project/appendix_E2_SM_geometry.tex §6`. |
| SU(3)_C color carrier | **Representation/algebra verified; dynamical selection open** | Standard Gell-Mann algebra and a fundamental triplet carrier are constructed and numerically verified. The one-hot route gives `3⊕1^5`; the natural fermionic three-qubit route gives `1⊕3⊕3bar⊕1`. These are representation-level results. Derivation from `S[Θ]` of local color gauging, the Yang–Mills term, matter coupling and `g_s` remains open. |
| Full SM group G_SM = SU(3)×SU(2)×U(1) | **Candidate structural assembly** | Algebraic carriers for the factors are proposed, but their simultaneous local gauging, physical field assignments, hypercharge normalization, anomaly cancellation and couplings are not yet derived from one canonical UBT action. |

## Matter Content

| Element | Status | Notes |
|---------|--------|-------|
| Three generations of quarks and leptons | **Mechanism proved [L0] — ψ-winding modes; mass ratios supported numerically** | ψ-modes of Θ are proved independent [L0] with same SU(3) quantum numbers; ψ-parity forbids inter-generational mixing. Mass ratios: Hecke eigenvalue matches at p=137, p=139 (numerical support only). See `research_tracks/three_generations/`. |
| Chirality mechanism (L/R asymmetry) | **Proved [L1]** | ψ-parity P_ψ acts as γ⁵ (Proved); odd winding n>0 = left-handed (Proved); Gap C1 closed: W± vertex is P_ψ-odd because S[Θ] contains no W_R coupling — U(1)_Y is the only right-handed gauge interaction. Parity violation follows from ψ-circle orientation, not a separate postulate. See `consolidation_project/chirality_derivation/step3_gap_C1_resolution.tex`. |
| Quark color quantum numbers | **Partial** | A triplet carrier is explicit. Identifying UBT field modes with quark flavors, antiquarks and the full Standard Model charge assignments remains open. |
| Lepton number conservation | **Open** | No mechanism demonstrated. |

## Mass Generation

| Element | Status | Notes |
|---------|--------|-------|
| Higgs mechanism / EWSB | **Open** | Phase structure of Θ provides candidate, but SSB not derived. |
| Yukawa structure | **Open** | Why the observed hierarchy m_e ≪ m_μ ≪ m_τ? Candidate: toroidal eigenmodes (Appendix W, conjecture). |
| Lepton mass ratios | **Numerical support — Hecke at p=139, μ-error 0.05%** | Hecke eigenvalue matches at p=137, p=139 (μ: 0.05%); mechanism conjectured via toroidal eigenmodes. See `research_tracks/three_generations/step6_hecke_matches.tex`. |
| Neutrino masses and mixing | **Open** | Seesaw candidate in Appendix G6; not derived from first principles. |
| CKM mixing matrix | **Open** | Appendix QA2 presents candidates; no full derivation. |

## Anomaly Cancellation

| Element | Status | Notes |
|---------|--------|-------|
| Gauge anomaly cancellation | **Open** | Not analyzed in biquaternion framework. |
| Gravitational anomaly cancellation | **Open** | Not analyzed. |

## Running Couplings

| Element | Status | Notes |
|---------|--------|-------|
| N_eff = 12 from ℂ⊗ℍ algebra | **Proved [L0] — zero free parameters** | 3×2×2 = N_phases × N_helicity × N_charge; N_phases=3 from dim Im(ℍ)=3; zero free parameters. See `consolidation_project/N_eff_derivation/`. |
| B₀ = 8π (one-loop β-function coefficient) | **Proved [L1]** | B₀ = 2π·N_eff/3 = 2π × dim_ℂ(ℂ⊗ℍ) = 8π; zero free parameters. See `consolidation_project/N_eff_derivation/step2_vacuum_polarization.tex`. |
| G_μν = 8πG T_μν | **Proved [L1] — Hilbert variation** | Derived from Hilbert variation; 8πG = (dim_ℝ(ℍ)/2) × vol(S²) × G. See `consolidation_project/T_munu_derivation/step3_einstein_with_matter.tex`. |
| ΔN_eff ≈ 0.046 | **Predicted** | UBT zero-modes contribute above CMB-S4 detection threshold 0.03. See `consolidation_project/N_eff_derivation/step3_N_eff_result.tex`. |
| QED at φ=const (photon massless, g-factor, α running) | **Mostly proved** | U(1)_EM unbroken at φ=const (photon massless, Proved); anomalous magnetic moment a_e=α/(2π) reproduced (Proved); α(μ) running unchanged from QED (Proved). See `consolidation_project/qed_phi_const/`. |
| Fine structure constant α | **Partial** | Specific numerical derivation exists but relies on auxiliary assumptions (see reports/alpha_audit/). |
| Strong coupling α_s | **Open** | Not derived from first principles. |
| Weinberg angle θ_W | **Open** | Candidate in Appendix K2; not a full derivation. |

---

## Language Policy

All UBT documents must use the following phrasings:

| Instead of | Use |
|-----------|-----|
| "UBT derives the Standard Model" | "UBT framework supports candidate gauge structures; full derivation remains open." |
| "SU(3) emerges from biquaternions" | "A candidate mechanism for SU(3)-like structure is presented; see Appendix G for open problems." |
| "The three generations are explained" | "A candidate mechanism (toroidal eigenmodes) is proposed; verification pending." |

---

## References

- Appendix G: SU(3) candidate construction (status: candidate, not derivation)
- Appendix W: Lepton mass ratios from toroidal eigenmodes (status: conjecture)
- Appendix QA2: Quark/CKM candidates (status: candidate)
- `reports/alpha_audit/`: Alpha derivation status
- `speculative_extensions/`: Speculative interpretations (not core physics)
