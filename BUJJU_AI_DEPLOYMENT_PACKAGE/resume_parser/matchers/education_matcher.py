"""
Recruitment Intelligence Platform
Education Matcher
"""

from __future__ import annotations


class EducationMatcher:
    """
    Match candidate education against required education.
    """

    @staticmethod
    def match(
        candidate_education: list[dict],
        required_degrees: list[str],
    ) -> dict:

        candidate = {
            item.get("degree", "").strip().lower()
            for item in candidate_education
            if item.get("degree")
        }

        required = {
            degree.strip().lower()
            for degree in required_degrees
            if degree
        }

        matched = sorted(candidate & required)

        missing = sorted(required - candidate)

        score = (
            round(
                (len(matched) / len(required)) * 100,
                2,
            )
            if required
            else 100.0
        )

        return {
            "matched": matched,
            "missing": missing,
            "matched_count": len(matched),
            "required_count": len(required),
            "score": score,
        }