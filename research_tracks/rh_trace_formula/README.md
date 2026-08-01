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


# rh_trace_formula — UBT Hamiltonian / Trace Formula / Riemann Zeta

**Status**: Open  
**Track**: research_tracks  
**Author**: Ing. David Jaroš  

---

## Purpose

This track investigates whether the 1-dimensional **ψ-sector Hamiltonian**
arising from the Unified Biquaternion Theory (UBT) can be connected to
the **completed Riemann zeta function** via a heat-kernel trace formula.

The goal is to **rigorously document what is known, what is conjectural,
and what must be proved** before any such connection could be established.

> ⚠️ **This track does NOT claim a proof of the Riemann Hypothesis.**
> Any step that assumes zeta zeros as input is circular and inadmissible.

---

## Relation to the Hilbert–Pólya Programme

The Hilbert–Pólya conjecture posits that the non-trivial zeros of ζ(s)
are eigenvalues of a self-adjoint operator.  Berry–Keating (1999) proposed
a specific semiclassical Hamiltonian H = xp.  Connes (1999) gave a
spectral-theoretic framework using an adelic trace formula.

This track asks: does the UBT ψ-sector Hamiltonian H_ψ provide a
candidate operator within that programme?

---

## Files in This Directory

| File | Contents |
|------|----------|
| `README.md` | This file — overview, scope, warnings |
| `ubt_hamiltonian_trace_formula.md` | Main technical document: Hamiltonian definition, theta heat kernel, Mellin transform, conjectural ζ-link |
| `gap_inventory.md` | Structured checklist of all open gaps (G1–G6) that must be closed before any connection is established |
| `notes_on_weight_problem.md` | Detailed analysis of the modular-weight obstruction that prevents naive identification of θ₃³ with ζ(s) |

---

## Confidence Label

**Open** — no complete derivation known; active problem.

The individual components carry different confidence levels:

| Component | Level |
|-----------|-------|
| Theta heat kernel (standard) | Established |
| Mellin transform / functional equation | Established |
| θ → ζ Jacobi bridge | Established |
| UBT ψ-Hamiltonian definition | Candidate |
| Adelic/local factorization | Conjectural |
| Hilbert–Pólya identification | Conjectural |
| Proof of RH via UBT | **Prohibited claim** |

---

## Related Tracks

- `research_tracks/hecke_bridge/` — modular-form connections
- `research_tracks/automorphic/` — automorphic L-functions
- `canonical/algebra/` — biquaternion algebra foundation
- `canonical/geometry/` — emergent spacetime geometry

---

**Last Updated**: 2026-05-04
