# References

## Mathematical Background

### SU(3) and Gell-Mann Matrices

1. **Gell-Mann, M.** (1961). "The Eightfold Way: A Theory of Strong Interaction Symmetry."
   California Institute of Technology report CTSL-20.
   — Original introduction of the λ matrices.

2. **Peskin, M.E. & Schroeder, D.V.** (1995). *An Introduction to Quantum Field Theory.*
   Addison-Wesley. Section 15.1–15.4.
   — Standard reference for SU(3) gauge theory and Gell-Mann matrices.

3. **Georgi, H.** (1982). *Lie Algebras in Particle Physics.*
   Benjamin/Cummings.
   — Comprehensive treatment of SU(N) representations and structure constants.

### Qubit Formalism and Pauli Operators

4. **Nielsen, M.A. & Chuang, I.L.** (2000). *Quantum Computation and Quantum Information.*
   Cambridge University Press.
   — Chapter 2 covers the Pauli operator formalism and tensor products.

5. **Brylinski, J.L. & Brylinski, R.** (2001). "Universal Quantum Gates."
   arXiv:quant-ph/0108062.
   — Tensor product decomposition of multi-qubit operators.

### Representation Theory

6. **Humphreys, J.E.** (1972). *Introduction to Lie Algebras and Representation Theory.*
   Springer-Verlag.
   — Casimir operators, Weyl character formula, representation theory.

7. **Fulton, W. & Harris, J.** (1991). *Representation Theory: A First Course.*
   Springer-Verlag.
   — Chapter 12–13 for SU(3) representations.

### Qubit Simulation of Gauge Theories

8. **Banuls, M.C. et al.** (2020). "Simulating Lattice Gauge Theories within Quantum Technologies."
   *European Physical Journal D* 74, 165.
   — General review of gauge theories on quantum computers.

9. **Ciavarella, A., Klco, N., Savage, M.J.** (2021). "Trailhead for quantum simulation of SU(3)."
   *Physical Review D* 103, 094501. arXiv:2101.10227.
   — Explicit construction of SU(3) operators on qubits.

10. **Ji, Y. & Savage, M.J.** (2023). "Quantum computing SU(3) lattice gauge theory."
    *Physical Review D* 107, 114516. arXiv:2208.03209.
    — Optimized qubit encoding of SU(3).

## Relevant UBT Documents

- `consolidation_project/appendix_G_internal_color_symmetry.tex`  
  Derivation of SU(3) color symmetry from the UBT internal phase fiber

- `consolidation_project/SU3_derivation/`  
  Step-by-step derivation of SU(3) from the 8-dimensional biquaternion algebra

- `tools/verify_su3_from_biquaternion.py`  
  Numerical verification of SU(3) structure from ℂ⊗ℍ
