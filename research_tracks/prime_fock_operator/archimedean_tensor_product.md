<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Archimedean Sector and Tensor-Product Structure

**Track**: research_tracks/prime_fock_operator  
**Status**: Open (archimedean sector established; UBT embedding of full tensor product open)  
**Author**: Ing. David Jaroš  

---

> ⚠️ **Claim Control**  
> The partition function identity Z_total(t) = θ(t)^d · ζ(t) is a formal
> product of two established identities.  It does **not** prove RH and
> does **not** imply that the zeros of ζ arise from eigenvalues of either
> H_inf or H_prime.

---

## 1. Motivation

The Riemann zeta function admits a **factored analytic structure** inherited
from the adelic decomposition of ℚ:

```
ζ_completed(s)  =  π^{−s/2} Γ(s/2)  ×  ζ(s)
               =  Z_∞(s)             ×  Z_fin(s)
```

where Z_∞(s) = π^{−s/2} Γ(s/2) is the **archimedean (real-place) factor**
and Z_fin(s) = ζ(s) = Π_p (1−p^{−s})^{−1} is the **non-archimedean
(finite-place) factor** furnished by H_prime (see prime_fock_operator.md).

This document constructs the archimedean factor from the Hamiltonian
H_inf = −Δ on the d-torus T^d and combines both sectors into a total
Hamiltonian H_total = H_inf ⊗ I + I ⊗ H_prime.

---

## 2. The Archimedean Sector

### 2.1 The d-Torus and the Flat Laplacian

Let T^d = ℝ^d / ℤ^d be the standard d-dimensional flat torus.  Define

```
H_inf  =  −Δ_{T^d}
```

the (non-negative) Laplacian on L²(T^d) with periodic boundary conditions.

The eigenvalues of H_inf are

```
λ_k  =  4π² |k|²,    k = (k_1, …, k_d) ∈ ℤ^d
```

with eigenfunctions e^{2πi k·x}.  Each eigenvalue 4π²|k|² has multiplicity
equal to the number of lattice vectors k ∈ ℤ^d with |k|² = n (the
representation number r_d(n)).

### 2.2 The Heat Kernel of H_inf

**Theorem 2.1** (Heat kernel on T^d; standard).

The heat operator e^{−t H_inf} is trace-class for t > 0 with

```
Z_inf(t)  :=  Tr_{L²(T^d)}[ e^{−t H_inf} ]
           =  Σ_{k ∈ ℤ^d}  e^{−4π² |k|² t}
           =  θ_3(0 | it)^d
           =  θ(t)^d
```

where θ(t) := θ_3(0|it) = Σ_{n ∈ ℤ} e^{−4π² n² t} is the third Jacobi
theta function evaluated on the imaginary axis, and the d-th power reflects
the product structure T^d = (S¹)^d.

*Proof sketch*: Separate the d-dimensional sum into a product of d
one-dimensional sums:

```
Σ_{k ∈ ℤ^d}  e^{−4π² |k|² t}
    =  ( Σ_{n ∈ ℤ}  e^{−4π² n² t} )^d
    =  θ(t)^d.
```

Each one-dimensional factor is the standard theta-function heat trace on
S¹ = ℝ/ℤ. □

### 2.3 Jacobi Transformation

**Theorem 2.2** (Jacobi; modular transformation of θ).

```
θ(t)  =  t^{−1/2} θ(1/t),    t > 0.
```

Hence

```
Z_inf(t)  =  θ(t)^d  =  t^{−d/2} θ(1/t)^d  =  t^{−d/2} Z_inf(1/t).
```

This is the functional equation of Z_inf under t ↦ 1/t, reflecting
Poincaré duality on T^d.

### 2.4 Connection to the Gamma Factor

The Mellin transform of θ(t) − 1 produces the completed archimedean
zeta factor:

```
π^{−s/2} Γ(s/2)  =  ∫_0^∞  (θ(t) − 1)/2 · t^{s/2} dt/t,    Re(s) > 1.
```

For d > 1 the Mellin transform of θ(t)^d yields a product of Gamma functions
(the archimedean L-factor for the GL(d) automorphic form).

---

## 3. The Non-Archimedean Sector (H_prime)

The non-archimedean sector is defined in `prime_fock_operator.md`.  The key
identity recalled here for convenience:

```
Z_prime(s)  :=  Tr_F[ e^{−s H_prime} ]  =  ζ(s),    Re(s) > 1.
```

---

## 4. The Total Hamiltonian

### 4.1 Hilbert Space

Define the **total Hilbert space**

```
H_total  =  L²(T^d) ⊗ F
```

where L²(T^d) is the archimedean sector and F = ⊗_p l²(ℕ₀) is the prime
Fock space.

### 4.2 Total Hamiltonian

**Definition 4.1** (Total Hamiltonian).

```
H_total  =  H_inf ⊗ I_F  +  I_{L²(T^d)} ⊗ H_prime
```

where:
- H_inf = −Δ acts on the L²(T^d) factor,
- H_prime = Σ_p log(p) N_p acts on the F factor.

Both summands commute (they act on different tensor factors), so H_total is
a well-defined symmetric operator on the algebraic tensor product

```
D(H_total)  =  D(H_inf) ⊗_alg D(H_prime).
```

### 4.3 Spectrum of H_total

The eigenvalues of H_total are

```
E_{k,m}  =  λ_k  +  log(m)
           =  4π² |k|²  +  log(m),    k ∈ ℤ^d,  m ∈ ℕ.
```

Each pair (k, m) gives an independent energy state |k⟩ ⊗ |m⟩.

---

## 5. Total Partition Function

**Theorem 5.1** (Total partition function).

For real t > 0 with t > 1 (ensuring convergence of the zeta part):

```
Z_total(t)  :=  Tr_{H_total}[ e^{−t H_total} ]
             =  Tr_{L²(T^d)}[ e^{−t H_inf} ]  ×  Tr_F[ e^{−t H_prime} ]
             =  θ(t)^d  ×  ζ(t).
```

*Proof*:

The trace over a tensor product of commuting operators factorizes:

```
Tr_{A ⊗ B}[ e^{−t(H_A ⊗ I + I ⊗ H_B)} ]
    =  Tr_A[ e^{−t H_A} ]  ×  Tr_B[ e^{−t H_B} ].
```

This is standard functional analysis (applicable whenever both traces
converge absolutely, which holds here for t > 1 from the ζ(t) factor). □

### 5.1 Explicit Form

Substituting the eigenvalues:

```
Z_total(t)
    =  Σ_{k ∈ ℤ^d}  Σ_{m=1}^∞  exp(−t (4π² |k|² + log m))
    =  ( Σ_{k ∈ ℤ^d}  e^{−4π² t |k|²} ) · ( Σ_{m=1}^∞  m^{−t} )
    =  θ(t)^d · ζ(t).
```

### 5.2 Finite-Prime Approximation

For computational purposes, replace ζ(t) by the truncated product

```
ζ_P(t)  =  Π_{p ≤ P}  (1 − p^{−t})^{−1}  =  Z_P(t)
```

giving the total truncated partition function

```
Z_total,P(t)  =  θ(t)^d · ζ_P(t).
```

As P → ∞, Z_total,P(t) → Z_total(t) monotonically for t > 1.

---

## 6. The Functional Equation of Z_total

The individual factors satisfy:

```
θ(t)   =  t^{−1/2} θ(1/t)              (Jacobi)
ζ(t)   has an analytic continuation to ξ(t)/Γ(t/2)π^{t/2}  (Riemann)
```

The functional equation of ξ(s) = π^{−s/2} Γ(s/2) ζ(s) is ξ(s) = ξ(1−s).

No simple functional equation for Z_total(t) = θ(t)^d · ζ(t) as a whole
is known, because the domain of convergence of θ(t)^d (all t > 0) and
ζ(t) (t > 1) are different.  Extending Z_total to the critical strip
requires analytic continuation of the ζ factor; see gap_inventory.md.

---

## 7. UBT Embedding (Open)

Within the Unified Biquaternion Theory, the proposed correspondence is:

| Mathematical object | UBT interpretation |
|--------------------|--------------------|
| T^d | Compact real spatial directions of the biquaternion coordinate q |
| F = ⊗_p l²(ℕ₀) | Prime-indexed KK modes in the compact ψ-direction |
| H_inf = −Δ_{T^d} | UBT spatial kinetic operator projected to real sector |
| H_prime = Σ_p log(p) N_p | UBT ψ-mode number operator weighted by prime energies |
| H_total | Combined UBT Hamiltonian in flat limit |

These identifications are **conjectural** — the derivation of H_total from
the full biquaternion field equations Θ(q,τ) has not been completed.  See
gap_inventory.md, Gap F1.

---

## 8. References

- [Ja29] Jacobi, C. G. J. (1829). *Fundamenta Nova Theoriae Functionum
  Ellipticarum*. Königsberg.
- [Ri1859] Riemann, B. (1859). *Über die Anzahl der Primzahlen unter einer
  gegebenen Grösse*. Monatsberichte der Berliner Akademie.
- [T50] Tate, J. (1950). *Fourier analysis in number fields and Hecke's
  zeta-functions*. In: Algebraic Number Theory (Cassels–Fröhlich).
- [Ti86] Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*
  (2nd ed.). Oxford University Press.

---

**Last Updated**: 2026-05-05
