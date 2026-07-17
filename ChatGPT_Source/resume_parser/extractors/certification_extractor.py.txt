"""
Recruitment Intelligence Platform
Certification Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List

from resume_parser.utils.knowledge_base import CERTIFICATIONS


class CertificationExtractor:
    """
    Extract certifications using the certification
    knowledge base.
    """

    @staticmethod
    def _compile(certification: str):

        return re.compile(
            rf"\b{re.escape(certification)}\b",
            re.IGNORECASE,
        )

    @classmethod
    def extract(cls, text: str) -> List[Dict]:

        if not text:
            return []

        certifications = []

        for certification in CERTIFICATIONS:

            pattern = cls._compile(certification)

            if pattern.search(text):

                certifications.append(
                    {
                        "certification": certification,
                        "confidence": 100.0,
                    }
                )

        certifications.sort(
            key=lambda item: item["certification"]
        )

        return certifications