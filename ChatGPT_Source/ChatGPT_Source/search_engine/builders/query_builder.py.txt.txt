"""
Recruitment Intelligence Platform
Query Builder
"""

from __future__ import annotations


class QueryBuilder:
    """
    Builds normalized search queries.
    """

    @classmethod
    def build(
        cls,
        keywords: list[str] | None = None,
        skills: list[str] | None = None,
        locations: list[str] | None = None,
        experience: int | None = None,
    ) -> str:

        parts: list[str] = []

        if keywords:
            parts.extend(
                keyword.strip()
                for keyword in keywords
                if keyword.strip()
            )

        if skills:
            parts.extend(
                skill.strip()
                for skill in skills
                if skill.strip()
            )

        if locations:
            parts.extend(
                location.strip()
                for location in locations
                if location.strip()
            )

        if experience is not None:
            parts.append(
                f"{experience} years"
            )

        return " AND ".join(parts)