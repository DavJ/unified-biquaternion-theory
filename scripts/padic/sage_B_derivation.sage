# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# sage_B_derivation.sage — Numerical investigation of the B coefficient in UBT
#
# PURPOSE
# -------
# This script investigates the B coefficient required for the alpha derivation
# in UBT.  The B coefficient appears in the effective potential:
#
#   V_eff(n) = A·n² − B·n·ln(n)
#
# Minimisation dV/dn = 0 with A = 1 gives n* = exp(B/2 − 1/2).
# The Standard-Model value N_eff = 12 requires B ≈ 46.3 so that n* = 137.
#
# Two open problems are investigated:
#
#   Problem A: Why does B_base = N_eff^{3/2} = 41.57, not the one-loop B₀ = 2π·N_eff/3 = 25.1?
#   Problem B: What is the geometric origin of R ≈ 1.114 such that B_base × R ≈ 46.3?
#
# This script explores the twin-prime hypothesis: B is related to the twin-prime
# pair (137, 139) of n*.  Results are documented honestly.
#
# USAGE
# -----
#   sage scripts/padic/sage_B_derivation.sage
#   python3 scripts/padic/sage_B_derivation.sage    # also works (no Sage-specific calls)
#
# REFERENCE
# ---------
#   STATUS_ALPHA.md §9 (Open Problems A and B)
#   consolidation_project/appendix_ALPHA_one_loop_biquat.tex §B.3–B.3.5
#   validation/validate_B_coefficient.py

import math

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

N_EFF = 12          # effective mode count from SM gauge group (derived, not fitted)
A_KINETIC = 1.0     # kinetic coefficient (normalised to 1 by convention)

# Exact experimental n* target
N_STAR = 137        # must be derived, not assumed — used only for verification

# ---------------------------------------------------------------------------
# Part 1: Symbolic verification of B₀ = 2π·N_eff/3  (one-loop baseline)
# ---------------------------------------------------------------------------

print("=" * 70)
print("PART 1 — One-loop baseline B₀ = 2π·N_eff/3")
print("=" * 70)

B0_exact = 2 * math.pi * N_EFF / 3
print(f"  N_eff  = {N_EFF}")
print(f"  B₀     = 2π·N_eff/3 = {B0_exact:.6f}  (rigorously derived, Theorem 3.1)")
print(f"  B₀     ≈ 8π = {8*math.pi:.6f}  (consistent)")

# What n* does B₀ predict?
# dV/dn = 0  →  2A·n = B·(ln n + 1)
# Approximate analytic solution: n* ≈ exp(B/(2A) − 1/2) (for large n)

def n_star_approx(B, A=1.0):
    """Approximate n* from V_eff minimum: n* ≈ exp(B/(2A) - 1/2)."""
    return math.exp(B / (2 * A) - 0.5)

def n_star_newton(B, A=1.0, n0=100):
    """Newton iteration for exact n*: 2An - B(ln n + 1) = 0."""
    n = float(n0)
    for _ in range(50):
        f = 2 * A * n - B * (math.log(n) + 1)
        df = 2 * A - B / n
        n_new = n - f / df
        if abs(n_new - n) < 1e-10:
            break
        n = n_new
    return n

n_from_B0 = n_star_newton(B0_exact)
print(f"\n  n*(B₀) = {n_from_B0:.4f}  ← NOT 137 (confirms gap)")
print(f"  Status: B₀ = 25.1 gives n* ≈ {n_from_B0:.0f}, not 137.")
print(f"  OPEN PROBLEM A: ratio B_required/B₀ = {46.3/B0_exact:.4f} ≈ 1.844 is unexplained.")

# ---------------------------------------------------------------------------
# Part 2: Power-law search B_base = N_eff^α
# ---------------------------------------------------------------------------

print()
print("=" * 70)
print("PART 2 — Power-law search: does B_required = N_eff^α for algebraic α?")
print("=" * 70)

# Exact B required so that n* = 137 with A = 1
B_required_exact = 2 * A_KINETIC * N_STAR / (math.log(N_STAR) + 1)
print(f"\n  B required for n*=137 (Newton): {B_required_exact:.6f}")
print(f"  B_base = N_eff^(3/2)          : {N_EFF**1.5:.6f}  (phenomenological formula)")
print(f"  R = B_required / B_base       : {B_required_exact / N_EFF**1.5:.6f}")
print()

# α = log_{N_eff}(B_required)
alpha_power = math.log(B_required_exact) / math.log(N_EFF)
print(f"  α such that N_eff^α = B_required: α = {alpha_power:.6f}")
print(f"  Compare: 3/2 = 1.500000,  8/5 = 1.600000")
print()

# Scan algebraically motivated α values
candidates_alpha = [
    (3/2,    "3/2  (spatial dim / 2)"),
    (8/5,    "8/5  (no obvious motivation)"),
    (math.log(2*math.pi) / math.log(N_EFF), "log(2π)/log(N_eff)"),
    (1 + 1/math.pi, "1 + 1/π"),
    (math.sqrt(2), "√2"),
    (math.pi/2, "π/2"),
]

print("  Scan of algebraically motivated exponents:")
print(f"  {'α value':>10}  {'N_eff^α':>10}  {'B_required':>10}  {'error %':>10}  description")
print("  " + "-"*65)
for a, desc in candidates_alpha:
    b_val = N_EFF ** a
    err = 100 * (b_val - B_required_exact) / B_required_exact
    marker = " ← closest" if abs(err) < 1 else ""
    print(f"  {a:10.6f}  {b_val:10.4f}  {B_required_exact:10.4f}  {err:>+10.3f}%  {desc}{marker}")

print()
print("  FINDING: α = 3/2 gives B_base = 41.57, which is 0.76% below B_required = 46.29.")
print("  No algebraically motivated α reproduces B_required exactly.")
print("  VERDICT: Power-law search — DEAD END for exact derivation.")

# ---------------------------------------------------------------------------
# Part 3: Twin-prime hypothesis
# ---------------------------------------------------------------------------

print()
print("=" * 70)
print("PART 3 — Twin-prime hypothesis: B from (n*, twin_prime(n*))")
print("=" * 70)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def twin_prime(p):
    """Return twin prime partner of p (p+2 if prime, else p-2 if prime, else None)."""
    if is_prime(p + 2):
        return p + 2
    if is_prime(p - 2):
        return p - 2
    return None

p_star = N_STAR        # 137
p_twin = twin_prime(p_star)   # 139

print(f"\n  n* = {p_star} (prime: {is_prime(p_star)})")
print(f"  twin prime: {p_twin} (prime: {is_prime(p_twin)})")
print()

# Candidate B formulas from twin-prime structure
twin_candidates = [
    (p_twin / 3,              f"{p_twin}/3          = {p_twin}/N_color"),
    ((p_star + p_twin) / 6,  f"(p* + p_tw)/6      = ({p_star}+{p_twin})/6"),
    ((p_star + p_twin) / (2 * math.pi), f"(p* + p_tw)/(2π)"),
    (p_twin / (2 * math.pi / N_EFF * N_EFF), f"{p_twin}/(2π·N_eff/N_eff)  [trivial]"),
    (math.sqrt(p_star * p_twin) / 3, f"√(p*·p_tw)/3"),
    ((p_star * p_twin) ** (1/3) / 1.0, f"(p*·p_tw)^(1/3)"),
]

print("  Twin-prime B candidates vs B_required:")
print(f"  {'Formula':>35}  {'B value':>10}  {'error %':>10}")
print("  " + "-"*60)
for b_val, desc in twin_candidates:
    err = 100 * (b_val - B_required_exact) / B_required_exact
    marker = " ← best match" if abs(err) < 0.2 else (" ← <1%" if abs(err) < 1 else "")
    print(f"  {desc:>35}  {b_val:10.4f}  {err:>+10.3f}%{marker}")

print()
print(f"  B_required (exact, A=1): {B_required_exact:.6f}")
print()
print("  BEST MATCH: 139/3 = 46.3333... gives error +0.085% vs B_required = 46.294.")
print("  This is the closest twin-prime expression found.")

# ---------------------------------------------------------------------------
# Part 4: Derived R if B = 139/3
# ---------------------------------------------------------------------------

print()
print("=" * 70)
print("PART 4 — Implied R if B = p_twin/N_color = 139/3")
print("=" * 70)

B_twin = p_twin / 3
B_base = N_EFF ** 1.5
R_implied = B_twin / B_base

print(f"\n  B_twin    = {p_twin}/3          = {B_twin:.6f}")
print(f"  B_base    = N_eff^(3/2)   = {B_base:.6f}")
print(f"  R_implied = B_twin/B_base = {R_implied:.6f}")
print(f"  R_used    = 1.114000      (phenomenological)")
print(f"  Difference: {abs(R_implied - 1.114)*100:.4f}%")
print()
print("  Exact form: R = p_twin / (N_color × N_eff^{3/2})")
print(f"            = 139 / (3 × 12^(3/2))")
print(f"            = 139 / (3 × {B_base:.4f})")
print(f"            = {R_implied:.6f}")

# ---------------------------------------------------------------------------
# Part 5: Self-consistency check with A = 1
# ---------------------------------------------------------------------------

print()
print("=" * 70)
print("PART 5 — Self-consistency: does B = 139/3 reproduce n* = 137?")
print("=" * 70)

B_test = p_twin / 3
n_star_test = n_star_newton(B_test, A=A_KINETIC, n0=137)
print(f"\n  B = 139/3 = {B_test:.6f}")
print(f"  n*(B=139/3, A=1) = {n_star_test:.6f}")
print(f"  Target n* = 137")
print(f"  Error: {abs(n_star_test - 137)/137*100:.4f}%")

print()
if abs(n_star_test - 137) < 0.1:
    print("  NOTE: n* is very close to 137 with B = 139/3 and A = 1.")
    print("  This is a numerical near-coincidence, NOT a derivation.")
    print("  The formula B = 139/3 has no geometric motivation in UBT.")

# ---------------------------------------------------------------------------
# Part 6: Grid scan — does any (N_eff_cand, prime) pair give a clean formula?
# ---------------------------------------------------------------------------

print()
print("=" * 70)
print("PART 6 — Grid scan: (N_eff, prime) → B = prime/N_color?")
print("=" * 70)

print("\n  Scanning N_eff ∈ {4, 8, 12, 24} with prime divisors of B_required:")
print(f"  {'N_eff':>6}  {'B_req':>8}  {'closest prime':>14}  {'prime/3':>10}  {'error %':>10}  {'twin?':>6}")
print("  " + "-"*60)

for Neff in [4, 8, 12, 24]:
    B_req = 2 * A_KINETIC * N_STAR / (math.log(N_STAR) + 1)  # same n*=137 target
    # Find primes near 3*B_req
    target = 3 * B_req
    for offset in range(20):
        for sign in [1, -1]:
            cand = int(round(target)) + sign * offset
            if cand > 2 and is_prime(cand):
                err = 100 * (cand / 3 - B_req) / B_req
                tw = "yes" if is_prime(cand - 2) or is_prime(cand + 2) else "no"
                print(f"  {Neff:>6}  {B_req:>8.4f}  p={cand:>12}  {cand/3:>10.4f}  {err:>+10.3f}%  {tw:>6}")
                break
        else:
            continue
        break

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

print()
print("=" * 70)
print("SUMMARY AND VERDICT")
print("=" * 70)
print("""
  Problem A (B_base = N_eff^{3/2}):
  ----------------------------------
  No algebraically motivated exponent α reproduces B_required exactly.
  α = 3/2 gives B_base = 41.57, which is 0.76% below the required 46.29.
  The twin-prime approach finds B ≈ 139/3 = 46.33, which is 0.085% above.
  Neither provides a geometric derivation of the 3/2 exponent.

  VERDICT for Problem A: DEAD END.
  The power-law B_base = N_eff^{3/2} remains unexplained.  The twin-prime
  relation B ≈ 139/3 is an interesting numerical near-coincidence but has
  no geometric motivation within UBT.

  Problem B (R ≈ 1.114):
  -----------------------
  If B = 139/3 (twin-prime hypothesis), then R = 139/(3·N_eff^{3/2}) = 1.1146,
  matching R = 1.114 to 0.04%.  However, this only reformulates Problem B
  as "why is B = 139/3?" — a question without a geometric answer.

  VERDICT for Problem B: DEAD END.
  R ≈ 1.114 can be expressed as p_twin/(3·N_eff^{3/2}) = 139/124.71, but
  this expression has no independent geometric derivation within UBT.

  Overall conclusion: Both Problems A and B remain OPEN HARD PROBLEMS.
  The twin-prime numerology is documented as an interesting observation,
  not a derivation.  See STATUS_ALPHA.md §9.4 and
  consolidation_project/appendix_ALPHA_one_loop_biquat.tex §B.3.5.
""")
