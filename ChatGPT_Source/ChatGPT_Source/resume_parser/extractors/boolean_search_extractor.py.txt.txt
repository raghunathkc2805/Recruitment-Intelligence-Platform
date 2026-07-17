"""
Recruitment Intelligence Platform
Boolean Search Extractor
"""

from __future__ import annotations


class BooleanSearchExtractor:
    """
    Generates Boolean search strings from a parsed candidate profile.
    """

    @classmethod
    def extract(cls, candidate: dict) -> dict:

        skills = candidate.get("skills", {})

        keywords = []

        keywords.extend(
            skills.get("technical_skills", [])
        )

        keywords.extend(
            skills.get("functional_skills", [])
        )

        keywords.extend(
            skills.get("soft_skills", [])
        )

        for item in candidate.get("education", []):

            if item.get("degree"):
                keywords.append(item["degree"])

        for item in candidate.get("employers", []):

            if item.get("company"):
                keywords.append(item["company"])

        keywords = sorted(
            {
                keyword.strip()
                for keyword in keywords
                if keyword
            }
        )

        boolean_string = " OR ".join(
            f'"{keyword}"'
            for keyword in keywords
        )

        return {
            "keywords": keywords,
            "boolean_search": boolean_string,
            "keyword_count": len(keywords),
        }