<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Theta Complex-Time Bridge

Status: Bridge / non-canonical derivation

Purpose: This document introduces a mathematically structured bridge between the Jacobi-theta complex-time construction and the operator language already present in Unified Biquaternion Theory (UBT). It does not replace the canonical UBT definitions in `canonical/fields/biquaternion_time.tex` or `canonical/fields/theta_field.tex`.

## Claim Labels

- Canonical: statement already present in canonical UBT material.
- Bridge: mathematically motivated compatibility statement connecting the theta formalism to UBT.
- Conjectural: plausible extension not yet derived inside canonical UBT.

## Motivation

Canonical: UBT already uses biquaternion time

$$
T_B = t + i\psi + j\chi + k\xi,
$$

with the complex-time limit

$$
\tau = t + i\psi
$$

in the isotropic sector.

Bridge: The Jacobi-theta construction provides a compact reduced model in which the real part of complex time generates quadratic phase evolution while the imaginary part generates Gaussian damping. This gives a controlled mathematical bridge between complex time, diffusion-like structure, and reduced propagator-like observables.

Conjectural: A full derivation of the complete UBT field content, metric sector, or Standard Model sector from this reduced theta construction is not established here.

## Jacobi Theta Starting Point

Bridge: Start from the classical Jacobi theta function

$$
\theta(z,\tau) = \sum_{n \in \mathbb{Z}} \exp\!\left(\pi i \tau n^2 + 2\pi i n z\right),
\qquad \Im(\tau) > 0.
$$

Bridge: Introduce complex time in the reduced theta model as

$$
\tau = t + i\phi.
$$

Bridge: Then

$$
\exp(\pi i \tau n^2) = \exp(-\pi \phi n^2)\,\exp(\pi i t n^2).
$$

Bridge: This separates the kernel into a damping factor and an oscillatory quadratic-phase factor.

## Discrete Theta Projection

Bridge: For a reduced discrete mode sequence $a_n^{(s)}$, define the theta projection amplitude

$$
S_s(t,\phi) = \sum_{n=0}^{N-1} a_n^{(s)}\,\exp(-\pi \phi n^2)\,\exp(\pi i t n^2).
$$

Bridge: The index $s$ is an external evolution label for the reduced system. It is not the same object as the internal kernel time $t$, and it is not the same object as the damping parameter $\phi$.

Bridge: The decomposition has the following interpretation.

- $a_n^{(s)}$: reduced discrete mode amplitude or projected field component.
- $t$: real kernel time controlling quadratic phase evolution.
- $\phi$: imaginary diffusion or damping scale in the reduced complex-time kernel.
- $s$: external evolution index attached to the family of reduced mode sequences.

## Energy Observable

Bridge: Define the energy-like observable

$$
\Theta_s(t,\phi) = \left|S_s(t,\phi)\right|^2.
$$

Bridge: Expanding gives

$$
\Theta_s(t,\phi)
=
\sum_{n,m}
a_n^{(s)}\overline{a_m^{(s)}}\,
\exp\!\left(-\pi \phi (n^2+m^2)\right)\,
\exp\!\left(\pi i t (n^2-m^2)\right).
$$

Bridge: This double-sum form makes pairwise mode interference explicit. The single-sum and double-sum forms are equivalent at the level of the energy observable.

## Phi-Averaged Observable

Bridge: To reduce sensitivity to a single damping scale, define

$$
\overline{\Theta}_s(t) = \frac{1}{P}\sum_{j=1}^{P}\Theta_s(t,\phi_j).
$$

Bridge: In reduced-model language, this is a stabilized energy profile over the real kernel time $t$ after averaging over a family of imaginary-time scales.

## UBT Notation Alignment

Canonical: In canonical UBT notation, the isotropic complex-time variable is written as

$$
\tau = t + i\psi,
$$

where $\psi$ is the scalar imaginary time component and the full canonical object is $T_B = t + i\psi + j\chi + k\xi$.

Bridge: To avoid silently changing symbols, the sprint notation $\phi$ should be read as a reduced-model symbol that maps to the canonical UBT scalar imaginary time $\psi$ only in the isotropic limit. Accordingly,

$$
\phi \longleftrightarrow \psi
$$

is a notation bridge, not a new canonical definition.

Bridge: In UBT-aligned notation the same reduced amplitude can therefore be written as

$$
S_s(t,\psi) = \sum_{n=0}^{N-1} a_n^{(s)}\,e^{-\pi \psi n^2} e^{\pi i t n^2},
$$

with the understanding that this lives inside the complex-time limit of UBT rather than the full biquaternion-time theory.

Canonical: The symbol $\Theta$ is already reserved in UBT for the fundamental field $\Theta(q,T_B)$.

Bridge: To avoid collision with the canonical field symbol, it is preferable in UBT-facing discussions to rename the reduced observable

$$
\Theta_s(t,\psi)
$$

as

$$
\mathcal{E}_s(t,\psi),
$$

and similarly

$$
\overline{\Theta}_s(t) \mapsto \overline{\mathcal{E}}_s(t).
$$

Bridge: This is a notation hygiene step only. It does not alter the reduced mathematics.

## Operator Viewpoint Inside UBT

Canonical: UBT already uses operator language through covariant derivatives, Laplace-type operators, and field equations acting on $\Theta(q,T_B)$.

Bridge: The reduced theta kernel

$$
e^{-\pi \psi n^2} e^{\pi i t n^2}
$$

resembles a complex-time propagator on a discrete mode space. The damping factor is heat-kernel-like, while the quadratic phase factor is oscillatory and spectral.

Bridge: In that sense, $S_s(t,\psi)$ may be interpreted as a reduced projected propagator-like amplitude on a compact or discrete mode space, and $\overline{\mathcal{E}}_s(t)$ as a reduced observable derived from that amplitude.

Bridge: This is compatible with UBT’s use of spectral decomposition and diffusion-style reasoning in the complex-time sector, but it is not yet the full UBT field propagator.

## Connection Points to Existing UBT Structure

Canonical: Complex time already appears in UBT through the isotropic limit $\tau = t + i\psi$.

Canonical: Diffusion and heat-kernel language already appear in the Fokker-Planck and heat-equation material in the repository.

Bridge: The theta reduced model connects to those structures by pairing an imaginary-time Gaussian kernel with a real-time quadratic phase.

Bridge: The mode index $n$ supports a spectral interpretation, so the reduced model can be viewed as a compatible layer for studying operator spectra or reduced observable sectors.

Conjectural: Embedding this reduced theta amplitude directly into the full biquaternion-valued evolution of $\Theta(q,T_B)$ remains open.

## Limits of the Current Bridge

Canonical: The canonical field remains $\Theta(q,T_B)$, not $S_s(t,\psi)$.

Bridge: The construction here is a reduced model and a bridge formalism.

Conjectural: This document does not derive the metric sector, General Relativity limit, Standard Model sector, or the full UBT action from the theta reduced model.

Conjectural: This document does not prove that $a_n^{(s)}$ are fundamental UBT field degrees of freedom. They may instead be projected field samples, modal amplitudes, or reduced observables.

Conjectural: The extension from scalar complex time $\tau = t + i\psi$ to full biquaternion time $T_B = t + i\psi + j\chi + k\xi$ is not derived here.

## Next Steps

Bridge: Derive an operator form whose matrix elements reproduce $S_s(t,\psi)$ as a reduced amplitude.

Bridge: Test whether $\overline{\mathcal{E}}_s(t)$ behaves like a reduced propagator observable on discrete mode spaces already natural in UBT.

Bridge: Compare the reduced theta construction against the existing canonical complex-time formalism in `canonical/fields/biquaternion_time.tex` and `canonical/fields/theta_field.tex`.

Conjectural: Determine whether $a_n^{(s)}$ should be interpreted as projected field samples, modal amplitudes, or reduced observables inside UBT.

Conjectural: Determine whether the quadratic phase $e^{\pi i t n^2}$ can be embedded naturally into biquaternion-valued evolution without breaking canonical structure.
