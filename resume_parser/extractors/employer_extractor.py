"""
Recruitment Intelligence Platform
Employer Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List

from resume_parser.utils.knowledge_base import COMPANIES


class EmployerExtractor:
    """
    Extract employers using the company knowledge base.
    """

    @staticmethod
    def _compile(company: str):

        return re.compile(
            rf"\b{re.escape(company)}\b",
            re.IGNORECASE,
        )

    @classmethod
    def extract(cls, text: str) -> List[Dict]:

        if not text:
            return []

        employers = []

        for company in COMPANIES:

            pattern = cls._compile(company)

            if pattern.search(text):

                employers.append(
                    {
                        "company": company,
                        "confidence": 100.0,
                    }
                )

        employers.sort(key=lambda item: item["company"])

        return employers