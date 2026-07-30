"""
Recruitment Intelligence Platform
Production Phone Extractor
"""

from __future__ import annotations

import re
from typing import List, Optional


PHONE_REGEX = re.compile(
    r"""
    (?:
        (?:\+91[\s\-]?)?
        (?:0[\s\-]?)?
        [6-9]\d{9}
    )
    |
    (?:
        \+\d{1,3}[\s\-]?\d{6,14}
    )
    |
    (?:
        \(\d{2,5}\)[\s\-]?\d{6,10}
    )
    |
    (?:
        \d{2,5}[\s\-]\d{6,10}
    )
    """,
    re.VERBOSE,
)


class PhoneExtractor:

    @staticmethod
    def normalize(phone: str) -> str:

        phone = phone.strip()

        plus = phone.startswith("+")

        digits = re.sub(r"\D", "", phone)

        if plus:
            return "+" + digits

        return digits

    @classmethod
    def is_valid(cls, phone: str) -> bool:

        digits = re.sub(r"\D", "", phone)

        return 10 <= len(digits) <= 15

    @classmethod
    def extract_all(cls, text: str) -> List[str]:

        if not text:
            return []

        phones = []
        seen = set()

        for match in PHONE_REGEX.finditer(text):

            phone = cls.normalize(match.group())

            if not cls.is_valid(phone):
                continue

            if phone not in seen:
                seen.add(phone)
                phones.append(phone)

        return phones

    @classmethod
    def extract(cls, text: str) -> Optional[str]:

        phones = cls.extract_all(text)

        if not phones:
            return None

        return phones[0]