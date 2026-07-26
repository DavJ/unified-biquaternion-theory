from __future__ import annotations

import ast
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROVENANCE_TESTS = (
    REPO_ROOT / "tests" / "test_data_provenance.py",
    REPO_ROOT / "tests" / "test_manifest_path_resolution.py",
    REPO_ROOT / "tests" / "test_manifest_validation_strict.py",
)


def _top_level_sys_path_mutations(path: Path) -> list[str]:
    """Return source snippets for top-level sys.path mutations in *path*."""
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    mutations: list[str] = []
    for node in tree.body:
        if not isinstance(node, ast.Expr) or not isinstance(node.value, ast.Call):
            continue
        call = node.value
        func = call.func
        if not isinstance(func, ast.Attribute) or func.attr not in {"insert", "append"}:
            continue
        owner = func.value
        if (
            isinstance(owner, ast.Attribute)
            and isinstance(owner.value, ast.Name)
            and owner.value.id == "sys"
            and owner.attr == "path"
        ):
            mutations.append(ast.get_source_segment(source, node) or "sys.path mutation")
    return mutations


def test_provenance_tests_use_package_imports_without_path_shadowing() -> None:
    """Provenance tests must not shadow the repository's root ``tools`` package."""
    for path in PROVENANCE_TESTS:
        source = path.read_text(encoding="utf-8")
        assert "from scripts import hash_dataset, validate_manifest" in source
        assert _top_level_sys_path_mutations(path) == [], (
            f"{path.relative_to(REPO_ROOT)} mutates sys.path at module import time; "
            "this can make tools/forensic_fingerprint/tools shadow the root tools package"
        )
