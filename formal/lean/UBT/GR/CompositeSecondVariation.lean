import Mathlib

/-!
# Complete second-variation chain rule

For an actual twice differentiable scalar function and a twice differentiable
curve, the composite second derivative has both the pulled-back Hessian and
the derivative applied to the curve's acceleration. The hypotheses specify
ordinary first and second derivatives; they do not assume the conclusion or
stationarity. The second term cannot be discarded just because the map being
substituted is called a composite tetrad.
-/

namespace UBT.GR

theorem hasSecondVariation_composite
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (f : E → ℝ) (g g₁ : ℝ → E) (g₂ : E) (t : ℝ)
    (H : E →L[ℝ] E →L[ℝ] ℝ)
    (hf : Differentiable ℝ f)
    (hH : HasFDerivAt (fderiv ℝ f) H (g t))
    (hg : ∀ r, HasDerivAt g (g₁ r) r)
    (hg₂ : HasDerivAt g₁ g₂ t) :
    HasDerivAt (fun r => deriv (f ∘ g) r)
      (H (g₁ t) (g₁ t) + fderiv ℝ f (g t) g₂) t := by
  have first : (fun r => deriv (f ∘ g) r) =
      (fun r => fderiv ℝ f (g r) (g₁ r)) := by
    funext r
    exact ((hf (g r)).hasFDerivAt.comp_hasDerivAt r (hg r)).deriv
  rw [first]
  have hd := hH.comp_hasDerivAt t (hg t)
  exact hd.clm_apply hg₂

theorem secondVariation_composite
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (f : E → ℝ) (g g₁ : ℝ → E) (g₂ : E) (t : ℝ)
    (H : E →L[ℝ] E →L[ℝ] ℝ)
    (hf : Differentiable ℝ f)
    (hH : HasFDerivAt (fderiv ℝ f) H (g t))
    (hg : ∀ r, HasDerivAt g (g₁ r) r)
    (hg₂ : HasDerivAt g₁ g₂ t) :
    deriv (fun r => deriv (f ∘ g) r) t =
      H (g₁ t) (g₁ t) + fderiv ℝ f (g t) g₂ :=
  (hasSecondVariation_composite f g g₁ g₂ t H hf hH hg hg₂).deriv

end UBT.GR
