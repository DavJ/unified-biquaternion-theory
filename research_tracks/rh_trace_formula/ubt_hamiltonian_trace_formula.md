<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT Hamiltonian, Heat Kernel, and the Completed Riemann Zeta Function

**Track**: research_tracks/rh_trace_formula  
**Status**: Open (Conjectural framework; no proof of RH)  
**Author**: Ing. David Jaroš  

---

> ⚠️ **Critical Warning**  
> This document explores a *possible* structural connection between a
> UBT-derived operator and the Riemann zeta function.  It does **not**
> establish, claim, or imply a proof of the Riemann Hypothesis (RH).  
> Any construction that takes the non-trivial zeros of ζ(s) as *input*
> is circular and cannot constitute evidence for RH.

---

## 1. Background and Motivation

### 1.1 The Hilbert–Pólya Programme

The **Hilbert–Pólya conjecture** asserts that there exists a self-adjoint
operator T on a Hilbert space H such that

```
spec(T)  =  { t_n : ζ(1/2 + i t_n) = 0,  t_n ∈ ℝ }
```

Under the Riemann Hypothesis the zeros ½ + it_n lie on the critical line,
so the spectrum is real, which is automatic for a self-adjoint operator.
The conjecture gives an *operator-theoretic* route to RH.

Key references:
- **Berry & Keating (1999)**: semiclassical H = xp approach [BK99].
- **Connes (1999)**: adelic trace formula on the space of adèles [C99].
- **Tate (1950)**: Fourier analysis on the adèle ring; functional equation
  of ζ(s) as a global-local factorization [T50].
- **Selberg (1956)**: trace formula relating lengths of closed geodesics to
  eigenvalues of the Laplacian on a hyperbolic surface [S56].

### 1.2 UBT Context

In the Unified Biquaternion Theory the fundamental field is

```
Θ(q, τ),    q ∈ ℂ ⊗ ℍ,    τ = t + iψ ∈ ℂ
```

The imaginary-time component ψ parameterizes a compact direction.
Restricting to **real spatial degrees of freedom** and treating ψ as the
single dynamical variable yields a 1-dimensional system whose spectral
theory is the subject of this track.

---

## 2. The ψ-Sector Hamiltonian

### 2.1 Definition (Candidate)

**Definition 2.1** (Candidate; not yet proved self-adjoint on the stated domain).

Let S¹_ψ be the circle of circumference L_ψ (to be determined by the
UBT moduli of the ψ-direction).  Define the candidate Hamiltonian

```
H_ψ  =  − d²/dψ²  +  V_eff(ψ)
```

acting on H = L²(S¹_ψ) with periodic boundary conditions

```
f(0) = f(L_ψ),    f'(0) = f'(L_ψ).
```

The effective potential V_eff(ψ) is inherited from the UBT curvature
of the ψ-direction:

```
V_eff(ψ)  =  κ  Re[ ⟨Θ† Θ⟩_q ] |_{ψ}
```

where ⟨·⟩_q denotes the expectation value over the spatial biquaternion
directions, and κ is the UBT coupling constant.

> **Gap G1**: Essential self-adjointness of H_ψ on the domain
> D(H_ψ) = H²(S¹_ψ) ∩ {periodic b.c.} has not been proved within UBT.
> For V_eff smooth this follows from standard Sturm–Liouville theory,
> but V_eff derived from the full biquaternion field has not been shown
> smooth or even bounded below.

### 2.2 Spectrum (Formal)

Formally, if H_ψ is self-adjoint, the spectrum consists of a discrete set

```
0 ≤ λ₀ ≤ λ₁ ≤ λ₂ ≤ …
```

and the heat operator e^{−t H_ψ} is trace-class for t > 0.

---

## 3. Established Results: Theta Heat Kernel

*The following results are standard mathematics, independent of UBT.*

### 3.1 The Jacobi Theta Function

The **Jacobi theta function** (third theta function) is

```
θ₃(τ)  =  Σ_{n ∈ ℤ}  q^{n²},    q = e^{iπτ},    Im(τ) > 0.
```

For real t > 0, setting q = e^{−πt}:

```
θ₃(it)  =  Σ_{n ∈ ℤ}  e^{−π n² t}
```

This is the **heat kernel trace** of the Laplacian −d²/dψ² on the circle
ℝ/ℤ with flat metric, evaluated at time t.  More precisely, for the
operator −d²/dψ² with eigenvalues (2πn)²:

```
Tr[ e^{−t(−d²/dψ²)} ]  =  θ₃(it/(π))   (up to normalization)
```

**Theorem 3.1** (Jacobi; standard).

```
θ₃(it)  =  t^{−1/2} θ₃(i/t)      (t > 0)
```

This is the modular transformation of θ₃ under τ ↦ −1/τ, with **modular
weight 1/2**.

### 3.2 Mellin Transform and the Completed Zeta Function

**Theorem 3.2** (Standard; see e.g. Titchmarsh [Ti86]).

Define the **completed Riemann zeta function**

```
ξ(s)  =  π^{−s/2} Γ(s/2) ζ(s),    Re(s) > 1.
```

Then ξ(s) extends to an entire function satisfying

```
ξ(s)  =  ξ(1−s).
```

The standard **theta/zeta bridge** is:

```
ξ(s)  =  ½ ∫₀^∞  [ θ₃(it) − 1 ]  t^{s/2}  dt/t     (Re(s) > 1)
```

This integral converges, and its meromorphic continuation yields ξ(s)
with the known functional equation.

**Proof sketch**: Expand θ₃(it) − 1 = 2 Σ_{n≥1} e^{−πn²t}, integrate
term by term, obtain Σ_{n≥1} π^{−s/2} Γ(s/2) n^{−s} = ξ(s). □

---

## 4. The Conjectural UBT–Zeta Link

*The following is **conjectural**.  None of the claims in this section
have been proved.*

### 4.1 The Heat Trace of H_ψ

**Conjecture 4.1** (Trace formula, unproved).

Assume G1 (self-adjointness) is resolved.  Assume moreover that the
spectrum of H_ψ on S¹_ψ coincides, up to a finite-rank perturbation,
with the spectrum of the flat Laplacian −d²/dψ² modulo a correction
from V_eff.  Then the heat trace of H_ψ satisfies

```
Z_H(t)  :=  Tr[ e^{−t H_ψ} ]  =  θ₃(it; V_eff)
```

where θ₃(·; V_eff) is a **perturbed theta function** that agrees with
θ₃(it) at leading order in t.

> **Gap G2**: The exact heat trace Z_H(t) for H_ψ with the UBT-derived
> V_eff has not been computed.  In particular, the correction terms from
> V_eff may destroy the theta-function identity needed for the Mellin
> transform argument below.

### 4.2 The Central Conjectural Formula

**Conjecture 4.2** (ζ-link, unproved).

Suppose Gaps G1–G5 are all resolved.  Then the spectral zeta function
of H_ψ,

```
ζ_H(s)  =  Tr[ H_ψ^{−s} ]  =  Σ_n λ_n^{−s}
```

satisfies

```
ζ_H(s)  =  π^{−s/2} Γ(s/2) ζ(s) G(s)
```

where:
- π^{−s/2} Γ(s/2) ζ(s) is the completed Riemann zeta function ξ(s) up
  to the factor ½,
- **G(s)** is an *a priori unknown* correction factor encoding:
  - contributions from V_eff,
  - adelic/local corrections from the p-adic sector of UBT,
  - the modular-weight discrepancy (see Section 5 and
    `notes_on_weight_problem.md`).

> **Gap G5**: G(s) must be proved holomorphic and **nonvanishing** on
> the strip 0 < Re(s) < 1 for the zeros of ζ_H(s) to coincide with
> those of ζ(s).  This is an independent hard problem.

### 4.3 Adelic Factorization (Conjectural)

**Conjecture 4.3** (Adelic structure, unproved).

The UBT framework suggests a **local–global decomposition** of the form

```
ζ_H(s)  =  ζ_∞(s)  ×  Π_p  ζ_p(s)
```

where ζ_∞(s) is the archimedean factor (from the real ψ-direction) and
ζ_p(s) are p-adic contributions from the UBT mirror/p-universe sectors.

**Conjecture 4.4** (Local Euler factors, unproved).

For each prime p, the local factor is conjectured to be

```
ζ_p(s)  =  ( 1 − p^{−s} )^{−1}
```

which is precisely the local Euler factor of ζ(s).  This would require
deriving the p-adic sector Hamiltonians H_p and computing their spectra.

> **Gap G3**: The adelic/local factorization of ζ_H(s) has not been
> derived.  This requires extending H_ψ to a full adelic operator.

> **Gap G4**: The local Euler factors (1 − p^{−s})^{−1} have not been
> derived from the UBT p-adic Hamiltonians.

### 4.4 Hilbert–Pólya Interpretation (Conjectural)

**Conjecture 4.5** (Hilbert–Pólya identification, unproved).

If Conjectures 4.2–4.4 and G(s) ≢ 0 on 0 < Re(s) < 1 are all proved,
then the zeros of ζ_H(s) coincide with the zeros of ζ(s).  If moreover
H_ψ is self-adjoint (Gap G1), then its eigenvalues are real, and the
non-trivial zeros of ζ(s) lie on the line Re(s) = ½.

> **This chain of implications has NOT been established.  It is stated
> here purely as a research target, not as a result.**

---

## 5. The Explicit Formula and Gap G6

The classical **Riemann–Weil explicit formula** (Weil [W52]) relates
the zeros of ζ(s) to prime powers:

```
Σ_{γ} h(γ)  =  ĥ(1) + ĥ(0) − Σ_p Σ_{k≥1} (log p / p^{k/2}) ĥ(k log p)
             − (terms from Γ factors)
```

for suitable test functions h.  A trace-formula approach to RH would
need to reproduce this identity from the spectral theory of H_ψ.

> **Gap G6**: Connecting the trace formula for H_ψ to the explicit
> formula for ζ(s) without assuming the location of zeta zeros as input
> has not been done.  Any derivation that starts by placing the zeros on
> the critical line is **circular** and does not constitute progress
> toward RH.

---

## 6. Summary of Levels

| Item | Level | Notes |
|------|-------|-------|
| Theta heat kernel (Theorem 3.1) | **Established** | Standard 19th-century mathematics |
| Mellin transform / ξ functional equation (Theorem 3.2) | **Established** | Riemann (1859), Titchmarsh (1930s) |
| θ₃ → ζ(s) Jacobi bridge | **Established** | Standard |
| H_ψ definition (Definition 2.1) | **Candidate** | UBT-motivated; self-adjointness unproved (G1) |
| Heat trace Z_H(t) computation | **Open** | G2 unresolved |
| Adelic factorization | **Conjectural** | G3, G4 unresolved |
| G(s) holomorphic and nonvanishing | **Open** | G5 unresolved |
| Explicit formula connection | **Open** | G6 unresolved |
| Identification with ζ zeros → RH | **Prohibited claim** | Circular without G1–G6 |

---

## 7. References

- [BK99] Berry, M. V. & Keating, J. P. (1999). *The Riemann zeros and eigenvalue
  asymptotics*. SIAM Review 41(2), 236–266.
- [C99] Connes, A. (1999). *Trace formula in noncommutative geometry and the
  zeros of the Riemann zeta function*. Selecta Math. 5, 29–106.
- [S56] Selberg, A. (1956). *Harmonic analysis and discontinuous groups in
  weakly symmetric Riemannian spaces*. J. Indian Math. Soc. 20, 47–87.
- [T50] Tate, J. (1950). *Fourier analysis in number fields and Hecke's
  zeta-functions*. In: Algebraic Number Theory (Cassels–Fröhlich), pp. 305–347.
- [Ti86] Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*
  (2nd ed., revised by Heath-Brown). Oxford University Press.
- [W52] Weil, A. (1952). *Sur les "formules explicites" de la théorie des
  nombres premiers*. Comm. Sém. Math. Univ. Lund (Medd. Lunds Mat. Sem.),
  Tome Suppl., 252–265.

---

**Last Updated**: 2026-05-04
