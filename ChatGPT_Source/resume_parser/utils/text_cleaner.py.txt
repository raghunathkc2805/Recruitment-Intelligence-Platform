"""
Recruitment Intelligence Platform
Text Cleaner
"""

from __future__ import annotations

import html
import re


class TextCleaner:
    """
    Standard text normalization used across all resume parsers.
    """

    _MULTIPLE_SPACES = re.compile(r"[ \t]+")
    _MULTIPLE_NEWLINES = re.compile(r"\n{3,}")
    _NON_BREAKING_SPACE = re.compile(r"[\u00A0\u2007\u202F]")
    _ZERO_WIDTH = re.compile(r"[\u200B-\u200D\uFEFF]")

    @classmethod
    def clean(cls, text: str | None) -> str:

        if not text:
            return ""

        text = html.unescape(text)

        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        text = cls._NON_BREAKING_SPACE.sub(" ", text)
        text = cls._ZERO_WIDTH.sub("", text)

        lines = []

        for line in text.split("\n"):

            line = cls._MULTIPLE_SPACES.sub(" ", line)

            line = line.strip()

            lines.append(line)

        text = "\n".join(lines)

        text = cls._MULTIPLE_NEWLINES.sub("\n\n", text)

        return text.strip()


clean = TextCleaner.clean