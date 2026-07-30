"""
Recruitment Intelligence Platform
Domain Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List

from resume_parser.utils.knowledge_base import DOMAINS


class DomainExtractor:
    """
    Extract business/technology domains from resume text.
    """

    @staticmethod
    def _compile(domain: str):

        return re.compile(
            rf"\b{re.escape(domain)}\b",
            re.IGNORECASE,
        )

    @classmethod
    def extract(cls, text: str) -> List[Dict]:

        if not text:
            return []

        results = []

        for domain in DOMAINS:

            if cls._compile(domain).search(text):

                results.append(
                    {
                        "domain": domain,
                        "confidence": 100.0,
                    }
                )

        return sorted(
            results,
            key=lambda item: item["domain"],
        )