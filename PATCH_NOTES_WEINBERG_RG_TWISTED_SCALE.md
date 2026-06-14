# Patch notes — Weinberg RG twisted-scale branch

This patch attacks the RG descent of the Weinberg angle after the UBT boundary
condition `sin^2(theta_W)=3/8` has been established.

Added:

- `research_tracks/EW/weinberg_angle_rg_twisted_scale_closure.tex`
- `tools/compute_weinberg_rg_running.py`
- `docs/reports/weinberg_angle_rg_twisted_status.md`

Updated:

- `research_tracks/EW/weinberg_angle_ew1_rg.tex`

Main results:

- Minimal non-supersymmetric SM one-loop running from the 3/8 boundary gives
  `sin^2(theta_W)(M_Z)=0.185469...`; this is an obstruction for that branch.
- A twisted odd-spinor / MSSM-like branch with `b1=33/5`, `b2=1`,
  `M_UBT=2e16 GeV`, and `alpha_UBT^-1=24.3` gives
  `sin^2(theta_W)(M_Z)=0.231143639964`.
- The exact reference `0.23122` corresponds to
  `alpha_UBT^-1=24.325465722412` on that branch.

Status:

- GUT boundary: L1.
- RG-to-MZ: viable on twisted odd-spinor branch, still conditional.
- Remaining proof tasks: derive twisted beta coefficients, scale, and unified
  coupling from canonical UBT.
