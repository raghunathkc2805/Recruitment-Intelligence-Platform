"""
Recruitment Intelligence Platform
Education Matcher
"""

from __future__ import annotations


class EducationMatcher:
    """
    Matches candidate education.
    """

    @staticmethod
    def match(
        candidate_education: list[dict],
        required_education: list[str],
    ) -> dict:

        candidate = {
            item["degree"].strip().lower()
            for item in candidate_education
            if item.get("degree")
        }

        required = {
            item.strip().lower()
            for item in required_education
            if item
        }

        matched = sorted(
            candidate & required
        )

        missing = sorted(
            required - candidate
        )

        additional = sorted(
            candidate - required
        )

        score = (
            round(
                len(matched)
                / len(required)
                * 100,
                2,
            )
            if required
            else 100
        )

        return {
            "matched": matched,
            "missing": missing,
            "additional": additional,
            "score": score,
        }