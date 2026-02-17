"""
Utility helpers for path-robust test access to repository layout.

Usage in tests::

    from tests.utils_repo_paths import forensic_root, repo_root

    sys.path.insert(0, str(forensic_root() / 'cmb_comb'))
"""
from pathlib import Path


def repo_root() -> Path:
    """Return the repository root directory."""
    return Path(__file__).resolve().parents[1]


def forensic_root() -> Path:
    """Return the forensic_fingerprint canonical directory.

    Resolves via the root-level shim: always points at
    ``ubt_with_chronofactor/forensic_fingerprint/``.
    """
    import forensic_fingerprint  # noqa: F401 — triggers shim / path injection
    from forensic_fingerprint import get_target_root
    return get_target_root()
