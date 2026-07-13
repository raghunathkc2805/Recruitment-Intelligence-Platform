"""
Recruitment Intelligence Platform
Location Matcher
"""

from __future__ import annotations


class LocationMatcher:
    """
    Matches candidate location with required location.
    """

    @staticmethod
    def match(
        candidate_locations: list[dict],
        required_locations: list[str],
    ) -> dict:

        candidate = {
            item.get("location", "").strip().lower()
            for item in candidate_locations
            if item.get("location")
        }

        required = {
            item.strip().lower()
            for item in required_locations
            if item
        }

        matched = sorted(candidate & required)

        missing = sorted(required - candidate)

        additional = sorted(candidate - required)

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
            "additional": additional,
            "matched_count": len(matched),
            "required_count": len(required),
            "candidate_count": len(candidate),
            "score": score,
        }