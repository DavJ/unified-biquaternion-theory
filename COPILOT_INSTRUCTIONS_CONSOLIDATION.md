# COPILOT MASTER INSTRUCTIONS FOR UBT CONSOLIDATION

## Phase 1 — Directory restructuring
1. Create directory: canonical/
2. Move all legacy TeX/MD into "original_release_of_ubt/"
3. Create subfolders:
   canonical/fields/
   canonical/geometry/
   canonical/interactions/
   canonical/consciousness/
   canonical/appendices/

## Phase 2 — Canonical definitions
Use ONLY these definitions:
- Theta field: Theta(q, tau) ∈ C^(4x4) (extendable to 8x8)
- Complex time: tau = t + i psi
- Metric:
    g_{μν} = Re Tr(∂μΘ ∂νΘ†)
- Stress-energy tensor:
    T_{μν} = ∂μΘ ∂νΘ† 
             - 1/2 g_{μν} g^{αβ} ∂αΘ ∂βΘ†
- QED/QCD Lagrangian:
    L = Tr[(DμΘ)† (DμΘ)] 
        - 1/4 Fμν Fμν 
        - 1/4 Gμν^a Gμν^a

## Phase 3 — Consolidation
- Remove duplicate versions of complex time, metric, stress-energy.
- Rewrite all appendix derivations to use the canonical definitions.
- Merge all QED sections into single file canonical/interactions/qed.tex.
- Merge all QCD sections into canonical/interactions/qcd.tex.

## Phase 4 — Symbol unification
- α must ONLY mean coupling constant.
- ψ must ONLY mean imaginary component of complex time.
- q must ONLY mean biquaternion coordinate with 4 DOF (extendable).
- Remove all conflicting uses.

## Phase 5 — Main article
- Create UBT_main.tex in canonical/
- Structure it into 12 sections:
  1. Introduction
  2. Biquaternion algebra
  3. Theta field
  4. Complex time
  5. Geometry and metric
  6. Stress-energy tensor
  7. Einstein equation
  8. QED
  9. QCD
 10. Theta-functions and torus
 11. Psychons and consciousness
 12. Experimental designs

## Phase 6 — Remove experimental drafts
Move holography, p-adic, dark energy, etc.
into directory research_extensions/.


