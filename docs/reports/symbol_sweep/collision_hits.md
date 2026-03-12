# Symbol Collision Hits: `\mathcal{G}_{\mu\nu}` used as Einstein tensor

**Date**: 2026-02-28  
**Sweep**: `ubt_symbol_collision_sweep_v3`

**Rule**: `\mathcal{G}_{\mu\nu}` must denote ONLY the biquaternionic metric.  
`\mathcal{E}_{\mu\nu}` denotes the biquaternionic Einstein tensor.

---

## Detection Patterns (4 types)

| Pattern ID | Regex / text signal | Meaning |
|-----------|---------------------|---------|
| P1 | `\mathcal{G}_{\mu\nu} = \kappa` | Field equation LHS — Einstein tensor |
| P2 | `\mathcal{G}_{\mu\nu} = \mathcal{R}` | Einstein-tensor definition |
| P3 | `Einstein tensor.*\mathcal{G}` or `\mathcal{G}.*Einstein tensor` | Prose labelling G as Einstein |
| P4 | `G_{\mu\nu}.*Re(\mathcal{G}` or `\Re(\mathcal{G}.*= \kappa` | Real projection of Einstein tensor |

---

## Hits by File (before sweep)

### `canonical/geometry/biquaternion_curvature.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 123 | `\boxed{\mathcal{G}_{\mu\nu} = \mathcal{R}_{\mu\nu} - ...}` | P2 | LHS → `\mathcal{E}_{\mu\nu}` |
| 136 | `G_{\mu\nu} = \text{Re}(\mathcal{G}_{\mu\nu}) = R_{\mu\nu} - ...` | P4 | `Re(\mathcal{G})` → `Re(\mathcal{E})` |
| 167 | `\nabla^\mu \mathcal{G}_{\mu\nu} = 0` | P2 (Bianchi for Einstein) | → `\nabla^\mu \mathcal{E}_{\mu\nu} = 0` |
| 242 | `\boxed{\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}}` | P1 | LHS → `\mathcal{E}_{\mu\nu}` |
| 247 | `$\mathcal{G}_{\mu\nu} = \mathcal{R}_{\mu\nu} - ... $ is the biquaternionic Einstein tensor` | P2+P3 | LHS → `\mathcal{E}_{\mu\nu}` |
| 257 | `\text{Re}(\mathcal{G}_{\mu\nu}) = \kappa \text{Re}(\mathcal{T}_{\mu\nu})` | P4 | → `\text{Re}(\mathcal{E}_{\mu\nu})` |
| 272 | `\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu} \quad \text{(biquaternionic)}` | P1 | → `\mathcal{E}_{\mu\nu}` |
| 378 | `\mathcal{G}_{\mu\nu} = \mathcal{R}_{\mu\nu} - \frac{1}{2} \mathcal{G}_{\mu\nu} \mathcal{R}` | P2 | LHS → `\mathcal{E}_{\mu\nu}` |
| 383 | `G_{\mu\nu} = \text{Re}(\mathcal{G}_{\mu\nu})` | P4 | → `Re(\mathcal{E}_{\mu\nu})` |

### `canonical/UBT_canonical_main.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 210 | `\boxed{\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}}` | P1 | → `\mathcal{E}_{\mu\nu}` |
| 215 | `$\mathcal{G}_{\mu\nu} = \mathcal{R}_{\mu\nu} - ...$ is the biquaternionic Einstein tensor` | P2+P3 | LHS → `\mathcal{E}_{\mu\nu}` |
| 233 | `\text{Re}(\mathcal{G}_{\mu\nu}) = \kappa \text{Re}(\mathcal{T}_{\mu\nu})` | P4 | → `Re(\mathcal{E})` |
| 297 | `\mathcal{G}_{\mu\nu} + \Lambda \mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}` | P1 | First `\mathcal{G}` → `\mathcal{E}` |

### `canonical/geometry/curvature.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 165 | `G_{\mu\nu} = \text{Re}(\mathcal{G}_{\mu\nu})` | P4 | → `Re(\mathcal{E})` |
| 168 | `$\mathcal{G}_{\mu\nu} = \mathcal{R}_{\mu\nu} - ...$ is the biquaternionic Einstein tensor.` | P2+P3 | LHS → `\mathcal{E}` |
| 206 | `\mathcal{G}_{\mu\nu} = \kappa ... \Rightarrow \text{Re}(\mathcal{G}_{\mu\nu}) = ...` | P1+P4 | Both → `\mathcal{E}` |
| 219 | `\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu} \quad \text{(biquaternionic)}` | P1 | → `\mathcal{E}` |
| 370 | `Einstein tensor $\mathcal{G}_{\mu\nu} \to G_{\mu\nu}$` | P3 | → `\mathcal{E}` |
| 371 | `Field equation $\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu} \to ...$` | P1 | → `\mathcal{E}` |

### `canonical/geometry/stress_energy.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 153 | `\mathcal{G}_{\mu\nu} = \kappa ... \Rightarrow \text{Re}(\mathcal{G}_{\mu\nu}) = ...` | P1+P4 | Both → `\mathcal{E}` |

### `canonical/geometry/biquaternion_stress_energy.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 208 | `\boxed{\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}}` | P1 | → `\mathcal{E}` |
| 213 | `$\mathcal{G}_{\mu\nu} = \mathcal{R}_{\mu\nu} - ...$ is the biquaternionic Einstein tensor` | P2+P3 | LHS → `\mathcal{E}` |
| 224 | `\text{Re}(\mathcal{G}_{\mu\nu}) = \kappa \text{Re}(\mathcal{T}_{\mu\nu})` | P4 | → `Re(\mathcal{E})` |
| 239 | `\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}` | P1 | → `\mathcal{E}` |
| 405 | `\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}` | P1 | → `\mathcal{E}` |

### `consolidation_project/appendix_R_GR_equivalence.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 10 | `\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu} \quad \text{where } \mathcal{G}_{\mu\nu}...` | P1 | Both `\mathcal{G}` on LHS and in `where` → `\mathcal{E}` |
| 15 | `G_{\mu\nu} := \text{Re}(\mathcal{G}_{\mu\nu}) = 8\pi G ...` | P4 | → `Re(\mathcal{E})` |

### `consolidation_project/appendix_FORMAL_emergent_metric.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 251 | `G_{\mu\nu} = \Re\left(\mathcal{G}_{\mu\nu}\right),` | P4 | → `Re(\mathcal{E})` |
| 253 | `$\mathcal{G}_{\mu\nu}$ is the biquaternionic Einstein tensor satisfying $\mathcal{G}_{\mu\nu} = \kappa...$` | P3+P1 | Both → `\mathcal{E}` |
| 316 | `From the biquaternionic field equation $\mathcal{G}_{\mu\nu} = \kappa...$` | P1 | → `\mathcal{E}` |
| 318 | `\Re(\mathcal{G}_{\mu\nu}) &= \Re(\kappa\mathcal{T}_{\mu\nu})` | P4 | → `Re(\mathcal{E})` |

### `UBT_Main.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 52 | `The fundamental equation is $\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}$ (biquaternionic Einstein tensor).` | P1+P3 | → `\mathcal{E}` |

### `THEORY_STATUS_DISCLAIMER.tex`

| Line | Snippet | Pattern | Fix |
|------|---------|---------|-----|
| 38 | `The fundamental equation is $\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}$ (biquaternionic).` | P1 | → `\mathcal{E}` |

---

## Metric uses preserved (NOT changed)

These occurrences correctly use `\mathcal{G}_{\mu\nu}` as the biquaternionic metric and are left unchanged:

- `g_{\mu\nu} := \text{Re}(\mathcal{G}_{\mu\nu})` (everywhere)
- `\mathcal{G}_{\mu\nu} = \text{Sc}(E_\mu E_\nu^\dagger)` (metric definition)
- `\mathcal{G}^{\mu\nu}`, `\mathcal{G}^{\rho\sigma}` (inverse metric)
- `\det \mathcal{G}` (metric determinant)
- `\text{Im}(\mathcal{G}_{\mu\nu})` (imaginary part of metric, dark sector)
- `\mathcal{G}_{\mu\nu} \to g_{\mu\nu}` in the "Biquaternionic metric" list item of the GR summary
- `- \frac{1}{2}\mathcal{G}_{\mu\nu}\mathcal{R}` on the RHS (metric × Ricci scalar)
- `- \frac{1}{2}\mathcal{G}_{\mu\nu}\langle D\Theta, D\Theta\rangle` (metric in stress-energy)
- `\mathcal{P}\mathcal{G}_{\mu\nu}` (pressure term in perfect fluid)
- `\mathcal{G}_{\mu\nu}\mathcal{F}...` (EM tensor metric factor)
