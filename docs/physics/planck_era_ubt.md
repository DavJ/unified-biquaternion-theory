# UBT and the Planck Era: What Happens at t < t_Planck

**Author:** David Jaroš  
**Date:** 2026-03-06  
**Status labels:** Proven (GR structure) / Conjecture (bounce) / Speculative (Hartle-Hawking analogy)

---

## 1. The Standard Physics Problem

### 1.1 Where GR fails

General Relativity predicts that at t = 0 (the Big Bang singularity), the
curvature scalar R diverges:

```
R → ∞   as   t → 0
```

Classical GR has no model for t < 0 — the Big Bang is a boundary of
spacetime, not an event inside it. The Penrose–Hawking singularity
theorems guarantee this breakdown under reasonable energy conditions.

### 1.2 Where QFT fails

Quantum field theory is formulated on a fixed background spacetime. Near
t ~ t_Planck, where

```
t_Planck ~ √(ħG/c⁵) ~ 5.4 × 10⁻⁴⁴ s
l_Planck ~ √(ħG/c³) ~ 1.6 × 10⁻³⁵ m
```

the spacetime curvature becomes of order 1/l_Planck² and the background
approximation breaks down. Standard QFT has no self-consistent quantum
gravity model for this regime.

### 1.3 The no-model zone

For t < t_Planck, no established physics framework applies. Loop Quantum
Cosmology (LQC) and string theory propose mechanisms to resolve the
singularity (bounce and string gas cosmology, respectively), but both
require significant extensions of current theory.

---

## 2. The UBT Framework

### 2.1 The core field

UBT describes all physics through a single biquaternionic field
Θ(x, τ) defined over complex time τ = t + iψ. The field equation is:

```
∇†∇ Θ(x, τ) = κ 𝒯(x, τ)
```

In the real limit (ψ → 0), this reduces to Einstein's field equations
R_μν − ½g_μν R = 8πG T_μν. UBT does NOT replace GR — it embeds GR
as a special case.

### 2.2 Compactification of ψ

The imaginary time ψ is compactified:

```
ψ ~ ψ + 2π R_ψ,    R_ψ ~ l_Planck
```

This is the crucial difference from standard GR: the ψ-circle prevents
the imaginary-time direction from shrinking to zero. The field Θ
always "sees" a minimum length R_ψ in the ψ-direction.

### 2.3 Why ψ-compactification avoids singularities

Consider the UBT metric in the vicinity of t = 0. The full complex-time
metric has components:

```
g_{ττ} = g_{tt} + 2i g_{tψ} - g_{ψψ}
```

Near the classical Big Bang singularity (t → 0, ψ = 0):
- The real metric g_{tt} → ∞ (classical GR singularity)
- The imaginary-time metric g_{ψψ} receives contributions from the
  ψ-winding modes Θ_n with n/R_ψ mass terms

The winding mass terms in g_{ψψ} provide a "floor" that prevents
the full complex metric from diverging even when g_{tt} → ∞.

**Status: CONJECTURE.** A rigorous proof would require solving the full
UBT field equation near the classical singularity and showing that
g_{ψψ} remains bounded. This has not been done.

---

## 3. What UBT Predicts Near t = t_Planck

### 3.1 The ψ-direction becomes dominant

At t ~ t_Planck, the real-time kinetic energy E_t ~ ħ/t_Planck equals
the ψ-winding energy E_ψ ~ ħ/R_ψ (since R_ψ ~ l_Planck ~ c t_Planck).
Near this point:

```
t ~ R_ψ / c = l_Planck / c = t_Planck
```

Below t_Planck, the condition t << R_ψ means the ψ-direction is
relatively larger than the t-direction. In this regime the field
equation ∇†∇ Θ = κ 𝒯 is dominated by ψ-derivatives:

```
∂²Θ/∂ψ² >> ∂²Θ/∂t²   (for t << R_ψ)
```

This is equivalent to a rotation from Lorentzian (−, +, +, +, ψ)
to Euclidean (+, +, +, +, ψ) signature in the τ-plane.

### 3.2 Euclidean signature and the no-boundary analogy

The transition to Euclidean-dominant dynamics is analogous to the
Hartle-Hawking no-boundary proposal (1983), where the wave function
of the universe is computed using Euclidean path integral with no
singular boundary at t = 0. In the Hartle-Hawking approach:

```
τ_HH = i t   (Wick rotation: Lorentzian → Euclidean)
```

In UBT, the ψ-direction plays the role of the Euclidean time. When
t → 0, the ψ-circle becomes the dominant "time" direction and the
universe can be described as a finite-size Euclidean 5-manifold
(4 spatial + 1 ψ-circle) without a singular boundary.

**Status: SPECULATIVE analogy.** UBT is not the Hartle-Hawking
proposal. However, the mathematical structure (complex time τ = t + iψ,
Euclidean-Lorentzian transition) is formally similar. Whether the
physics is identical requires computing the UBT path integral, which
has not been done.

### 3.3 Is there a "bounce"?

Loop Quantum Cosmology (LQC) predicts a "quantum bounce" at t = t_Planck:
the universe contracts, reaches minimum volume ~ l_Planck³, and
re-expands. The singularity is replaced by a quantum tunneling event.

Does UBT predict a bounce? Tentative answer:

- If the ψ-winding modes provide a "pressure" term P_ψ ~ ħ/R_ψ⁴ in
  the UBT stress-energy tensor, this acts like a repulsive force at
  Planck density, analogous to the LQC quantum correction.
- This would give a classical Big Bounce in UBT, with the universe
  contracting from a previous cycle and re-expanding through the
  Planck phase.
- The key parameter is whether P_ψ can be large enough to halt
  contraction at t ~ t_Planck.

**Status: OPEN HARD PROBLEM.** No derivation of P_ψ from the UBT
field equations has been completed.

---

## 4. The ψ-Circle as Natural UV Cutoff

### 4.1 Standard UV divergences

In quantum field theory, loop integrals diverge at high momenta (UV
divergences). This requires renormalization — an insertion of
counterterms that absorb the divergences. The divergences signal
that the theory is incomplete at short distances.

### 4.2 UBT's built-in cutoff

The UBT kinetic term in momentum space gives a propagator:

```
G(k, n) = 1 / (k² + (n/R_ψ)²)   for winding mode n
```

The minimum propagator denominator is (n_max/R_ψ)² where n_max is the
highest winding mode populated. This provides a physical UV cutoff:

```
Λ_UV ~ 1/R_ψ ~ 1/l_Planck = E_Planck/ħc
```

All loop integrals are automatically finite if R_ψ > 0. The Planck
scale emerges as the natural UV cutoff from the ψ-compactification.

**Status: CONJECTURE (plausible but unproven).** Whether the UBT
propagator structure truly regulates all UV divergences of the full
biquaternionic field theory requires a complete one-loop calculation.

---

## 5. Summary: What UBT Says vs. What Remains Open

### Proven within UBT (subject to UBT being a valid framework)

- [x] UBT embeds General Relativity (ψ → 0 limit gives Einstein equations)
- [x] ψ-compactification gives a minimum length scale R_ψ ~ l_Planck
- [x] Winding modes Θ_n exist with mass m_n = n/R_ψ
- [x] The Planck scale arises naturally from R_ψ (no tuning required)

### Conjectured with partial support

- [ ] ψ-winding floor prevents divergence of full metric at t = 0
- [ ] The UV cutoff from R_ψ renders loop integrals finite
- [ ] The low-l CMB suppression arises from k_min = 1/R_ψ
  (qualitative calculation done; quantitative pending)

### Speculative (no calculation done)

- [ ] UBT predicts a Big Bounce at t = t_Planck (LQC analogy)
- [ ] The Hartle-Hawking no-boundary proposal is recovered as a
  special case of UBT in the ψ-dominant regime
- [ ] Pre-Big-Bang physics is described by a pure ψ-circle phase

### Open Hard Problems

- [ ] Solve UBT field equation near t = 0 (requires functional analysis
  on complex-time manifolds; no existing mathematical framework)
- [ ] Derive R_ψ from the UBT action (why R_ψ ~ l_Planck and not
  some other scale?)
- [ ] Quantize the UBT field (path integral over biquaternionic fields;
  mathematically ill-defined at present)

---

## 6. Connection to CMB Observations

The only currently observable consequence of the Planck-era UBT
structure is through the primordial power spectrum:

- If R_ψ ~ c/H_0 (Hubble scale): predicts CMB low-l suppression
  (see `docs/predictions/cmb_prediction.md`)
- If R_ψ ~ l_Planck (standard Planck scale): no observable CMB effect
  (modes with k ~ 1/l_Planck exit the horizon 60 e-folds before the
  observable window)

The fact that the observed low-l anomaly (Planck 2018, l = 2–4
suppression) has the same sign and approximate magnitude as the
UBT Scenario B prediction is suggestive but not conclusive.

---

## References

- Hartle, J.B., Hawking, S.W. (1983). Wave function of the Universe.
  Physical Review D 28, 2960.
- Bojowald, M. (2001). Absence of a singularity in loop quantum
  cosmology. Physical Review Letters 86, 5227.
- Planck Collaboration (2018). Planck 2018 results. CMB power spectra
  and likelihoods. arXiv:1807.06205.
- `simulations/prediction_models/ubt_primordial_spectrum.py`
- `docs/predictions/cmb_prediction.md`
