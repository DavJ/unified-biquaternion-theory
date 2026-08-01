<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Prediction Inventory — Polariton Supersolid Research Track

**Track:** `research_tracks/polariton_supersolid/`  
**Status:** Draft  
**Last Updated:** 2025

Predictions are organized into two tiers:

- **Tier A — Standard Physics Predictions:** Follow directly from the ddGP equations
  and established condensed-matter theory. No UBT required. These are the scientific
  core of this track.
- **Tier B — UBT Bridge Predictions:** Require the speculative bridge hypotheses in
  `ubt_bridge/BRIDGE_HYPOTHESES.md`. These are labeled **SPECULATIVE** and are currently
  unverified and unproven.

---

## Tier A: Standard Physics Predictions

### A1. Threshold pump power for condensation

**Prediction:**  
Condensation onset at pump power density:

```
P_th = Γ_C × Γ_R / R
```

where Γ_C = cavity photon decay rate, Γ_R = reservoir decay rate, R = stimulated
scattering rate.

**Observable:** Threshold in photoluminescence intensity vs. pump power.  
**Status:** Well-established experimentally in polariton BEC (Kasprzak 2006).  
**Confidence:** High — standard result, not new.

---

### A2. Superfluid flow below critical velocity

**Prediction:**  
For pump above threshold, the condensate flows without scattering around a static
obstacle (defect or engineered barrier) when the flow velocity v < v_c, where:

```
v_c = √(g n_C / m*)   (Bogoliubov critical velocity)
```

Above v_c, vortex pairs nucleate and superfluid flow breaks down.

**Observable:** Far-field emission from condensate flowing past a photonic defect;
absence of scattering halo below v_c.  
**Status:** Experimentally demonstrated (Amo et al. 2009).  
**Confidence:** High — standard result.

---

### A3. Stripe phase instability threshold (two-component)

**Prediction:**  
In a two-component (spinor) polariton condensate with cross-component interaction g₁₂,
a stripe phase with wavevector k_ss is stabilized when:

```
|g₁₂| > g    and    |g₁₂| > ℏ² k_ss² / (4 m* n_C)
```

The stripe wavevector satisfies:

```
k_ss = √[ 4 m* (|g₁₂| − g) n_C / ℏ² ]
```

**Observable:**
- Density modulation period λ_ss = 2π/k_ss in real-space imaging
- Two symmetric peaks at ±k_ss in momentum-space (far-field photoluminescence)
- Simultaneous phase coherence across stripes (interferometric measurement)

**Status:** Predicted theoretically; analogous to spin-orbit coupled BEC (Li et al. 2017).
Not yet definitively observed in polariton systems.  
**Confidence:** Medium — theoretical prediction, awaiting polariton experiment.

---

### A4. Diffusive Goldstone mode (non-equilibrium signature)

**Prediction:**  
The phase (Goldstone) mode of a polariton condensate is **diffusive** (not acoustic):

```
ω(k→0) ≈ −i D k²   (diffusive)   instead of   ω = c_s k   (acoustic)
```

where D = g n_C / (ℏ Γ_C / 2) is an effective diffusion constant.

**Observable:** Measurement of condensate fluctuation spectrum via homodyne or
heterodyne detection; linewidth scaling as k² rather than k for small k.  
**Status:** Predicted theoretically (Wouters & Carusotto 2007) and indirectly supported
by linewidth measurements.  
**Confidence:** Medium — not directly measured with k-resolution in most experiments.

---

### A5. Roton minimum and crystallization instability

**Prediction:**  
In single-component polariton condensates with momentum-dependent (finite-range)
interactions or in structured photonic lattices, the Bogoliubov dispersion develops
a roton minimum at k = k_rot. When the roton energy ε_rot drops to zero, a density
wave (crystalline order) spontaneously forms.

```
ε_rot → 0   ⟹   supersolid instability
```

**Observable:**
- Roton minimum visible in Brillouin scattering or two-photon emission spectrum
- Spontaneous density modulation appearing at wavevector k_rot
- Simultaneous superfluid fraction remaining non-zero

**Status:** Not yet observed in polariton systems. Predicted to occur in systems with
engineered photonic band curvature or Feshbach-enhanced interactions.  
**Confidence:** Low-Medium — theoretically motivated, experimentally open.

---

### A6. Non-classical rotational inertia (polariton NCRI analogue)

**Prediction:**  
If a polariton supersolid is established (simultaneous density wave + superfluid order),
the effective rotational inertia I_eff should satisfy:

```
I_eff = I_classic × (1 − f_s)   where 0 < f_s ≤ 1
```

i.e., the system responds to rotation as if a fraction f_s of the condensate is
"missing" from the rigid-body response — direct analogue of Leggett's NCRI criterion.

**Observable (photonic analogue):** Rotating trap or effective gauge field; measurement
of angular momentum in far-field emission.  
**Status:** Untested in polariton systems. Realizing a rotating polariton system is
technically challenging.  
**Confidence:** Low — feasibility of the experiment is uncertain.

---

## Tier B: UBT Bridge Predictions (SPECULATIVE)

**⚠️ WARNING:** The following predictions depend on the speculative bridge hypotheses
in `ubt_bridge/BRIDGE_HYPOTHESES.md`. None of these has been derived rigorously.
They are listed as **research hypotheses** to be tested if and when the bridge is
established.

---

### B1. Stripe wavevector quantization from UBT spectral modes (H4 bridge)

**Speculative prediction:**  
If the UBT Θ-field spectral modes on a 2D flat domain are quantized as k_n = n × k₁
for integer n, and if the stripe wavevector k_ss is locked to the lowest non-trivial
spectral mode, then:

```
k_ss = k₁ = 2π / L_UBT
```

where L_UBT is a characteristic length derived from UBT algebraic data (not yet computed).

**What it would take:** Compute UBT spectral modes on 2D flat domain; derive k₁;
compare prediction k_ss = k₁ with ddGP prediction k_ss = f(g, g₁₂, m*, n_C).  
**Distinguishing test:** UBT predicts a specific k_ss independent of interaction
parameters; standard ddGP predicts k_ss varies with g₁₂ and density.  
**Status:** **Not derived.** No UBT spectral computation for 2D domain exists yet.

---

### B2. Phase coherence length from complex-time diffusion (H1 bridge)

**Speculative prediction:**  
If the imaginary component of UBT complex time ψ_UBT controls phase decoherence
analogously to the gain/loss rate in ddGP, the phase coherence length of the polariton
condensate should scale as:

```
l_coh ~ √(ℏ D / Γ_eff)
```

where Γ_eff is determined by the imaginary-time parameter in UBT rather than just
the cavity decay rate Γ_C. Specifically, UBT predicts a correction:

```
Γ_eff = Γ_C - δΓ_UBT,   with δΓ_UBT = f(UBT parameters, to be derived)
```

This would produce a coherence length systematically longer than predicted by ddGP
alone.

**Distinguishing test:** Precision measurement of spatial coherence function g⁽¹⁾(r)
vs. distance; compare with ddGP prediction and UBT-corrected prediction.  
**Status:** **Not derived.** The function f(UBT parameters) is unknown.

---

### B3. Non-equilibrium universality class modification (H3 bridge)

**Speculative prediction:**  
If the Keldysh ↔ complex-time correspondence (Hypothesis 3) is established, UBT
predicts that the non-equilibrium universality class of the polariton BEC transition
is modified from the Kardar-Parisi-Zhang (KPZ) universality class (standard prediction)
to a different class determined by the UBT action's complex-time structure.

**Distinguishing test:** Scaling exponents of density-density correlations near threshold;
measure dynamical exponent z and roughness exponent χ; compare with KPZ (z=3/2, χ=1/2)
and UBT-modified prediction (to be derived).  
**Status:** **Not derived.** The UBT modification to KPZ universality class is unknown.

---

## Summary Table

| ID | Tier | Prediction | Observable | Confidence |
|----|------|-----------|-----------|-----------|
| A1 | Standard | Condensation threshold P_th | PL intensity vs pump | High |
| A2 | Standard | Superfluid flow / critical velocity | Scattering from defect | High |
| A3 | Standard | Stripe phase threshold k_ss(g₁₂) | Real-space density + momentum space | Medium |
| A4 | Standard | Diffusive Goldstone mode | Fluctuation spectrum scaling | Medium |
| A5 | Standard | Roton minimum → crystallization | Brillouin scattering, density modulation | Low-Medium |
| A6 | Standard | NCRI analogue | Angular momentum in rotating trap | Low |
| B1 | **SPECULATIVE** | k_ss locked to UBT spectral mode | k_ss independence from g₁₂ | **Not derived** |
| B2 | **SPECULATIVE** | Coherence length correction from ψ_UBT | g⁽¹⁾(r) precision measurement | **Not derived** |
| B3 | **SPECULATIVE** | KPZ universality class modification | Scaling exponents near threshold | **Not derived** |

---

## Falsification Criteria

### For Tier A predictions

- **A3 fails** if stripe phase never appears in spinor polariton condensates even when
  |g₁₂| > g. This would suggest missing physics in the mean-field treatment or that
  dissipation prevents stripe formation.
- **A5 fails** if no roton minimum can be reached by engineering photonic band structure.

### For Tier B predictions

Any Tier B prediction is **automatically falsified** if the corresponding bridge
hypothesis (H1–H4) is shown to be algebraically inconsistent.

If the bridge is established and the prediction is derived, it is falsified if the
observable disagrees with the UBT derivation at the 2σ level.

---

## Experimental Requirements

To test Tier A (especially A3, A5, A6):
- Spinor (two-component) polariton microcavities with tunable TE-TM splitting
- Feshbach resonance control of polariton-polariton interactions (or cavity-mediated tuning)
- High-resolution real-space imaging (sub-μm) + k-space spectroscopy
- Interferometric phase imaging for coherence measurement

To test Tier B:
- All of the above
- Precision measurement of k_ss to ≤ 1% (to test B1 quantization)
- Scaling exponent measurement near threshold with large dynamic range (to test B3)

---

**Status:** Tier A predictions are scientifically well-defined and experimentally
accessible. Tier B predictions require bridge derivation first.

**No consciousness claims are present in any prediction.**
