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
| SU(2)_L weak isospin | **Proved** | Generators T^a: M → (iσ^a/2)M from left action on ℂ⊗ₐℍ; commutation [T^a,T^b]=ε^{abc}T^c verified by direct computation. See `consolidation_project/appendix_E2_SM_geometry.tex §6`. |
| SU(3)_C color symmetry | **Candidate construction only** | See Appendix G; three imaginary axes ≠ SU(3) without additional assumptions. |
| Full SM group G_SM = SU(3)×SU(2)×U(1) | **Open** | Decoupling of factors not demonstrated; direct product structure not derived. |

## Matter Content

| Element | Status | Notes |
|---------|--------|-------|
| Three generations of quarks and leptons | **Mechanism proved; mass ratios supported numerically** | ψ-modes of Θ are proved independent [L0] with same SU(3) quantum numbers; ψ-parity forbids inter-generational mixing. Mass ratios: Hecke eigenvalue matches at p=137, p=139 (numerical support only). See `research_tracks/three_generations/`. |
| Chirality mechanism (L/R asymmetry) | **Open** | Key missing piece; biquaternionic structure is formally symmetric. |
| Quark color quantum numbers | **Open** | Dependent on SU(3) derivation (see above). |
| Lepton number conservation | **Open** | No mechanism demonstrated. |

## Mass Generation

| Element | Status | Notes |
|---------|--------|-------|
| Higgs mechanism / EWSB | **Open** | Phase structure of Θ provides candidate, but SSB not derived. |
| Yukawa structure | **Open** | Why the observed hierarchy m_e ≪ m_μ ≪ m_τ? Candidate: toroidal eigenmodes (Appendix W, conjecture). |
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
| N_eff = 12 from ℂ⊗ℍ algebra | **Proved** | 3×2×2 = N_phases × N_helicity × N_charge; N_phases=3 from dim Im(ℍ)=3; zero free parameters. See `consolidation_project/N_eff_derivation/`. |
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
