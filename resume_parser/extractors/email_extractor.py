"""
Recruitment Intelligence Platform
Candidate Email Extractor
"""

from __future__ import annotations

from typing import List, Optional

from resume_parser.utils import regex_patterns


class EmailExtractor:
    """
    Extract email addresses from resume text.
    """

    @classmethod
    def extract_all(cls, text: str) -> List[str]:
        """
        Return all unique email addresses.
        """

        if not text:
            return []

        emails = regex_patterns.EMAIL.findall(text)

        unique = []

        for email in emails:

            email = email.strip().lower()

            if email not in unique:
                unique.append(email)

        return unique

    @classmethod
    def extract(cls, text: str) -> Optional[str]:
        """
        Return the primary email address.
        """

        emails = cls.extract_all(text)

        if not emails:
            return None

        return emails[0]

    @classmethod
    def is_valid(cls, email: str) -> bool:

        if not email:
            return False

        return bool(regex_patterns.EMAIL.fullmatch(email))