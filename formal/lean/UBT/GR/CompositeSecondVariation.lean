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

/-- The full bilinear Hessian chain rule, for arbitrary pairs of variations.
Both derivatives on the right are actual Frechet derivatives of the stated
functions. This includes the derivative of the substituted connection/tetrad
map whenever it is part of g. -/
theorem secondFDeriv_composite
    {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F]
    (f : F → ℝ) (g : E → F) (x u v : E)
    (hf : Differentiable ℝ f) (hg : Differentiable ℝ g)
    (hf₂ : DifferentiableAt ℝ (fderiv ℝ f) (g x))
    (hg₂ : DifferentiableAt ℝ (fderiv ℝ g) x) :
    fderiv ℝ (fderiv ℝ (f ∘ g)) x u v =
      fderiv ℝ (fderiv ℝ f) (g x) (fderiv ℝ g x u) (fderiv ℝ g x v)
        + fderiv ℝ f (g x) (fderiv ℝ (fderiv ℝ g) x u v) := by
  have first : fderiv ℝ (f ∘ g) =
      (fun y => (fderiv ℝ f (g y)).comp (fderiv ℝ g y)) := by
    funext y
    exact fderiv_comp y (hf (g y)) (hg y)
  rw [first]
  have hd := hf₂.hasFDerivAt.comp x (hg x).hasFDerivAt
  have hfull := hd.clm_comp hg₂.hasFDerivAt
  simpa [add_comm] using
    congrArg (fun A : E →L[ℝ] E →L[ℝ] ℝ => A u v) hfull.fderiv

end UBT.GR
