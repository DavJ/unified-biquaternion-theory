# ST-5: Falsifiability of Imaginary-Sector Invisibility in UBT

**Status:** SPECULATIVE  
**Track:** Invisibility / Imaginary Sector  
**Date:** 2026-03-03  
**Author:** David Jaroš  

---

> **⚠️ All content in this file is SPECULATIVE.** It describes
> hypothetical observational consequences of a non-validated theoretical
> conjecture (existence of imaginary-sector matter in UBT). These are
> research hypotheses, not established predictions.

---

## Overview

If imaginary-sector matter exists in UBT (as formalised in ST-1–ST-4),
it would be:

- **Electromagnetically invisible**: no photon emission, absorption,
  or scattering at leading order.
- **Gravitationally active**: real energy-momentum tensor
  $T_{\mu\nu}[\Theta_I] \neq 0$, sourcing spacetime curvature.
- **Stable on cosmological timescales**: suppressed sector-mixing
  transitions, conserved imaginary-sector charge $Q_I$.

This phenomenology is structurally identical to cold dark matter (CDM).
The key question is whether the UBT imaginary sector predicts any
*deviation* from standard CDM that could distinguish it observationally.

---

## Candidate Observational Signatures

### 1. Gravitational Lensing Without Visible Source

**Prediction:** Regions of space that produce measurable gravitational
lensing (deflection of background galaxy images, Einstein rings) but
contain no detectable baryonic or luminous matter — and no detectable
non-baryonic radiation consistent with standard WIMP dark matter.

**Distinguishing feature from CDM:** Standard CDM lensing is consistent
with particle dark matter with a thermal mass spectrum. UBT imaginary-sector
matter has a mass spectrum determined by the biquaternion potential
$V(\widetilde\Theta_I^\dagger\widetilde\Theta_I)$. If this potential has
distinctive features (e.g., an exponential form arising from the
$\mathcal{B} = \mathbb{C} \otimes \mathbb{H}$ algebra), the resulting
power spectrum of density fluctuations would differ from CDM at small scales.

**Status:** Existing observations of galaxy cluster lensing (e.g., Bullet
Cluster) are consistent with cold, collisionless dark matter and would
equally be consistent with UBT imaginary-sector matter. No discriminating
prediction can be made without specifying the form of $V$.

---

### 2. Anomalous Perihelion Precession in Binary Systems

**Prediction:** In a binary stellar system embedded in a background
imaginary-sector density $\rho_I$, the effective gravitational potential
receives an additional contribution:

$$\Phi_\mathrm{eff}(r) = -\frac{GM}{r} - \frac{4\pi G \rho_I r^2}{3}$$

The second term is the standard tidal contribution of a uniform dark
matter background. However, if the imaginary-sector matter forms a
concentrated halo around individual stars (rather than a smooth
background), there would be an additional perihelion advance:

$$\delta\dot\omega \;\sim\; \frac{3\pi G M_I}{a\,c^2(1-e^2)}$$

where $M_I$ is the imaginary-sector mass within the binary orbit,
$a$ is the semi-major axis, and $e$ is the eccentricity.

**Status:** Current pulsar timing observations (double pulsar PSR J0737–3039)
constrain anomalous perihelion precession to better than 0.1% of GR
predictions, setting an upper bound $M_I \lesssim 10^{-3} M_\odot$ within
typical binary separations. This is consistent with UBT imaginary-sector
matter — it does not predict a large local concentration — but does not
confirm it.

---

### 3. Primary Concrete Falsifiable Prediction

**This is the one concrete falsifiable prediction from UBT imaginary-sector theory.**

#### Statement

> *If UBT imaginary-sector matter is the dominant dark matter component,
> then the matter power spectrum $P(k)$ must exhibit a suppression at
> wavenumbers $k > k_J$, where the Jeans wavenumber $k_J$ is:*
>
> $$k_J \;=\; \sqrt{\frac{4\pi G \rho_I}{c_I^2}}$$
>
> *with $c_I$ the imaginary-sector sound speed determined by the UBT
> potential. For the simplest biquaternion potential
> $V = \frac{\lambda}{4}(\widetilde\Theta_I^\dagger\widetilde\Theta_I - v^2)^2$,
> the sound speed is:*
>
> $$c_I^2 \;=\; \frac{\partial^2 V / \partial\rho^2}{\partial^2 V / \partial\rho^2 + m_I^2/\hbar^2}$$
>
> *If no such suppression is observed at the predicted scale, UBT
> imaginary-sector dark matter is **falsified at that scale**.*

#### Why this is falsifiable

- The suppression scale $k_J$ translates into a minimum halo mass
  $M_\mathrm{min} \sim (3/4\pi)\rho_I (π/k_J)^3$.
- Observations of satellite galaxy counts around the Milky Way constrain
  $M_\mathrm{min} \lesssim 10^7 M_\odot$ (i.e., the power spectrum is
  not suppressed on scales larger than dwarf galaxies).
- If the UBT potential $V$ predicts $M_\mathrm{min} > 10^{10} M_\odot$
  (too heavy to form dwarf galaxies), the model is falsified.
- If the UBT potential predicts $M_\mathrm{min} \ll 10^7 M_\odot$
  (ultra-light or cold), it is consistent with satellite galaxy counts
  but may conflict with other constraints (Lyman-alpha forest, BBN).

#### Required theoretical input

To convert this into a quantitative prediction, the UBT imaginary-sector
mass $m_I$ must be derived from the biquaternion algebra
$\mathcal{B} = \mathbb{C} \otimes \mathbb{H}$ and the canonical UBT
potential $V$. This has not been done and is listed as future work.

---

### 4. CMB Anomalies from Imaginary-Sector Background

**Prediction:** If imaginary-sector matter has a non-zero pressure
$p_I \neq 0$ (dark energy component), it would contribute to the
effective equation of state:

$$w_I \;=\; \frac{p_I}{\rho_I}$$

For $w_I < -1/3$ this acts as dark energy and would modify the
late-time CMB lensing power spectrum and the integrated Sachs-Wolfe
effect.

**Status:** Too unconstrained to make a numerical prediction. The
equation of state $w_I$ depends entirely on the form of $V$, which
is not yet derived from first principles.

---

## Summary Table

| Signature | Testable? | Predicted scale | Current status |
|-----------|-----------|-----------------|----------------|
| Lensing without visible source | ✅ Yes | Galaxy/cluster scale | Consistent with CDM, no discrimination yet |
| Anomalous perihelion precession | ✅ Yes | Binary orbit scale | $M_I < 10^{-3} M_\odot$ within binary; not ruled out |
| **Power spectrum suppression** | ✅ **Yes** | $k_J$ scale (derived from $V$) | **Primary falsifiable prediction** |
| CMB equation-of-state effect | ⚠️ Partially | $w_I$ scale | Under-constrained; needs $V$ derivation |

---

## What Would Confirm or Falsify Imaginary-Sector Dark Matter

### Confirmation (all must be satisfied)
1. Dark matter observations consistent with a single scalar field
   with the UBT potential $V$.
2. No direct detection signal from WIMP-like interactions (consistent
   with electromagnetic silence of $\Theta_I$).
3. Power spectrum suppression at the $k_J$ scale predicted by UBT.

### Falsification (any one is sufficient)
1. Power spectrum suppression measured at a scale inconsistent with
   the UBT prediction for $k_J$.
2. Dark matter direct detection signal inconsistent with a purely
   imaginary-sector object (i.e., a real electromagnetic cross-section).
3. Observed sector-mixing transitions (imaginary-sector decays to
   visible particles) at a rate higher than the UBT stability estimate.

---

## Connection to ST-2 Key Result

From ST-2: *imaginary-sector objects cannot be completely dark — they
always gravitate.* This makes the theory testable in principle. A theory
with a completely decoupled imaginary sector would predict nothing and be
unfalsifiable. UBT predicts *partial* invisibility with *gravitational*
detectability, which is a stronger and more falsifiable position.

---

## Next Steps (Research Agenda)

1. Derive $m_I$ and $V$ from first principles in UBT (requires solving
   the imaginary-sector equations of motion in the UBT canonical frame).
2. Compute the power spectrum $P_I(k)$ for imaginary-sector matter.
3. Compare to CMB TT, TE, EE, lensing, and BAO data from Planck 2018.
4. If consistent, identify target scales for future surveys (Euclid, SKA,
   CMB-S4).

---

*All statements in this document are **SPECULATIVE**. No claim constitutes
an established result of the canonical UBT framework.*
