# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
Layer 2 Coding Constraints and Fine-Structure Constant α — Scan Script
=======================================================================

Route A4: Test whether Hamming (8,4,4), Gray transport, or the 1⊕3⊕3̄⊕1
decomposition of the biquaternion algebra fix the U(1) phase quantization
in a way that constrains or determines α.

Acceptance criteria:
  - No fitted parameter chosen to match α.
  - Every numerical input must come from another UBT sector.
  - Output must classify status as:
      proven / conditional / numerical coincidence / failed

Usage:
    python layer2_coding_alpha_scan.py

Output:
    Console report of all test results with classifications.
    No CSV output — all results are symbolic/analytical.

References:
    research_tracks/gray_transport_layer/gray_vs_hamming_layer2.md
    canonical/alpha/alpha_derivation_routes.md
    docs/STATUS_ALPHA.md
"""

import math
from typing import Optional

# ──────────────────────────────────────────────────────────────────────────────
# Physical constants (rounded reference values used as comparison targets only)
# Precise CODATA values are not hard-coded here; see docs/STATUS_ALPHA.md.
# ──────────────────────────────────────────────────────────────────────────────

ALPHA_INV_OBSERVED = 137.036   # approximate observed value (CODATA ~137.036)
ALPHA_OBSERVED = 1.0 / ALPHA_INV_OBSERVED


# ──────────────────────────────────────────────────────────────────────────────
# Section 1: Hamming (8,4,4) Code Structure
# ──────────────────────────────────────────────────────────────────────────────

def generate_hamming_844_codewords() -> list[int]:
    """
    Generate all 16 codewords of the extended Hamming (8,4,4) code.

    The code has parameters [n=8, k=4, d_min=4].
    Generator matrix G (systematic form) over GF(2):
        G = [I_4 | P]
    where the parity part P is:
        P = [[1,1,1,0],
             [1,1,0,1],
             [1,0,1,1],
             [0,1,1,1]]

    Returns list of 16 integers representing the 8-bit codewords.
    """
    # Parity sub-matrix P (4x4) such that codeword = [message | message * P]
    # Using standard extended Hamming construction
    P = [
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 0],
    ]
    codewords = []
    for msg in range(16):  # 4-bit messages: 0..15
        bits = [(msg >> (3 - i)) & 1 for i in range(4)]
        # Compute parity bits
        parity = [0, 0, 0, 0]
        for j in range(4):
            parity[j] = sum(bits[i] * P[i][j] for i in range(4)) % 2
        codeword_bits = bits + parity
        codeword_int = sum(b << (7 - i) for i, b in enumerate(codeword_bits))
        codewords.append(codeword_int)
    return codewords


def hamming_weight(x: int, nbits: int = 8) -> int:
    """Count number of 1-bits in the nbits-bit representation of x."""
    return bin(x & ((1 << nbits) - 1)).count('1')


def hamming_distance(a: int, b: int, nbits: int = 8) -> int:
    """Hamming distance between two integers (nbits-bit representation)."""
    return hamming_weight(a ^ b, nbits)


def minimum_code_distance(codewords: list[int]) -> int:
    """Compute the minimum Hamming distance between any two distinct codewords."""
    d_min = 8
    for i in range(len(codewords)):
        for j in range(i + 1, len(codewords)):
            d = hamming_distance(codewords[i], codewords[j])
            if d < d_min:
                d_min = d
    return d_min


def test_hamming_844_structure() -> dict:
    """
    Test 1: Verify Hamming (8,4,4) code properties and assess whether they
    constrain the charge spectrum or coupling magnitude.

    Returns dict with findings and classification.
    """
    codewords = generate_hamming_844_codewords()
    d_min = minimum_code_distance(codewords)
    n_codewords = len(codewords)

    # Weights of codewords
    weights = sorted(set(hamming_weight(c) for c in codewords))

    # Check: does d_min = 4 relate to physical charge fractions?
    # In the 1⊕3⊕3̄⊕1 decomposition (dim=8), minimum distance 4 = dim/2.
    # If charges are quantized in units of e/d_min, the elementary unit is e/4.
    # But e is not fixed by the coding structure; only the ratio is constrained.

    # Hypothetical: if charge unit is 1/d_min (pure counting), then alpha would be:
    # alpha = (1/d_min)^2 / (4pi) in natural units with e_unit = 1
    # This is dimensionless but not related to alpha unless we set e_unit explicitly.
    charge_unit_hypothesis = 1.0 / d_min  # = 1/4, dimensionless
    alpha_if_charge_quarter = charge_unit_hypothesis**2 / (4 * math.pi)

    return {
        "test": "Hamming (8,4,4) structure",
        "n_codewords": n_codewords,
        "d_min": d_min,
        "codeword_weights": weights,
        "observation": (
            f"d_min = {d_min}, matching 1⊕3⊕3̄⊕1 half-dimension (8/2 = 4). "
            "This is a structural match but does NOT fix the coupling magnitude."
        ),
        "alpha_if_e_equals_1_over_dmin": alpha_if_charge_quarter,
        "matches_observed_alpha": abs(alpha_if_charge_quarter - ALPHA_OBSERVED) < 0.001,
        "classification": "failed",
        "reason": (
            "The Hamming code fixes which charge values are ALLOWED "
            "(quantization spectrum), not the MAGNITUDE of the elementary charge. "
            "alpha = e^2/(4pi) requires e in physical units, which the coding "
            "layer does not provide."
        ),
    }


# ──────────────────────────────────────────────────────────────────────────────
# Section 2: Gray Code Transport Layer
# ──────────────────────────────────────────────────────────────────────────────

def standard_gray_code(n: int) -> list[int]:
    """
    Generate standard reflected binary Gray code for n-bit symbols.
    Returns list of 2^n integers in Gray order.
    """
    return [i ^ (i >> 1) for i in range(1 << n)]


def is_gray_adjacent(a: int, b: int, gray_order: list[int]) -> bool:
    """Return True if a and b are adjacent in the given Gray ordering."""
    try:
        ia = gray_order.index(a)
        ib = gray_order.index(b)
        return abs(ia - ib) == 1
    except ValueError:
        return False


def test_gray_transport_layer() -> dict:
    """
    Test 2: Assess whether Gray transport constraints fix the U(1) phase
    quantization in a way that determines α.

    Gray adjacency: sequential phase-symbol transitions prefer single-bit changes.
    Phase step = 2π / N_symbols per Gray-adjacent step.

    Returns dict with findings and classification.
    """
    # For 4-bit symbols (N=16): phase step = 2π/16 = π/8
    nbits = 4
    N = 1 << nbits  # 16
    gray = standard_gray_code(nbits)
    phase_step = 2 * math.pi / N  # π/8

    # Hypothetical: if U(1) charge is quantized with phase_step,
    # then q_unit = phase_step / (2π) = 1/16.
    # Then alpha = q_unit^2 / (4π) (unphysical pure counting)
    q_unit_from_gray_4bit = phase_step / (2 * math.pi)  # = 1/16
    alpha_gray_4bit = q_unit_from_gray_4bit**2 / (4 * math.pi)

    # For 8-bit symbols (N=256): phase step = 2π/256
    nbits_8 = 8
    N_8 = 1 << nbits_8  # 256
    phase_step_8 = 2 * math.pi / N_8
    q_unit_from_gray_8bit = phase_step_8 / (2 * math.pi)  # = 1/256
    alpha_gray_8bit = q_unit_from_gray_8bit**2 / (4 * math.pi)

    # Neither matches observed alpha ≈ 1/137
    return {
        "test": "Gray transport layer",
        "n_bits_4": nbits,
        "N_symbols_4": N,
        "alpha_from_4bit_gray": alpha_gray_4bit,
        "alpha_from_4bit_gray_inv": 1.0 / alpha_gray_4bit if alpha_gray_4bit != 0 else None,
        "alpha_from_8bit_gray": alpha_gray_8bit,
        "alpha_from_8bit_gray_inv": 1.0 / alpha_gray_8bit if alpha_gray_8bit != 0 else None,
        "observed_alpha_inv": ALPHA_INV_OBSERVED,
        "matches_4bit": abs(1 / alpha_gray_4bit - ALPHA_INV_OBSERVED) < 1.0,
        "matches_8bit": abs(1 / alpha_gray_8bit - ALPHA_INV_OBSERVED) < 1.0,
        "classification": "failed",
        "reason": (
            "Gray transport fixes the discretization step of phase symbols "
            "(2π/N per step), but N is a free parameter of the symbol alphabet. "
            "Neither N=16 nor N=256 produces α ≈ 1/137. "
            "Gray transport constrains TRANSITION COST, not coupling magnitude."
        ),
    }


# ──────────────────────────────────────────────────────────────────────────────
# Section 3: 1⊕3⊕3̄⊕1 Decomposition
# ──────────────────────────────────────────────────────────────────────────────

def test_su2_decomposition_1330() -> dict:
    """
    Test 3: Assess whether the 1⊕3⊕3̄⊕1 decomposition of the biquaternion
    algebra under SU(2) constrains U(1) phase normalization.

    The biquaternion algebra B = C⊗H has real dimension 8.
    Under SU(2) acting on the quaternion part:
        B = 1 ⊕ 3 ⊕ 3̄ ⊕ 1

    Dimensions: 1 + 3 + 3 + 1 = 8. ✓

    The two singlets (1, 1) correspond to the real and imaginary scalar parts;
    the two triplets (3, 3̄) correspond to the quaternion imaginary parts
    and their complex conjugates.

    Returns dict with findings and classification.
    """
    # Casimir eigenvalues for SU(2) representations
    # j=0: C_2 = 0 (singlet)
    # j=1: C_2 = j(j+1) = 2 (triplet)
    j_values = [0, 1, 1, 0]  # singlet, triplet, anti-triplet, singlet
    dims = [2 * j + 1 for j in j_values]  # [1, 3, 3, 1]
    total_dim = sum(dims)  # 8

    # The U(1)_Y generator Y must commute with all of SU(2)_L.
    # By Schur's lemma, Y acts as a scalar on each irrep:
    #   Y|singlet_1⟩ = y_1 |singlet_1⟩
    #   Y|triplet_3⟩ = y_3 |triplet_3⟩  (same for all 3 components)
    #   Y|triplet_3̄⟩ = y_3bar |triplet_3̄⟩
    #   Y|singlet_4⟩ = y_4 |singlet_4⟩

    # The hypercharge assignments are free (y_1, y_3, y_3bar, y_4 undetermined
    # from algebra alone without further physical input).
    n_free_hypercharges = 4  # one per irrep block (here 4 distinct blocks)

    # For the Higgs doublet analog: we need a doublet (j=1/2) representation.
    # BUT: the 1⊕3⊕3̄⊕1 decomposition has NO j=1/2 (doublet) representations!
    # This is a critical observation.

    has_doublet = any(j == 0.5 for j in j_values)

    # The SM Higgs doublet requires j=1/2. The absence of j=1/2 in B means
    # the Higgs-analog must come from a product representation or a sub-algebra.

    # Possible doublet: take a 2-dimensional subspace spanning one singlet and
    # one component of a triplet. But this is NOT an irreducible SU(2) doublet;
    # it is a reducible representation.

    return {
        "test": "1⊕3⊕3̄⊕1 decomposition under SU(2)",
        "irreps": list(zip(j_values, dims)),
        "total_dim": total_dim,
        "n_free_hypercharge_assignments": n_free_hypercharges,
        "has_SU2_doublet_irrep": has_doublet,
        "critical_finding": (
            "The 1⊕3⊕3̄⊕1 decomposition contains NO j=1/2 doublet representations. "
            "The SM Higgs requires a doublet. The UBT Higgs-analog must come from "
            "a different construction (e.g., product representation, sub-algebra, "
            "or extended field content). This is Gap EW-2."
        ),
        "coupling_constraint": (
            "Hypercharge assignments y_1, y_3, y_3bar, y_4 are free parameters "
            "of the embedding of U(1)_Y into Aut(B). The decomposition fixes the "
            "STRUCTURE of allowed charge assignments but not their magnitude."
        ),
        "classification": "failed",
        "reason": (
            "1⊕3⊕3̄⊕1 fixes the representation structure but: "
            "(1) contains no j=1/2 doublet needed for SM Higgs, "
            "(2) does not fix the U(1)_Y normalization, "
            "(3) does not determine the ratio g'/g."
        ),
    }


# ──────────────────────────────────────────────────────────────────────────────
# Section 4: Combined Coding Constraints — Can They Fix α?
# ──────────────────────────────────────────────────────────────────────────────

def test_combined_coding_constraint() -> dict:
    """
    Test 4: Combined assessment — do all three coding constraints together
    fix α?

    Layer 2 structure:
      L2S (Hamming): fixes state survival rules (which states are protected)
      L2T (Gray):    fixes transition cost structure (which paths are preferred)
      1⊕3⊕3̄⊕1:     fixes representation structure of B under SU(2)

    For α = e²/(4π), we need e in physical units.
    The coding layer provides:
      - Charge quantization: q ∈ ℤ · e_unit   (from Hamming minimum distance)
      - Phase discretization: Δφ = 2π/N       (from Gray code, N free)
      - Representation structure               (from 1⊕3⊕3̄⊕1)

    None of these determines the SCALE of e_unit in physical units.

    Returns dict with overall assessment.
    """
    # Summary of what coding constrains vs. what remains free
    constrained = [
        "Charge spectrum: integer multiples of e_unit (Dirac quantization + Hamming)",
        "Phase step: 2π/N per symbol (Gray, N free)",
        "Representation structure under SU(2): 1⊕3⊕3̄⊕1",
        "State parity: Hamming syndrome = 0 for physical states",
    ]
    free_parameters = [
        "Magnitude of e_unit (requires S[Θ] dynamics, not coding)",
        "Gray code alphabet size N (not fixed by UBT)",
        "Ratio g'/g = tan(θ_W) (not fixed by coding structure)",
        "Overall coupling normalization (UV cutoff dependent)",
    ]

    # Check: is there ANY combination of coding parameters that gives α?
    # Try: α = C_hamming / (4π · N_gray^k) for integers k and coding constant C

    # Hamming-related: d_min = 4, n = 8, k = 4 (message bits)
    d_min, n_ham, k_ham = 4, 8, 4
    # Gray-related: test N = 16 (4-bit) and N = 256 (8-bit)
    candidates = []
    for N_gray in [2, 4, 8, 16, 32, 64, 128, 256]:
        for power in [1, 2, 3]:
            for numerator in [1, d_min, k_ham, n_ham, d_min**2, k_ham**2]:
                val = numerator / (N_gray**power)
                alpha_candidate = val**2 / (4 * math.pi)
                if alpha_candidate > 0:
                    alpha_inv = 1.0 / alpha_candidate
                    if 130 < alpha_inv < 145:  # within 5% of observed 137
                        candidates.append({
                            "numerator": numerator,
                            "N_gray": N_gray,
                            "power": power,
                            "charge_unit": val,
                            "alpha_inv": alpha_inv,
                            "deviation_from_137": abs(alpha_inv - ALPHA_INV_OBSERVED),
                            "note": "Near-miss — check if UBT-motivated",
                        })

    return {
        "test": "Combined coding constraints",
        "constrained_by_coding": constrained,
        "free_parameters": free_parameters,
        "near_miss_candidates": candidates,
        "classification": "failed",
        "reason": (
            "Coding constraints (Hamming + Gray + 1⊕3⊕3̄⊕1) fix the STRUCTURE "
            "of allowed charges and transitions, but do not determine the "
            "magnitude of the elementary charge unit e in physical units. "
            "α = e²/(4π) requires the magnitude, which must come from the "
            "dynamics of S[Θ], not from the coding layer."
        ),
    }


# ──────────────────────────────────────────────────────────────────────────────
# Section 5: What the Coding Layer CAN Contribute
# ──────────────────────────────────────────────────────────────────────────────

def test_positive_contributions() -> dict:
    """
    Test 5: Identify what the coding layer CAN contribute to the α derivation.

    Even if coding cannot fix α, it may:
    (a) Fix the charge spectrum (which charges are kinematically allowed).
    (b) Enforce the Dirac quantization condition from a discrete perspective.
    (c) Constrain the winding number n in the V_eff(n) attractor (existing result).
    (d) Support the prime-attractor argument for n* = 137.

    Returns dict with positive findings.
    """
    # Hamming minimum distance = 4 → 4-fold symmetry → quarter-charge allowed
    # This is consistent with quark charges ±1/3, ±2/3 (which are multiples of 1/3,
    # NOT 1/4). So Hamming d_min=4 alone does not explain quark charges.

    # However: for integer charges (electrons, protons), Hamming imposes
    # that states must have Hamming weight differing by d_min=4 from the vacuum.
    # One-hot triqubit states (|r>, |g>, |b>) have weight 1; paired states have weight 2.

    # Winding number constraint:
    # The Dirac quantization condition from ψ-circle gives n ∈ ℤ.
    # The Hamming code gives a discrete subset: states with syndrome = 0.
    # The intersection: physical winding numbers are those satisfying Hamming parity.
    # All integers n are compatible with Hamming parity (the syndrome depends on
    # the binary representation of n mod 8, not on n directly).

    # Primeness of n* = 137:
    # The V_eff(n) attractor selects the minimum over n ∈ ℕ+.
    # Hamming parity does NOT select primes; it selects syndrome-zero integers.
    # Therefore, the coding layer does NOT enforce the prime constraint.
    # The prime constraint comes from homotopy theory of π_1(S^1_ψ), not from coding.

    codewords = generate_hamming_844_codewords()
    # How many winding numbers 1..200 are syndrome-zero (trivially: all integers
    # have a well-defined 8-bit representation with a syndrome, but the syndrome
    # depends on how n is encoded, not on n itself as a physical winding number)

    return {
        "test": "Positive contributions of coding to alpha derivation",
        "finding_1": (
            "Hamming (8,4,4) d_min=4 is consistent with EM charge quantization "
            "(integer charges) but does NOT select the charge unit magnitude."
        ),
        "finding_2": (
            "Coding does NOT enforce primeness of winding numbers; "
            "the prime constraint n*=137 comes from π_1(S^1_ψ) homotopy, "
            "independent of the Hamming or Gray structures."
        ),
        "finding_3": (
            "Gray transport constrains phase-symbol PATHS (preferred transitions), "
            "not the magnitude of the coupling. It is a geometric kinematic constraint."
        ),
        "finding_4": (
            "The 1⊕3⊕3̄⊕1 structure correctly predicts that color charges come "
            "in triplets and singlets, but does not fix the overall coupling strength."
        ),
        "positive_role_of_coding": (
            "Layer 2 coding provides a SELECTION RULE for the charge spectrum "
            "(which charge states are stable) but not the NORMALIZATION of the "
            "coupling. It is a necessary but not sufficient condition for α."
        ),
        "classification": "conditional",
        "condition": (
            "Coding provides necessary structure (charge quantization, "
            "representation content), but the coupling magnitude must come from "
            "the dynamical sector S[Θ] (existing prime-attractor + one-loop result)."
        ),
    }


# ──────────────────────────────────────────────────────────────────────────────
# Main Report
# ──────────────────────────────────────────────────────────────────────────────

def print_result(result: dict) -> None:
    """Print a formatted result block."""
    print(f"\n{'='*70}")
    print(f"TEST: {result['test']}")
    print(f"CLASSIFICATION: {result['classification'].upper()}")
    print(f"-" * 70)
    for key, value in result.items():
        if key in ("test", "classification"):
            continue
        if isinstance(value, list):
            print(f"  {key}:")
            for item in value:
                if isinstance(item, dict):
                    print(f"    {item}")
                else:
                    print(f"    - {item}")
        elif isinstance(value, float):
            print(f"  {key}: {value:.6g}")
        else:
            print(f"  {key}: {value}")


def main() -> None:
    print("=" * 70)
    print("UBT Layer 2 Coding Constraints — Alpha Derivation Scan")
    print("Route A4: Hamming / Gray / 1⊕3⊕3̄⊕1 vs. Fine-Structure Constant")
    print(f"Observed α⁻¹ = {ALPHA_INV_OBSERVED:.6f} (CODATA 2018)")
    print("=" * 70)
    print()
    print("ACCEPTANCE CRITERIA:")
    print("  • No parameter fitted to match α")
    print("  • All inputs from UBT algebra or coding structure")
    print("  • Classification: proven / conditional / numerical coincidence / failed")

    results = [
        test_hamming_844_structure(),
        test_gray_transport_layer(),
        test_su2_decomposition_1330(),
        test_combined_coding_constraint(),
        test_positive_contributions(),
    ]

    for r in results:
        print_result(r)

    # Final summary
    print(f"\n{'='*70}")
    print("SUMMARY OF ROUTE A4")
    print("=" * 70)
    print()
    print("Layer 2 coding constraints (Hamming + Gray + 1⊕3⊕3̄⊕1):")
    print()
    print("  WHAT IS CONSTRAINED BY CODING:")
    print("    ✓ Charge spectrum structure (integer/half-integer multiples)")
    print("    ✓ Phase-symbol transition costs (Gray adjacency preference)")
    print("    ✓ Representation content under SU(2) (1⊕3⊕3̄⊕1)")
    print("    ✓ State stability (Hamming syndrome = 0)")
    print()
    print("  WHAT IS NOT CONSTRAINED BY CODING:")
    print("    ✗ Magnitude of elementary charge e (requires S[Θ] dynamics)")
    print("    ✗ Weinberg angle θ_W = arctan(g'/g)")
    print("    ✗ Overall U(1) coupling normalization")
    print("    ✗ Fine-structure constant α = e²/(4π)")
    print()
    print("  CLASSIFICATION: FAILED")
    print("  REASON: Coding layer is a necessary but insufficient condition.")
    print("          The coupling magnitude comes from the prime-attractor")
    print("          mechanism (existing L1 result), not from coding.")
    print()
    print("  Near-miss candidates found:", end=" ")
    near_misses = results[3]["near_miss_candidates"]
    if near_misses:
        print(len(near_misses))
        for nm in near_misses[:3]:
            print(f"    α⁻¹ ≈ {nm['alpha_inv']:.4f} "
                  f"(from q={nm['numerator']}/N^{nm['power']}, N={nm['N_gray']})"
                  f" — deviation {nm['deviation_from_137']:.4f} — "
                  "no UBT motivation")
    else:
        print("0 (no near-misses within 5% of observed α)")
    print()
    print("  RECOMMENDATION: Route A4 should be closed for α derivation.")
    print("  Coding constraints are relevant for charge spectrum selection")
    print("  and state stability, not for coupling magnitude.")


if __name__ == "__main__":
    main()
