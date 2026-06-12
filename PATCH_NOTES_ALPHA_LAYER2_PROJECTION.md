# Patch notes — alpha Layer2 projection correction

This differential patch updates the alpha information-loss research track.

## Main update

The paper now interprets the finite correction through Layer2
observable-sector coding/projection:

```text
C_Q(n) = 4 - ((pi - 3)/2) * ((n - 3)/n)
```

where

```text
(pi - 3)/2 = 12*pi*sum_{m>=1} m/(exp(2*pi*m)-1)
```

comes from the self-dual eta spectrum, and

```text
(n - 3)/n
```

is the proposed Layer2 projection-rank factor associated with the protected
three-dimensional SU(3)/color-code subspace.

## Numerical result

```text
alpha^-1_UBT = 137.035999142931...
```

Compared with CODATA/NIST 2022,

```text
alpha^-1 = 137.035999177(21)
```

this is approximately `-1.62 sigma`.

## Status

Research-track only. The remaining open theorem is to derive the Layer2
projection-rank factor from the canonical UBT projection kernel.
