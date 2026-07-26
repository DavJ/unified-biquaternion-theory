"""Regression checks for active GitHub Actions paths.

Active CI must not execute or watch removed pre-detox package trees. Historical
references remain allowed under ARCHIVE, but workflow commands and path filters
must point to the active repository layout.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"

STALE_ACTIVE_PREFIXES = (
    "ubt_with_chronofactor/",
    "ubt_no_chronofactor/",
    "archive/consolidation_project/",
)


def test_active_workflows_do_not_reference_removed_trees() -> None:
    offenders: list[str] = []
    for path in sorted(WORKFLOWS.glob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        for prefix in STALE_ACTIVE_PREFIXES:
            if prefix in text:
                offenders.append(f"{path.relative_to(ROOT)}: {prefix}")
    assert not offenders, "Stale active workflow references:\n" + "\n".join(offenders)


def test_repaired_workflow_targets_exist() -> None:
    expected = (
        "experiments/alpha_core_repro",
        "tools/forensic_fingerprint",
        "tools/planck_validation",
        "tests/test_alpha_export_runs.py",
        "tests/test_forensic_fingerprint.py",
        "tests/test_planck_validation_mapping.py",
    )
    missing = [rel for rel in expected if not (ROOT / rel).exists()]
    assert not missing, f"Workflow targets missing: {missing}"


def test_workflows_cover_active_paths() -> None:
    alpha = (WORKFLOWS / "alpha_two_loop.yml").read_text(encoding="utf-8")
    forensic = (WORKFLOWS / "forensic_fingerprint.yml").read_text(encoding="utf-8")
    planck = (WORKFLOWS / "planck_validation.yml").read_text(encoding="utf-8")

    assert "tests/test_alpha_provenance.py" in alpha
    assert "tools/forensic_fingerprint/**" in forensic
    assert "experiments/forensic_fingerprint/**" in forensic
    assert "tools/planck_validation/**" in planck
    assert "experiments/planck.py" in planck
