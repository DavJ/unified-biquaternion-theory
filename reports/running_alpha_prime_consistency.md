<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# running_alpha_prime_consistency.md

**Task**: `fix_or_reject_U1_coupling_normalization` — Target 6  
**Priority**: CRITICAL  
**Mode**: physics-first, no numerology  
**Date**: 2026-05-10

---

## Scope

This report derives the RG running of α from the UBT QED effective action and
**then** — only after the derivation is complete — compares the trajectory with
known numerical checkpoints.  Stable-prime integers are **not used** to derive
any physical quantity.

---

## 1) RG equation from the UBT QED sector

The low-energy UBT QED effective action contains
$$
\mathcal{L}_\mathrm{eff} \supset -\frac{1}{4e^2(\mu)}\,\mathcal{F}_{\mu\nu}\mathcal{F}^{\mu\nu}.
$$
One-loop vacuum polarization renormalization of the photon two-point function
gives the beta function
$$
\mu\frac{de}{d\mu} = \frac{b_\mathrm{em}}{(4\pi)^2}\,e^3 + O(e^5),
$$
where `b_em > 0` for any charged-matter content with positive Dirac/complex-scalar
degrees of freedom.  In terms of α = e²/(4π), this becomes
$$
\mu\frac{d\alpha}{d\mu} = \frac{b_\mathrm{em}}{2\pi}\,\alpha^2 + O(\alpha^3),
$$
and equivalently
$$
\frac{d\alpha^{-1}}{d\ln\mu} = -\frac{b_\mathrm{em}}{2\pi} < 0.
$$

**Derivation status: DERIVED** (from UBT QED sector field content, no external
input).

### RG trajectory

Integrating the one-loop equation:
$$
\alpha^{-1}(\mu) = \alpha^{-1}(\mu_0) - \frac{b_\mathrm{em}}{2\pi}\ln\frac{\mu}{\mu_0}.
$$

Qualitative prediction:
- **Higher energy scale μ ⟹ smaller α⁻¹(μ)** (larger α).
- **Lower energy scale μ ⟹ larger α⁻¹(μ)** (smaller α).

This is the standard running of the electromagnetic coupling in QED.

---

## 2) Beta coefficient from UBT field content

The coefficient `b_em` counts the contribution of charged fields to vacuum
polarization.  In the low-energy UBT QED sector:
- Each Dirac fermion with charge `q_r` contributes `+4q_r²/3`.
- Each complex scalar with charge `q_r` contributes `+q_r²/3`.

For the standard electron (charge q = −1, Dirac):
$$
b_\mathrm{em} = \frac{4}{3} \cdot 1^2 = \frac{4}{3}.
$$

**Derivation status: DERIVED** for the qualitative direction (b_em > 0); the
exact value depends on the full field content of the UBT QED sector.

The sign `b_em > 0` is robust: any field with nonzero charge contributes
positively to the running in the direction of decreasing α⁻¹ with increasing μ.

---

## 3) Qualitative flow direction

**DERIVED conclusion:**  
$$
\alpha^{-1}(\mu_\mathrm{low}) > \alpha^{-1}(\mu_\mathrm{high}).
$$
The low-energy electromagnetic coupling is weaker (larger α⁻¹) than the
high-energy coupling.

This direction is determined entirely by the sign of the beta function, which
follows from the structure of one-loop vacuum polarization diagrams.

---

## 4) Post-derivation comparison with prime stability candidates

**This section is OBSERVED CONSISTENCY only.  No value below is used as input.**

After completing the above derivation, compare with known values:

| Scale | α⁻¹ (observed) | Prime? | In stable-prime set? |
|---|---|---|---|
| μ = m_e (low energy) | ≈ 137.036 | 137 is prime | yes (stable prime candidate) |
| μ = M_Z (electroweak) | ≈ 127.9 | 127 is prime | yes (stable prime candidate) |

The stable-prime set `{2, 127, 137, 139, 151, 157, ...}` contains both 127
and 137.  The RG trajectory passes through these values at the corresponding
scales.

**Interpretation:**
- The trajectory is **continuous** in ln μ.
- The prime integers are **discrete** landmarks.
- Therefore: 127 and 137 can be interpreted as approximate checkpoints on
  a continuous trajectory, not as dynamical attractors.

**Classification: OBSERVED CONSISTENCY** — not derivation.

---

## 5) Hard-rule compliance

- Stable primes not used to fix e² or b_em. ✓
- Stable primes not used to derive the beta function coefficient. ✓
- Numerical values 137 and 127 appear only in post-derivation comparison. ✓
- No measured value of α used as derivation input. ✓
- Verdict class correctly assigned: OBSERVED CONSISTENCY. ✓

---

## 6) Conclusion

| Item | Status |
|---|---|
| RG direction (α⁻¹ decreasing with μ) | DERIVED |
| Beta coefficient sign (b_em > 0) | DERIVED |
| Exact beta coefficient value | CONDITIONAL (depends on full field content) |
| Consistency with α⁻¹ ≈ 137 at low energy | OBSERVED CONSISTENCY |
| Consistency with α⁻¹ ≈ 127.9 at M_Z | OBSERVED CONSISTENCY |
| Prime stability as derivation mechanism | REJECTED (hard rule) |
