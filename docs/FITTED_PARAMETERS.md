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

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
