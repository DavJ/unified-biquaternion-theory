<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Prime Fock Operator — Rigorous Construction

**Track**: research_tracks/prime_fock_operator  
**Status**: Open (Fock-space identity established; UBT embedding and analytic continuation open)  
**Author**: Ing. David Jaroš  

---

> ⚠️ **Critical Claim Control**  
> This document constructs a Fock-space Hamiltonian H_prime whose
> partition function equals ζ(s).  It does **not** prove the Riemann
> Hypothesis, does **not** identify eigenvalues of H_prime with zeros of
> ζ(s), and does **not** claim H_prime is the Hilbert–Pólya operator.  
> The Hilbert–Pólya programme remains entirely open.

---

## 1. Motivation

The Euler product formula for the Riemann zeta function,

```
ζ(s) = Π_p (1 − p^{−s})^{−1},    Re(s) > 1,
```

has a natural interpretation in terms of **independent harmonic
oscillators**, one for each prime p.  The bosonic Fock space over primes
with occupancy-weighted energy log(p) per quantum provides a Hamiltonian
H_prime whose statistical-mechanics partition function is exactly ζ(s).

This construction is rigorous, finite-dimensional on truncations, and free
from ad-hoc Euler products: the product *emerges* from the tensor-product
structure of the Fock space rather than being inserted by hand.

### 1.1 Context within UBT

In the Unified Biquaternion Theory the fundamental field is

```
Θ(q, τ),    q ∈ ℂ ⊗ ℍ,    τ = t + iψ ∈ ℂ.
```

Prime-indexed Kaluza–Klein modes of Θ in the compact ψ-direction are
naturally associated with occupation numbers n_p ∈ ℕ₀.  The prime Fock
operator gives a precise Hilbert-space realization of these modes.

---

## 2. The Prime Fock Space

### 2.1 Single-Prime Factor

For a fixed prime p, define the single-mode **bosonic Fock space**

```
F_p  =  l²(ℕ₀)  =  span{ |n_p⟩ : n_p = 0, 1, 2, … }
```

with the standard inner product ⟨m_p|n_p⟩ = δ_{m_p, n_p}.

The **number operator** for prime p is

```
N_p |n_p⟩  =  n_p |n_p⟩.
```

### 2.2 Full Fock Space

Let {p_1, p_2, p_3, …} = {2, 3, 5, 7, 11, …} be the sequence of all primes.
Define the **prime Fock space**

```
F  =  ⊗_{k ≥ 1}  F_{p_k}  =  ⊗_p  l²(ℕ₀).
```

Basis vectors in F are labeled by **multi-indices** n = (n_2, n_3, n_5, …)
∈ ℕ₀^∞ with finitely many non-zero entries (the algebraic tensor product):

```
|n⟩  =  ⊗_p  |n_p⟩,    n_p ∈ ℕ₀,    #{p : n_p ≠ 0} < ∞.
```

Each such n corresponds to the **smooth integer**

```
m(n)  =  Π_p  p^{n_p}  ∈  ℕ,
```

which is the unique positive integer with prime factorization
p_1^{n_{p_1}} · p_2^{n_{p_2}} · …  The map n ↦ m(n) is a bijection
between the algebraic basis of F and ℕ (by the Fundamental Theorem of
Arithmetic).

> **Notation**: We write |m⟩ for the basis vector corresponding to
> m ∈ ℕ, with prime factorization m = Π_p p^{n_p(m)}.

---

## 3. The Prime Fock Hamiltonian

### 3.1 Definition

**Definition 3.1** (Prime Fock Hamiltonian).

```
H_prime  =  Σ_p  log(p) · N_p  ⊗  I_{F/F_p}
```

where the sum runs over all primes p, N_p acts on the F_p factor, and
I_{F/F_p} is the identity on all remaining factors.

Acting on a basis vector |m⟩ with m = Π_p p^{n_p}:

```
H_prime |m⟩  =  ( Σ_p  n_p(m) log(p) ) |m⟩
              =  log( Π_p p^{n_p(m)} ) |m⟩
              =  log(m) |m⟩.
```

### 3.2 Spectrum

**Proposition 3.2** (Spectrum of H_prime).

The operator H_prime is diagonal in the basis {|m⟩ : m ∈ ℕ} with

```
H_prime |m⟩  =  E_m |m⟩,    E_m  =  log(m).
```

The spectrum is

```
spec(H_prime)  =  { log(m) : m ∈ ℕ }
               =  { 0, log 2, log 3, 2 log 2, log 5, log 2 + log 3, … }.
```

The eigenvalue E_m = log(m) has **multiplicity one** (since m ↦ |m⟩ is
a bijection by unique factorization).

*Proof*: Direct computation from Definition 3.1. □

---

## 4. Partition Function Identity

### 4.1 Finite-Prime Truncation

For a finite set P of primes define the truncated Fock space

```
F_P  =  ⊗_{p ∈ P}  l²(ℕ₀)
```

and the truncated Hamiltonian

```
H_P  =  Σ_{p ∈ P}  log(p) · N_p.
```

**Proposition 4.1** (Truncated partition function).

For Re(s) > 0:

```
Z_P(s)  :=  Tr_{F_P}[ e^{−s H_P} ]
          =  Π_{p ∈ P}  Σ_{n_p ≥ 0}  e^{−s n_p log p}
          =  Π_{p ∈ P}  Σ_{n_p ≥ 0}  (p^{−s})^{n_p}
          =  Π_{p ∈ P}  (1 − p^{−s})^{−1}.
```

*Proof*: The trace factorizes over the tensor-product factors because
H_P is a sum of commuting operators each acting on a separate factor. □

### 4.2 Equivalence to Smooth-Number Sum

**Corollary 4.2** (Smooth-number Dirichlet series).

The P-smooth numbers (positive integers with all prime factors in P)
are exactly the integers m = Π_{p ∈ P} p^{n_p} for (n_p)_{p ∈ P} ∈ ℕ₀^P.
Hence

```
Z_P(s)  =  Σ_{m P-smooth}  m^{−s}.
```

*Proof*: The multinomial expansion of Π_{p ∈ P} (1 − p^{−s})^{−1}, combined
with the bijection between occupation-number vectors and smooth integers,
gives the Dirichlet series. □

### 4.3 Full Partition Function

**Theorem 4.3** (Partition function equals zeta).

For Re(s) > 1, the trace of exp(−s H_prime) over F converges absolutely:

```
Tr_F[ e^{−s H_prime} ]  =  Σ_{m=1}^∞  m^{−s}  =  ζ(s).
```

*Proof*:

```
Tr_F[ e^{−s H_prime} ]
    =  Σ_{m ∈ ℕ}  ⟨m| e^{−s H_prime} |m⟩
    =  Σ_{m=1}^∞  e^{−s log m}
    =  Σ_{m=1}^∞  m^{−s}
    =  ζ(s)                              (absolute convergence for Re(s) > 1).
```

The step Tr = Σ_m is justified by the orthonormal basis {|m⟩}_{m ∈ ℕ} of F.
The passage from F_P to F in the limit P → all primes uses monotone convergence:
Z_P(s) ↑ ζ(s) as P → {all primes}, since all terms are positive for real s > 1. □

---

## 5. Claim Control

The following controls are **mandatory** for this track.

### 5.1 What is proved

| Statement | Level | Comment |
|-----------|-------|---------|
| H_prime is well-defined on algebraic ⊗_p l²(ℕ₀) | **Established** | Direct from Definition 3.1 |
| spec(H_prime) = {log m : m ∈ ℕ} | **Established** | Proposition 3.2 |
| Z_P(s) = Π_{p≤P} (1−p^{−s})^{−1} | **Established** | Proposition 4.1; standard trace factorization |
| Z_P(s) = Σ_{m P-smooth} m^{−s} | **Established** | Corollary 4.2; combinatorial identity |
| Tr(e^{−s H_prime}) = ζ(s) for Re(s) > 1 | **Established** | Theorem 4.3; monotone convergence |

### 5.2 What is NOT proved (and is not claimed)

| False claim | Why it is false / inadmissible |
|-------------|-------------------------------|
| The zeros of ζ(s) are eigenvalues of H_prime | **False**: eigenvalues of H_prime are {log m : m ∈ ℕ} ⊂ [0,∞). None of these are complex numbers with Re = 1/2. |
| H_prime is the Hilbert–Pólya operator | **Unsubstantiated**: the Hilbert–Pólya operator (if it exists) must have spectrum {t_n} where ½+it_n are zeros of ζ(s). H_prime has a completely different spectrum. |
| The analytic continuation of Z(s) to Re(s) ≤ 1 can be read off from H_prime | **Open**: H_prime is only defined for Re(s) > 1 as a trace. The extension to the critical strip requires separate analytic arguments (see gap_inventory.md). |
| This construction proves RH | **Prohibited claim**: RH asserts all non-trivial zeros of ζ(s) have Re(s) = ½. Nothing in this construction addresses the location of zeros. |

### 5.3 Zeros of ζ(s) and the partition function

The function ζ(s) is the **analytic continuation** of Z(s) = Σ m^{−s} to
ℂ \ {1}.  The non-trivial zeros of ζ(s) lie in the critical strip 0 < Re(s) < 1,
which is **outside the region of convergence** of the trace Tr(e^{−s H_prime}).

The zeros of ζ(s) are therefore:
- Zeros of the analytically continued partition function, **not** eigenvalues
  of H_prime.
- Completely inaccessible to H_prime as a trace-class operator on F.
- Subject to the Riemann Hypothesis as an **independent open problem**.

---

## 6. Extension of H_prime to a Bounded Operator

For applications requiring a bounded operator, one may define

```
A_prime  =  e^{−σ H_prime}    (σ > 1  fixed reference)
```

which is a bounded positive self-adjoint operator on F (compact, since its
eigenvalues m^{−σ} → 0).  The partition function of H_prime at parameter s
then equals the trace of A_prime^{s/σ}.  This formulation is useful for
perturbation theory and functional calculus but does not change the
claim-control statements above.

---

## 7. References

- [Eu1737] Euler, L. (1737). *Variae observationes circa series infinitas*.
  Commentarii Academiae Scientiarum Imperialis Petropolitanae 9, 160–188.
  (First statement of the Euler product for ζ(s).)
- [Ri1859] Riemann, B. (1859). *Über die Anzahl der Primzahlen unter einer
  gegebenen Grösse*. Monatsberichte der Berliner Akademie.
- [Ti86] Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*
  (2nd ed.). Oxford University Press.
- [IK04] Iwaniec, H. & Kowalski, E. (2004). *Analytic Number Theory*.
  AMS Colloquium Publications 53.
- [BK99] Berry, M. V. & Keating, J. P. (1999). *The Riemann zeros and
  eigenvalue asymptotics*. SIAM Review 41(2), 236–266.
- [C99] Connes, A. (1999). *Trace formula in noncommutative geometry and the
  zeros of the Riemann zeta function*. Selecta Math. 5, 29–106.

---

**Last Updated**: 2026-05-05
