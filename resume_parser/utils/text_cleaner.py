"""
Recruitment Intelligence Platform
Resume Parser - Text Cleaner

Normalizes extracted text before it reaches
the extractors.
"""

import unicodedata

from . import regex_patterns as patterns


def normalize_unicode(text: str) -> str:
    """Normalize unicode characters."""
    if not text:
        return ""

    return unicodedata.normalize("NFKC", text)


def remove_control_characters(text: str) -> str:
    """Remove hidden control characters."""
    return patterns.CONTROL_CHARACTERS.sub("", text)


def normalize_quotes(text: str) -> str:
    """Replace smart quotes with ASCII quotes."""

    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201C": '"',
        "\u201D": '"',
        "\u2032": "'",
        "\u2033": '"'
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def normalize_hyphens(text: str) -> str:
    """Normalize unicode hyphens."""

    return patterns.HYPHENS.sub("-", text)


def remove_bullets(text: str) -> str:
    """Convert bullets into line prefixes."""

    return patterns.BULLETS.sub("-", text)


def normalize_whitespace(text: str) -> str:
    """Normalize spaces and line endings."""

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    text = patterns.MULTIPLE_SPACES.sub(" ", text)
    text = patterns.MULTIPLE_NEWLINES.sub("\n\n", text)

    return text


def strip_lines(text: str) -> str:
    """Strip whitespace from every line."""

    cleaned = []

    for line in text.split("\n"):
        cleaned.append(line.strip())

    return "\n".join(cleaned)


def clean(text: str) -> str:
    """
    Complete cleaning pipeline.
    """

    if not text:
        return ""

    text = normalize_unicode(text)

    text = remove_control_characters(text)

    text = normalize_quotes(text)

    text = normalize_hyphens(text)

    text = remove_bullets(text)

    text = normalize_whitespace(text)

    text = strip_lines(text)

    return text.strip()