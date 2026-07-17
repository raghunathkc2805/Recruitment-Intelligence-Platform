"""
Recruitment Intelligence Platform
Location Matcher
"""

from __future__ import annotations


class LocationMatcher:
    """
    Match candidate locations against required locations.
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
            location.strip().lower()
            for location in required_locations
            if location
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