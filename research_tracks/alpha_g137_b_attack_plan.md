<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Gap G137-B Attack Plan (focused, non-claiming)

## Exact statement of Gap G137-B

Given

- `V_eff(n) = n^2 - B n log n`
- stationarity `2n* = B(log n* + 1)`

derive the effective coupling `B ≈ 46.284–46.298` directly from UBT primitives and
`S[Θ]`, without using `alpha_exp`, `137`, or back-solved `B_required` as input.

## What is already derived

- Effective potential structure `V_eff(n) = n^2 - B n log n`.
- Stationary condition `2n* = B(log n* + 1)`.
- Prime stability logic for discrete prime minimizers.
- One-loop baseline `B0 = 8π ≈ 25.133` (safe baseline, still insufficient for 137).

## What is not derived

- `B ≈ 46.284–46.298` from `S[Θ]`.
- Physical correction `137 -> 137.036` from first principles.

## Failed / obsolete routes

- Constant winding correction `ΔB ≈ 18.5` as a constant shift: **obsolete / NO-GO**.
- Any route that inserts `alpha_exp` or `137` by hand and then claims derivation.

## Candidate derivation routes

### A. Heat-kernel / spectral determinant correction to B

- **Input assumptions**: spectral expansion of `det(∇†∇)` on the UBT background is well-defined and renormalized non-circularly.
- **Equations to derive**: closed expression for loop-corrected coefficient multiplying `n log n` in `V_eff`.
- **Possible failure mode**: corrections produce `n`-dependent coefficients or non-log terms only.
- **How to falsify**: show all admissible Seeley–DeWitt terms fail to yield a constant additive shift to `B` near +21.15.
- **Constant-B or n-dependent**: can produce either; must isolate constant part explicitly.

### B. Modular index route via `μ(Γ0(137))/3 = 46`

- **Input assumptions**: modular quantity enters from UBT partition structure, not by selecting 137 externally.
- **Equations to derive**: map from modular invariant/index computed from `S[Θ]` to the `B` coefficient in `V_eff`.
- **Possible failure mode**: remains numerical coincidence with no action-level insertion theorem.
- **How to falsify**: prove modular index can be varied without changing the derived `B` term in the action.
- **Constant-B or n-dependent**: target is constant `B`; route fails if only `n`-dependent coupling emerges.

### C. Renormalized entropy / Gamma-function correction

- **Input assumptions**: entropy or determinant regularization contributes a finite universal constant to `B`.
- **Equations to derive**: explicit finite renormalized term from Γ-function / zeta regularization entering the `n log n` coefficient.
- **Possible failure mode**: scheme-dependent finite parts with no canonical fixation.
- **How to falsify**: show correction changes under allowed renormalization schemes without UBT-internal selector.
- **Constant-B or n-dependent**: should produce constant only; otherwise route downgraded.

### D. Representation-counting correction from `C ⊗ H` degrees of freedom

- **Input assumptions**: representation multiplicities beyond one-loop baseline contribute a strict combinatorial factor.
- **Equations to derive**: non-circular multiplicity factor taking `B0=8π` to the required `B` window.
- **Possible failure mode**: multiplicity argument restates already-counted modes or double-counts sectors.
- **How to falsify**: independent counting audit proving no new irreducible mode contribution exists.
- **Constant-B or n-dependent**: intended constant factor; invalid if state-counting depends on `n`.

### E. Two-loop effective action correction

- **Input assumptions**: two-loop terms are computable from UBT action without fitted constants.
- **Equations to derive**: explicit two-loop correction `ΔB^(2)` in the constant `n log n` coefficient.
- **Possible failure mode**: correction too small, wrong sign, or absorbed into higher `n` structure.
- **How to falsify**: full two-loop computation showing bounded contribution far from required range.
- **Constant-B or n-dependent**: must show constant extraction unambiguously.

## Strict success criterion

Gap G137-B is formally resolved only if B is computed from UBT primitives without using
alpha_exp, 137, or B_required as input.
