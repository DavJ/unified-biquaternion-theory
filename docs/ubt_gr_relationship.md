<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT ↔ GR Relationship Map

**Path**: `docs/ubt_gr_relationship.md`  
**Date**: 2026-03-11  
**Audience**: Physicists, reviewers, and newcomers to UBT  
**Purpose**: Concise visual and conceptual map of how UBT and GR relate

---

## The Relationship at a Glance

```
UBT full Θ dynamics
      |
      |  restrict to admissible sector A_UBT
      |  (conditions C1–C6: regularity, gauge-reduction,
      |   decoupling of extra modes; see gr_sector_conditions.tex)
      v
metric-generating classical sector
      |
      |  real projection  Re(ℰ_μν) = κ Re(𝒯_μν)
      v
      GR  —  G_μν = 8πG T_μν
      |
      |  weak-field / non-relativistic limit
      v
Newtonian gravity
```

Each downward arrow involves a restriction or projection.  GR is not
"derived from scratch" by discarding UBT structure—it is the dynamics that
remains after restricting to the metric-observable sector and projecting away
the additional biquaternionic degrees of freedom.

---

## What Is Inside the GR Sector

The admissible sector $\mathcal{A}_{\mathrm{UBT}}$ contains:

- **All classical GR solutions** (at minimum flat space and linearised
  perturbations; non-linear solutions are expected and are an active area of
  work — see `AUDITS/followup_gap_backlog_2026_03.md` GAP-01 and GAP-04).
- **Standard matter coupled to gravity**: the stress-energy tensor $T_{\mu\nu}$
  arises from the biquaternionic matter Lagrangian $\mathcal{L}_\Theta$ in the
  standard way.
- **Lorentzian signature** $(-,+,+,+)$: guaranteed by AXIOM B (complex time)
  and the signature theorem (`step3_signature_theorem.tex`).
- **Bianchi identity** $\nabla^\mu G_{\mu\nu} = 0$: proved under assumptions
  A1–A2 (`appendix_R_GR_equivalence.tex`).
- **Conservation law** $\nabla^\mu T_{\mu\nu} = 0$: follows from Bianchi
  identity on the GR sector.

On this sector, **UBT and GR make identical predictions**.  All experimental
tests of GR (perihelion precession, gravitational wave detection, GPS
corrections, black hole imaging, etc.) automatically validate UBT's GR sector.

---

## What May Exist Outside the GR Sector

Outside $\mathcal{A}_{\mathrm{UBT}}$, the full UBT dynamics may contain:

- **Phase-curvature solutions**: configurations where the imaginary part of
  $\mathcal{G}_{\mu\nu}$ is non-zero and carries energy not present in
  classical GR.
- **Complex-time oscillations**: modes associated with the $\psi$-circle that
  have no GR counterpart.
- **Non-metric biquaternionic polarisations**: additional spin states of the
  $\Theta$ field beyond the standard spin-2 graviton.
- **Non-GR equations of motion**: UBT configurations where the combined
  Euler–Lagrange condition $\mathcal{E}_\Theta + J^*\mathcal{E}_g = 0$ is
  satisfied without $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ holding pointwise.

These are **physical predictions** of UBT that go beyond GR.  They are not
inconsistencies; they are the reason UBT is a more general framework.  Whether
they are observable depends on the energy scale at which the extra $\Theta$
modes become active.

---

## Why This Is Expected for a Deeper Theory

A deeper theory should:

1. **Reproduce the known theory** (GR) in the appropriate regime — ✅ UBT does.
2. **Predict new phenomena** beyond the known theory — ✅ UBT does (extra modes,
   complex time effects, non-GR sector).
3. **Provide a mathematically consistent extension** — ✅ UBT is a consistent
   biquaternionic field theory.

This pattern is universal in theoretical physics:
- **String theory** contains GR as the low-energy effective description of the
  graviton sector; it does not reproduce GR for every string configuration.
- **Loop quantum gravity** recovers GR in the classical/semiclassical limit;
  the quantum geometry differs fundamentally.
- **Kaluza–Klein theories** contain GR as the zero-mode sector after
  compactification; higher modes give new physics.

UBT follows exactly the same pattern: GR is the zero-mode / classical-sector
/ metric-sector projection of a richer structure.

---

## Clarification: No Contradiction Between UBT and GR

**There is no contradiction** between UBT and GR.

The claim "UBT extends GR" is not the same as "UBT contradicts GR".  A theory
extends another when it:
- reproduces the other theory's predictions in the appropriate regime (✅), and
- makes additional predictions outside that regime (✅).

A theory contradicts another when it:
- gives different predictions in the regime where the other is well-tested (❌, not the case here).

UBT's combined Euler–Lagrange equation $\mathcal{E}_\Theta + J^*\mathcal{E}_g = 0$
is weaker than the pair $\{\mathcal{E}_\Theta = 0,\, \mathcal{E}_g = 0\}$.
This means UBT admits more solutions than GR, not fewer.  GR solutions are a
subset of UBT solutions, not a separate class.

---

## Proof Status Summary

| Claim | Level | Status |
|-------|-------|--------|
| $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ from Hilbert variation | Level 1 (exact) | ✅ Proved |
| Linearised GR recovery in pure-$\Theta$ formulation | Level 2 (sector) | ✅ Proved |
| Lorentzian signature from AXIOM B | Level 2 | ✅ Proved |
| Non-degeneracy of metric for $\mathcal{A}_{\mathrm{UBT}}$ | Level 2 | ✅ Proved |
| Bianchi identity + conservation | Level 2 | ✅ Proved (under A1–A2) |
| Non-linear GR recovery (pure-$\Theta$) | Level 2–3 | ⚠️ Partial / open |
| GR as low-energy effective limit | Level 3 | ⚠️ Plausible |
| All GR solutions lift to $\mathcal{A}_{\mathrm{UBT}}$ | Level 1 | ❓ Open problem |

**Key language rule** (enforced by `tests/test_gr_status_consistency.py`):  
Whenever only Level 2 or Level 3 is established, the repository must not claim
"full exact $\Theta$-only Einstein derivation completed" and must instead say
"GR-compatible sector recovered" or "partial/projected recovery".

---

## References

- `consolidation_project/GR_closure/theta_vs_metric_variation_note.tex` — why combined
  variation ≠ termwise separation
- `consolidation_project/GR_closure/gr_sector_conditions.tex` — explicit conditions C1–C6
- `reports/gr_recovery_levels.md` — three levels of GR recovery defined
- `reports/gr_recovery_final_status.md` — current detailed status
- `consolidation_project/appendix_R_GR_equivalence.tex` — canonical GR equivalence proof
- `DERIVATION_INDEX.md §GR Recovery Status` — derivation tracking
- `AUDITS/followup_gap_backlog_2026_03.md` — open problems (GAP-01, GAP-04)
