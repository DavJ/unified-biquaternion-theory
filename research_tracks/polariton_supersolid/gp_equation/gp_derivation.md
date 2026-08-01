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


# Gross-Pitaevskii Equation for Polariton Supersolids

**Track:** `research_tracks/polariton_supersolid/`  
**Status:** Standard condensed-matter physics — no UBT assumptions  
**Last Updated:** 2025

---

## 1. Physical Setup

A **semiconductor microcavity** confines photons between two distributed Bragg
reflectors (DBR mirrors) separated by a distance L_cav ~ λ/2. The confined photon
mode resonantly couples to exciton (electron-hole pair) transitions in embedded
quantum wells. When the coupling strength g exceeds the linewidths κ (photon decay)
and γ (exciton dephasing), the system enters the **strong coupling regime**, producing
two new eigenmodes called **upper** and **lower polariton branches**.

The lower polariton branch (LP) has a very small effective mass:

```
m* = ℏ/( c² / (2 n² L_cav) ) ~ 10⁻⁵ mₑ
```

This tiny mass enables Bose-Einstein condensation at temperatures up to room temperature
in some material systems (GaN, ZnO, organic).

### Polariton decay and pumping

Polaritons decay because photons tunnel through the imperfect mirrors at rate γ_C
(cavity photon loss rate, typically ns⁻¹). To maintain a non-equilibrium steady state,
an external laser pump P(r) continuously creates excitons that scatter into the
condensate. This makes the polariton condensate fundamentally **driven-dissipative**.

---

## 2. Second-Quantized Hamiltonian

Start from the full microscopic Hamiltonian (photon + exciton + coupling + interactions).
After a Hopfield transformation to polariton modes (a_k = X_k b_k + C_k â_k, where
X_k, C_k are Hopfield coefficients), the lower-polariton Hamiltonian reads:

```
H = Σ_k ε_k a†_k a_k  +  (g/2V) Σ_{k,k',q} a†_{k+q} a†_{k'-q} a_{k'} a_k
```

where:
- `ε_k = ε_LP(k)` = LP dispersion (parabolic near k=0: ε_k ≈ ε_0 + ℏ²k²/2m*)
- `g = |X_k|⁴ g_x` = effective polariton-polariton interaction (dominated by
  exciton fraction X_k; g > 0, repulsive)
- V = quantization area

The reservoir excitons (off-resonant, high-momentum excitations created by the pump)
couple to the condensate and must be tracked separately.

---

## 3. Mean-Field and Reservoir Equations

### 3.1 Order parameter

Define the condensate mean field (order parameter):

```
ψ(r, t) = ⟨â(r, t)⟩
```

This is a complex scalar field: ψ = √(n_C) exp(iφ), where n_C = |ψ|² is the local
condensate density and φ is the local phase.

### 3.2 Reservoir dynamics

Hot incoherent excitons (reservoir) are created by the pump at rate P(r) and relax
to the condensate via stimulated scattering at rate R. The reservoir density n_R(r, t)
obeys:

```
∂n_R/∂t = P(r) − (Γ_R + R |ψ|²) n_R          ... (1)
```

where:
- `P(r)` = pump injection rate [m⁻² s⁻¹]
- `Γ_R` = reservoir decay rate (non-radiative + radiative; ps⁻¹)
- `R` = stimulated scattering rate from reservoir to condensate (m² s⁻¹)

### 3.3 Driven-Dissipative Gross-Pitaevskii (ddGP) Equation

Applying the mean-field approximation and Markov approximation for the reservoir
coupling, the equation of motion for ψ is:

```
iℏ ∂ψ/∂t = [ −ℏ²∇²/(2m*)  +  V(r)  +  g |ψ|²  +  g_R n_R
              +  (iℏ/2)(R n_R − Γ_C)
            ] ψ  +  F(r,t)          ... (2)
```

**Symbol dictionary:**

| Symbol | Meaning | Typical value |
|--------|---------|---------------|
| m\* | LP effective mass | 5 × 10⁻⁵ mₑ |
| V(r) | external potential (trap, disorder) | 0 in homogeneous case |
| g | polariton-polariton interaction (real part) | 1–10 μeV μm² |
| g_R | interaction with reservoir excitons | ~ 2g |
| n_R | reservoir exciton density | coupled via eq. (1) |
| Γ_C | polariton decay rate (photon leakage) | 0.01–1 ps⁻¹ |
| R | stimulated scattering rate into condensate | ~ 10⁻² μm² ps⁻¹ |
| F(r,t) | coherent drive field (optional, for resonant pumping) | 0 in nonresonant case |

### 3.4 Steady-State Threshold

In the simplest 0D (spatially homogeneous) case with F = 0, setting ∂n_R/∂t = 0 and
∂ψ/∂t = 0 gives the threshold condition:

```
R n_R^(th) = Γ_C   →   n_R^(th) = Γ_C / R
P^(th) = Γ_R n_R^(th) = Γ_C Γ_R / R
```

Above threshold (P > P^(th)), a macroscopic condensate density builds up:

```
|ψ|² = (P/Γ_C − P^(th)/Γ_C) × Γ_R / (R Γ_C)    [approximate]
```

---

## 4. Supersolid Phase Criterion

A **supersolid** requires simultaneous:

### 4.1 Superfluid order (off-diagonal long-range order)

Non-zero condensate fraction:
```
f_s = N_0 / N_total > 0
```
In 2D (our main case) this is rigorously a quasi-long-range order (BKT phase).

Operationally: the phase φ(r,t) is spatially coherent over distances much larger than
the density modulation period.

### 4.2 Density modulation (diagonal long-range order)

The static structure factor S(k) has a peak at k ≠ 0:

```
S(k) = (1/N) |Σ_j exp(ik·r_j)|²  →  (1/A) |∫ n_C(r) e^{ik·r} d²r|²
```

A peak at k = k_ss ≠ 0 signals periodic density modulation with period λ_ss = 2π/k_ss.

### 4.3 Physical mechanism for supersolid instability

The instability toward density-modulated order is driven by **roton softening**: if the
LP dispersion (or effective dispersion renormalized by interactions) develops a local
minimum at finite k = k_rot (a "roton minimum"), fluctuations at that wavevector grow
unstable and spontaneously create a periodic density pattern.

Conditions for roton softening in polariton systems:
- Beyond-mean-field quantum fluctuations (Lee-Huang-Yang correction)
- Momentum-dependent interactions (finite-range effects from exciton wavefunctions)
- Photonic band engineering (structured cavities)
- Two-component condensate with cross-species interactions (bistability)

---

## 5. Two-Component Extension

In spinor (σ = ±1/2 spin) polariton condensates, two coupled GP equations apply:

```
iℏ ∂ψ_+/∂t = [ −ℏ²∇²/2m* + g|ψ_+|² + g₁₂|ψ_−|² + (iℏ/2)(R n_R − Γ_C) ] ψ_+
                + Ω ψ_−                                ... (3a)

iℏ ∂ψ_−/∂t = [ −ℏ²∇²/2m* + g|ψ_−|² + g₁₂|ψ_+|² + (iℏ/2)(R n_R − Γ_C) ] ψ_−
                + Ω ψ_+                                ... (3b)
```

where:
- g₁₂ = cross-component interaction (can be negative → attractive, drives phase separation
  and stripe instability)
- Ω = effective Rabi coupling between spin components (from TE-TM splitting or applied
  magnetic field)

When |g₁₂| > g, the two-component system becomes unstable toward stripe formation —
this is the analog of the Li et al. 2017 spin-orbit-coupled BEC supersolid.

---

## 6. Bogoliubov Excitation Spectrum

Linearizing eqs. (2) around the homogeneous steady state (ψ₀ = √n₀, n_R^(ss)):

```
ψ = (√n₀ + δψ) exp(−i μ t/ℏ),   δψ(r,t) = u_k e^{ik·r−iωt} + v_k* e^{−ik·r+iω*t}
```

The Bogoliubov dispersion is (for the non-dissipative limit Γ_C → 0, F = 0):

```
ω_k = √[ (ℏk²/2m*)² + 2 g n₀ (ℏk²/2m*) ] / ℏ        ... (4)
```

This is the standard Bogoliubov spectrum: linear (phonon) at small k, quadratic (free
particle) at large k. A roton minimum does not appear in the simplest single-component
case; it requires additional physics (see Section 5 or momentum-dependent g(k)).

In the **driven-dissipative** case, ω_k acquires an imaginary part:

```
Im(ω_k) = −(Γ_C − R n_R^(ss)) / 2    [for all k, at mean-field level]
```

The Goldstone (k→0) mode is diffusive (Im(ω₀) = 0, Re(ω₀) = 0), not propagating,
reflecting the non-equilibrium breaking of U(1) symmetry (Wouters & Carusotto 2007).

---

## 7. Order Parameters and Diagnostics

| Quantity | Formula | Supersolid signature |
|----------|---------|---------------------|
| Condensate density | n_C(r) = |ψ(r)|² | Must be modulated: n_C(r) = n̄ + δn cos(k_ss · r) |
| Phase map | φ(r) = arg(ψ(r)) | Coherent across density maxima |
| Structure factor | S(k) = |FT[n_C]|² | Peak at k_ss ≠ 0 AND at k = 0 (coherence) |
| Superfluid fraction | f_s = 1 − (I/I_classic) × NCRI | > 0 (polariton analogue) |
| Momentum distribution | n(k) = |ψ̃(k)|² | Peaks at ±k_ss AND at k = 0 |

---

## 8. Relation to UBT

*This section is intentionally brief. Detailed hypotheses are in `ubt_bridge/BRIDGE_HYPOTHESES.md`.*

The ddGP equation (2) is a nonlinear Schrödinger equation for a complex field ψ(r,t)
with non-Hermitian (gain/loss) terms. UBT's fundamental field Θ(q,τ) is also complex-
valued with a non-trivial time structure (τ = t + iψ). The structural parallel is:

```
Standard:  iℏ ∂_t ψ = H[ψ] ψ + i Γ[ψ] ψ
UBT:       ∇†∇ Θ = κ 𝒯     (with τ = t + iψ complex)
```

This is a **formal analogy only**. No precise algebraic mapping has been established.
The imaginary part of τ in UBT plays a role structurally analogous to the gain/loss
term i Γ[ψ] in ddGP, but the physical content is different.

---

**Standard physics; no speculative claims beyond stated formal analogy.**
