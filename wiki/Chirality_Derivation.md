<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# Chirality Derivation — SU(2)_L Selection

The left-handedness of the weak force (SU(2)_L not SU(2)_L×SU(2)_R) is
derived from ψ-parity analysis of the UBT action S[Θ].

**Canonical source**: [`canonical/chirality/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/canonical/chirality)

---

## Key Theorem

**Theorem 5** (step1_psi_parity.tex §6): The ψ-parity operator P_ψ acts as γ⁵
in the ψ-sector. Modes with ψ-parity −1 (odd modes ℋ₋) couple to W± bosons;
modes with ψ-parity +1 (even modes ℋ₊) do not. The W vertex is P_ψ-odd, which
**selects SU(2)_L exclusively** from the full SU(2)_L × SU(2)_R of the ℍ algebra.

Status: **Proved [L1]** — Gap C1 (W± vertex from S[Θ]) is CLOSED.

---

## Derivation Status

<!-- BEGIN GENERATED: chirality_status -->
| Result | Status | File |
|--------|--------|------|
| ℍ gives SU(2)_L × SU(2)_R from left/right actions | ✅ **Proved** | [`appendix_E2_SM_geometry.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex) |
| P_ψ maps modes n → -n (ψ-parity) | ✅ **Proved** | [`step1_psi_parity.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step1_psi_parity.tex) |
| ∂_ψ anti-commutes with P_ψ | ✅ **Proved** | [`step1_psi_parity.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step1_psi_parity.tex) |
| P_ψ acts as γ⁵ in ψ-sector | ✅ **Proved** | [`step1_psi_parity.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step1_psi_parity.tex) |
| Preferred ψ-circle orientation (matter n>0 by CPT) | ✅ **Proved** | [`step1_psi_parity.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step1_psi_parity.tex) |
| SU(2)_L on odd modes ℋ₋ | ✅ **Proved** | [`step1_psi_parity.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step1_psi_parity.tex) |
| Gap C1 — W± vertex P_ψ-odd from S: **CLOSED** — no W_R in S; se… | ✅ **Proved** |  |
<!-- END GENERATED: chirality_status -->

> **Note:** Gap C1 (W± vertex P_ψ-odd from S[Θ]) is CLOSED — see [`step3_gap_C1_resolution.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step3_gap_C1_resolution.tex)

---

## Step Files

| File | Content |
|------|---------|
| [`step1_psi_parity.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step1_psi_parity.tex) | P_ψ definition, γ⁵ identification, SU(2)_L selection |
| [`step2_chirality_result.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step2_chirality_result.tex) | Summary of chirality result |
| [`step3_gap_C1_resolution.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/chirality/step3_gap_C1_resolution.tex) | Gap C1 closure: no W_R in S[Θ] |

---

## Physical Interpretation

The biquaternion algebra ℍ admits both left and right SU(2) actions (Spin(4) ≅
SU(2)_L × SU(2)_R). The ψ-circle orientation (matter modes have n > 0 by CPT)
selects one orientation and forces W to couple exclusively to left-handed modes.

---

## See Also

- [Gauge Structure](Gauge_Structure) — full SM gauge group derivation
- [Particle Spectrum](Particle_Spectrum) — fermion content and quantum numbers
- [Fundamental Objects](Fundamental_Objects) — ℂ⊗ℍ algebra and involutions
