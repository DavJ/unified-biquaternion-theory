# UBT CMB Prediction: ψ-Compactification and the Low-l Anomaly

**Author:** David Jaroš  
**Date:** 2026-03-06  
**Status labels:** Computed (mechanism identified) / NOT consistent with Planck 2018 at current level of approximation

---

## Prediction Statement

> **UBT predicts suppression of CMB primordial power at wavenumbers
> k < k_min = 1/R_ψ due to the ψ-compactification infrared cutoff.
> For Scenario B (R_ψ = c/H_0 ≈ 4449 Mpc), the Sachs-Wolfe approximation
> with matter transfer function gives C_2^UBT / C_2^ΛCDM ≈ 0.996 (0.4%
> suppression). This is NOT consistent with the Planck 2018 observed
> suppression of ~36% at l=2. The UBT ψ-compactification via primordial
> spectrum cutoff does NOT explain the low-l CMB anomaly at the computed
> level of approximation. This is documented as a constraint on the
> mechanism, not a falsification of core UBT.**

---

## Physical Mechanism

### Setup

UBT introduces complex time τ = t + iψ, where the imaginary part ψ is
compactified on a circle of radius R_ψ:

```
ψ ~ ψ + 2π R_ψ
```

The Fourier expansion of the field Θ(x, τ) in ψ-space gives modes
Θ_n(x, t) with effective mass m_n = n/R_ψ (winding number mass).

### Minimum wavenumber

No modes exist with physical spatial wavenumber k < k_min = 1/R_ψ.
In comoving coordinates, this translates to a cutoff in the
primordial power spectrum P_UBT(k) → 0 for k → 0.

### From P(k) to C_l

The CMB multipole l probes comoving scales k_l ~ l/η_0, where
η_0 ≈ 14,000 Mpc is the conformal distance to last scattering.

For l = 2: k_2 ~ 2/14000 ~ 1.4×10⁻⁴ Mpc⁻¹  
For l = 3: k_3 ~ 3/14000 ~ 2.1×10⁻⁴ Mpc⁻¹

If R_ψ ~ c/H_0 ~ 4449 Mpc, then k_min = 1/R_ψ ~ 2.2×10⁻⁴ Mpc⁻¹.

This is right in the range k_2 to k_3, which motivated the conjecture.

---

## Quantitative Result (Sachs-Wolfe approximation with transfer function)

Using `simulations/prediction_models/ubt_cmb_cl.py` with the
Sachs-Wolfe approximation and simplified matter transfer function
T(k) = 1/√(1 + (k/k_eq)⁴), k_eq = 0.015 Mpc⁻¹:

### Scenario B: R_ψ = c/H_0 ≈ 4449 Mpc

| l  | C_l^UBT / C_l^ΛCDM | Planck obs / ΛCDM | Status |
|----|-------------------|-------------------|--------|
| 2  | ~0.996 (0.4% supp.) | ~0.64 (36% supp.) | **NOT consistent** |
| 3  | ~0.999 (0.1% supp.) | ~0.72 (28% supp.) | **NOT consistent** |
| 5  | ~1.002             | ~0.94             | Consistent |
| 10 | ~1.002             | ~0.96             | Consistent |

### Why the suppression is small

The C_l integral receives contributions from a range of k, not just
k ~ l/η_0. Even though F_ψ(k_l2) ≈ 0.65 at the representative
wavenumber, the integral ∫ dk P(k) F_ψ(k) j_l²(kη_0) T²(k) is dominated
by k > k_min where F_ψ → 1. The fraction of C_2 from k < k_min
is only ~0.1% of the total (verified numerically).

The C_l kernel j_l²(kη_0) T²(k) has support across a wide range of k;
the k_min cutoff's narrow effect in P(k) translates to negligible
suppression in C_l via the SW integral.

---

## Comparison with Planck 2018 Data

### The low-l anomaly in Planck 2018

The Planck 2018 release (arXiv:1807.06205) documents:

- l=2: observed D_l ≈ 1160 μK², ΛCDM prediction ≈ 1800 μK²
  (ratio ≈ 0.64, significance ~1.5σ)
- l=3: observed D_l ≈ 1060 μK², ΛCDM prediction ≈ 1480 μK²
  (ratio ≈ 0.72, significance ~1.0σ)

### UBT vs. data

The UBT primordial spectrum cutoff (Scenario B) predicts ~0.4%
suppression at l=2, compared to the observed ~36%. The mechanism
as implemented does NOT explain the low-l anomaly.

**Classification of result:**

> **NOT CONSISTENT (at current approximation):** The UBT ψ-compactification
> cutoff in P(k) predicts negligible C_l suppression (~0.4%) at l=2,3
> in the Sachs-Wolfe + transfer-function approximation. This is not
> consistent with the Planck 2018 observed suppression (~36% at l=2).
>
> Caveats:
> (a) The SW + simplified transfer function approximation may miss
>     ISW and integrated effects that could change the result;
> (b) The low-l anomaly itself is only ~1.5σ and could be cosmic variance;
> (c) A different UBT mechanism (not primordial P(k) cutoff) might
>     produce the suppression.

---

## Falsifiable Prediction

> **UBT Prediction (Falsifiable):**  
> The ψ-compactification cutoff in P(k) with R_ψ = c/H_0 predicts
> C_l^UBT / C_l^ΛCDM − 1 < 1% for l = 2, 3 (in SW approximation).  
> This is consistent with any future observation finding the low-l
> anomaly ABSENT (C_l^obs / C_l^ΛCDM > 0.99).  
> If the low-l anomaly is confirmed at > 3σ by LiteBIRD or CMB-S4,
> this specific UBT mechanism (primordial P(k) cutoff) is ruled out.
> A different mechanism would then be needed to explain the suppression
> within UBT, or UBT makes no prediction for the low-l anomaly.

---

## Observational Constraint on R_ψ

The fact that the P(k) cutoff gives negligible C_l suppression means
this specific observable provides no constraint on R_ψ: any R_ψ value
gives the same result (C_l ratio ≈ 1).

The prior CMB comb null result (Variant C, p=0.919) and the current
suppression non-result together suggest that the CMB power spectrum
is not the primary observational window for UBT signatures at current
approximation levels.

---

## What Is Needed for More Precise Comparison

1. **Boltzmann code:** Run CAMB or CLASS with P_UBT(k) as input
   to get precise C_l values replacing the SW approximation. This
   might reveal larger suppression through ISW contributions.
2. **Exact Planck 2018 data:** Download from PLA (https://pla.esac.esa.int/)
   the low-l C_l values and error bars for χ² comparison.
3. **R_ψ from theory:** Derive R_ψ from the UBT field equations
   rather than setting it to c/H_0.

---

## Status Summary

| Item | Status |
|------|--------|
| Physical mechanism | **Derived** (ψ-compactification IR cutoff) |
| P_UBT(k) parametrization | **Derived** (phenomenological; see ubt_primordial_spectrum.py) |
| SW + transfer function C_l | **Computed** (~0.4% suppression at l=2) |
| Consistency with Planck low-l anomaly | **NOT consistent** (36% suppression not reproduced) |
| Boltzmann code comparison | **Pending** |
| Falsifiability | **YES** — see Falsifiable Prediction above |

---

## References

- Planck Collaboration 2018, Power spectra and likelihoods, arXiv:1807.06205
- `simulations/prediction_models/ubt_primordial_spectrum.py`
- `simulations/prediction_models/ubt_cmb_cl.py`
- `docs/physics/planck_era_ubt.md`
- `docs/physics/cmb_status.md` (existing CMB null result summary)
