"""
Recruitment Intelligence Platform
Resume Search Extractor
"""

from __future__ import annotations

from typing import Dict, List


class ResumeSearchExtractor:
    """
    Generates searchable keywords from a parsed resume.
    """

    @classmethod
    def extract(cls, candidate: dict) -> Dict:

        keywords = set()

        if candidate.get("name"):
            keywords.add(candidate["name"])

        skills = candidate.get("skills", {})

        keywords.update(
            skills.get("technical_skills", [])
        )

        keywords.update(
            skills.get("functional_skills", [])
        )

        keywords.update(
            skills.get("soft_skills", [])
        )

        for item in candidate.get("education", []):

            if item.get("degree"):
                keywords.add(item["degree"])

        for item in candidate.get("employers", []):

            if item.get("company"):
                keywords.add(item["company"])

        for item in candidate.get("locations", []):

            if item.get("location"):
                keywords.add(item["location"])

        for item in candidate.get("certifications", []):

            if item.get("certification"):
                keywords.add(item["certification"])

        return {
            "keywords": sorted(keywords),
            "keyword_count": len(keywords),
        }