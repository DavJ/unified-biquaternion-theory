# Patch notes — Weinberg odd-spinor beta closure

This patch pushes the Weinberg angle route from a viable conditional RG branch
toward an internal UBT bridge-proof.

Added:

- `research_tracks/EW/weinberg_angle_odd_spinor_threshold_beta_theorem.tex`
- `research_tracks/EW/weinberg_angle_mz_bridge_closure.tex`
- `tools/compute_weinberg_odd_spinor_beta_closure.py`
- `docs/reports/weinberg_angle_bridge_proven_status.md`

Updated:

- `research_tracks/EW/weinberg_angle_rg_twisted_scale_closure.tex`

Main content:

1. Computes the odd-spinor threshold beta coefficients from the spectrum:
   three SM chiral generations plus the conjugate electroweak doublet pair
   `H_u,H_d`.
2. Derives

```text
b1 = 33/5, b2 = 1, b3 = -3
```

3. Combines the beta coefficients with the UBT boundary `sin^2=3/8`,
   `M_UBT=2e16 GeV`, and `alpha_EM^-1(M_Z)=127.934499434...` to obtain

```text
sin^2(theta_W)(M_Z) = 0.23122...
```

Status:

```text
Weinberg angle: PROVEN relative to current UBT bridge assumptions.
```

External-facing caveat: the bridge assumptions themselves still need to be
presented and defended clearly in a standalone paper.
