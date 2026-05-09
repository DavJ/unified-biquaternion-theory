<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT Bridge Hypotheses — Polariton Supersolid

**Track:** `research_tracks/polariton_supersolid/`  
**Status:** 🔵 SPECULATIVE — Candidate hypotheses, not derived  
**Confidence:** Candidate (at best)  
**Last Updated:** 2025

---

## ⚠️ Mandatory Disclaimer

Everything in this document is **speculative**.

- None of these hypotheses has been derived from canonical UBT.
- None has been experimentally verified.
- No consciousness claims are made.
- These are research directions, not results.

The standard-physics content (`gp_derivation.md`, `gp_simulator.py`) is independent
of all of the below. The polariton supersolid is real condensed-matter physics whether
or not any UBT connection exists.

---

## Context: What Would a Bridge Require?

A valid UBT bridge hypothesis must provide:

1. A **precise algebraic mapping** from polariton field theory to a sector of the
   UBT Θ-field (not just a structural analogy).
2. A **novel prediction** — something the polariton community has not already computed
   from standard field theory.
3. **Falsifiability** — an observable that would discriminate UBT-bridge from standard
   theory in an experiment.

None of the hypotheses below yet satisfies all three requirements.

---

## Hypothesis 1: Complex-Time Analogue

**Informal statement:**  
The driven-dissipative Gross-Pitaevskii equation (ddGP) for polariton condensates
involves a complex-valued order parameter ψ evolving under a non-Hermitian generator.
UBT's fundamental field Θ(q, τ) is also complex-valued and evolves under the
complex-time equation ∇†∇ Θ = κ 𝒯 with τ = t + iψ. The imaginary part of τ plays
a role that is **structurally analogous** to the gain/loss term in ddGP.

**Formal analogy (not a derivation):**

```
ddGP:   iℏ ∂_t ψ = H_eff[ψ] ψ + (iℏ/2)(R n_R − Γ_C) ψ

UBT:    ∂²_τ Θ + ∇²_q Θ = κ 𝒯,   τ = t + iψ_UBT
```

If one identifies the imaginary-time parameter ψ_UBT with the net gain rate
`(R n_R − Γ_C)/2`, and the real-space Laplacian ∇²_q with the kinetic term, then
the two equations have similar structure in appropriate limits.

**Status:** Formal analogy only. The identification of ψ_UBT with a gain rate is
not derived; it requires specifying how the UBT field Θ projects onto a condensed-
matter effective field theory. Open.

**What would close this gap:**  
Derive the ddGP equation as an effective field theory from UBT by integrating out
high-energy biquaternionic modes, showing explicitly how the complex-time parameter
produces the gain/loss structure.

---

## Hypothesis 2: Supersolid Order as Emergent Biquaternionic Phase Structure

**Informal statement:**  
In the supersolid phase, the condensate simultaneously carries:
- Long-range phase coherence (U(1) ODLRO)
- Periodic density modulation (broken translational symmetry)

UBT's Θ-field carries more symmetry than a single complex scalar: it is a biquaternion
Θ ∈ ℂ ⊗ ℍ. The quaternionic degrees of freedom may allow simultaneous encoding of
both types of order in a single object, whereas standard single-component complex
field theory requires either a two-component or modified interaction to produce
both orders.

**Candidate structure:**

Write Θ = (θ₀ + θ₁ e₁ + θ₂ e₂ + θ₃ e₃) × (real + imaginary time part).
The U(1) phase corresponds to the overall complex phase of Θ (superfluid order).
The remaining quaternionic components e₁, e₂, e₃ may encode the density modulation
direction and amplitude (crystalline order).

**Status:** Structural analogy. The hypothesis requires:
- An explicit reduction of Θ to a two-level or four-component field in the
  condensed-matter limit.
- A mechanism by which the quaternionic components generate a roton instability
  that is absent in a single-component complex field.

Currently: **open problem**, not even a candidate derivation exists.

**What would close this gap:**  
Reduce UBT's field equations in the non-relativistic, single-cavity limit and show
that the resulting effective Lagrangian contains an interaction term that softens the
roton. Compute the resulting wavevector k_ss and compare with experiment.

---

## Hypothesis 3: Keldysh ↔ Complex-Time Correspondence

**Informal statement:**  
The Keldysh path-integral formalism for open quantum systems introduces a doubling of
degrees of freedom (forward and backward time contour). This doubled structure is
reminiscent of the complexification of time in UBT (t → τ = t + iψ), where the
imaginary part tracks phase evolution.

Concretely: in the Keldysh formalism, a field Φ is split into:
```
Φ_cl = (Φ₊ + Φ₋)/√2    (classical component)
Φ_q  = (Φ₊ − Φ₋)/√2    (quantum noise component)
```

In UBT, the field Θ has real and imaginary parts with respect to complex time.
The candidate correspondence is:
```
Φ_cl ↔ Re[Θ(q, τ)]   (coupled to real metric, visible sector)
Φ_q  ↔ Im[Θ(q, τ)]   (imaginary sector, decoupled from classical observations)
```

**Status:** Structural resemblance only. The Keldysh doubling is a mathematical trick
for computing non-equilibrium correlators and does not imply a literal complex time.
The correspondence would need to be made precise at the level of the action, not
just the field decomposition. Open.

**What would close this gap:**  
Show that the UBT action S[Θ] evaluated on the complex-time contour produces, in the
non-relativistic limit, a Keldysh action equivalent to the driven-dissipative Lindblad
master equation for a polariton condensate. This would be a significant result.

---

## Hypothesis 4: Stripe Wavevector from UBT Spectral Modes

**Informal statement:**  
The supersolid stripe wavevector k_ss in a polariton system is set by the minimum of
the effective roton dispersion. In standard theory, k_ss depends on the interaction
parameters (g, g₁₂, m*). UBT predicts a spectral mode structure for the Θ-field
that may constrain the allowed k values to a discrete set related to UBT's algebraic
data (the eigenvalues of the biquaternionic Laplacian on the physical sector).

**Candidate prediction (speculative):**  
The stripe wavevector k_ss might be related to the inverse of a characteristic length
scale derived from UBT's field spectrum. If UBT's lowest non-trivial spectral mode has
wavenumber k₁, then k_ss / k₁ = integer.

**Status:** No derivation. The spectral structure of the UBT Θ-field on a flat
2D domain has not been computed (as of this writing). This hypothesis is therefore
at the level of a research question, not a candidate derivation.

**What would close this gap:**  
1. Compute the eigenspectrum of ∇†∇ acting on the flat 2D sector of UBT.
2. Identify the lowest non-trivial mode k₁.
3. Predict k_ss(g, g₁₂, m*) from UBT and compare with ddGP prediction and experiment.

---

## Summary Table

| Hypothesis | Formal Status | Key Gap | Testability |
|-----------|--------------|---------|------------|
| H1: Complex-time analogue | Structural analogy | Derive ddGP from UBT | Indirect (effective field theory) |
| H2: Biquaternionic supersolid | Structural analogy | Roton from quaternionic components | Novel k_ss prediction (in principle) |
| H3: Keldysh ↔ complex time | Structural resemblance | Match UBT action to Keldysh action | Spectral function comparison |
| H4: Stripe wavevector from spectrum | Research question | Compute UBT spectral modes on 2D | Direct k_ss measurement |

---

## What Is NOT Claimed

- ❌ Polariton condensates **are** UBT fields
- ❌ Supersolid order **proves** complex time
- ❌ Any connection to consciousness, psychons, or mental states
- ❌ These hypotheses are part of canonical UBT
- ❌ Any of these hypotheses is currently experimentally confirmed

---

## Path to Promotion

A bridge hypothesis may be promoted from "Speculative / Candidate" to "Candidate (Partial)"
when:
1. The formal analogy is elevated to an algebraic mapping (even if approximate).
2. The mapping produces at least one falsifiable numerical prediction.

It may be promoted to "Candidate" when the prediction is quantitatively derived.
It reaches "Experimental" status when it is tested against data.

---

**Last Updated:** 2025  
**Status:** All hypotheses open. No derivations exist. Research directions only.
