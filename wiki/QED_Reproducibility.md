<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# QED Reproducibility at φ = const

UBT must reproduce standard QED not only at φ = 0 (vacuum limit) but for any
constant scalar background φ = const ≠ 0. This section tracks the stronger
constraint.

**Canonical source**: [`canonical/qed_phi_const/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/canonical/qed_phi_const)  
**Verification script**: [`tools/verify_qed_phi_const.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/tools/verify_qed_phi_const.py)

---

## Step Files

| Step | File | Result |
|------|------|--------|
| 1 | [`step1_u1_protection.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step1_u1_protection.tex) | U(1)_EM unbroken at φ=const — **Proved** |
| 2 | [`step2_electron_mass.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step2_electron_mass.tex) | Electron mass m_e=y·v — **Sketch** |
| 3 | [`step3_beta_function.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step3_beta_function.tex) | δB(φ)=0 at one loop — **Proved** |
| 4 | [`step4_schwinger_term.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step4_schwinger_term.tex) | Schwinger term a_e=α/(2π) — **Proved** |
| 5 | [`step5_lamb_shift.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step5_lamb_shift.tex) | Lamb shift 1057.8 MHz — **Sketch** |
| 6 | [`step6_qed_summary.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step6_qed_summary.tex) | QED reproducibility summary — **Substantially Proved** |

---

## Derivation Status

<!-- BEGIN GENERATED: qed_phi_const_status -->
| Result | Status | File |
|--------|--------|------|
| U(1)\_EM unbroken at φ=const | ✅ **Proved** | [`step1_u1_protection.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step1_u1_protection.tex) |
| Electron mass m\_e=y·v at φ=const | ❓ **Unknown** | [`step2_electron_mass.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step2_electron_mass.tex) |
| δB(φ)=0 at one loop — α(μ) running unchanged | ✅ **Proved** | [`step3_beta_function.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step3_beta_function.tex) |
| Schwinger term a\_e=α/(2π) at φ=const | ✅ **Proved** | [`step4_schwinger_term.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step4_schwinger_term.tex) |
| Lamb shift 1057.8 MHz at φ=const | ❓ **Unknown** | [`step5_lamb_shift.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step5_lamb_shift.tex) |
| QED reproducibility summary | ❓ **Unknown** | [`step6_qed_summary.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/qed_phi_const/step6_qed_summary.tex) |
| Gap | ❓ **Unknown** |  |
| Y1 | ❓ **Unknown** |  |
| Y2 | ❓ **Unknown** |  |
| L1 | ❓ **Unknown** |  |
| Prediction | ❓ **Unknown** |  |
| P-QED-1 | ❓ **Unknown** |  |
| P-QED-2 | ❓ **Unknown** |  |
<!-- END GENERATED: qed_phi_const_status -->

---

## UBT Predictions from φ-Background

| Prediction | Value | Observable |
|------------|-------|-----------|
| P-QED-1 | δα/α ~ 10⁻²¹ at 2-loop | α running in cosmological φ-background |
| P-QED-2 | δa_e ~ 10⁻¹⁶ | electron g-2 (below current sensitivity ~10⁻¹³) |

---

## Open Sub-Tasks

| Gap | Description | Priority |
|-----|-------------|----------|
| Y1 | Derive Yukawa coupling y from S[Θ] | HIGH |
| Y2 | Derive VEV v from V_eff(θ₀) on ψ-circle | HIGH |
| L1 | Explicit UBT path-integral Lamb-shift computation at φ=const | MEDIUM |

---

## See Also

- [Gauge Structure](Gauge_Structure) — U(1)_EM derivation
- [Fine Structure Constant α](Alpha_Constant) — α derivation chain
- [GR Recovery](GR_Recovery) — φ as physical field vs. gauge artifact
