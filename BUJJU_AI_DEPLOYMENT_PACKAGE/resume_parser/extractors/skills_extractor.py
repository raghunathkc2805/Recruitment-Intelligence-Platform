"""
Recruitment Intelligence Platform
Production Skills Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List

from resume_parser.utils.knowledge_base import SKILLS


class SkillsExtractor:
    """
    Production-grade Skills Extractor.

    Features
    --------
    ✓ Whole-word matching
    ✓ Duplicate removal
    ✓ Case-insensitive
    ✓ Category-wise extraction
    ✓ Confidence score
    """

    @staticmethod
    def _compile(skill: str):

        return re.compile(
            rf"\b{re.escape(skill)}\b",
            re.IGNORECASE,
        )

    @classmethod
    def _extract_category(
        cls,
        text: str,
        skills: List[str],
    ) -> List[str]:

        found = []

        for skill in skills:

            pattern = cls._compile(skill)

            if pattern.search(text):

                found.append(skill)

        return sorted(set(found))

    @classmethod
    def extract(cls, text: str) -> Dict:

        if not text:

            return {

                "technical_skills": [],

                "functional_skills": [],

                "soft_skills": [],

                "matched_skills": 0,

                "confidence": 0.0

            }

        technical = cls._extract_category(
            text,
            SKILLS["technical_skills"]
        )

        functional = cls._extract_category(
            text,
            SKILLS["functional_skills"]
        )

        soft = cls._extract_category(
            text,
            SKILLS["soft_skills"]
        )

        total = len(
            technical
        ) + len(
            functional
        ) + len(
            soft
        )

        kb_total = (
            len(SKILLS["technical_skills"])
            + len(SKILLS["functional_skills"])
            + len(SKILLS["soft_skills"])
        )

        confidence = round(
            (total / kb_total) * 100,
            2,
        )

        return {

            "technical_skills": technical,

            "functional_skills": functional,

            "soft_skills": soft,

            "matched_skills": total,

            "confidence": confidence

        }