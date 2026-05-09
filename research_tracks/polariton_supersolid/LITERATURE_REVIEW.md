<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Polariton Supersolid — Literature Review

**Track:** `research_tracks/polariton_supersolid/`  
**Status:** Draft  
**Last Updated:** 2025

This review covers three areas relevant to the polariton supersolid research track:
1. Exciton-polariton condensation and non-equilibrium dynamics
2. Supersolid physics (theory and experiments)
3. Candidate connections to field-theoretic frameworks (context for UBT bridge)

---

## 1. Foundational Polariton Physics

### 1.1 Exciton-Polariton Condensation

**Weisbuch, C., Nishioka, M., Ishikawa, A., & Arakawa, Y. (1992)**  
*Observation of the coupled exciton-photon mode splitting in a semiconductor quantum microcavity.*  
Physical Review Letters, 69(23), 3314–3317.  
https://doi.org/10.1103/PhysRevLett.69.3314

> First experimental observation of strong coupling between excitons and cavity photons,
> leading to the formation of exciton-polariton branches. Foundational experimental paper.

---

**Kasprzak, J., et al. (2006)**  
*Bose-Einstein condensation of exciton polaritons.*  
Nature, 443, 409–414.  
https://doi.org/10.1038/nature05131

> First clear observation of polariton BEC in a CdTe microcavity. Demonstrates macroscopic
> occupation of the lowest momentum state, spontaneous coherence buildup, and a sharp threshold
> reminiscent of BEC. Landmark experimental result. The condensate is non-equilibrium (driven-
> dissipative), not a true ground-state BEC.

---

**Carusotto, I., & Ciuti, C. (2013)**  
*Quantum fluids of light.*  
Reviews of Modern Physics, 85, 299–366.  
https://doi.org/10.1103/RevModPhys.85.299

> Comprehensive review of non-equilibrium quantum fluids of light, including polariton BEC,
> superfluidity, vortices, and solitons. Derives the driven-dissipative Gross-Pitaevskii (GP)
> equation and explains the mean-field treatment of polariton condensates. Essential reference
> for this track's GP derivation.

---

**Deng, H., Haug, H., & Yamamoto, Y. (2010)**  
*Exciton-polariton Bose-Einstein condensation.*  
Reviews of Modern Physics, 82, 1489–1537.  
https://doi.org/10.1103/RevModPhys.82.1489

> Review of exciton-polariton BEC across various semiconductor platforms (GaAs, CdTe, GaN,
> organic materials). Discusses the role of reservoir excitons, threshold behavior, and the
> differences from equilibrium BEC.

---

### 1.2 Polariton Superfluidity

**Amo, A., et al. (2009)**  
*Superfluidity of polaritons in semiconductor microcavities.*  
Nature Physics, 5, 805–810.  
https://doi.org/10.1038/nphys1364

> Experimental demonstration of polariton superfluidity: flow without scattering around a
> defect below a critical velocity. Direct analogue of Landau's criterion. Important for
> understanding the superfluid component in polariton supersolid discussions.

---

**Nardin, G., et al. (2011)**  
*Hydrodynamic nucleation of quantized vortex pairs in a polariton quantum fluid.*  
Nature Physics, 7, 635–641.  
https://doi.org/10.1038/nphys2007

> Observation of vortex nucleation in polariton quantum fluids. Confirms the Berezinskii-
> Kosterlitz-Thouless (BKT) physics in 2D polariton systems, relevant to the superfluid
> order in potential supersolid phases.

---

## 2. Driven-Dissipative GP Dynamics

**Wouters, M., & Carusotto, I. (2007)**  
*Excitations in a nonequilibrium Bose-Einstein condensate of exciton polaritons.*  
Physical Review Letters, 99, 140402.  
https://doi.org/10.1103/PhysRevLett.99.140402

> Derives the driven-dissipative Gross-Pitaevskii equation (ddGP) with reservoir coupling.
> Identifies the Bogoliubov-like excitation spectrum and shows that the Goldstone mode (sound)
> is diffusive rather than propagating due to the non-equilibrium character. This is the
> standard theoretical framework used in `gp_equation/gp_derivation.md`.

---

**Keeling, J., & Berloff, N. G. (2008)**  
*Spontaneous rotating vortex lattices in a pumped decaying condensate.*  
Physical Review Letters, 100, 250401.  
https://doi.org/10.1103/PhysRevLett.100.250401

> Shows that non-equilibrium polariton condensates can spontaneously form vortex lattices
> due to the interplay of gain, loss, and interactions. Demonstrates the richness of the
> non-equilibrium phase diagram.

---

**Sieberer, L. M., Huber, S. D., Altman, E., & Diehl, S. (2013)**  
*Dynamical Critical Phenomena in Driven-Dissipative Systems.*  
Physical Review Letters, 110, 195301.  
https://doi.org/10.1103/PhysRevLett.110.195301

> Field-theoretic (Keldysh) treatment of driven-dissipative BEC. Shows that the universality
> class of the phase transition differs from equilibrium BEC. Relevant for understanding
> what "supersolid order" means in a non-equilibrium context.

---

## 3. Supersolid Physics

### 3.1 Theoretical Foundations

**Leggett, A. J. (1970)**  
*Can a Solid Be Superfluid?*  
Physical Review Letters, 25, 1543–1546.  
https://doi.org/10.1103/PhysRevLett.25.1543

> Original theoretical proposal: a quantum solid could exhibit superfluid flow if atoms can
> tunnel through lattice sites (non-classical rotational inertia, NCRI). Defines the superfluid
> fraction for a system with broken translational symmetry. Foundation of all modern supersolid
> discussions.

---

**Andreev, A. F., & Lifshitz, I. M. (1969)**  
*Quantum theory of defects in crystals.*  
Soviet Physics JETP, 29, 1107–1113.

> Proposes that delocalized vacancies in a quantum crystal could condense, producing both
> crystalline order and superfluidity. Independent proposal of the supersolid concept.

---

**Chester, G. V. (1970)**  
*Speculations on Bose-Einstein condensation and quantum crystals.*  
Physical Review A, 2, 256–258.  
https://doi.org/10.1103/PhysRevA.2.256

> Argues from a variational perspective that a Bose system with Jastrow-type correlations
> can exhibit simultaneously crystalline and superfluid order.

---

### 3.2 Dipolar Quantum Gas Supersolids (2019 Experimental Breakthrough)

**Tanzi, L., et al. (2019)**  
*Observation of a Dipolar Quantum Gas with Metastable Supersolid Properties.*  
Physical Review Letters, 122, 130405.  
https://doi.org/10.1103/PhysRevLett.122.130405

> First experimental evidence of a supersolid state in a dipolar BEC (Er atoms with
> dysprosium-like interactions). Simultaneous measurement of density modulation (crystalline
> order via in-situ imaging) and superfluid response (interference fringe visibility after
> release from trap).

---

**Böttcher, F., et al. (2019)**  
*Transient Supersolid Properties in an Array of Dipolar Quantum Droplets.*  
Physical Review X, 9, 011051.  
https://doi.org/10.1103/PhysRevX.9.011051

> Observes droplet array (self-assembled density modulation) with evidence of phase coherence
> across droplets (supersolidity). Shows both density-wave and superfluid properties coexist
> transiently.

---

**Chomaz, L., et al. (2019)**  
*Long-Lived and Transient Supersolid Behaviors in Dipolar Quantum Gases.*  
Physical Review X, 9, 021012.  
https://doi.org/10.1103/PhysRevX.9.021012

> Systematic study of the timescales of supersolid behavior in dysprosium dipolar BEC.
> Identifies parameter regimes with long-lived vs. transient supersolid character. Useful
> for understanding what experimental signatures to look for.

---

**Norcia, M. A., et al. (2021)**  
*Two-dimensional supersolidity in a dipolar quantum gas.*  
Nature, 596, 357–361.  
https://doi.org/10.1038/s41586-021-03718-8

> First 2D supersolid: extends the 1D stripe phase to a 2D triangular droplet lattice in a
> dysprosium BEC. Critical reference for polariton analogues in 2D microcavities.

---

### 3.3 Spin-Orbit Coupled BEC Supersolids

**Li, J.-R., et al. (2017)**  
*A stripe phase with supersolid properties in spin-orbit-coupled Bose-Einstein condensates.*  
Nature, 543, 91–94.  
https://doi.org/10.1038/nature21431

> First observation of supersolid stripe phase in a spin-orbit-coupled BEC (⁸⁷Rb). The
> stripe phase is a density modulation arising from interference between two momentum
> components, combined with phase coherence. Most direct analogue to predicted polariton
> supersolid stripe phases.

---

### 3.4 Towards Polariton Supersolids

**Lagoudakis, K. G., et al. (2008)**  
*Quantized vortices in an exciton–polariton condensate.*  
Nature Physics, 4, 706–710.  
https://doi.org/10.1038/nphys1051

> Observation of vortex cores in a polariton condensate. Establishes the superfluid character
> and provides tools (imaging density + phase simultaneously) needed to detect supersolid order.

---

**Cristofolini, P., et al. (2013)**  
*Coupling Quantum Tunneling with Cavity Photons.*  
Science, 336, 704–707.  
https://doi.org/10.1126/science.1219010

> Demonstrates control of polariton-polariton interactions via Feshbach-like resonances.
> Tunable interactions are essential for reaching the parameter regime where supersolid
> instability occurs.

---

**Regemortel, M. V., et al. (2017)**  
*Spontaneous Beliaev-Landau scattering out of equilibrium.*  
Physical Review A, 96, 053854.  
https://doi.org/10.1103/PhysRevA.96.053854

> Theoretical analysis of roton softening in polariton systems with structured photonic
> bands or spatially modulated pumping. A soft roton minimum is the precursor of density
> wave (crystalline) order — the key instability leading to a supersolid phase.

---

**Ferrier-Barbut, I. (2019)**  
*Ultradilute quantum droplets.*  
Physics Today, 72(4), 46.  
https://doi.org/10.1063/PT.3.4184

> Accessible review of quantum droplet formation and its relation to supersolid physics.
> Useful context for understanding the interplay of quantum fluctuations and mean-field
> interactions that drives supersolid formation.

---

**Estrecho, E., et al. (2021)**  
*Direct measurement of polariton–polariton interaction strength in the Thomas-Fermi regime
of exciton-polaritons.*  
Physical Review B, 100, 035306.  
https://doi.org/10.1103/PhysRevB.100.035306

> Careful experimental measurement of polariton-polariton interaction constants. Essential
> input parameters for any GP simulation aiming to reach the supersolid regime.

---

## 4. Field-Theoretic and Emergent-Geometry Context

*These references motivate the UBT bridge hypotheses in `ubt_bridge/BRIDGE_HYPOTHESES.md`
but do not constitute evidence for them.*

**Altland, A., & Simons, B. (2010)**  
*Condensed Matter Field Theory* (2nd ed.). Cambridge University Press.

> Standard graduate textbook. Chapters 6–8 (coherent state path integral, BEC, superfluid)
> provide the field-theoretic language used in the bridge hypotheses.

---

**Sieberer, L. M., Buchhold, M., & Diehl, S. (2016)**  
*Keldysh field theory for driven open quantum systems.*  
Reports on Progress in Physics, 79, 096001.  
https://doi.org/10.1088/0034-4885/79/9/096001

> Modern Keldysh-path-integral treatment of driven-dissipative quantum systems. The doubled
> Hilbert space structure (forward/backward Keldysh contour) has structural similarity to
> the complex-time formalism in UBT. This is one starting point for the UBT bridge.

---

**Penrose, R., & Rindler, W. (1984)**  
*Spinors and Space-Time* (Vol. 1). Cambridge University Press.

> Two-spinor / twistor formalism that underpins UBT's biquaternionic algebra.
> Referenced to contextualize the algebraic structures in the bridge hypotheses.

---

## 5. Summary Table

| Ref. | Topic | Relevance |
|------|-------|-----------|
| Kasprzak et al. 2006 | First polariton BEC | Core experimental baseline |
| Carusotto & Ciuti 2013 | ddGP derivation | GP equation derivation |
| Wouters & Carusotto 2007 | ddGP excitation spectrum | Simulation scaffold |
| Leggett 1970 | Supersolid definition | Theoretical foundation |
| Tanzi et al. 2019 | First dipolar supersolid | Experimental benchmark |
| Li et al. 2017 | SOC stripe supersolid | Closest polariton analogue |
| Norcia et al. 2021 | 2D supersolid | 2D geometry reference |
| Sieberer et al. 2016 | Keldysh for driven systems | UBT bridge motivation |
| Estrecho et al. 2021 | Polariton interaction constants | Simulation parameters |

---

**Status:** Draft — additional references to be added as the track develops.
