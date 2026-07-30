"""
Recruitment Intelligence Platform
Designation Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List

from resume_parser.utils.knowledge_base import DESIGNATIONS


class DesignationExtractor:
    """
    Extract designations from resume text using the knowledge base.
    Falls back to common designation patterns when needed.
    """

    FALLBACK_DESIGNATIONS = [
        "Software Engineer",
        "Senior Software Engineer",
        "Lead Software Engineer",
        "Technical Lead",
        "Team Lead",
        "Project Manager",
        "Program Manager",
        "Engineering Manager",
        "Architect",
        "Solution Architect",
        "DevOps Engineer",
        "Cloud Engineer",
        "Network Engineer",
        "System Engineer",
        "Data Engineer",
        "Data Scientist",
        "Business Analyst",
        "QA Engineer",
        "Test Engineer",
        "Consultant",
    ]

    @staticmethod
    def _compile(value: str):

        return re.compile(
            rf"\b{re.escape(value)}\b",
            re.IGNORECASE,
        )

    @classmethod
    def _knowledge_base_designations(cls) -> List[str]:

        values = []

        if isinstance(DESIGNATIONS, dict):

            for item in DESIGNATIONS.values():

                if isinstance(item, list):
                    values.extend(item)

                elif isinstance(item, str):
                    values.append(item)

        elif isinstance(DESIGNATIONS, list):

            values.extend(DESIGNATIONS)

        return values

    @classmethod
    def extract(cls, text: str) -> List[Dict]:

        if not text:
            return []

        results = []

        seen = set()

        all_designations = (
            cls._knowledge_base_designations()
            + cls.FALLBACK_DESIGNATIONS
        )

        for designation in all_designations:

            key = designation.lower()

            if key in seen:
                continue

            if cls._compile(designation).search(text):

                results.append(
                    {
                        "designation": designation,
                        "confidence": 100.0,
                    }
                )

                seen.add(key)

        return sorted(
            results,
            key=lambda item: item["designation"],
        )