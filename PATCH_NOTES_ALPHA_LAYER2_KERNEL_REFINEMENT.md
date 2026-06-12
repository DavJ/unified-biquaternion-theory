# Patch notes — alpha Layer2 kernel refinement

This differential patch updates the alpha information-loss research track.

## Main update

The previous sharp Layer2 projection used

```text
r_eff = 3
```

and gave

```text
alpha^-1_UBT = 137.035999142931...
```

The new first eta-kernel refinement uses

```text
r_eff = 3 * (1 + Omega_eta(1))
Omega_eta(1) = sum_{m>=1} m/(exp(2*pi*m)-1)
             = 1/24 - 1/(8*pi)
```

The effective channel coefficient is

```text
C_Q(n) = 4 - ((pi - 3)/2) * ((n - r_eff)/n)
```

## Numerical result

```text
alpha^-1_UBT = 137.035999177549...
```

Compared with CODATA/NIST 2022,

```text
alpha^-1 = 137.035999177(21)
```

this is approximately `+0.026 sigma`.

## Status

Research-track only.

The remaining open theorem is to derive the effective Layer2 readout rank

```text
r_eff = 3 * (1 + Omega_eta(1))
```

from the canonical UBT Layer2 readout/decoding kernel.
