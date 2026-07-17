"""
Recruitment Intelligence Platform
Email Validator
"""

from __future__ import annotations

from resume_parser.extractors.email_extractor import EmailExtractor


class EmailValidator:
    """
    Validate email addresses.
    """

    @staticmethod
    def validate(email: str | None) -> bool:

        if not email:
            return False

        return EmailExtractor.is_valid(email)