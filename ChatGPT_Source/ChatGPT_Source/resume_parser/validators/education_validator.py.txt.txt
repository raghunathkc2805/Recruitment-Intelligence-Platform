"""
Recruitment Intelligence Platform
Education Validator
"""

from __future__ import annotations


class EducationValidator:
    """
    Validate extracted education records.
    """

    REQUIRED_FIELDS = {
        "degree",
        "text",
    }

    @classmethod
    def validate(cls, education: list | None) -> bool:

        if not education:
            return False

        if not isinstance(education, list):
            return False

        for record in education:

            if not isinstance(record, dict):
                return False

            if not cls.REQUIRED_FIELDS.issubset(record.keys()):
                return False

            if not record.get("degree"):
                return False

        return True