# Alpha proof closure — non-zero electroweak minimum

Status: L1 conditional theorem.

This report records the next closure step in the alpha derivation.  The previous
Theta0 vacuum-orbit theorem reduced the electroweak part of the alpha proof to
the existence of a non-zero minimum in the minimal electroweak doublet sector.

The new theorem makes that condition explicit.  For the projected potential

```math
V_EW(Phi) = V0 - mu_EW^2 Phi^dagger Phi + lambda_EW (Phi^dagger Phi)^2,
lambda_EW > 0,
mu_EW^2 > 0,
```

the global minimum is non-zero:

```math
Phi^dagger Phi = mu_EW^2/(2 lambda_EW) = v^2/2.
```

Combined with the Theta0 orbit theorem, this gives

```math
Theta0 ~ (0, v/sqrt(2))^T,
Y = 1.
```

Then the EM projection theorem gives

```math
Q_EM = T3 + Y/2,
```

and the compact-U(1) Maxwell modular identification gives

```math
n = 4 pi/e^2 = alpha^{-1}.
```

## Remaining condition

The remaining condition is no longer the existence of a non-zero minimum in a
stable low-energy potential.  It is the UV/sign problem:

```math
derive mu_EW^2 > 0 from the full canonical S[Theta].
```

This should remain explicitly conditional until a canonical UBT derivation of
the electroweak symmetry-breaking sign and scale is added.
