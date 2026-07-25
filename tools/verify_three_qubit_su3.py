#!/usr/bin/env python3
"""Print residuals for the natural fermionic three-qubit SU(3) representation."""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
RESEARCH_TRACKS = REPO_ROOT / "research_tracks"
if str(RESEARCH_TRACKS) not in sys.path:
    sys.path.insert(0, str(RESEARCH_TRACKS))

from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.fock import (  # noqa: E402
    verification_residuals,
)


def main() -> int:
    tolerance = 1e-12
    residuals = verification_residuals()
    print("Three-qubit fermionic SU(3) verifier")
    print("=" * 42)
    for name, value in residuals.items():
        status = "PASS" if value < tolerance else "FAIL"
        print(f"{status:4s}  {name:34s} {value:.3e}")

    print("\nVerified representation:")
    print("  H_8 = Lambda^0 C^3 + Lambda^1 C^3 + Lambda^2 C^3 + Lambda^3 C^3")
    print("      = 1 + 3 + 3bar + 1")
    print("\nInterpretation limit:")
    print("  The six non-singlet states are 3 + 3bar, not six quark flavors.")
    print("  W + anti-W is not a one-X-flip-detecting code.")
    return 0 if all(value < tolerance for value in residuals.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
