#!/usr/bin/env python3
"""Verify orthogonal UBT machine/human/editorial review profiles."""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = ROOT / "PROVENANCE_REVIEW.yaml"
BEGIN = "UBT-REVIEW-PROFILE-BEGIN"
END = "UBT-REVIEW-PROFILE-END"
SCHEMA = "ubt-review-profile/v1"


class ReviewProfileError(RuntimeError):
    """Raised when the review registry or a source block is invalid."""


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader that rejects duplicate keys."""


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


def load_registry(path: Path = DEFAULT_REGISTRY) -> dict[str, Any]:
    try:
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise ReviewProfileError(f"Cannot load review registry {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ReviewProfileError("Review registry must be a YAML mapping")
    if data.get("schema") != SCHEMA or data.get("version") != 1:
        raise ReviewProfileError(f"Expected schema {SCHEMA!r}, version 1")
    if not isinstance(data.get("allowed_values"), dict):
        raise ReviewProfileError("allowed_values must be a mapping")
    if not isinstance(data.get("profiles"), dict):
        raise ReviewProfileError("profiles must be a mapping")
    return data


def _date(value: object, field: str, rel: str) -> dt.date:
    if isinstance(value, dt.date):
        return value
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError as exc:
        raise ReviewProfileError(f"{rel}: {field} must be an ISO date") from exc


def expected_block(profile: dict[str, Any], rel: str, suffix: str) -> str:
    fields = [
        BEGIN,
        f"schema: {SCHEMA}",
        f"machine_verification: {profile['machine_verification']['status']}",
        f"human_review: {profile['human_review']['status']}",
        f"editorial_approval: {profile['editorial_approval']['status']}",
        f"registry: {'../' * (len(Path(rel).parts) - 1)}PROVENANCE_REVIEW.yaml",
        END,
    ]
    if suffix == ".tex":
        return "\n".join(f"% {line}" for line in fields)
    if suffix == ".md":
        return "<!--\n" + "\n".join(fields) + "\n-->"
    raise ReviewProfileError(f"{rel}: unsupported profiled suffix {suffix}")


def extract_block(text: str, suffix: str) -> str | None:
    if suffix == ".tex":
        pattern = re.compile(
            rf"(?ms)^% {re.escape(BEGIN)}\n.*?^% {re.escape(END)}$"
        )
    elif suffix == ".md":
        pattern = re.compile(
            rf"(?ms)^<!--\n{re.escape(BEGIN)}\n.*?{re.escape(END)}\n-->$"
        )
    else:
        return None
    match = pattern.search(text)
    return match.group(0) if match else None


def validate_profile(rel: str, profile: dict[str, Any], data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    source = ROOT / rel
    if not source.is_file():
        return [f"{rel}: profiled source does not exist"]
    if source.suffix.lower() not in {".tex", ".md"}:
        errors.append(f"{rel}: review blocks support only .tex and .md sources")

    labels = profile.get("publication_labels")
    if not isinstance(labels, dict):
        errors.append(f"{rel}: publication_labels must be a mapping")
    else:
        for key in ("machine", "human", "editorial"):
            if not str(labels.get(key) or "").strip():
                errors.append(f"{rel}: publication_labels.{key} is required")

    allowed = data["allowed_values"]
    for axis in ("machine_verification", "human_review", "editorial_approval"):
        value = profile.get(axis)
        if not isinstance(value, dict):
            errors.append(f"{rel}: {axis} must be a mapping")
            continue
        status = value.get("status")
        if status not in allowed.get(axis, []):
            errors.append(f"{rel}: invalid {axis} status {status!r}")

    machine = profile.get("machine_verification", {})
    evidence = machine.get("evidence", [])
    if machine.get("status") not in {"none", None}:
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{rel}: non-none machine verification requires evidence")
        else:
            for item in evidence:
                if not (ROOT / str(item)).is_file():
                    errors.append(f"{rel}: missing machine-verification evidence {item}")

    human = profile.get("human_review", {})
    if human.get("status") not in {"none", None}:
        if not human.get("reviewed_by"):
            errors.append(f"{rel}: human review requires reviewed_by")
        if not human.get("reviewed_on"):
            errors.append(f"{rel}: human review requires reviewed_on")
        else:
            try:
                _date(human["reviewed_on"], "reviewed_on", rel)
            except ReviewProfileError as exc:
                errors.append(str(exc))
        claims = human.get("claims", [])
        if not isinstance(claims, list) or not claims:
            errors.append(f"{rel}: human review requires an explicit claims list")

    approval = profile.get("editorial_approval", {})
    if approval.get("status") == "approved":
        if not approval.get("responsible_person"):
            errors.append(f"{rel}: approved profile requires responsible_person")
        if not approval.get("approved_on"):
            errors.append(f"{rel}: approved profile requires approved_on")
        else:
            try:
                _date(approval["approved_on"], "approved_on", rel)
            except ReviewProfileError as exc:
                errors.append(str(exc))

    if source.is_file() and source.suffix.lower() in {".tex", ".md"}:
        actual = extract_block(source.read_text(encoding="utf-8"), source.suffix.lower())
        expected = expected_block(profile, rel, source.suffix.lower())
        if actual != expected:
            errors.append(f"{rel}: missing or stale UBT review-profile source block")
        if source.suffix.lower() == ".tex" and isinstance(labels, dict):
            macro = (
                "\\UBTReviewProfile"
                f"{{{labels.get('machine', '')}}}"
                f"{{{labels.get('human', '')}}}"
                f"{{{labels.get('editorial', '')}}}"
            )
            if macro not in source.read_text(encoding="utf-8"):
                errors.append(f"{rel}: LaTeX review-profile macro does not match registry labels")
    return errors


def verify(path: Path = DEFAULT_REGISTRY) -> list[str]:
    data = load_registry(path)
    errors: list[str] = []
    for rel, profile in sorted(data["profiles"].items()):
        if not isinstance(profile, dict):
            errors.append(f"{rel}: profile must be a mapping")
            continue
        errors.extend(validate_profile(rel, profile, data))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args(argv)
    try:
        errors = verify(args.registry.resolve())
    except ReviewProfileError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    count = len(load_registry(args.registry.resolve())["profiles"])
    print(f"Verified {count} orthogonal review profile(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
