# Phase Special Values: Invariant Analysis at φ ∈ {0, π/4, π/2, π}
## Checking the Speciality of φ = π/4 in the UBT Field Θ

**Status:** [DERIVED] for algebraic identities; [HYPOTHESIS] for dynamical interpretation  
**Layer:** [L1] — biquaternionic scalar geometry  
**Task:** STEP — CHECK φ = π/4 SPECIALITY  
**Author:** Ing. David Jaroš  
**Sources:**
- Scalar decomposition: `unified_biquaternion_theory/solution_scalar_equation_P1/solution_scalar_equation_P1.tex`
- Phase projection: `canonical/geometry/phi_gauge_vs_physical.tex`
- Entropic invariants: `consolidation_project/appendix_N3_entropic_full_derivation.tex`

---

## 1. Field Decomposition: Where Θ Splits into Amplitude and Phase

### 1.1 Scalar polar decomposition (P1 constraint equation)

From `solution_scalar_equation_P1.tex §2`, the UBT scalar field is written in
polar form as:

    Θ = ρ(q) · exp(iφ(q)),    ρ ∈ ℝ⁺,  φ ∈ ℝ

where ρ is the real amplitude and φ is the local phase.  This is the starting
point for all invariant calculations below.

### 1.2 Hermitian / anti-Hermitian decomposition

The polar form induces a canonical split of Θ into its Hermitian (H) and
anti-Hermitian (A) parts.  For the scalar field with Θ† = Θ* = ρ·exp(−iφ):

    H  = (Θ + Θ†)/2   = ρ cos φ          [Hermitian / real part]
    iA = (Θ − Θ†)/2   = iρ sin φ
    A  = ρ sin φ                           [anti-Hermitian amplitude]

So that Θ = H + iA = ρ cos φ + i ρ sin φ.

For the matrix (n×n) case Θ = ρ exp(iφ) · Iₙ, the same formulae hold
component-wise with all scalars promoted to multiples of the identity.

### 1.3 Phase-frame projection (biquaternionic metric)

From `canonical/geometry/phi_gauge_vs_physical.tex §2–3`, the biquaternionic
metric 𝒰_μν = g_μν + i h_μν projects under a U(1) phase rotation as:

    P_φ[𝒰_μν] = cos φ · g_μν + sin φ · h_μν     [DERIVED, eq. proj_result]

The coupling strength (fine-structure constant analogue) becomes:

    α(φ) = α(0) [cos²φ + 2ρᵣ r cos φ sin φ + r² sin²φ]

where r = |𝒜^I|/|𝒜^R| is the imaginary-to-real gauge-field amplitude ratio and
ρᵣ is their correlation coefficient.

---

## 2. Invariants That Depend Explicitly on φ

The following invariants of Θ = ρ exp(iφ) all carry explicit φ-dependence:

| # | Invariant | Expression | Notes |
|---|-----------|------------|-------|
| 1 | Re(Θ) | ρ cos φ | real / Hermitian sector |
| 2 | Im(Θ) | ρ sin φ | imaginary / anti-Hermitian sector |
| 3 | Θ² | ρ² exp(2iφ) | quadratic field |
| 4 | Re(Θ²) | ρ² cos(2φ) | **key invariant** — see §3 |
| 5 | Im(Θ²) | ρ² sin(2φ) | **key invariant** — see §3 |
| 6 | \|H\|² − \|A\|² | ρ²(cos²φ − sin²φ) = ρ² cos(2φ) | sector imbalance |
| 7 | H·A cross-term | ρ² cos φ sin φ = (ρ²/2) sin(2φ) | inter-sector mixing |
| 8 | arg(det Θ) | n φ  (mod 2π) | n = matrix dimension |
| 9 | Im(log det Θ) | n φ | phase entropy (Im(𝒮)) |
| 10 | P_φ metric | cos φ · g_μν + sin φ · h_μν | projection for GR recovery |
| 11 | α(φ) | see §1.3 | cross-term peaks at φ = π/4 |

The following invariants are **independent of φ** (depend only on ρ):

- \|det Θ\| = ρⁿ
- Re(log det Θ) = n log ρ
- Real entropy S = 2kB log\|det Θ\| = 2n kB log ρ
- Tr(Θ†Θ) = n ρ²

---

## 3. Evaluation at φ ∈ {0, π/4, π/2, π}

### Trigonometric keys

| φ | cos φ | sin φ | cos(2φ) | sin(2φ) |
|---|-------|-------|---------|---------|
| 0 | 1 | 0 | 1 | 0 |
| π/4 | 1/√2 | 1/√2 | **0** | **1** |
| π/2 | 0 | 1 | −1 | 0 |
| π | −1 | 0 | 1 | 0 |

### Main invariant table (scalar case, n = 1)

| Invariant | φ = 0 | φ = π/4 | φ = π/2 | φ = π |
|-----------|-------|---------|---------|-------|
| H = Re(Θ) | ρ | ρ/√2 | 0 | −ρ |
| A = Im(Θ) | 0 | ρ/√2 | ρ | 0 |
| \|H\|² | ρ² | ρ²/2 | 0 | ρ² |
| \|A\|² | 0 | ρ²/2 | ρ² | 0 |
| \|H\|²−\|A\|² | ρ² | **0** | −ρ² | ρ² |
| Re(Θ²) | ρ² | **0** | −ρ² | ρ² |
| Im(Θ²) | 0 | **ρ²** ← max | 0 | 0 |
| H·A | 0 | **ρ²/2** ← max | 0 | 0 |
| det Θ | ρ | ρ exp(iπ/4) | iρ | −ρ |
| \|det Θ\| | ρ | ρ | ρ | ρ |
| arg(det Θ) | 0 | π/4 | π/2 | π |
| Re(log det Θ) | log ρ | log ρ | log ρ | log ρ |
| Im(log det Θ) | 0 | π/4 | π/2 | π |
| S = 2kB log\|det Θ\| | 2kB log ρ | 2kB log ρ | 2kB log ρ | 2kB log ρ |

### Extended table for 4×4 matrix Θ = ρ exp(iφ) · I₄

| Invariant | φ = 0 | φ = π/4 | φ = π/2 | φ = π |
|-----------|-------|---------|---------|-------|
| det Θ | ρ⁴ | ρ⁴ exp(iπ) = **−ρ⁴** | ρ⁴ exp(2πi) = ρ⁴ | ρ⁴ exp(4πi) = ρ⁴ |
| arg(det Θ) | 0 | **π** (arg reaches branch cut) | 2π ≡ 0 | 4π ≡ 0 |
| Im(log det Θ) | 0 | **π** | 0 (or 2π) | 0 (or 4π) |
| Re(Θ²) · I₄ | ρ²·I₄ | **0** | −ρ²·I₄ | ρ²·I₄ |
| Tr(Re Θ²) | 4ρ² | **0** | −4ρ² | 4ρ² |

> **Note on n=4:** For the physical 4×4 UBT matrix, φ = π/4 maps det Θ to the
> **negative real axis** (arg = π).  This is the principal branch cut of log(z).
> If the theory uses the principal branch of log, the phase entropy
> Im(𝒮) = kB arg(det Θ) has a **discontinuity** as φ crosses π/4 from below.

### Fine-structure coupling (phase-projection case)

From `canonical/geometry/phi_gauge_vs_physical.tex §3`, with r = ratio of
imaginary to real gauge amplitudes and ρᵣ = their correlation:

| φ | α(φ) / α(0) | d α/d φ / α(0) |
|---|-------------|----------------|
| 0 | 1 | 2ρᵣ r |
| π/4 | (1+r²)/2 + ρᵣ r | r²−1 |
| π/2 | r² | −2ρᵣ r |
| π | 1 | 2ρᵣ r |

Special sub-case **r = 1** (equal imaginary and real gauge amplitudes):

| φ | α(φ) / α(0) | d α/d φ / α(0) | d²α/dφ² / α(0) |
|---|-------------|----------------|-----------------|
| 0 | 1 | 2ρᵣ | 0 |
| π/4 | 1 + ρᵣ | **0** ← critical point | −4ρᵣ |
| π/2 | 1 | −2ρᵣ | 0 |
| π | 1 | 2ρᵣ | 0 |

When r = 1, φ = π/4 is an **extremum** of α(φ):
- A **maximum** of α(φ) when ρᵣ > 0 (d²α/dφ² < 0)
- A **minimum** of α(φ) when ρᵣ < 0 (d²α/dφ² > 0)

---

## 4. Summary of What φ = π/4 Causes

| Effect | Invariant | Behaviour at φ = π/4 | Mechanism |
|--------|-----------|----------------------|-----------|
| **Term vanishes** | Re(Θ²) | = 0 | cos(2φ) = 0 |
| **Term vanishes** | \|H\|²−\|A\|² | = 0 | cos(2φ) = 0 |
| **Term vanishes** | Tr(Re Θ²) (n=4) | = 0 | cos(2φ) = 0 |
| **Maximum** | Im(Θ²) | = ρ² | sin(2φ) = 1 |
| **Maximum** | H·A cross-term | = ρ²/2 | sin(2φ) = 1 |
| **Maximum** | α(φ) cross-term | = ρᵣ r α(0) | sin(2φ) = 1 |
| **Extremum of α** | α(φ) | critical point (max if ρᵣ>0, min if ρᵣ<0) | r = 1, see §3 |
| **Equal partition** | \|H\|² = \|A\|² | = ρ²/2 each | cos(2φ) = 0 |
| **Branch-cut crossing** | arg(det Θ) n=4 | = π (negative real det) | 4φ = π |

---

## 5. Stability Analysis

### 5.1 Potential dynamics: V(φ) ∝ Re(Θ²)

If the effective potential depends on the real part of the squared field,

    V(φ) = −λ ρ² cos(2φ),    λ > 0

then the equation of motion is:

    dφ/dt ∝ −dV/dφ = −2λ ρ² sin(2φ)

**Fixed points** (dφ/dt = 0): sin(2φ) = 0 → φ* ∈ {0, π/2, π, 3π/2, …}

**Stability of fixed points** (d²V/dφ²):

    d²V/dφ² = 4λ ρ² cos(2φ)

| φ* | d²V/dφ² | Stability |
|----|---------|-----------|
| 0 | 4λρ² > 0 | **Stable attractor** (V minimum) |
| π/2 | −4λρ² < 0 | **Unstable repellor** (V maximum) |
| π | 4λρ² > 0 | **Stable attractor** (V minimum) |

**φ = π/4 is not a fixed point** of this potential.  It is a **zero-crossing
of V** (V = 0 there) and an **inflection point of dV/dφ** (the driving force
sin(2φ) is at its maximum).  Trajectories passing through φ = π/4 are driven
most strongly toward the attractor at φ = 0 or φ = π.

### 5.2 Cross-sector dynamics: Im(Θ²) coupling

If the imaginary cross-sector term Im(Θ²) = ρ² sin(2φ) enters the action (e.g.,
as a mixing term between real and imaginary gauge sectors), then φ = π/4 is the
point of **maximum inter-sector coupling**.  A second-order phase transition
(bifurcation) can occur if the coupling exceeds a critical threshold:

- For φ < π/4: |H|² > |A|² (Hermitian sector dominates)
- At φ = π/4: |H|² = |A|² (critical balance — saddle point between sectors)
- For φ > π/4: |H|² < |A|² (anti-Hermitian sector dominates)

### 5.3 Branch-cut crossing (n = 4 matrix)

For the 4×4 UBT field, arg(det Θ) = 4φ crosses the principal branch cut at
arg = π when **φ = π/4**.  This causes:

- A discontinuity in Im(log det Θ) = Im(𝒮)/kB if the principal branch is used
- A **winding number change** by 1 in the complex logarithm
- Potentially observable as a topological phase transition in the determinant map

This discontinuity is an artefact of the branch-cut convention; physical
observables constructed from |det Θ| = ρ⁴ remain smooth.

### 5.4 Stability conclusion

| φ | Role under V ~ Re(Θ²) | Role in cross-sector coupling |
|---|----------------------|------------------------------|
| 0 | **Stable attractor** | Decoupled (Im(Θ²) = 0) |
| π/4 | **Zero-crossing / transition point** | **Maximum coupling** (saddle between sectors) |
| π/2 | **Unstable repellor** | Decoupled (Im(Θ²) = 0) |
| π | **Stable attractor** | Decoupled (Im(Θ²) = 0) |

> **Primary conclusion:** φ = π/4 is distinguished by three simultaneous
> conditions: (a) Re(Θ²) = 0 (the real quadratic term vanishes), (b) Im(Θ²)
> is at its global maximum (purely imaginary quadratic term), and (c) the
> Hermitian and anti-Hermitian sectors carry equal weight.  It is not a
> dynamical attractor for potentials linear in Re(Θ²), but it is the maximum-
> coupling saddle point between the two sectors, making it a natural
> **bifurcation locus** if the inter-sector coupling drives the dynamics.

---

## 6. Cross-references

| Topic | File |
|-------|------|
| Scalar decomposition Θ = ρe^{iφ} | `unified_biquaternion_theory/solution_scalar_equation_P1/solution_scalar_equation_P1.tex §2` |
| Phase projection P_φ and α(φ) derivation | `canonical/geometry/phi_gauge_vs_physical.tex` |
| log det Θ and entropy | `consolidation_project/appendix_N3_entropic_full_derivation.tex` |
| φ as universe selector (moduli space) | `docs/PHI_UNIVERSE_PARAMETER.md` |
| Cosmological attractor at φ* | `docs/COSMOLOGICAL_ATTRACTOR_SCENARIO.md` |

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
