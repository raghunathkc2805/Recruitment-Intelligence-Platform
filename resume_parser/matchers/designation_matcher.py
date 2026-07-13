"""
Recruitment Intelligence Platform
Designation Matcher
"""

from __future__ import annotations


class DesignationMatcher:
    """
    Match candidate designations against required designations.
    """

    @staticmethod
    def match(
        candidate_designations: list[str],
        required_designations: list[str],
    ) -> dict:

        candidate = {
            designation.strip().lower()
            for designation in candidate_designations
            if designation
        }

        required = {
            designation.strip().lower()
            for designation in required_designations
            if designation
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