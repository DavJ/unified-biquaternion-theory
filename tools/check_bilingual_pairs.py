#!/usr/bin/env python3
"""Fail closed when paired English/Czech documents drift structurally."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


LANG_RE = re.compile(r"^(?P<stem>.+)\.(?P<lang>en|cs)(?P<suffix>\.(?:md|tex|rst))$")
TEXT_SUFFIXES = {".md", ".tex", ".rst"}
EXCLUDED_PARTS = {
    ".git",
    "ARCHIVE",
    "archive_legacy",
    "generated",
    "build",
    "vendor",
    "node_modules",
}
GOVERNANCE_FILES = {
    "AGENTS.md",
    "CONTRIBUTING.md",
    ".github/pull_request_template.md",
}
SHARED_LANGUAGE_NEUTRAL_FILES = {
    "docs/textbook/main.tex",
    "docs/textbook/chapters/04_covariant_tetrad_geometry.tex",
}

MATH_RE = re.compile(
    r"\$\$(.*?)\$\$|\\\[(.*?)\\\]|\\\((.*?)\\\)|"
    r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)"
    r"\\end\{\4\}",
    re.DOTALL,
)
LABEL_RE = re.compile(r"\\(?:label|ref|eqref|autoref)\{([^}]+)\}")
CITE_RE = re.compile(r"\\cite[a-zA-Z*]*\{([^}]+)\}|\[@([^\]]+)\]")
TEX_STRUCTURE_RE = re.compile(
    r"\\(part|chapter|section|subsection|subsubsection|paragraph|"
    r"begin|end|theoremstyle|newtheorem)\b(?:\{([^}]+)\})?"
)
MD_HEADING_RE = re.compile(r"^(#{1,6})\s+", re.MULTILINE)
FENCE_RE = re.compile(r"^```[^\n]*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?")
STATUS_RE = re.compile(
    r"\b(?:GAP-[A-Za-z0-9*_-]+|OPEN|NARROWED|CLOSED(?:\s+CONDITIONALLY)?|"
    r"PROVED|UNPROVED|SPECULATIVE|HISTORICAL|L[0-9])\b"
)
UNIT_RE = re.compile(r"BILINGUAL-UNIT:\s*([A-Za-z0-9_.:-]+)")


def compact(value: str) -> str:
    return re.sub(r"\s+", "", value)


def matches(pattern: re.Pattern[str], text: str) -> list[str]:
    result: list[str] = []
    for match in pattern.finditer(text):
        groups = [group for group in match.groups() if group is not None]
        result.append("|".join(compact(group) for group in groups))
    return result


@dataclass(frozen=True)
class Signature:
    units: tuple[str, ...]
    structure: tuple[str, ...]
    math: tuple[str, ...]
    labels: tuple[str, ...]
    citations: tuple[str, ...]
    code: tuple[str, ...]
    numbers: tuple[str, ...]
    statuses: tuple[str, ...]


def signature(path: Path) -> Signature:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".tex":
        structure = []
        for match in TEX_STRUCTURE_RE.finditer(text):
            command, argument = match.groups()
            structure.append(
                command if command in {"part", "chapter", "section", "subsection", "subsubsection", "paragraph"}
                else f"{command}|{compact(argument or '')}"
            )
        code: list[str] = []
    else:
        structure = [str(len(marker)) for marker in MD_HEADING_RE.findall(text)]
        code = [compact(block) for block in FENCE_RE.findall(text)]
    return Signature(
        units=tuple(UNIT_RE.findall(text)),
        structure=tuple(structure),
        math=tuple(matches(MATH_RE, text)),
        labels=tuple(LABEL_RE.findall(text)),
        citations=tuple(matches(CITE_RE, text)),
        code=tuple(code),
        numbers=tuple(NUMBER_RE.findall(text)),
        statuses=tuple(STATUS_RE.findall(text)),
    )


def pair_for(path: Path) -> Path | None:
    match = LANG_RE.match(path.name)
    if not match:
        return None
    other = "cs" if match.group("lang") == "en" else "en"
    return path.with_name(f"{match.group('stem')}.{other}{match.group('suffix')}")


def excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def all_pairs(root: Path) -> set[tuple[Path, Path]]:
    pairs: set[tuple[Path, Path]] = set()
    for path in root.rglob("*"):
        if not path.is_file() or excluded(path.relative_to(root)):
            continue
        other = pair_for(path)
        if other is not None:
            en = path if ".en." in path.name else other
            cs = path if ".cs." in path.name else other
            pairs.add((en, cs))
    return pairs


def changed_paths(root: Path, base: str) -> list[Path]:
    command = ["git", "diff", "--name-only", "--diff-filter=AM", f"{base}...HEAD"]
    output = subprocess.check_output(command, cwd=root, text=True)
    return [root / line for line in output.splitlines() if line]


def check_pair(en: Path, cs: Path) -> list[str]:
    errors: list[str] = []
    if not en.is_file() or not cs.is_file():
        missing = en if not en.is_file() else cs
        return [f"missing language pair: {missing}"]
    en_sig, cs_sig = signature(en), signature(cs)
    for field in Signature.__dataclass_fields__:
        if getattr(en_sig, field) != getattr(cs_sig, field):
            errors.append(f"{field} mismatch: {en} != {cs}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--changed-base")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    pairs = all_pairs(root)
    for en, cs in sorted(pairs):
        errors.extend(check_pair(en, cs))

    if args.changed_base:
        for path in changed_paths(root, args.changed_base):
            relative = path.relative_to(root)
            if (
                path.suffix not in TEXT_SUFFIXES
                or excluded(relative)
                or relative.as_posix() in GOVERNANCE_FILES
                or relative.as_posix() in SHARED_LANGUAGE_NEUTRAL_FILES
            ):
                continue
            other = pair_for(path)
            if other is None:
                errors.append(
                    f"governed text must use an .en/.cs pair: {relative.as_posix()}"
                )
            else:
                en = path if ".en." in path.name else other
                cs = path if ".cs." in path.name else other
                errors.extend(check_pair(en, cs))

    if errors:
        print("Bilingual document gate failed:", file=sys.stderr)
        for error in sorted(set(errors)):
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Bilingual document gate passed ({len(pairs)} pair(s) checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
