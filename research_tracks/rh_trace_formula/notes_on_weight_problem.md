<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Notes on the Modular Weight Problem

**Track**: research_tracks/rh_trace_formula  
**Status**: Analysis only; obstruction identified  
**Author**: Ing. David Jaroš  

---

## 1. The Problem in One Sentence

The full UBT theta function θ₃³ has modular weight **3/2**, whereas the
Riemann zeta function ζ(s) has a functional equation centered at Re(s) = ½
corresponding to modular weight **1/2**.  The two weights do not match, so
**θ₃³ cannot be naively identified with ζ(s)**.

---

## 2. Modular Weights: Definitions

A **modular form of weight k** for a congruence subgroup Γ ⊂ SL₂(ℤ) is a
holomorphic function f : ℍ → ℂ satisfying

```
f( (aτ+b)/(cτ+d) )  =  (cτ+d)^k  f(τ)    for all [[a,b],[c,d]] ∈ Γ.
```

Under the specific transformation τ ↦ −1/τ (the S-transformation):

```
f(−1/τ)  =  τ^k  f(τ).
```

Setting τ = it (t > 0 real):

```
f(i/t)  =  (it)^k  f(it)  =  i^k  t^k  f(it).
```

---

## 3. Individual Theta Functions and Their Weights

### 3.1 θ₃ (weight 1/2)

The Jacobi theta function

```
θ₃(τ)  =  Σ_{n ∈ ℤ}  e^{iπn²τ}
```

transforms as

```
θ₃(−1/τ)  =  (−iτ)^{1/2}  θ₃(τ)
```

i.e. θ₃ is a **modular form of weight 1/2** for Γ₀(4) (with a character).
Setting τ = it:

```
θ₃(i/t)  =  t^{1/2}  θ₃(it).
```

This is the **Jacobi identity** and is the basis of the standard θ → ζ bridge.

### 3.2 The Mellin Transform of θ₃ Gives ξ(s)

From the Jacobi identity one derives (see `ubt_hamiltonian_trace_formula.md`,
Theorem 3.2):

```
ξ(s)  =  π^{−s/2} Γ(s/2) ζ(s)  =  ½ ∫₀^∞ [θ₃(it)−1] t^{s/2} dt/t
```

The **functional equation ξ(s) = ξ(1−s)** follows directly from the
Jacobi identity θ₃(i/t) = t^{1/2} θ₃(it) and the substitution t ↦ 1/t.

The **centering at Re(s) = 1/2** in the functional equation is a direct
consequence of the **weight 1/2** of θ₃.

---

## 4. The Three-Sector UBT Theta Function θ₃³

In the 3-dimensional UBT formulation, the full theta sum over the T3 sector
involves three ψ-directions, giving

```
Θ_{T3}(τ)  =  θ₃(τ)³  =  Σ_{(n₁,n₂,n₃) ∈ ℤ³}  e^{iπ(n₁²+n₂²+n₃²)τ}
```

### 4.1 Modular Weight of θ₃³

Since θ₃ has weight 1/2, and modular weights are **additive under products**:

```
weight(θ₃³)  =  3 × (1/2)  =  3/2.
```

The transformation law is:

```
θ₃(i/t)³  =  t^{3/2}  θ₃(it)³.
```

### 4.2 What Functional Equation Would θ₃³ Give?

Define the Mellin transform of θ₃³:

```
Z_{T3}(s)  =  ∫₀^∞  [θ₃(it)³ − 1]  t^{s/2}  dt/t.
```

Splitting at t = 1 and substituting t ↦ 1/t in the [0,1] piece, using
θ₃(i/t)³ = t^{3/2} θ₃(it)³:

```
Z_{T3}(s)  =  Z_{T3}(3 − s).
```

The functional equation is centered at **Re(s) = 3/2**, not 1/2.

This corresponds to the **completed Epstein zeta function** of the 3D
integer lattice ℤ³:

```
Z_{T3}(s)  ∝  π^{−s/2} Γ(s/2) Z_{Epstein}(ℤ³, s)
```

where Z_{Epstein}(ℤ³, s) = Σ_{(n₁,n₂,n₃)≠(0,0,0)} (n₁²+n₂²+n₃²)^{−s/2}.

**Z_{Epstein}(ℤ³, s) is NOT equal to ζ(s).**

---

## 5. The Obstruction: A Precise Statement

**Lemma 5.1** (Weight obstruction).

Let f(τ) be a modular form of weight k for a congruence subgroup.  If

```
ξ_f(s)  :=  ∫₀^∞  [f(it) − f(i∞)]  t^{s/2}  dt/t
```

satisfies a functional equation ξ_f(s) = ±ξ_f(c − s) for some c ∈ ℝ,
then **c = k**, i.e. the functional equation is centered at Re(s) = k/2.

**Corollary 5.2**.

- θ₃ (weight 1/2): functional equation centered at s = 1/2. ✓ Matches ζ(s).
- θ₃² (weight 1): functional equation centered at s = 1. Does not match ζ(s).
- θ₃³ (weight 3/2): functional equation centered at s = 3/2. Does not match ζ(s).

**Conclusion**: The **full T3 sector** of UBT, involving θ₃³, **cannot be
naively identified with ζ(s)**.

---

## 6. Resolution: The 1D ψ-Subsector

The resolution is to use **one** ψ-direction rather than all three.

**Observation 6.1**.

The 1D Hamiltonian H_ψ = −d²/dψ² + V_eff(ψ) on L²(S¹_ψ) has a heat trace

```
Z_H(t)  =  Tr[e^{−t H_ψ}]
```

which, at leading order (V_eff = 0), equals

```
Z_H(t)  ∼  θ₃(it L_ψ²/(4π))
```

which is a **weight 1/2** theta function.  Its Mellin transform yields a
functional equation centered at s = 1/2, compatible with ζ(s).

**This is the correct subsector to use.**  The T3 full sector must be
projected onto the 1D subsector before any ζ-link is attempted.

---

## 7. Alternative Routes: Quotient or Projection

If one insists on working with all three ψ-directions, two approaches
are conceivable (both currently unproved):

### 7.1 Quotient Construction

Define an equivalence relation on the T3 spectrum that identifies eigenvalues
related by the SO(3) symmetry of the ℤ³ lattice, reducing to a 1D spectrum.
The resulting quotient Hamiltonian would need to have weight 1/2.

**Status**: No such construction has been defined or proved within UBT.

### 7.2 Projection Construction

Project onto a distinguished 1D sublattice, e.g. the ψ₁-axis:

```
π : ℤ³ → ℤ,    (n₁, n₂, n₃) ↦ n₁
```

The projected heat trace recovers θ₃(it) × (multiplicity from π²,π³ directions).
The multiplicity factor introduces G(s) (see Conjecture 4.2 in the main document).

**Status**: This is the most natural route, but the multiplicity factor
must be computed precisely and shown not to introduce zeros on the
critical strip (Gap G5).

---

## 8. Summary of Constraints

| Sector | Weight | Functional eq. center | Compatible with ζ? |
|--------|--------|-----------------------|--------------------|
| θ₃ (1D ψ-sector) | 1/2 | s = 1/2 | ✓ Yes (at leading order) |
| θ₃² (2D ψ-sector) | 1 | s = 1 | ✗ No |
| θ₃³ (full T3 sector) | 3/2 | s = 3/2 | ✗ No |
| Quotient of T3 | ? | ? | Unknown; requires construction |
| Projection of T3 to 1D | 1/2 (leading) | 1/2 (leading) | Potentially yes; G(s) must be controlled |

---

## 9. Consequences for the Research Programme

1. **The ζ-link, if it exists, must use the 1D ψ-subsector or a carefully
   constructed projection.**  Working with θ₃³ directly leads to Epstein
   zeta, not Riemann zeta.

2. **The correction factor G(s)** in Conjecture 4.2 of the main document
   partially arises from the weight discrepancy: matching the 1D subsector
   to the full T3 sector introduces extra factors that must be controlled.

3. **Any candidate proof strategy that starts with the full T3 theta function**
   and claims to arrive at ζ(s) without an explicit projection/quotient step
   and a nonvanishing argument for G(s) is **incomplete**.

---

## 10. References

- Jacobi, C. G. J. (1829). *Fundamenta nova theoriae functionum ellipticarum*.
- Serre, J.-P. (1973). *A Course in Arithmetic*, Ch. VII (modular forms and
  theta series).
- Zagier, D. (2008). *Elliptic Modular Forms and Their Applications*. In:
  1-2-3 of Modular Forms, Springer.
- Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*, §2.4.
- Epstein, P. (1903). *Zur Theorie allgemeiner Zetafunktionen*, Math. Ann. 56.

---

**Last Updated**: 2026-05-04
