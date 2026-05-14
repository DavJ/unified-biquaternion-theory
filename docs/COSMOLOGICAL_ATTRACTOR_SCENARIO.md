# Cosmological Attractor Scenario in UBT
## How the Universe Selects Its Fine Structure Constant

**Status:** [CONJECTURE — conceptual framework; detailed calculations pending]  
**Layer:** [L1] — phase-space geometry  
**Task:** Task 8 — Connect Chaotic Attractor to Cosmological Initial Conditions  
**Author:** Ing. David Jaroš  

---

## 1. The Scenario

In the Unified Biquaternion Theory, the imaginary part of complex time ψ
is a dynamical degree of freedom governed by the drift-diffusion equation:

    ∂_t ψ = D·∇²ψ - α·∂V/∂ψ   [POSTULATE — eq. H.2, Appendix H]

where V(ψ) is the effective potential (see `ubt_core/verify_Vpsi.py` for
numerical verification of its properties).

**The attractor scenario [CONJECTURE]:**

1. **Initial condition:** At the Big Bang, ψ(x, t=0) is in a generic (chaotic / thermal) state.
2. **Evolution:** The drift-diffusion equation drives ψ toward stable fixed points.
3. **Attractors:** The stable fixed points are located at ψ_p = 2πk/p for prime p
   (Prime Attractor Theorem — see `tests/test_prime_attractor_stability.py`).
4. **Our universe:** The system relaxes to p = 137, giving α⁻¹ ≈ 137.

---

## 2. Classical vs. Quantum Relaxation

**Question:** Is the relaxation ψ → ψ_p classical or quantum?

### Classical relaxation [CONJECTURE]
If ψ is a classical field, it relaxes via:
- **Diffusion:** Random initial fluctuations spread out on scale L
- **Drift:** V'(ψ) ≠ 0 drives ψ toward the nearest minimum

Relaxation timescale (dimensional estimate):

    τ_relax ~ L² / D

where:
- L = characteristic spatial scale at which ψ is correlated
- D = diffusion coefficient in phase space

**Cosmological constraint:** τ_relax must be ≤ Planck time to reach attractor
before Standard Model physics begins, OR the attractor must already be pre-selected
by quantum effects.

### Quantum relaxation [CONJECTURE]
If ψ is quantized, the initial state may be a superposition of attractors:

    |ψ⟩ = Σ_p c_p |ψ_p⟩

Decoherence by coupling to standard matter selects one branch. The probability
of each prime p is |c_p|² which must be determined from the cosmological initial
conditions.

**Open question:** Which relaxation mechanism is operative in UBT? This requires
knowing the Hilbert space structure of H_UBT and the decoherence rate.

---

## 3. The Measure Problem

If there are infinitely many prime attractors, what determines which prime
our universe lands on?

**Option A: Anthropic selection**

Only primes near 137 allow stable chemistry:
- If p ≪ 137: α ≫ 1/137, electromagnetic forces too strong → no stable atoms
- If p ≫ 137: α ≪ 1/137, electromagnetic forces too weak → no chemistry
- "Anthropic window": primes p ∈ [p_min, p_max] compatible with observers

*Status:* [CONJECTURE] — requires detailed nuclear/chemical stability analysis.

**Option B: Dynamical selection**

The drift-diffusion flow starting from a specific cosmological initial condition
selects a specific prime. The initial condition is set by the Planck-scale physics.

*Status:* [CONJECTURE] — requires solving the full cosmological attractor problem.

**Option C: Quantum superposition + decoherence**

The initial quantum state |ψ⟩ = Σ_p c_p|ψ_p⟩ evolves unitarily until coupling
to matter causes decoherence. The observed prime is then a quantum measurement outcome.

*Status:* [CONJECTURE] — compatible with UBT structure but requires quantum formalism.

**Working hypothesis:** Options A and B are both operative (anthropic + dynamical),
with the anthropic window filtering primes near 137 and the dynamics selecting
the specific prime within the window.

---

## 4. Stability Basin Around n = 137

**Definition [CONJECTURE]:**

The stability basin B_p is the set of initial ψ-values that flow to the
prime attractor ψ_p under the drift-diffusion equation.

For a potential V(ψ) = Σ_p (1/p)·(1 - cos(p·ψ)):

    B_137 = { ψ : |ψ - ψ_137| < δ_137 }  (first approximation)

where δ_137 is the half-width of the basin around ψ_137 = 2π/137.

**Estimate:** The basin width depends on the potential curvature at the minimum:

    δ_137 ~ 1/√(V''(ψ_137)) = 1/√(Σ_p p · Vp · cos(p·ψ_137))

For large p = 137, V''(ψ_137) ~ 137/137 = 1, so δ_137 ~ O(1).
The basin of p = 139 is located at ψ_139 = 2π/139 ≈ 0.04524 rad,
only 0.0006 rad away from ψ_137 ≈ 0.04588 rad.

**Key question:** Are the basins of p = 131, 137, 139 overlapping or separated?
This requires numerical integration of the drift-diffusion flow (computationally
accessible once V(ψ) is fully derived from the action principle — Task 1).

---

## 5. Falsifiability Statement

**Prediction 1: CMB multipole signature [CONJECTURE]**

If the prime attractor scenario is correct and ψ has a spatial correlation
length L_ψ at recombination, then CMB temperature fluctuations should show
enhanced power at multipole:

    ℓ ~ π · r_last / L_ψ

where r_last is the comoving distance to the last-scattering surface (~14 Gpc).

For ℓ ~ 137: L_ψ ~ π · 14 Gpc / 137 ~ 320 Mpc.

*Current status:* Forensic fingerprint null result — no statistically significant
excess at ℓ = 137 (see `forensic_fingerprint/` for analysis tools). This is
consistent with L_ψ > Hubble radius (ψ is homogeneous at recombination) or
with ψ not coupling to photon temperature.

**Prediction 2: Variation of α at early times [CONJECTURE]**

If ψ relaxes to its attractor during a cosmological phase transition, α may
have been different before relaxation. Detection: 21-cm hydrogen line at
high redshift (z ~ 100) could probe α at early times.

**Prediction 3: Discrete spectrum in CMB non-Gaussianity [CONJECTURE]**

The prime structure of V(ψ) could imprint a discrete spectrum in the
bispectrum B(ℓ₁, ℓ₂, ℓ₃) at configurations related to primes.
Specific prediction requires full V(ψ) derivation (Task 1, blocked).

---

## 6. Connection to the Phase-Frame Moduli Space

From `docs/PHI_UNIVERSE_PARAMETER.md`:
- The phase parameter φ ∈ U(1) labels different GR universes within UBT.
- The prime attractor selects discrete values φ_p = 2π/p.
- The cosmological scenario connects these: ψ relaxes → selects p → selects φ_p.

The full chain is:

    {Cosmological initial conditions}
           ↓  [drift-diffusion on ψ-field]
    {Prime attractor p selected}
           ↓  [τ = t + iψ_p maps to phase-frame φ_p]
    {Specific GR universe g^(φ_p)_μν realized}
           ↓  [projection → Standard Model couplings]
    {Observed physics: α = 1/(137+...), m_e, etc.}

---

## 7. Relaxation Time Estimate

For the drift-diffusion equation ∂_t ψ = D·∇²ψ - α·V'(ψ):

The homogeneous relaxation time (ignoring diffusion) is:

    τ_drift ~ 1 / (α · V''(ψ_p))

where V''(ψ_p) = Σ_q q² · Vq · cos(q · ψ_p) ≈ Σ_q q/q · cos(q·2π/p) = Σ_q cos(2πq/p).

For the Fourier sum, this is a Gauss sum: Σ_{q≤Q} cos(2πq/p) ~ p/2 (Dirichlet).

So τ_drift ~ 2 / (α_drift · p) where α_drift is the drift coefficient.

For our universe (p = 137) to have relaxed before Big Bang nucleosynthesis
(t_BBN ~ 1 s): τ_drift ≤ t_Planck ~ 5 × 10⁻⁴⁴ s.

This requires α_drift ≥ 2 / (137 · t_Planck) ~ 3 × 10⁴¹ s⁻¹,
a Planck-scale drift rate, consistent with the expectation that ψ-dynamics
operates at Planck scales.

---

## 8. Open Problems

1. **Derive V(ψ) from S[Θ]** — blocks all quantitative predictions (Task 1).
2. **Compute τ_relax** exactly using the derived V(ψ).
3. **Map stability basins** B_p numerically for primes near p = 137.
4. **Determine quantum vs. classical** relaxation mechanism.
5. **Link to inflation** — does the ψ-attractor operate during or after inflation?

---

## References

- `Appendix_H_Theta_Phase_Emergence.tex` — Phase dynamics
- `ubt_core/verify_Vpsi.py` — V(ψ) numerical verification
- `tests/test_prime_attractor_stability.py` — Prime attractor evidence
- `docs/PHI_UNIVERSE_PARAMETER.md` — Phase-frame moduli space
- `forensic_fingerprint/` — CMB analysis tools
