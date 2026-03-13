<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT Fitted Parameters Register

> **Purpose**: Track which parameters in UBT are fitted/semi-empirical (not derived),
> and which have been promoted to fully derived status.
>
> **Maintenance rule (R5):** Update this file on every gap closure.
> - Remove a parameter when it is derived from first principles.
> - Keep a parameter when it remains fitted to data.

---

## How to Read This Register

| Column | Meaning |
|---|---|
| **Parameter** | Symbol and brief description |
| **Domain** | Physics domain where it appears |
| **Formula** | Where the parameter enters |
| **Current Status** | `Fitted` / `Derived` / `Semi-empirical` |
| **Data Used** | What data it was fitted to (if any) |
| **Gap** | Which Gap task addresses this parameter |

---

## Active (Not Yet Derived) Parameters

| Parameter | Domain | Formula | Current Status | Data Used | Gap |
|---|---|---|---|---|---|
| **B̃** (logarithmic correction) | Fine structure α | V_eff(n) = An² − B̃·n·ln(n) | Semi-empirical | SM gauge-boson content (N_eff = 12) | Gap 6 |
| **R factor** | Fine structure α | B coefficient from N_eff | Semi-empirical | SM particle spectrum | Gap 6 |
| **Λ** (cosmological constant) | Cosmology / GR | FRW embedding | Semi-empirical | CMB Planck data | — |
| **Electroweak mixing angle** | Standard Model | SU(2)×U(1) embedding | Semi-empirical (Sketch) | PDG value sin²θ_W = 0.231 | — |
| **R_ψ** (ψ-circle radius) | Geometry / α | R_ψ = ℏ/(m_e·c) | Calibrated | m_e (electron mass, PDG) | Task 3 |
| **C/A ratio** (curvature-to-kinetic) | Geometry / α | α_predicted = C/(2A) | Sketch | required C/A = 2α_exp for α ≈ 1/137 | Task 2 |

---

## Promoted: Formerly Fitted, Now Derived

| Parameter | Derived in | Gap | Reference | Date |
|---|---|---|---|---|
| **A** (quadratic coefficient) | KK kinetic energy: A = ℏ²/(2m_field·R_ψ²) | Gap 1 | [`Appendix_H_Theta_Phase_Emergence.tex`](../Appendix_H_Theta_Phase_Emergence.tex) §H.3a.3 | 2025 |

---

## Notes

- **B̃**: The one-loop logarithmic coefficient B̃ in V_eff(n) = An² − B̃·n·ln(n) remains
  semi-empirical pending the full one-loop computation (Gap 6).
  The A coefficient has been derived analytically from Kaluza-Klein kinematics (Gap 1).

- **A coefficient derivation (Gap 1):** A = κ/R_ψ² = ℏ²/(2m_field·R_ψ²), derived from
  the kinetic energy of winding-n KK configurations on S¹ of radius R_ψ.
  No free parameters: κ and R_ψ are determined by the UBT field content.
  See `ubt_core/verify_Vpsi.py` class `WindingPotential`.

- **R_ψ (Task 3 result):** The identification R_ψ = ℏ/(m_e·c) is necessary for
  consistency but was not derivable from pure geometry (2026-03-04).
  Three topological candidates were tested (self-duality, winding consistency,
  modularity) — all dead ends or reproductions of the calibrated value.
  See `canonical/geometry/biquaternionic_vacuum_solutions.tex §2` for the analysis.
  Status remains: **Calibrated** — will be promoted to Derived when a geometric
  derivation of R_ψ independent of m_e is found.

- **C/A ratio (Task 2 result):** The stationarity conditions on the (t,ψ) torus give
  α_predicted = C/(2A) for the simplest curvature potential U_geom = −C/(R_t·R_ψ).
  The ratio C/A = 2α_exp ≈ 0.01460 is required for α_predicted = α_exp.
  This is a prediction for the biquaternionic curvature-to-kinetic ratio.
  Computing C from ℒ_geom closes the derivation (currently [SKETCH]).
  See `tools/m0_from_torus.py` and `appendix_E_m0_derivation_strict.tex §E.4`.

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
