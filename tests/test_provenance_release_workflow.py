"""Regression checks for provenance-aware publication workflows."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_latex_publication_requires_human_signoff() -> None:
    text = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    assert "Enforce signed provenance release gate" in text
    assert "test_tier_map_is_signed_off" in text
    assert "tools/apply_provenance_headers.py --check" in text
    assert "tools/verify_provenance_review.py" in text
    assert "tests/test_provenance_review.py" in text
    assert "poppler-utils" in text


def test_publication_does_not_run_after_failed_gate() -> None:
    text = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    publish = text.index("- name: Publish curated canonical PDFs")
    upload = text.index("- name: Upload all successful PDFs")
    block = text[publish:upload]
    assert "if: success()" in block
    assert "verify_pdf_provenance.py --require-all" in block
    assert "regenerate_sha256sums.py" in block
    assert "tools/verify_sha256sums.py --quiet" in block


def test_automated_commit_is_success_only_and_includes_checksums() -> None:
    text = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    commit = text.index("- name: Commit report and curated PDFs")
    block = text[commit:]
    assert "if: success() && github.event_name == 'push'" in block
    assert "git add docs/pdfs SHA256SUMS.txt" in block
    assert "if: always() && github.event_name == 'push'" not in block


def test_full_verify_workflow_installs_yaml_dependency() -> None:
    text = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
    assert "pip install -r requirements.txt" in text
    assert "pytest -q" in text


def test_checksum_verification_is_platform_independent() -> None:
    apply_text = (ROOT / "APPLY_AI_PROVENANCE_ART50_2026-08-01.sh").read_text(encoding="utf-8")
    release_text = (ROOT / "APPLY_PROVENANCE_RELEASE_GATE_2026-08-01.sh").read_text(encoding="utf-8")
    workflow = (ROOT / ".github/workflows/latex_build.yml").read_text(encoding="utf-8")
    for text in (apply_text, release_text, workflow):
        assert "tools/verify_sha256sums.py" in text
        assert "sha256sum -c" not in text
