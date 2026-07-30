"""
Recruitment Intelligence Platform
Location Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List

from resume_parser.utils.knowledge_base import LOCATIONS


class LocationExtractor:
    """
    Extract locations using the location knowledge base.
    """

    @staticmethod
    def _compile(location: str):

        return re.compile(
            rf"\b{re.escape(location)}\b",
            re.IGNORECASE,
        )

    @classmethod
    def extract(cls, text: str) -> List[Dict]:

        if not text:
            return []

        results = []

        for location in LOCATIONS:

            pattern = cls._compile(location)

            if pattern.search(text):

                results.append(
                    {
                        "location": location,
                        "confidence": 100.0
                    }
                )

        results.sort(key=lambda item: item["location"])

        return results