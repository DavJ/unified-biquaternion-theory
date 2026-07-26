from pathlib import Path

from tools.verify_gradient_composite_flatness import (
    determinant_identity,
    nonlinear_pullback_riemann_zero,
)


def test_exact_gradient_metric_determinant_identity():
    assert determinant_identity()


def test_nonlinear_exact_gradient_pullback_is_flat():
    assert nonlinear_pullback_riemann_zero()


def test_ledgers_do_not_call_gradient_branch_surviving():
    repo_root = Path(__file__).resolve().parents[1]
    paths = [
        repo_root / "CLAIMS.yaml",
        repo_root / "CLAIMS_MATRIX.md",
        repo_root / "STATUS.md",
        repo_root / "STATUS_OF_UBT.md",
        repo_root / "WHAT_IS_PROVED.md",
        repo_root / "papers" / "UBT_GR_Submission.tex",
    ]
    forbidden = (
        "surviving minimal continuation is composite",
        "curved dynamics of the surviving composite branch",
        "GAP-10T-COMPOSITE-FLAT & \\textbf{CLOSED}",
    )
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for phrase in forbidden:
            assert phrase not in text, f"stale overclaim {phrase!r} in {path}"
