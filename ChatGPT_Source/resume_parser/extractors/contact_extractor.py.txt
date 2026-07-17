"""
Recruitment Intelligence Platform
Contact Extractor
"""

from __future__ import annotations

from typing import Dict

from resume_parser.extractors.email_extractor import EmailExtractor
from resume_parser.extractors.name_extractor import NameExtractor
from resume_parser.extractors.phone_extractor import PhoneExtractor


class ContactExtractor:
    """
    Extract candidate contact information.
    """

    @classmethod
    def extract(cls, text: str) -> Dict:

        return {
            "name": NameExtractor.extract(text),
            "email": EmailExtractor.extract(text),
            "phone": PhoneExtractor.extract(text),
        }