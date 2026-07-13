"""
Recruitment Intelligence Platform
Achievements Extractor
"""

from __future__ import annotations

from typing import List


class AchievementsExtractor:
    """
    Extract achievements section from resume.
    """

    HEADERS = {
        "achievements",
        "key achievements",
        "professional achievements",
        "awards",
        "accomplishments",
        "recognition",
        "honors",
        "honours",
    }

    STOP_HEADERS = {
        "education",
        "experience",
        "projects",
        "skills",
        "technical skills",
        "certifications",
        "languages",
        "references",
        "interests",
    }

    @classmethod
    def extract(cls, text: str) -> List[str]:

        if not text:
            return []

        achievements = []

        collecting = False

        for line in text.splitlines():

            value = line.strip()

            if not value:
                continue

            lower = value.lower()

            if lower in cls.HEADERS:
                collecting = True
                continue

            if collecting:

                if lower in cls.STOP_HEADERS:
                    break

                achievements.append(value)

        return achievements