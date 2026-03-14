<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# φ-Universe Parameter and h_μν Vacuum

The parameter φ in UBT (the scalar phase of Θ) can be physical or pure gauge
depending on the vacuum structure. For a two-mode winding vacuum, φ is physical
and the metric has a non-trivial imaginary component h_μν.

**Canonical source**: [`canonical/geometry/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/canonical/geometry)  
**Status document**: [`docs/PHI_UNIVERSE_PARAMETER.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/PHI_UNIVERSE_PARAMETER.md)

---

## Key Results

| Result | Status | File |
|--------|--------|------|
| φ-projection theorem | **Proved [L1]** | [`phase_projection.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/phase_projection.tex) |
| h_μν = 0 (single-mode vacuum) | **Proved [L1]** | [`biquaternionic_vacuum_solutions.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/biquaternionic_vacuum_solutions.tex) |
| h_μν ≠ 0 (two-mode vacuum) | **Proved [L1]** | [`biquaternionic_vacuum_solutions.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/biquaternionic_vacuum_solutions.tex) |
| φ is physical for two-mode vacuum | **Proved [L1]** | [`docs/PHI_UNIVERSE_PARAMETER.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/PHI_UNIVERSE_PARAMETER.md) |

---

## Derivation Status

<!-- BEGIN GENERATED: phi_universe_status -->
| Result | Status | File |
|--------|--------|------|
| φ-projection theorem (P_φ satisfies GR) | ✅ **Proved** | [`phase_projection.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/phase_projection.tex) |
| ∂α/∂φ = 2ρr·α(0) formula | ✅ **Proved** | [`phi_gauge_vs_physical.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/phi_gauge_vs_physical.tex) |
| h_μν = 0 for single-mode winding vacuum | ✅ **Proved** | [🌐 `biquaternionic_vacuum_solutions.tex`](https://davj.github.io/unified-biquaternion-theory/canonical/geometry/biquaternionic_vacuum_solutions.html) · [pdf](https://davj.github.io/unified-biquaternion-theory/UBT_canonical_main.pdf) · [tex](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/biquaternionic_vacuum_solutions.tex) |
| h_μν ≠ 0 two-mode winding vacuum | ✅ **Proved** | [🌐 `biquaternionic_vacuum_solutions.tex`](https://davj.github.io/unified-biquaternion-theory/canonical/geometry/biquaternionic_vacuum_solutions.html) · [pdf](https://davj.github.io/unified-biquaternion-theory/UBT_canonical_main.pdf) · [tex](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/biquaternionic_vacuum_solutions.tex) |
| r ≈ 4.66 for canonical two-mode vacuum | ✅ **Proved** | [`compute_h_munu_vacuum.py`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/tools/compute_h_munu_vacuum.py) |
| φ is physical (not pure gauge) for two-mode vacuum | ✅ **Proved** | [`PHI_UNIVERSE_PARAMETER.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/PHI_UNIVERSE_PARAMETER.md) |
| ψ↔φ are distinct operations (not equivalent) | ✅ **Proved** | [`PHI_UNIVERSE_PARAMETER.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/PHI_UNIVERSE_PARAMETER.md) |
| dim(ℳ_UBT) ≥ 1 (U(1) moduli) | ✅ **Proved** | [`PHI_UNIVERSE_PARAMETER.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/PHI_UNIVERSE_PARAMETER.md) |
| dim(ℳ_UBT) = 4 (U(1)×Sp(1)) | 💭 **Conjecture** | [`PHI_UNIVERSE_PARAMETER.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/docs/PHI_UNIVERSE_PARAMETER.md) |
<!-- END GENERATED: phi_universe_status -->

---

## Physical Significance

The two vacuum types have different observable signatures:

- **Single-mode winding vacuum**: h_μν = 0, φ is pure gauge → standard GR
- **Two-mode winding vacuum**: h_μν ≠ 0, φ is physical → extended UBT metric

The moduli space of UBT vacua has dimension ≥ 1 (U(1) phase rotations);
the full quaternionic extension dim(ℳ_UBT) = 4 is conjectured.

---

## Relation to φ-Universe

The φ parameter acts as a cosmological background that does not break U(1)_EM
(the scalar is electrically neutral). The α-running in a φ background gives
δα/α ~ 10⁻²¹ — below current observational sensitivity.

→ See [QED Reproducibility](QED_Reproducibility) for QED constraints.

---

## See Also

- [GR Recovery](GR_Recovery) — metric and Einstein equations
- [Emergent Spacetime](Emergent_Spacetime) — metric from Θ
- [QED Reproducibility](QED_Reproducibility) — QED at φ=const
