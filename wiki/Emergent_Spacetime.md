<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# Emergent Spacetime

Spacetime geometry in UBT is **not fundamental** — it emerges from the biquaternion
field Θ. The metric tensor g_μν is a derived object, not an input.

**Canonical sources**: [`canonical/geometry/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/canonical/geometry)  
**GR recovery chain**: [`canonical/bridges/GR_chain_bridge.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/bridges/GR_chain_bridge.tex)

---

## Emergent Metric

The spacetime metric g_μν is defined as:

```
g_μν = Re Tr(∂_μΘ · ∂_νΘ†)
```

This is the **real part of the biquaternionic derivative inner product**.

Status: **Proved [L1]**  
File: [`canonical/geometry/metric.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/metric.tex)

---

## Θ as Tensor Potential for Gravity

In precise analogy with electromagnetism — where the vector potential A_μ
generates the field strength F_μν = ∂_μA_ν − ∂_νA_μ — the field Θ acts as a
**tensor potential** for the gravitational metric:

    g_μν = Re Tr(∂_μΘ · ∂_νΘ†)

Key properties:
- The metric is **not independent** of Θ — it is fully determined by Θ's derivative structure
- This is not a postulate but follows from the variational principle δS[Θ] = 0
- In the real limit ψ → 0, this reduces to standard GR metric with Lorentzian signature

Status: **Proved [L1]**  
Source: [`canonical/geometry/metric.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/metric.tex)

---

## Key Properties of the Emergent Metric

| Property | Status | File |
|----------|--------|------|
| Non-degeneracy: det(g) ≠ 0 | **Proved [L0]** | [`GR_closure/step2_nondegeneracy.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/GR_closure/step2_nondegeneracy.tex) |
| Lorentzian signature (−,+,+,+) | **Proved [L0]** | [`GR_closure/step3_signature_theorem.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/GR_closure/step3_signature_theorem.tex) |
| Levi-Civita connection Γ | **Standard GR** | [`canonical/geometry/connection.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/connection.tex) |
| Riemann curvature tensor | **Standard GR** | [`canonical/geometry/curvature.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/curvature.tex) |
| Einstein equations from Hilbert variation | **Proved [L1]** | [`canonical/geometry/gr_as_limit.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/gr_as_limit.tex) |
| Conservation ∇^μ T_μν = 0 | **Standard GR** | [`canonical/geometry/stress_energy.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/stress_energy.tex) |

---

## The GR Recovery Chain

UBT recovers GR through a six-step chain:

```
Θ(q,τ)
  Step 1: g_μν = Re Tr(∂_μΘ · ∂_νΘ†)          [Proved L1]
  Step 2: det(g) ≠ 0                             [Proved L0]
  Step 3: signature (−,+,+,+)                    [Proved L0]
  Step 4a: Levi-Civita connection Γ              [Standard GR]
  Step 4b: Riemann curvature → G_μν             [Standard GR]
  Step 5: G_μν = 8πG T_μν  (Hilbert variation)  [Proved L1]
  Step 6: Off-shell Θ-only closure              [OPEN L2]
```

Steps 1–5 are sufficient for the physical claim that GR is recovered.  
Step 6 is additional theoretical tightening that remains open.

→ Full details: [GR Recovery](GR_Recovery)

---

## The Imaginary Sector

The imaginary components of the biquaternionic metric represent **phase curvature**
and nonlocal energy configurations. These extra degrees of freedom are invisible to
classical observations because ordinary matter couples only to the real metric g_μν.

This explains why GR appears complete experimentally, while UBT extends it.

---

## Canonical Files

| File | Content |
|------|---------|
| [`canonical/geometry/metric.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/metric.tex) | Emergent metric definition |
| [`canonical/geometry/connection.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/connection.tex) | Levi-Civita connection |
| [`canonical/geometry/curvature.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/curvature.tex) | Riemann tensor, Einstein tensor |
| [`canonical/geometry/gr_as_limit.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/gr_as_limit.tex) | GR recovery theorem |
| [`canonical/geometry/stress_energy.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/geometry/stress_energy.tex) | Stress-energy tensor T_μν |
| [`canonical/gr_limit/GR_limit_of_UBT.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/gr_limit/GR_limit_of_UBT.tex) | Full GR limit derivation |

---

## See Also

- [Theta Field](Theta_Field) — Θ(q,τ) definition and field equation
- [GR Recovery](GR_Recovery) — detailed derivation status
- [Operator Formalism](Operator_Formalism) — ∇ operator structure
