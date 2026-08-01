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


# prime_fock_operator — Rigorous Fock-Space Hamiltonian for the Riemann Zeta Function

**Status**: Open  
**Track**: research_tracks  
**Author**: Ing. David Jaroš  

---

## Purpose

This track replaces the ad-hoc Euler product used in the hybrid UBT model
by a rigorous **Fock-space Hamiltonian** whose partition function is the
Riemann zeta function.

The Hamiltonian is defined on a **bosonic Fock space over primes** and is
exactly solvable.  Its partition function equals ζ(s) for Re(s) > 1 by a
direct combinatorial identity (the Euler product formula).

> ⚠️ **This track does NOT claim a proof of the Riemann Hypothesis.**  
> The zeros of ζ(s) are zeros of the analytically continued partition
> function, **not** eigenvalues of H_prime.  The Hilbert–Pólya operator
> (if it exists) remains an open problem entirely separate from this
> construction.

---

## Contents

| File | Contents |
|------|----------|
| `README.md` | This file — overview, scope, warnings |
| `prime_fock_operator.md` | Main technical document: Fock-space definition, H_prime, partition function identity, claim controls |
| `archimedean_tensor_product.md` | Archimedean sector H_inf, theta-function kernel, tensor product Z_total = θ(t)^d · ζ(t) |
| `gap_inventory.md` | Structured inventory of open gaps between this construction and deeper conjectures (analytic continuation, RH) |

---

## Confidence Label

**Open** — the partition-function identity Z_P(s) → ζ(s) is a standard
combinatorial result (Euler product), not a UBT-specific claim.  The
physical embedding in the UBT framework and the connection to the full
analytic structure of ζ(s) remain open.

| Component | Level |
|-----------|-------|
| Fock-space Hamiltonian H_prime (definition) | Established |
| Tr(exp(−s H_prime)) = ζ(s) for Re(s) > 1 | Established |
| Finite-P truncation Z_P(s) → ζ(s) | Established |
| Archimedean sector Z_inf = θ(t)^d | Established |
| Total partition function Z_total = θ^d · ζ | Established (formal product) |
| Analytic continuation of Z_total | Open |
| RH via self-adjointness or spectrum of H_prime | **Prohibited claim** |

---

## Relation to Other Tracks

- `research_tracks/rh_trace_formula/` — ψ-Hamiltonian route to ζ; shares
  the goal of an operator-theoretic zeta function but uses a different
  (and more speculative) mechanism
- `research_tracks/p_universes/` — p-adic sector; the prime Fock space
  can be viewed as the direct-sum decomposition of the p-universe
  Hilbert spaces
- `canonical/algebra/` — biquaternion algebra foundation underlying the
  UBT embedding

---

**Last Updated**: 2026-05-05
