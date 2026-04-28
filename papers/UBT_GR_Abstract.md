<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT_GR_Abstract.md — Flagship Paper Abstract

**Paper**: *General Relativity as a Real-Projected Limit of Unified Biquaternion Theory*  
**Track**: T1_GR  
**Target venues**: Journal of Mathematical Physics / Classical and Quantum Gravity  
**LaTeX source**: `papers/UBT_GR_Flagship.tex`  
**Date**: 2026-04-28  
**Status**: Paper-ready draft; all theorems proved at [L1]; two [L2] open problems
explicitly stated

---

## Abstract

We prove that Einstein's field equations G_μν = 8πG T_μν emerge as the
real-sector projection of the Unified Biquaternion Theory (UBT) field equation
∇†∇Θ(q,τ) = κ𝒯(q,τ) over complex time τ = t + iψ.

The derivation proceeds through a five-step chain:

1. **Metric emergence**: the spacetime metric g_μν is a derived quantity, not
   postulated, emerging as the real-valued bilinear
   g_μν = Re[Tr(∂_μΘ · ∂_νΘ†)]/𝒩.

2. **Non-degeneracy**: det(g) ≠ 0 follows from the admissibility condition on
   the fundamental field.

3. **Lorentzian signature**: the signature (−,+,+,+) is an algebraic theorem from
   the complex-time axiom (AXIOM-B), not a postulate.

4. **Standard GR structure**: the Levi-Civita connection and curvature tensors
   follow by standard differential geometry applied to the derived metric.

5. **Einstein field equations**: G_μν = 8πG T_μν follows from Hilbert variation
   of the total UBT action.

The Schwarzschild metric in isotropic coordinates is reproduced analytically and
numerically verified to relative error < 10⁻¹⁵.  The odd-parity graviton
satisfies the Regge-Wheeler equation without additional input.

The off-shell Θ-only closure (GAP-10) and the even-parity Zerilli equation
(GAP-Z) are identified as open problems at level [L2]; they do not affect the
on-shell validity of the main result.

---

## Key Claims (one-sentence version)

**Main theorem**: In the real-sector limit (ψ → 0), the UBT field equations
reduce identically to Einstein's field equations; the metric, its non-degeneracy,
and the Lorentzian signature are all derived, not postulated.

---

## Proof Status Summary

| Step | Claim | Status | Source file |
|------|-------|--------|-------------|
| 1 | Metric g_μν from Θ | Proved [L1] | `canonical/gr_closure/step1_metric_bridge.tex` |
| 2 | Non-degeneracy det(g) ≠ 0 | Proved [L1] | `canonical/gr_closure/step2_nondegeneracy.tex` |
| 3 | Signature (−,+,+,+) from AXIOM-B | Proved [L1] | `canonical/gr_closure/step3_signature_theorem.tex` |
| 4 | g → Γ → R geometric chain | Standard GR | Wald 1984, MTW 1973 |
| 5 | Einstein eqs G_μν = 8πG T_μν | Proved [L1] | `canonical/t_munu/step3_einstein_with_matter.tex` |
| 6a | Schwarzschild metric (spatial) | Proved [L1]; verified < 10⁻¹⁵ | `tools/verify_schwarzschild_theta.py` |
| 6b | ASD condition / twistor | Proved [L1] | `research_tracks/research/asd_condition_ubt.tex` |
| 6c | Regge-Wheeler equation | Proved [L1] | linearised GR chain |
| 7a | Zerilli equation (even-parity) | Open [L2] — GAP-Z | `reports/GR_final_gap_checklist.md` |
| 7b | Off-shell Θ-only closure | Open [L2] — GAP-10 | `reports/GR_final_gap_checklist.md` |

---

## Novelty vs. Prior Work

| Feature | This paper | Prior biquaternion gravity |
|---------|-----------|---------------------------|
| Metric derivation | Derived from Θ bilinear | Postulated or imposed |
| Lorentzian signature | Proved from AXIOM-B | Assumed |
| Einstein equations | Complete 5-step chain [L1] | Partial or assumed |
| Free parameters in GR chain | None | Typically present |
| Schwarzschild recovery | Analytical + numerical < 10⁻¹⁵ | Not demonstrated |
| Regge-Wheeler equation | Proved [L1] | Not addressed |

---

## Submission Readiness

- **Blocking gaps**: zero (all [L2] gaps are explicitly stated)
- **Target journal readiness**: high — external reviewers can read end-to-end
- **Outstanding tasks**: final proofreading pass, arXiv submission
- **Estimated time to arXiv**: ready now; 1–2 weeks for final polish

---

## References

Full bibliography: `papers/UBT_GR_Flagship.bib`  
Canonical source files: `canonical/gr_closure/`, `canonical/t_munu/`, `canonical/geometry/`  
Gap analysis: `reports/GR_final_gap_checklist.md`  
Reviewer preparation: `reports/GR_reviewer_objections_and_answers.md`
