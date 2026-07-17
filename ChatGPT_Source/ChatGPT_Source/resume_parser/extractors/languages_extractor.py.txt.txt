"""
Recruitment Intelligence Platform
Language Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List

from resume_parser.utils.knowledge_base import LANGUAGES


class LanguageExtractor:
    """
    Extract languages known by the candidate.
    """

    PROFICIENCY_PATTERN = re.compile(
        r"(basic|beginner|intermediate|advanced|fluent|native|professional)",
        re.IGNORECASE,
    )

    @staticmethod
    def _compile(language: str):

        return re.compile(
            rf"\b{re.escape(language)}\b",
            re.IGNORECASE,
        )

    @classmethod
    def extract(cls, text: str) -> List[Dict]:

        if not text:
            return []

        results = []

        for language in LANGUAGES:

            pattern = cls._compile(language)

            for match in pattern.finditer(text):

                start = max(0, match.start() - 50)
                end = min(len(text), match.end() + 50)

                context = text[start:end]

                proficiency = cls.PROFICIENCY_PATTERN.search(context)

                results.append(
                    {
                        "language": language,
                        "proficiency": (
                            proficiency.group(0).title()
                            if proficiency
                            else None
                        ),
                        "confidence": 100.0,
                    }
                )

                break

        return sorted(
            results,
            key=lambda x: x["language"],
        )