# Biquaternion Operator Update (v1)

## Purpose
This patch upgrades the operator `M_BQ` to its full 8D definition on 
$\mathbb{C}\otimes\mathbb{H}$ and introduces Lean formal structures for rigorous proof.

## Steps
1. Unzip this archive into the **root** of your repo `unified-biquaternion-theory/`.
2. Rebuild Lean sources:
   ```bash
   cd lean
   lake build
   ```
3. Check syntax:
   ```bash
   lean --check src/BiQuaternion/Operators.lean
   ```
4. Run Copilot to formalize lemma `M_BQ_selfadjoint` (currently `sorry`).
5. Recompile LaTeX and verify that `docs/spectral_framework.pdf` reflects the new definitions.

## Next Tasks
- Extend `V(τ_BQ)` to symbolic potential preserving Hermiticity.
- Define domain of `M_BQ` in `FunctionalAnalysis.lean`.
- Compute symbolic form of $(M_{BQ})^\dagger M_{BQ}$.
