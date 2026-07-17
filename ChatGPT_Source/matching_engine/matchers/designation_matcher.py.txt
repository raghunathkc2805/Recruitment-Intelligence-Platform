"""
Recruitment Intelligence Platform
Designation Matcher
"""

from __future__ import annotations


class DesignationMatcher:
    """
    Matches candidate designation.
    """

    @staticmethod
    def match(
        candidate_designations: list[str],
        required_designations: list[str],
    ) -> dict:

        candidate = {
            item.strip().lower()
            for item in candidate_designations
            if item
        }

        required = {
            item.strip().lower()
            for item in required_designations
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