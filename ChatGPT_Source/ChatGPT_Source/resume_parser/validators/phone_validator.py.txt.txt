"""
Recruitment Intelligence Platform
Phone Validator
"""

from __future__ import annotations

from resume_parser.extractors.phone_extractor import PhoneExtractor


class PhoneValidator:
    """
    Validate phone numbers.
    """

    @staticmethod
    def validate(phone: str | None) -> bool:

        if not phone:
            return False

        return PhoneExtractor.is_valid(phone)