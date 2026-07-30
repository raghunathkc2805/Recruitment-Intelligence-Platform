"""
Recruitment Intelligence Platform
Candidate Name Extractor
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from resume_parser.utils import regex_patterns


BLACKLIST = {
    "resume",
    "curriculum vitae",
    "cv",
    "profile",
    "summary",
    "objective",
    "experience",
    "education",
    "skills",
    "technical skills",
    "professional summary",
}


class NameExtractor:
    """
    Extract candidate name from resume text.
    """

    SEARCH_LINES = 15

    @classmethod
    def extract(cls, text: str) -> Optional[str]:

        if not text:
            return None

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        for line in lines[: cls.SEARCH_LINES]:

            value = line.lower()

            if value in BLACKLIST:
                continue

            if len(line) > 60:
                continue

            if any(char.isdigit() for char in line):
                continue

            if regex_patterns.EMAIL.search(line):
                continue

            if regex_patterns.PHONE.search(line):
                continue

            if regex_patterns.NAME.fullmatch(line):

                return line

        return None