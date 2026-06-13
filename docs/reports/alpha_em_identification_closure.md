<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Alpha EM identification closure note

This patch attempts to close the final interpretation gap in the UBT alpha
track: why the stationary winding index `n` should be read as `alpha^-1`.

The key observation is standard compact-U(1) gauge theory:

```text
tau_EM = theta_EM/(2*pi) + i * 4*pi/e^2
```

Since `alpha = e^2/(4*pi)`, the imaginary part is:

```text
Im(tau_EM) = 4*pi/e^2 = alpha^-1
```

The UBT electromagnetic winding modulus is written:

```text
tau_EM^UBT = chi + i*n
```

where `n` is the same winding stiffness selected by the eta/Layer2 fixed point.
Matching compact-U(1) Maxwell normalisation gives:

```text
n = 4*pi/e^2 = alpha^-1
```

Status: conditional closure.  The remaining structural assumption is that the
UBT EM projection is the compact unit-charge `U(1)_EM` line bundle of the
low-energy theory.  No new numerical parameter is introduced.
