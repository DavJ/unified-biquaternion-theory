<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# Gauge Structure

The Standard Model gauge group SU(3)×SU(2)_L×U(1)_Y emerges from the automorphism
and involution structure of the biquaternion algebra ℂ⊗ℍ, with **zero free parameters**
at the structural level.

**Canonical source**: [`canonical/interactions/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/canonical/interactions)  
**Gauge bridge**: [`canonical/bridges/gauge_emergence_bridge.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/bridges/gauge_emergence_bridge.tex)

---

## Derivation Status

<!-- BEGIN GENERATED: gauge_status -->
_No entries found in DERIVATION_INDEX.md for this section._
<!-- END GENERATED: gauge_status -->

---

## Electroweak Sector

### SU(2)_L — Left-Handed Weak Force

SU(2)_L arises from the **left action** of ℂ⊗ℍ on itself:

```
Generator T^a : M  →  (iσ^a/2) · M
[T^a, T^b] = ε^{abc} T^c
```

Status: **Proved [L0]**  
File: [`appendix_E2_SM_geometry.tex §6`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex)

The **chirality** of SU(2)_L (left-handed only, not SU(2)_L × SU(2)_R) is proved
through ψ-parity analysis:  
File: [`chirality_derivation/`](https://github.com/DavJ/unified-biquaternion-theory/tree/master/ARCHIVE/archive_legacy/consolidation_project/chirality_derivation)

### U(1)_Y — Hypercharge

U(1)_Y arises from the **right phase rotation**:

```
Θ  →  e^{-iθ} Θ
```

Status: **Proved [L0]**

### U(1)_EM — Electromagnetism

U(1)_EM arises from the phase of Θ on the ψ-circle:

Status: **Proved [L0]**  
File: [`canonical/interactions/qed.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/interactions/qed.tex)

### Weinberg Angle

The Weinberg angle θ_W cannot be fixed by ℂ⊗ℍ alone.  
Status: **Semi-empirical**

---

## Color Sector — SU(3)_c

SU(3)_c color symmetry is derived from **involutions on Im(ℍ)**. The three imaginary
quaternion units i, j, k correspond to the three color charges r, g, b.

The dimension dim Im(ℍ) = 3 **forces** SU(3) — there is no room for a different
color group given the ℂ⊗ℍ algebra.

Status: **Proved [L0]** ⭐  
Canonical file: [`appendix_G_internal_color_symmetry.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/ARCHIVE/archive_legacy/consolidation_project/appendix_G_internal_color_symmetry.tex)

→ Full details: [SU(3) Structure](SU3_Structure)

---

## Color Confinement

Free quarks are algebraically inadmissible in ℂ⊗ℍ: any free quark state has
⟨C₂⟩ = 4/3 ≠ 0 and is not a color singlet. All tested hadron types satisfy ⟨C₂⟩ = 0.

Status: **Conjectured with experimental support**  
Note: Distinct from Clay Millennium Prize (Yang–Mills mass gap).

---

## Canonical Files

| File | Content |
|------|---------|
| [`canonical/interactions/qed.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/interactions/qed.tex) | QED complete |
| [`canonical/interactions/qcd.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/interactions/qcd.tex) | QCD complete |
| [`canonical/interactions/sm_gauge.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/interactions/sm_gauge.tex) | Full SM gauge structure |
| [`canonical/bridges/gauge_emergence_bridge.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/master/canonical/bridges/gauge_emergence_bridge.tex) | Navigation bridge: SU(3)×SU(2)_L×U(1)_Y status |

---

## See Also

- [SU(3) Structure](SU3_Structure) — detailed SU(3) derivation
- [Fundamental Objects](Fundamental_Objects) — algebra ℂ⊗ℍ and involutions
- [Particle Spectrum](Particle_Spectrum) — fermion content
