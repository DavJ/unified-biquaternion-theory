# forensic_fingerprint/__init__.py
#
# Compatibility shim: delegates to ubt_with_chronofactor/forensic_fingerprint.
#
# This package was moved from the repository root into ubt_with_chronofactor/.
# This shim restores root-level importability for tests and CI that were written
# against the old layout.  It can later be switched to point at the
# ubt_no_chronofactor implementation once one is created.
from ._shim import ensure_importable, get_target_root

_TARGET = ensure_importable()

__all__ = ["ensure_importable", "get_target_root"]
