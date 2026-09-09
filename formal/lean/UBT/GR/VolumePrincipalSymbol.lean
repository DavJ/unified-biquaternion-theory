import UBT.GR.VolumeVariation

/-!
# The actual first-jet Hessian of the volume density

The second Frechet derivative exists because the determinant density is a
polynomial in the first jet. Its contraction with a common spacetime covector
vanishes in every pair of Lorentz-real field directions. No smoothness or
zero-symbol assumption is substituted for a proof about this density.

This is the second-order principal-symbol statement for the displayed local
action family. The integrated Euler/Jacobi formula and a general connection
depending on field derivatives are separate statements.
-/

namespace UBT.GR

/-- Relate genuine mixed real derivatives along affine lines to the Frechet
Hessian. The assumptions concern ordinary differentiability only. -/
theorem mixedSecondDeriv_eq_fderiv
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (L : E → ℝ) (hL : Differentiable ℝ L)
    (hL₂ : Differentiable ℝ (fderiv ℝ L)) (p u v : E) :
    deriv (fun s : ℝ => deriv (fun t : ℝ => L (p + s • u + t • v)) 0) 0 =
      fderiv ℝ (fderiv ℝ L) p u v := by
  have line (q w : E) : HasDerivAt (fun t : ℝ => q + t • w) w 0 := by
    simpa using ((hasDerivAt_id (0 : ℝ)).smul_const w).const_add q
  have first (q : E) :
      deriv (fun t : ℝ => L (q + t • v)) 0 = fderiv ℝ L q v := by
    simpa only [Function.comp_apply, zero_smul, add_zero] using
      ((hL (q + (0 : ℝ) • v)).hasFDerivAt.comp_hasDerivAt 0 (line q v)).deriv
  simp_rw [first]
  have hd := (hL₂ (p + (0 : ℝ) • u)).hasFDerivAt.comp_hasDerivAt 0 (line p u)
  have ha := hd.clm_apply (hasDerivAt_const (0 : ℝ) v)
  simpa using ha.deriv

namespace VolumeVariation

set_option maxHeartbeats 4000000 in
theorem contDiff_density_firstJet (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) : ContDiff ℝ 2 (density c f b x) := by
  simp only [density, ← detFour_eq_det, detFour,
    Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
  fun_prop

/-- The first-jet symbol is defined using the actual second Frechet derivative. -/
def firstJetSymbol (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) (p : Mat) (k u v : Vec) : ℝ :=
  fderiv ℝ (fderiv ℝ (density c f b x)) p (rankOne k u) (rankOne k v)

/-- All second-order field blocks vanish for any jet, covector and field pair.
The additive connection shift and scalar weight may depend on field values. -/
theorem firstJetSymbol_eq_zero (c : ℝ) (f : Vec → ℝ) (b : Vec → Mat)
    (x : Vec) (p : Mat) (k u v : Vec) :
    firstJetSymbol c f b x p k u v = 0 := by
  have hc := contDiff_density_firstJet c f b x
  have hL : Differentiable ℝ (density c f b x) := hc.differentiable (by norm_num)
  have hc₁ : ContDiff ℝ 1 (fderiv ℝ (density c f b x)) :=
    (contDiff_succ_iff_fderiv.mp hc).2.2
  have hL₂ : Differentiable ℝ (fderiv ℝ (density c f b x)) :=
    hc₁.differentiable one_ne_zero
  exact (mixedSecondDeriv_eq_fderiv (density c f b x) hL hL₂ p
    (rankOne k u) (rankOne k v)).symm.trans
    (mixedSecondDeriv_density_common_covector c f b x p k u v)

end VolumeVariation
end UBT.GR
