#!/usr/bin/env python3
"""Deterministic local validator for the Hypernovelty Verification Literacy Kit."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "labs/ai-literacy-failure-mode-mini-lab/README.md",
    "labs/ai-literacy-failure-mode-mini-lab/worksheet.md",
    "labs/ai-literacy-failure-mode-mini-lab/answer-key.md",
    "labs/ai-literacy-failure-mode-mini-lab/rendered/facilitator-page.html",
    "templates/agent-recovery-plan-card.md",
    "templates/claim-drift-harness-card.md",
    "templates/forecast-calibration-receipt.md",
    "templates/harness-audit-lite-card.md",
    "examples/synthetic/claim-drift-example.md",
    "examples/synthetic/harness-audit-lite-example.md",
)

BOUNDARY_DOCUMENTS = (
    "README.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "docs/PUBLIC_SAFETY_REVIEW_2026-07-06.md",
)

BOUNDARY_CHECKS = {
    "synthetic/public-safe posture": ("synthetic", "public-safe"),
    "not legal/financial/medical advice": (
        "not legal",
        "financial",
        "medical",
        "advice",
    ),
    "no credentials/secrets": ("credentials", "secrets"),
}

FACILITATOR_PAGE = "labs/ai-literacy-failure-mode-mini-lab/rendered/facilitator-page.html"

FACILITATOR_REQUIRED_HEADINGS = (
    "Mini-Lab Flow",
    "Materials",
    "Facilitator Prompts",
    "Answer-Key Boundary",
    "Synthetic Example Note",
)

HIGH_CONFIDENCE_SECRET_PATTERNS = {
    "aws_access_key_id": re.compile(r"\bA[KS]IA[0-9A-Z]{16}\b"),
    "github_token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,255}\b"),
    "github_fine_grained_token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,255}\b"),
    "openai_api_key": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "private_key_block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}

GENERIC_WARNING_PATTERNS = {
    "credential-boundary": re.compile(
        r"\b(?:credential|credentials|secret|secrets|password|passwords|api key|token|cookie|cookies)\b",
        re.IGNORECASE,
    ),
    "advice-boundary": re.compile(
        r"\b(?:legal|financial|medical|trading|procurement|cybersecurity)\b",
        re.IGNORECASE,
    ),
    "public-action-boundary": re.compile(
        r"\b(?:publish|public posting|payment|payments|account workflow|account workflows)\b",
        re.IGNORECASE,
    ),
}


def repo_root_from_args() -> Path:
    parser = argparse.ArgumentParser(description="Validate the local public-safety kit.")
    parser.add_argument(
        "repo_root",
        nargs="?",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Repository root to validate. Defaults to this script's parent repo.",
    )
    return parser.parse_args().repo_root.resolve()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def markdown_files(root: Path) -> list[Path]:
    ignored_parts = {".git", ".agents", ".codex"}
    return sorted(
        path
        for path in root.rglob("*.md")
        if not any(part in ignored_parts for part in path.relative_to(root).parts)
    )


def check_required_files(root: Path) -> list[str]:
    return [relative for relative in REQUIRED_FILES if not (root / relative).is_file()]


def check_public_boundary_language(root: Path) -> list[str]:
    corpus_parts = []
    for relative in BOUNDARY_DOCUMENTS:
        path = root / relative
        if path.is_file():
            corpus_parts.append(read_text(path).lower())
    corpus = "\n".join(corpus_parts)
    missing = []
    for label, required_terms in BOUNDARY_CHECKS.items():
        if not all(term in corpus for term in required_terms):
            missing.append(label)
    return missing


def check_facilitator_page(root: Path) -> list[str]:
    path = root / FACILITATOR_PAGE
    if not path.is_file():
        return [f"missing rendered facilitator page: {FACILITATOR_PAGE}"]

    text = read_text(path)
    missing = [heading for heading in FACILITATOR_REQUIRED_HEADINGS if f"<h2>{heading}</h2>" not in text]
    return [f"missing facilitator heading: {heading}" for heading in missing]


def scan_markdown(root: Path) -> tuple[dict[str, set[str]], dict[str, set[str]], int]:
    secret_hits: dict[str, set[str]] = defaultdict(set)
    warning_hits: dict[str, set[str]] = defaultdict(set)
    files = markdown_files(root)

    for path in files:
        text = read_text(path)
        relative = path.relative_to(root).as_posix()
        for label, pattern in HIGH_CONFIDENCE_SECRET_PATTERNS.items():
            if pattern.search(text):
                secret_hits[label].add(relative)
        for label, pattern in GENERIC_WARNING_PATTERNS.items():
            if pattern.search(text):
                warning_hits[label].add(relative)

    return secret_hits, warning_hits, len(files)


def format_category_hits(hits: dict[str, set[str]]) -> list[str]:
    lines = []
    for label in sorted(hits):
        files = ", ".join(sorted(hits[label]))
        lines.append(f"- {label}: {len(hits[label])} file(s): {files}")
    return lines


def validate(root: Path) -> int:
    errors: list[str] = []

    missing_files = check_required_files(root)
    if missing_files:
        errors.append("Missing required files:\n" + "\n".join(f"- {p}" for p in missing_files))

    missing_boundaries = check_public_boundary_language(root)
    if missing_boundaries:
        errors.append(
            "Missing public-boundary language:\n"
            + "\n".join(f"- {label}" for label in missing_boundaries)
        )

    facilitator_errors = check_facilitator_page(root)
    if facilitator_errors:
        errors.append(
            "Rendered facilitator page check failed:\n"
            + "\n".join(f"- {error}" for error in facilitator_errors)
        )

    secret_hits, warning_hits, markdown_count = scan_markdown(root)
    if secret_hits:
        errors.append(
            "High-confidence secret-like patterns found; matched strings are intentionally suppressed:\n"
            + "\n".join(format_category_hits(secret_hits))
        )

    if errors:
        print("FAIL kit validation failed", file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    if warning_hits:
        print("WARN category scan notes:")
        for line in format_category_hits(warning_hits):
            print(line)

    print(
        "PASS kit validation succeeded: "
        f"required_files={len(REQUIRED_FILES)} markdown_files={markdown_count} "
        f"warning_categories={len(warning_hits)} facilitator_page=ok"
    )
    return 0


def main() -> int:
    return validate(repo_root_from_args())


if __name__ == "__main__":
    raise SystemExit(main())
