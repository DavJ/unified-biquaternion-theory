"""Regression gates for UBT AI-provenance marking."""
from __future__ import annotations

import datetime as dt
import importlib.util
import subprocess
import sys
import warnings
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
MAP_PATH = ROOT / "PROVENANCE_TIERS.yaml"
TOOL_PATH = ROOT / "tools" / "apply_provenance_headers.py"
MAX_ATTESTED_FILES = 10


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader that rejects duplicate mapping keys instead of overwriting."""


def _construct_unique_mapping(loader: UniqueKeyLoader, node, deep: bool = False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def load_tool():
    spec = importlib.util.spec_from_file_location("ubt_provenance_tool", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


TOOL = load_tool()


def config() -> dict:
    return yaml.load(MAP_PATH.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)


def test_tier_map_is_editorially_bounded() -> None:
    data = config()
    attested = data["tiers"]["A_attested"]
    assert len(attested) <= MAX_ATTESTED_FILES
    assert len(attested) == len(set(attested))
    for path in attested:
        assert (ROOT / path).exists(), f"Attested path does not exist: {path}"


def test_tier_map_is_signed_off() -> None:
    """Intentional release gate: only the human author may make this pass."""
    data = config()
    signer = str(data.get("signed_off_by") or "")
    assert signer and not signer.upper().startswith("PENDING"), (
        "Author sign-off is pending in PROVENANCE_TIERS.yaml"
    )
    assert data.get("signed_off_date"), "signed_off_date must be set by the author"
    assert data.get("attested_as_of"), "attested_as_of must be set by the author"


def test_attestation_is_not_stale_when_signed() -> None:
    data = config()
    raw = data.get("attested_as_of")
    if raw is None:
        pytest.skip("author attestation is still pending")
    value = raw if isinstance(raw, dt.date) else dt.date.fromisoformat(str(raw))
    age = dt.date.today() - value
    if age.days > 90:
        warnings.warn(
            f"Tier-A attestation is {age.days} days old; author refresh required",
            RuntimeWarning,
        )


def test_all_markable_sources_match_the_tier_map() -> None:
    data = config()
    errors: list[str] = []
    for path, rel, tier in TOOL.iter_sources(ROOT, data):
        ok, message = TOOL.check_one(path, rel, tier)
        if not ok:
            errors.append(message)
    assert not errors, "\n" + "\n".join(errors[:80])


def test_provenance_inventory_matches_current_tree() -> None:
    """The committed inventory must describe the current classified source tree."""
    data = config()
    counts = {
        "A_attested": 0,
        "B_machine_verified": 0,
        "C_working": 0,
        "D_historical": 0,
        "excluded": 0,
    }
    for _path, _rel, tier in TOOL.iter_sources(ROOT, data):
        counts[tier] += 1
    expected = (
        "Provenance source inventory: "
        + ", ".join(
            f"{key}={counts[key]}"
            for key in (
                "A_attested",
                "B_machine_verified",
                "C_working",
                "D_historical",
                "excluded",
            )
        )
        + "\n"
    )
    inventory = ROOT / "PROVENANCE_INVENTORY_2026-08-01.txt"
    assert inventory.read_text(encoding="utf-8") == expected, (
        "PROVENANCE_INVENTORY_2026-08-01.txt is stale; run "
        "python3 tools/apply_provenance_headers.py --report > "
        "PROVENANCE_INVENTORY_2026-08-01.txt and regenerate SHA256SUMS.txt"
    )


def test_header_tool_check_mode_is_green() -> None:
    proc = subprocess.run(
        [sys.executable, str(TOOL_PATH), "--check"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout


def test_historical_sources_remain_unmarked() -> None:
    data = config()
    historical = 0
    for path, _rel, tier in TOOL.iter_sources(ROOT, data):
        if tier != "D_historical":
            continue
        historical += 1
        text = path.read_text(encoding="utf-8")
        assert TOOL.BEGIN not in text
        assert TOOL.END not in text
    assert historical > 0


def test_distributed_tex_roots_declare_matching_tiers() -> None:
    publish_map = ROOT / ".github" / "latex_publish_map.tsv"
    rows = []
    for raw in publish_map.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        pdf_source, _destination = raw.split("\t", 1)
        rows.append(pdf_source[:-4] + ".tex")
    data = config()
    for rel in rows:
        path = ROOT / rel
        assert path.exists(), rel
        tier = TOOL.classify_path(rel, data)
        assert tier in TOOL.TIERS
        short = TOOL.TIERS[tier].short
        text = path.read_text(encoding="utf-8")
        assert "\\usepackage{ubtprovenance}" in text, rel
        assert f"\\UBTTier{{{short}}}" in text, rel
        assert "\\UBTProvenanceNotice" in text, rel
        assert text.index("\\usepackage{ubtprovenance}") > text.index("hyperref"), rel
        assert text.index("\\UBTProvenanceNotice") > text.index("\\maketitle"), rel


def test_wiki_footer_markers_are_unique() -> None:
    for path in (ROOT / "wiki").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert text.count("BEGIN GENERATED: provenance_footer") == 1, path
        assert text.count("END GENERATED: provenance_footer") == 1, path
        assert "exhaustive human review is not claimed" in text, path


def test_latex_package_carries_visible_and_machine_readable_notice() -> None:
    text = (ROOT / "tex" / "ubtprovenance.sty").read_text(encoding="utf-8")
    assert "pdfsubject" in text
    assert "pdfkeywords" in text
    assert "AI provenance" in text
    assert "exhaustive human review is not claimed" in text
    assert "not AI-generated" in text
