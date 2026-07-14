# Pure-UBT GR closure status — 2026-07-14

This track uses only the existing UBT field `Theta(q,tau)`, the compact imaginary-time coordinate `psi = Im(tau)`, the induced metric, and the UBT action. It does **not** introduce an independent metric or an external embedding equation.

## Main result

The classical metric is taken in the fiber-completed form

```tex
g_{\mu\nu}(x)=\frac{1}{\mathcal N_0}\frac{1}{2\pi R_\psi}
\int_0^{2\pi R_\psi}
H(\partial_\mu\Theta(x,\psi),\partial_\nu\Theta(x,\psi))\,d\psi,
```

with constant `N_0`. The exact pure-Theta variation produces

```tex
\mathscr F_\Theta
+\frac{1}{\kappa\mathcal N_0}
\nabla_\nu\left[(G^{\mu\nu}-\kappa T^{\mu\nu})\partial_\mu\Theta\right]=0.
```

On the fixed-metric internal Theta shell `F_Theta = 0`, this reduces to the normal closure equation

```tex
(G^{\mu\nu}-\kappa T^{\mu\nu})B_{\mu\nu}=0.
```

If the ten normal vectors `B_{mu nu}` are linearly independent in the space of `psi` profiles, the complete Einstein equation follows.

## Rigorous status split

| Item | Status |
|---|---|
| Exact first variation | **PROVED** |
| Local normalization `N(x)=|<d0Theta,d0Theta>|` | **DISPROVED** for variable lapse |
| Single-`psi` section closure with `Theta in B ~= R^8` | **NO-GO**: closure rank <= 4 |
| Full `psi`-fiber removes the finite-dimensional rank obstruction | **PROVED kinematically** |
| Fiber-free configurations exist | **PROVED** |
| Fiber-free condition is open dense in sufficiently rich finite-mode holomorphic two-jet truncations | **PROVED** |
| Vacuum Einstein equation on fiber-free stationary sector | **PROVED** |
| Einstein equation with matter/gauge | **PROVED CONDITIONAL** on the canonical direct internal Theta equation |
| One-action separation of internal and metric equations | **OPEN** |
| Selected Jacobi-theta solution family is fiber-free | **OPEN** |
| Arbitrary local GR metric has an integrable on-shell Theta representation (GAP-10R) | **OPEN** |
| Global/topological closure | **OPEN** |

## Canonical corrections

1. `Sc(A B^dagger)` and a matrix trace are complex scalars, not full biquaternions. The full biquaternionic object is the unprojected product `Q_{mu nu}=E_mu E_nu^ddagger`.
2. A genuinely biquaternion-valued core field has four complex = eight real components. A generic `4x4` complex matrix is not a biquaternion and must be treated as a separate extension.
3. The `psi`-average is not a new field or new coordinate map. It uses the already postulated dependence `Theta(q,t+i psi)`.
4. Holomorphy or the Jacobi heat equation cannot increase the rank of a single-section metric map. The extra closure capacity comes from retaining the complete `psi` profile before classical projection.

See `canonical/gr_closure/pure_ubt_fiber_closure.tex` for proofs.
