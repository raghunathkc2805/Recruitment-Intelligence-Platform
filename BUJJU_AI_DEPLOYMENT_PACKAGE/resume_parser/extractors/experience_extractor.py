"""
Recruitment Intelligence Platform
Experience Extractor

Extracts total years/months of experience mentioned
explicitly in a resume.

Career timeline calculation is handled separately
in Resume Intelligence (Pack 2).
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional


class ExperienceExtractor:

    EXPERIENCE_PATTERN = re.compile(
        r"""
        (?P<years>\d+(?:\.\d+)?)
        \s*
        (?:\+)?\s*
        (?:years?|yrs?|year|yr)

        (?:\s*(?:and|&)?\s*)?

        (?:
            (?P<months>\d+)
            \s*
            (?:months?|mos?|month|mo)
        )?
        """,
        re.IGNORECASE | re.VERBOSE,
    )

    @classmethod
    def extract_all(cls, text: str) -> List[Dict]:

        if not text:
            return []

        matches = []

        for match in cls.EXPERIENCE_PATTERN.finditer(text):

            years = float(match.group("years"))

            months = match.group("months")

            months = int(months) if months else 0

            total_months = int(years * 12) + months

            matches.append(
                {
                    "text": match.group(0),
                    "years": years,
                    "months": months,
                    "total_months": total_months,
                }
            )

        return matches

    @classmethod
    def extract(cls, text: str) -> Optional[Dict]:

        experiences = cls.extract_all(text)

        if not experiences:
            return None

        return max(
            experiences,
            key=lambda item: item["total_months"],
        )