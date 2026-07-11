"""
Recruitment Intelligence Platform
Summary Extractor
"""

from __future__ import annotations

from typing import Optional


SUMMARY_HEADERS = {

    "professional summary",

    "summary",

    "profile",

    "career summary",

    "executive summary",

    "objective",

    "career objective",

    "about me",

}


STOP_HEADERS = {

    "experience",

    "professional experience",

    "employment",

    "education",

    "skills",

    "technical skills",

    "projects",

    "certifications",

    "languages",

    "achievements",

}


class SummaryExtractor:
    """
    Extract candidate summary/profile section.
    """

    @classmethod
    def extract(cls, text: str) -> Optional[str]:

        if not text:

            return None

        lines = text.splitlines()

        collecting = False

        summary = []

        for line in lines:

            value = line.strip()

            if not value:

                continue

            lower = value.lower()

            if lower in SUMMARY_HEADERS:

                collecting = True

                continue

            if collecting:

                if lower in STOP_HEADERS:

                    break

                summary.append(value)

        if not summary:

            return None

        return "\n".join(summary).strip()