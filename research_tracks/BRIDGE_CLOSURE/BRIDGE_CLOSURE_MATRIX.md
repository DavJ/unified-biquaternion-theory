# UBT Bridge Closure Matrix

Status vocabulary:

- **CLOSED-L1** — closed inside the current UBT bridge assumptions.
- **PARTIAL-L1** — main theorem exists, but sub-bridges remain open.
- **OPEN** — not closed; should not be used as a theorem.
- **MC** — motivated candidate.
- **LEGACY** — older route or outdated wording.

## Core bridge list

| ID | Bridge | Role | Current status | Main files | Remaining task |
|---|---|---|---|---|---|
| B1 | EM modular coupling bridge | Identifies fixed-point winding modulus `n` with `alpha^-1` | **CLOSED-L1** | `research_tracks/T3_ALPHA/em_modular_coupling_identification.tex`, `alpha_derivation_complete.tex` | External presentation only; no hidden numeric fit. |
| B2 | Layer2 readout / alpha kernel bridge | Gives `r_L2 = 3(1+Omega_eta)` and information-loss readout | **CLOSED-L1 inside alpha chain**, with legacy files still carrying older wording | `research_tracks/T3_ALPHA/layer2_kernel_derivation.tex`, `gap_A_proof.tex`, `information_loss_alpha_self_consistency.tex` | Harmonise legacy status wording; defend canonical Layer2 map in paper. |
| B3 | Odd-spinor EW threshold bridge | Gives active RG spectrum and `b1=33/5`, `b2=1`, `b3=-3` | **CLOSED-L1** | `research_tracks/EW/weinberg_angle_odd_spinor_threshold_beta_theorem.tex`, `weinberg_angle_mz_bridge_closure.tex` | Defend odd-spinor threshold interpretation externally. |
| B4 | Self-dual radius bridge | Fixes dimensionless `R_psi=1` / `R_psi=R_t` | **CLOSED-L1 at one-loop/self-dual level** | `canonical/geometry/Rpsi_dynamical_fix.tex`, `research_tracks/T3_ALPHA/gap_A_proof.tex` | Do not relabel as open. The open part is physical scale calibration. |
| B5 | Physical scale calibration bridge | Maps self-dual unit `R_psi=1` to `M_UBT ≈ 2e16 GeV` | **PARTIAL / MC** | `research_tracks/EW/rpsi_from_action.tex` | Derive the physical unit / condensate normalization exactly from `S[Theta]`. |
| B6 | Hypercharge bridge | Derives SM hypercharge table | **PARTIAL-L1** | `research_tracks/EW/hypercharge_from_ubt.tex` | Close C2-ii and C2-iii: baryon `U(1)_B` from psi winding and `B-L` coupling normalisation. |
| B7 | Metric / GR bridge | Reads effective metric and Einstein chain from `Theta` | **PARTIAL-L1** | `canonical/bridges/GR_chain_bridge.tex`, `canonical/gr_closure/step1_metric_bridge.tex` | Off-shell `Theta`-only closure remains open. |
| B8 | QCD / colour bridge | Connects Layer2 colour subspace to `SU(3)_c` | **PARTIAL-L1 / semi-empirical components** | `canonical/bridges/gauge_emergence_bridge.tex`, `canonical/interactions/colour_charge_lattice.tex` | Derive full adjoint gluon sector, beta coefficient, and confinement-compatible structure cleanly. |
| B9 | QED running bridge | Connects alpha(0) to alpha(MZ) for Weinberg closure | **PARTIAL-L1 / standard-QED compatible** | `research_tracks/qed_alpha_derivation/`, `research_tracks/EW/weinberg_angle_mz_bridge_closure.tex` | Put the alpha-to-MZ running into the Weinberg paper with explicit scheme assumptions. |

## Corrected `R_psi` statement

The old phrasing “derive `R_psi=1`” is no longer correct as an open task.
The repository already has an L1 self-dual derivation:

```text
R_psi = R_t, hence R_psi = 1 in natural units.
```

The remaining bridge is instead:

```text
why the self-dual psi unit corresponds physically to M_UBT ≈ 2e16 GeV.
```

## Recommended closure order

1. **B2 status harmonisation** — remove outdated “sole remaining gap” wording from legacy alpha files.
2. **B5 physical scale calibration** — turn the Scherk--Schwarz / gauge-condensate candidate into a theorem.
3. **B6 hypercharge sub-bridges** — close C2-ii and C2-iii.
4. **B8 QCD colour bridge** — write a theorem-level colour-sector paper.
5. **B7 GR off-shell bridge** — close the last GR structural gap.

## Strategic status

Alpha and Weinberg are now bridge-proven inside the current UBT assumptions.
The next stage is not to add new constants, but to promote the most important bridges from `CLOSED-L1 relative to bridges` to `canonical theorem`.
