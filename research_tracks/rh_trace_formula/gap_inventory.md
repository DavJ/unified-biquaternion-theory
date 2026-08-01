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


# Gap Inventory — UBT Hamiltonian / Trace Formula / Riemann Zeta

**Track**: research_tracks/rh_trace_formula  
**Status**: All gaps open  
**Author**: Ing. David Jaroš  

---

> ⚠️ **Warning**  
> Any construction that **assumes the non-trivial zeros of ζ(s) as input**
> is circular and cannot prove the Riemann Hypothesis.  All gaps below
> must be closed by independent arguments.

---

## Overview

Before any claim can be made connecting the UBT ψ-sector Hamiltonian H_ψ
to the Riemann zeta function, the following **six gaps (G1–G6)** must be
closed in sequence.  Closing a later gap before an earlier one is closed
is only permissible if the derivation is modular (i.e. the later argument
is conditional on the earlier gap being resolved).

The gaps are ordered by logical dependency:

```
G1 (self-adjointness)
  → G2 (heat trace)
      → G3 (adelic factorization)
          → G4 (local Euler factors)
      → G5 (G(s) non-vanishing)
  → G6 (explicit formula connection, requires G1–G5)
```

---

## Gap Table

| ID | Name | Statement | Difficulty | Status |
|----|------|-----------|------------|--------|
| G1 | Essential self-adjointness of H_ψ | Prove H_ψ = −d²/dψ² + V_eff(ψ) is essentially self-adjoint on D(H_ψ) ⊂ L²(S¹_ψ) with V_eff derived from the UBT biquaternion field | Hard | **Open** |
| G2 | Exact heat trace | Compute Tr[e^{−t H_ψ}] exactly (or to sufficient precision) and relate it to a theta function or modular form | Hard | **Open** |
| G3 | Adelic/local factorization | Derive a factorization ζ_H(s) = ζ_∞(s) × Π_p ζ_p(s) from the UBT structure without assuming the Euler product of ζ(s) | Very Hard | **Open** |
| G4 | Local Euler factors | Show ζ_p(s) = (1 − p^{−s})^{−1} by computing the spectrum of the UBT p-adic sector Hamiltonian H_p | Very Hard | **Open** |
| G5 | G(s) holomorphic and nonvanishing | Prove that the correction factor G(s) in ζ_H(s) = π^{−s/2} Γ(s/2) ζ(s) G(s) is holomorphic and nonvanishing on 0 < Re(s) < 1 | Very Hard | **Open** |
| G6 | Explicit formula connection | Derive the Riemann–Weil explicit formula from the trace formula of H_ψ without circular assumptions about the location of zeros | Hard | **Open** |

---

## Detailed Gap Descriptions

### G1 — Essential Self-Adjointness of H_ψ

**What must be proved:**

H_ψ = −d²/dψ² + V_eff(ψ) is essentially self-adjoint on the domain

```
D₀ = C^∞_per(S¹_ψ)  ⊂  L²(S¹_ψ)
```

(smooth, L_ψ-periodic functions) where L_ψ is the circumference of the
compact ψ-direction.

**Known partial results:**

- For V_eff ∈ L²(S¹_ψ) (square-integrable), self-adjointness follows from
  Kato–Rellich: V_eff is relatively bounded with respect to −d²/dψ² with
  bound < 1 if ‖V_eff‖_{L²} is small enough.
- For V_eff ∈ L^∞(S¹_ψ), self-adjointness is automatic by Kato–Rellich
  with relative bound 0.

**What is missing:**

An explicit derivation of V_eff(ψ) from the UBT Lagrangian/field equations
is needed to verify that V_eff satisfies one of the above conditions.

**Suggested approach:**

1. Derive V_eff(ψ) = κ Re[⟨Θ†Θ⟩_q]|_ψ by integrating the UBT field
   equations over the spatial biquaternion directions.
2. Show V_eff ∈ L^∞(S¹_ψ) (or at least V_eff ∈ L²).
3. Apply Kato–Rellich or Friedrich's extension theorem.

---

### G2 — Exact Heat Trace

**What must be proved:**

Compute

```
Z_H(t)  =  Tr[ e^{−t H_ψ} ]  =  Σ_n  e^{−t λ_n}
```

for t > 0, and identify its relationship to a known modular/theta function.

**Known partial results:**

- For V_eff = 0, H_ψ = −d²/dψ² has eigenvalues λ_n = (2πn/L_ψ)² and
  Z_H(t) = Σ_{n∈ℤ} e^{−t(2πn/L_ψ)²} = θ₃(it L_ψ²/(4π)).
- The perturbative correction to Z_H(t) from V_eff is of order t².

**What is missing:**

- The non-perturbative form of Z_H(t) for the UBT-derived V_eff.
- Whether the correction terms from V_eff are absorbed into the G(s)
  factor (see G5) or destroy the Mellin-transform argument entirely.

---

### G3 — Adelic/Local Factorization

**What must be proved:**

The spectral zeta function ζ_H(s) = Tr[H_ψ^{−s}] factorizes as

```
ζ_H(s)  =  Π_v  ζ_v(s)
```

over all places v of ℚ (archimedean place v = ∞ and finite places v = p
for each prime p), with the product converging absolutely.

**Known partial results:**

- In Tate's thesis, the completed zeta function of a Hecke character
  factorizes over all places via Fourier analysis on the adèle group.
- Connes (1999) constructs an adelic space on which the trace formula
  reproduces the explicit formula for ζ(s).

**What is missing:**

- An explicit embedding of H_ψ into an adelic operator.
- Identification of the local operators H_p corresponding to each prime p.
- A proof that the local spectra multiply to give ζ_H(s).

---

### G4 — Local Euler Factors

**What must be proved:**

For each prime p, define the p-adic sector Hamiltonian H_p from the UBT
p-adic/mirror sector.  Prove

```
ζ_p(s)  =  ( 1 − p^{−s} )^{−1}
```

**Known partial results:**

- The UBT p-adic sector is motivated by the p-universes research track
  (`research_tracks/p_universes/`), but no Hamiltonian H_p has been
  defined there.
- The Euler factor (1 − p^{−s})^{−1} arises from the spectrum of the
  p-adic shift operator on L²(ℤ_p) (see Tate's local computation).

**What is missing:**

- A definition of H_p within UBT.
- A computation of spec(H_p) that yields {p^k : k ≥ 0} with multiplicity 1.

---

### G5 — G(s) Holomorphic and Nonvanishing

**What must be proved:**

The correction factor G(s) defined by

```
ζ_H(s)  =  π^{−s/2} Γ(s/2) ζ(s) G(s)
```

satisfies:

1. G(s) extends to a holomorphic function on 0 < Re(s) < 1.
2. G(s) ≠ 0 for all s in 0 < Re(s) < 1.

If G(s) had zeros in the critical strip, the zeros of ζ_H(s) would not
coincide with those of ζ(s), breaking the Hilbert–Pólya connection.

**Known partial results:**

- None.  G(s) has not been computed.

**What is missing:**

- A formula for G(s) derived from G2 (the exact heat trace).
- An analytic continuation argument for G(s).
- A nonvanishing proof (likely requiring detailed control of the heat trace).

---

### G6 — Explicit Formula Connection

**What must be proved:**

The Riemann–Weil explicit formula

```
Σ_γ h(γ)  =  ĥ(1) + ĥ(0)  −  Σ_p Σ_{k≥1} (log p / p^{k/2}) ĥ(k log p)
             −  (Γ-factor contributions)
```

can be derived from the trace formula

```
Tr[ h(H_ψ) ]  =  (geometric side)
```

without assuming the Generalized Riemann Hypothesis or placing zeros on
the critical line as a hypothesis.

**Why this is hard:**

The standard derivation of the explicit formula *uses* the location of zeros
to derive the prime-sum on the right.  A trace-formula derivation would
need to *produce* the prime-sum from geometry (closed geodesics / prime
orbits) and *deduce* the zero location — the reverse direction.

> Any proof that proceeds by: (1) assume zeros at ½ + it_n, (2) compute
> trace, (3) get explicit formula — is **circular**.  The correct direction
> is: (1) compute trace from geometry, (2) get explicit formula, (3) deduce
> zeros on critical line.

---

## Progress Tracking

| Gap | Assigned To | Last Updated | Notes |
|-----|-------------|--------------|-------|
| G1 | — | 2026-05-04 | Awaiting V_eff derivation |
| G2 | — | 2026-05-04 | Perturbative expansion possible; non-perturbative open |
| G3 | — | 2026-05-04 | Requires adelic embedding of UBT |
| G4 | — | 2026-05-04 | Requires H_p definition |
| G5 | — | 2026-05-04 | Blocked by G2 |
| G6 | — | 2026-05-04 | Blocked by G1, G2, G3, G4, G5 |

---

**Last Updated**: 2026-05-04
