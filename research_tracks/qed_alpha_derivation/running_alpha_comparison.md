<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# running_alpha_comparison.md

## Scope
This note compares the UBT-induced QED running structure with low- and high-scale electromagnetic inverse-coupling values **only after** deriving the RG form from the effective action.

## 1) RG equation from the UBT QED sector
From the low-energy UBT QED action

\[
\mathcal{L}_{\mathrm{eff}}\supset -\frac{1}{4e^2(\mu)}\,\mathcal{F}_{\mu\nu}\mathcal{F}^{\mu\nu}
\]

and vacuum-polarization renormalization of the photon two-point function, one obtains at one loop

\[
\mu\frac{d\alpha}{d\mu}=\frac{b_{\mathrm{em}}}{2\pi}\alpha^2,
\qquad
\frac{d\alpha^{-1}}{d\ln\mu}=-\frac{b_{\mathrm{em}}}{2\pi},
\]

with positive effective coefficient for charged matter content.
Hence

\[
\alpha^{-1}(\mu)=\alpha^{-1}(\mu_0)-\frac{b_{\mathrm{em}}}{2\pi}\ln\frac{\mu}{\mu_0}.
\]

So the predicted qualitative trend is:
- higher scale \(\mu\) \(\Rightarrow\) larger \(\alpha(\mu)\),
- equivalently smaller \(\alpha^{-1}(\mu)\).

## 2) Post-derivation comparison with known checkpoints
After deriving the monotone trajectory above, compare with common checkpoints:
- low-energy inverse coupling near 137,
- electroweak-scale inverse coupling near 127.

This comparison is trend-compatible: inverse coupling decreases from IR to UV, matching the RG direction derived from the UBT QED sector.

## 3) Compatibility with stable integer set `{127, 137, ...}`
The RG flow is continuous in \(\ln\mu\), while stable-set candidates are discrete integers.
Therefore:
- RG alone does **not** select a discrete integer set.
- Discrete values can still be **compatible checkpoints** if they lie on (or near) the continuous trajectory at particular scales.

So compatibility is possible as an after-the-fact consistency relation, not as the primary derivation mechanism.

## 4) Conclusion
- UBT QED sector supports the correct running direction \(\alpha^{-1}(\mu_{\mathrm{low}})>\alpha^{-1}(\mu_{\mathrm{high}})\).
- The low/high inverse-coupling checkpoints are consistent with that trajectory.
- Stable-set integers remain auxiliary comparators, not the source of the running law.
