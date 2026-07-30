"""
Recruitment Intelligence Platform
Recruiter Query Extractor
"""

from __future__ import annotations


class RecruiterQueryExtractor:
    """
    Generates recruiter-friendly search queries from a parsed candidate profile.
    """

    @classmethod
    def extract(
        cls,
        candidate: dict,
    ) -> dict:

        skills = candidate.get("skills", {})

        technical = skills.get(
            "technical_skills",
            [],
        )

        functional = skills.get(
            "functional_skills",
            [],
        )

        locations = [
            item.get("location")
            for item in candidate.get(
                "locations",
                [],
            )
            if item.get("location")
        ]

        experience = candidate.get(
            "experience"
        )

        years = ""

        if isinstance(experience, dict):

            value = experience.get("years")

            if value is not None:

                years = f"{value} Years"

        query_parts = []

        if technical:
            query_parts.append(
                " ".join(technical)
            )

        if functional:
            query_parts.append(
                " ".join(functional)
            )

        if years:
            query_parts.append(years)

        if locations:
            query_parts.append(
                " OR ".join(locations)
            )

        return {
            "recruiter_query": " | ".join(query_parts),
            "technical_skills": technical,
            "functional_skills": functional,
            "locations": locations,
            "experience": years,
        }