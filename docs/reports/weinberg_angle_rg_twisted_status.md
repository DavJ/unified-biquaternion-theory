# Weinberg angle RG twisted-branch status

Status: research track / L1 conditional.

The UBT generator-norm theorem gives the boundary value

```text
sin^2(theta_W)(M_UBT) = 3/8.
```

The next question is whether RG running can connect this boundary to the
Z-pole value.

## Minimal SM one-loop branch

Using

```text
b1 = 41/10, b2 = -19/6,
M_UBT = 2e16 GeV,
alpha_UBT^-1 = 40,
```

the one-loop result is

```text
sin^2(theta_W)(M_Z) = 0.185469...
```

This is an obstruction for the minimal non-supersymmetric one-loop branch.

## Twisted odd-spinor / MSSM-like branch

The odd-winding spinor sector already used in the alpha proof suggests a
twisted Layer2 threshold with effective one-loop coefficients

```text
b1 = 33/5, b2 = 1.
```

With

```text
M_UBT = 2e16 GeV,
alpha_UBT^-1 = 24.3,
```

the one-loop result is

```text
sin^2(theta_W)(M_Z) = 0.231143639964.
```

The exact reference value 0.23122 would require

```text
alpha_UBT^-1 = 24.325465722412.
```

## Remaining gap

This is not yet a full canonical proof of the Z-pole Weinberg angle.  The
remaining precise tasks are:

1. derive the twisted odd-spinor threshold spectrum and hence `b1=33/5`,
   `b2=1` from the UBT Layer2 Hilbert space;
2. derive `M_UBT ≈ 2e16 GeV` from the compact ψ-radius / moduli sector;
3. derive `alpha_UBT^-1 ≈ 24.3` from the same UBT normalisation.

Thus the Weinberg angle status is:

```text
GUT boundary: proven within UBT hypercharge bridge assumptions.
RG-to-MZ: viable on the twisted odd-spinor branch, still conditional.
```
