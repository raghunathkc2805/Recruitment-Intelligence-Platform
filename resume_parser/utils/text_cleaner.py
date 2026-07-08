from __future__ import annotations

import re
from typing import Iterable


class TextCleaner:
    """
    Standard text cleaning utility for Resume Parser.

    - Normalizes whitespace
    - Removes null characters
    - Removes excessive blank lines
    - Normalizes unicode quotes/dashes
    """

    _SPACE_RE = re.compile(r"[ \t]+")
    _BLANK_LINES_RE = re.compile(r"\n\s*\n+")

    _REPLACEMENTS = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201C": '"',
        "\u201D": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u00A0": " ",
        "\x00": "",
    }

    @classmethod
    def clean(cls, text: str) -> str:
        if not text:
            return ""

        for old, new in cls._REPLACEMENTS.items():
            text = text.replace(old, new)

        lines = [cls._clean_line(line) for line in text.splitlines()]

        text = "\n".join(lines)

        text = cls._BLANK_LINES_RE.sub("\n\n", text)

        return text.strip()

    @classmethod
    def clean_lines(cls, lines: Iterable[str]) -> list[str]:
        return [
            cls._clean_line(line)
            for line in lines
            if line and line.strip()
        ]

    @classmethod
    def _clean_line(cls, line: str) -> str:
        line = cls._SPACE_RE.sub(" ", line)
        return line.strip()