# CMB Work in UBT — Status Summary

**Author:** David Jaroš  
**Date:** 2026-03-06  
**Status label:** Documented Null Result + New Directions Open

---

## What the Existing Code Computes

`simulations/prediction_models/cmb_phase_power_spectrum.py` implements
**UBT Variant C**: a periodic comb modulation of the CMB temperature
(TT) power spectrum,

```
C_l → C_l^ΛCDM × (1 + A_comb × cos(2π l / Δl + φ))
```

with **Δl = 137** (derived from UBT winding number quantization) and
**A_comb** and **φ** as free parameters. The script computes a mock
ΛCDM spectrum, applies the comb, and runs a Monte Carlo null test
estimating the sensitivity of Planck PR3 data to this signal.

`simulations/prediction_models/cmb_null_test_results.json` records
the output: the Planck PR3 test returned **p = 0.919** (no signal),
placing an upper limit A_comb < 0.17 at 95% confidence.

---

## What the Prediction Is and Where It Comes From

- **Winding number quantization:** UBT compactifies imaginary time
  ψ on a circle of radius R_ψ. Standing modes Θ_n have n full cycles
  around the ψ-circle. The fine-structure constant enters as
  α⁻¹ ≈ 137, fixing the winding period. The comb period Δl = 137
  in multipole space follows from this identification.
- **Amplitude A_comb** is not derived from UBT first principles;
  it was treated as a free (empirical) parameter.
- **Phase φ** is also undetermined.

---

## Null Result

**Classification: Null (not falsification of core UBT).**

The comb prediction was a Layer C (speculative) extension, not a
core prediction. The null result eliminates or severely constrains the
specific comb model (A_comb < 0.17 at 95% CL), but does not falsify
UBT's core field equations.

See `FINGERPRINTS/null_results/combined_verdict.md` for the full
statistical analysis.

---

## What Is Missing

### 1. Primordial power spectrum modification

The existing code applies a comb to the *angular* power spectrum C_l,
not to the *primordial* power spectrum P(k). A more fundamental UBT
prediction should modify P(k) directly through the ψ-compactification
structure, then propagate to C_l via the transfer function. This
derivation does not yet exist.

### 2. Low-l suppression (ψ-compactification cutoff)

The compactification of ψ at scale R_ψ ~ l_Planck introduces a
minimum wavenumber k_min ~ 1/R_ψ. Below k_min no modes exist.
In C_l space this manifests as power suppression at l ≤ 3 (large
angular scales), matching the well-known "low-l anomaly" in Planck 2018
data. This mechanism is independent of the comb and has not been
computed.

### 3. Connection to Planck era physics

The ψ-compactification is most relevant near t ~ t_Planck (Planck
time). Understanding what UBT predicts for t < t_Planck (before the
standard Big Bang era) is needed to make the primordial spectrum
derivation rigorous.

---

## Next Steps

1. Derive P_UBT(k) from S_kin[Θ] including ψ-winding contributions
   → `simulations/prediction_models/ubt_primordial_spectrum.py`
2. Convert P_UBT(k) to C_l using transfer function formalism
   → `simulations/prediction_models/ubt_cmb_cl.py`
3. Compare with Planck 2018 low-l data (l = 2, 3 suppression)
   → `docs/predictions/cmb_prediction.md`
4. Document UBT prediction for t < t_Planck
   → `docs/physics/planck_era_ubt.md`
