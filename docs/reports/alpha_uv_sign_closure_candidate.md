# Alpha proof closure — compact-psi UV sign candidate

Status: L2 candidate / conditional.

The previous closure reduced the final electroweak condition to the sign of the
quadratic term in the projected potential:

```math
V_EW = V0 - mu_EW^2 Phi^dagger Phi + lambda_EW (Phi^dagger Phi)^2.
```

This patch adds the strongest honest UV closure currently possible without a
fully specified canonical potential V(Theta):

```math
m_eff^2 = m_{0,EW}^2 - Gamma_psi M_psi^2.
```

Under modular criticality

```math
m_{0,EW}^2 = 0,
```

and positive compact-sector stiffness

```math
Gamma_psi > 0,
```

one gets

```math
m_eff^2 < 0,
mu_EW^2 = Gamma_psi M_psi^2 > 0.
```

Then the already-added low-energy theorem gives a non-zero EW minimum; the
Theta0 orbit theorem gives the standard doublet representative; the EM
projection theorem gives primitive U(1)_EM; and the Maxwell modular
identification gives n = alpha^{-1}.

## Remaining work

The remaining work is no longer a vague Higgs-sector gap.  It is the precise UV
problem:

```math
derive m_{0,EW}^2 = 0 and Gamma_psi > 0 from canonical S[Theta].
```

Until those two hypotheses are proven, the alpha derivation should be described
as complete as a conditional chain, not as an unconditional theorem of UBT.
