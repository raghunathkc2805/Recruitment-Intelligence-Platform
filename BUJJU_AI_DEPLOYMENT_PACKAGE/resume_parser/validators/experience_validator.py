"""
Recruitment Intelligence Platform
Experience Validator
"""

from __future__ import annotations


class ExperienceValidator:
    """
    Validate extracted experience information.
    """

    MAX_EXPERIENCE_YEARS = 60

    @classmethod
    def validate(cls, experience: dict | None) -> bool:

        if not experience:
            return False

        years = experience.get("years")

        if years is None:
            return False

        try:
            years = float(years)
        except (TypeError, ValueError):
            return False

        return 0 <= years <= cls.MAX_EXPERIENCE_YEARS