<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Alpha Spectral Relation Candidates

**Version:** v28 (UBT_v28_cosmo_hecke_neff)  
**Date:** 2026-03-06  
**Inputs:** `alpha_core_repro/`, `quantization_grid/`, `automorphic/hecke_l_route.py`  
**Status:** Layer 2 research — no curve fitting; geometric/spectral quantities only  
**Constraint:** FORBID_NUMERIC_FITTING — only geometric or spectral quantities allowed  

---

## 1. Purpose

Search for relations between the eigenvalue spectrum of the Θ-field operator
on T²(τ) and the fine structure constant α ≈ 1/137.036.

**Methodology:**
- Analyse spectral spacing of torus eigenvalues
- Test integer topological invariants
- Evaluate determinant of theta operator
- All candidates must arise from geometry alone — NO parameter fitting

---

## 2. Candidate 1: Spectral Counting Function

### 2.1 Setup

The number of torus eigenvalues below a cutoff Λ (Weyl asymptotics):

    N(Λ) ~ (L / 2π)^d × V_d × Λ^{d/2}

For d = 2 (T²) with unit period L = 1:

    N(Λ) ~ (1/4π) × Λ

**Candidate:** The value of Λ such that N(Λ) = 137 / (4π) gives
a spectral measure of α.

### 2.2 Numerical Evaluation

Setting N(Λ_α) = 1/(4πα) in the Weyl formula for d = 2, unit torus:

    Λ_α = 4π × N_α / (1 / (2π)²) = N_α

This is circular (Weyl formula just inverts N), so the counting function
approach does not yield a geometric α.

**Status:** ❌ Not a valid candidate (no geometric content beyond definition).

---

## 3. Candidate 2: Spectral Determinant

### 3.1 Zeta-Regularised Determinant

The spectral zeta function of the Laplacian on T^d:

    ζ_T(s) = Σ_{k≠0}  λ_k^{-s}   (Epstein zeta function)

The regularised determinant:

    log det'(-Δ) = -ζ'_T(0)

For the 2-torus with modular parameter τ:

    log det'(-Δ_{T²(τ)}) = -4π Im(τ) + log |η(τ)|^4 + const

where η(τ) is the Dedekind eta function.

### 3.2 Evaluation at τ = i

At τ = i (square torus R_t = R_ψ):

    η(i) = Γ(1/4) / (2π^{3/4})   (known closed form)

    |η(i)|^4 = [Γ(1/4)/(2π^{3/4})]^4 ≈ 0.00027

    log det' = -4π + log(0.00027) + const

This is a well-defined geometric quantity but does not directly equal α.

**Status:** ⚠️ Geometric quantity confirmed, but connection to α not
established without additional structure.

---

## 4. Candidate 3: Spectral Gap Ratio

### 4.1 Setup

The ratio of the second eigenvalue to the first massive eigenvalue:

    r = λ₁ / λ_gap = 4.0 / 1.0 = 4   (2D torus: second level has λ=2, no — let me check)

From the 2D spectrum:
- λ_0 = 0, λ_1 = 1, λ_2 = 2, λ_3 = 4, λ_4 = 5 ...

    spectral_gap = 1.0 (normalised)
    λ₂ / λ₁ = 2.0

**No direct α connection** from raw spectral ratios.

**Status:** ❌ Spectral ratios are small integers; no α-like quantity emerges.

---

## 5. Candidate 4: Theta Determinant via Dedekind η

### 5.1 Dedekind η Function

The Dedekind eta:

    η(τ) = q^{1/24} Π_{n=1}^∞ (1 - q^n),   q = e^{2πiτ}

At τ = i: η(i) = Γ(1/4)^{3/2} / (2 π^{9/8})   (up to known factors)

Numerically: |η(i)| ≈ 0.76823...

### 5.2 The B₁ Coefficient Connection

From `ubt_with_chronofactor/scripts/torus_theta_alpha_verification.wls`,
the Dedekind-η value enters the torus/theta mechanism for α:

    α^{-1} = 4π(A₀ + N_eff · B₁)
    B₁ = (value fixed by η(i))

The coefficient B₁ is determined by the geometry of the torus
(η(i) is a pure geometric quantity).  This provides a **spectral input**
to the α formula.

**Candidate:** B₁ from η(i) contributes to α via the one-loop running
of the gauge coupling on T²(τ = i).

**Status:** ✅ GEOMETRIC — B₁ is fixed by η(i) with no fitting.
However, A₀ still has a model-dependent piece.

---

## 6. Candidate 5: Eisenstein Series E₂ at τ = i

### 6.1 Setup

The Eisenstein series:

    E₂(τ) = 1 - 24 Σ_{n=1}^∞ σ₁(n) q^n,   q = e^{2πiτ}

At τ = i: E₂(i) = 3/π (known result from modular forms).

**Candidate:** The ratio

    E₂(i) = 3/π ≈ 0.9549...

does not directly give α, but enters the one-loop effective action for
the gauge coupling on T².  The combination

    (E₂(i) - 1) / 24 = (3/π - 1) / 24 ≈ -0.00188

is a pure geometric correction to the gauge coupling.

**Status:** ✅ GEOMETRIC — E₂(i) is known analytically.  Connection
to α requires a full one-loop calculation which remains open.

---

## 7. Candidate 6: Integer Topological Invariant

### 7.1 Winding Number

On T² the winding number w = (w_t, w_ψ) ∈ Z² labels topological sectors.
The sector with (w_t, w_ψ) = (0,0) is topologically trivial; non-zero
winding sectors are topological defects of the Θ field.

**Candidate:** The total number of topologically distinct sectors up to
mass M is counted by:

    N_sectors(M) = #{(n_t, n_ψ) : n_t² + n_ψ² ≤ (M R_ψ)²}

This is a purely geometric integer.  Setting N_sectors ≈ 137 would
require M R_ψ ≈ √137 ≈ 11.7.

**Status:** ⚠️ Geometric integer, but the choice M R_ψ = √137 has no
independent motivation.

---

## 8. Summary of Candidates

| Candidate | Geometric? | α-connection | Status |
|-----------|-----------|--------------|--------|
| Spectral counting N(Λ) | ✅ | Circular | ❌ |
| Spectral determinant log det' | ✅ | Indirect via η | ⚠️ |
| Spectral gap ratio | ✅ | None | ❌ |
| Dedekind η(i) → B₁ | ✅ | Enters α formula | ✅ (partial) |
| Eisenstein E₂(i) = 3/π | ✅ | One-loop correction | ✅ (partial) |
| Integer winding N_sectors ≈ 137 | ✅ | Requires motivation | ⚠️ |

**Best candidates:** η(i) and E₂(i) are the strongest geometric
spectral quantities that connect to α via the one-loop effective action.

---

## 9. Next Steps

1. Compute the full one-loop gauge coupling renormalisation on T²(τ = i)
   in terms of η(i) and E₂(i) — this would give a pure-geometry formula
   for A₀ in α^{-1} = 4π(A₀ + N_eff B₁).

2. Evaluate whether the determinant of the Dirac operator on T² produces
   α or its inverse directly.

3. Investigate the L-function L(ϑ₃, s) at s = 3/2 (where it reduces to
   L(χ₋₄, 3/2)) for a possible spectral α connection.

4. Test the Selberg zeta function of the hyperbolic surface associated to
   Γ₀(4) for eigenvalue sequences near 1/137.

---

## 10. Conclusion

**No direct spectral derivation of α has been found** using only geometric
quantities from the torus eigenvalue spectrum.  The closest candidates
are:
- **η(i)**: fixes B₁ in the α formula (purely geometric)
- **E₂(i) = 3/π**: one-loop correction (purely geometric)

These are **necessary inputs** to any spectral α formula but are not
alone sufficient.  A complete derivation would also require the
regularisation constant A₀ from first principles.

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
