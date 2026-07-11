"""
Recruitment Intelligence Platform
Production Phone Extractor

Supports:
- Indian Mobile Numbers
- International Numbers
- Landlines
- Multiple Phone Numbers
- Duplicate Removal
- Normalization
"""

from __future__ import annotations

import re
from typing import List, Optional


PHONE_REGEX = re.compile(
    r"""
    (?:
        (?:\+?\d{1,3})?          # Optional country code
        [\s\-./]*
    )
    (?:
        \(?\d{2,5}\)?            # Optional STD code
        [\s\-./]*
    )?
    (?:
        \d[\d\s\-./]{8,15}\d
    )
    """,
    re.VERBOSE,
)


class PhoneExtractor:

    MIN_DIGITS = 10
    MAX_DIGITS = 15

    @staticmethod
    def normalize(phone: str) -> str:
        """
        Convert phone number into a standard format.
        """

        phone = phone.strip()

        has_plus = phone.startswith("+")

        digits = re.sub(r"\D", "", phone)

        if has_plus:
            return "+" + digits

        return digits

    @classmethod
    def is_valid(cls, phone: str) -> bool:

        digits = re.sub(r"\D", "", phone)

        return cls.MIN_DIGITS <= len(digits) <= cls.MAX_DIGITS

    @classmethod
    def extract_all(cls, text: str) -> List[str]:

        if not text:
            return []

        phones = []

        for match in PHONE_REGEX.finditer(text):

            phone = cls.normalize(match.group(0))

            if not cls.is_valid(phone):
                continue

            if phone not in phones:
                phones.append(phone)

        return phones

    @classmethod
    def extract(cls, text: str) -> Optional[str]:

        phones = cls.extract_all(text)

        if not phones:
            return None

        return phones[0]