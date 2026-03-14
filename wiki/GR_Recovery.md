<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# GR Recovery

UBT **generalises and embeds** General Relativity — it does not replace or contradict it.

**Canonical bridge**: [`canonical/bridges/GR_chain_bridge.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/bridges/GR_chain_bridge.tex)  
**Topic index**: [`canonical/THEORY/topic_indexes/GR_index.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/THEORY/topic_indexes/GR_index.md)

---

## Summary

In the real-valued limit ψ → 0, the biquaternionic field equation

```
∇†∇ Θ(q,τ) = κ 𝒯(q,τ)
```

reduces exactly to Einstein's field equations:

```
G_μν = 8πG T_μν
```

The full derivation chain (Steps 1–5) is proved at level [L1] with one explicit
residual open problem at Step 6.

---

## Derivation Chain

<!-- BEGIN GENERATED: gr_recovery_status -->
| Result | Status | File |
|--------|--------|------|
| G_μν = 8πG T_μν from δS_total/δg^μν = 0 | ✅ **Proved** | [`step3_einstein_with_matter.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/t_munu/step3_einstein_with_matter.tex) |
| T_μν from Hilbert prescription | ✅ **Proved** | [`step3_einstein_with_matter.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/t_munu/step3_einstein_with_matter.tex) |
| ∇^μ T_μν = 0 from Bianchi identity | ✅ **Proved** | [`step3_einstein_with_matter.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/t_munu/step3_einstein_with_matter.tex) |
| Lorentzian signature (-,+,+,+) from AXIOM B | ✅ **Proved** | [`step3_signature_theorem.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/gr_closure/step3_signature_theorem.tex) |
| Metric non-degeneracy for A_UBT class | ✅ **Proved** | [`step2_nondegeneracy.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/gr_closure/step2_nondegeneracy.tex) |
| Derivative-based ≡ tetrad-based metric formula | ✅ **Proved** | [`step1_metric_bridge.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/gr_closure/step1_metric_bridge.tex) |
| GR chain summary (Θ→g→Γ→R→Einstein) | ✅ **Proved** | [`GR_chain_summary.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/gr_closure/GR_chain_summary.tex) |
| N is scale-fixing, not signature-fixing | ✅ **Proved** | [`step3_signature_theorem.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/gr_closure/step3_signature_theorem.tex) |
| UBT vs sigma model distinction | ✅ **Proved** | [`step1_metric_bridge.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/gr_closure/step1_metric_bridge.tex) |
| GR equivalence via tetrad pipeline | ⚠️ **Conditional** | [`appendix_R_GR_equivalence.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/appendix_R_GR_equivalence.tex) |
| Pure Θ-only closure (g substitution before variation, off-shell) | ❌ **Open** |  |
| Metric uniqueness beyond A_UBT | ❌ **Open** |  |
<!-- END GENERATED: gr_recovery_status -->

### Steps (static summary)

| Step | Result | Status | File |
|------|--------|--------|------|
| 1 | g_μν = Re Tr(∂_μΘ · ∂_νΘ†) | **Proved [L1]** | [`canonical/geometry/metric.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/metric.tex) |
| 1b | Equivalence: derivative ↔ tetrad definitions | **Proved [L0]** | [`GR_closure/step1_metric_bridge.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/GR_closure/step1_metric_bridge.tex) |
| 2 | Non-degeneracy: det(g) ≠ 0 | **Proved [L0]** | [`GR_closure/step2_nondegeneracy.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/GR_closure/step2_nondegeneracy.tex) |
| 3 | Lorentzian signature (−,+,+,+) | **Proved [L0]** | [`GR_closure/step3_signature_theorem.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/GR_closure/step3_signature_theorem.tex) |
| 4a | Levi-Civita connection Γ | **Standard GR** | [`canonical/geometry/connection.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/connection.tex) |
| 4b | Riemann curvature → Einstein tensor G_μν | **Standard GR** | [`canonical/geometry/curvature.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/curvature.tex) |
| 5 | G_μν = 8πG T_μν via Hilbert variation | **Proved [L1]** | [`canonical/geometry/gr_as_limit.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/gr_as_limit.tex) |
| 6 | Off-shell Θ-only closure | **Open [L2]** | [`canonical/geometry/gr_completion_attempt.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/gr_completion_attempt.tex) |

Steps 1–5 are sufficient for the physical claim that GR is recovered.

---

## All Experimental GR Confirmations Validate UBT

Because GR is the real-limit of UBT, all experimental tests that confirm GR also
confirm UBT's real sector:

- Perihelion precession of Mercury
- Gravitational lensing
- Gravitational waves (LIGO)
- Black hole imaging (EHT)
- Cosmological solutions (FLRW)

The imaginary components of UBT (phase curvature, ψ-modes) are invisible to
classical instruments, which is why classical GR appears complete experimentally.

---

## GR as the Real Limit

Mathematically:

```
UBT field equation:  ∇†∇ Θ = κ 𝒯
          ↓  ψ → 0  (real limit)
GR:       G_μν = 8πG T_μν
```

This holds for:
- Flat spacetime (Minkowski, R = 0)
- Weak fields
- Strong fields (black holes, neutron stars)
- Cosmological solutions (R ≠ 0)

---

## See Also

- [Emergent Spacetime](Emergent_Spacetime) — metric emergence from Θ
- [Theta Field](Theta_Field) — ∇†∇Θ = κ𝒯 field equation
- [Operator Formalism](Operator_Formalism) — structure of ∇
