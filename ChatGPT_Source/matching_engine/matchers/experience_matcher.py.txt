"""
Recruitment Intelligence Platform
Experience Matcher
"""

from __future__ import annotations


class ExperienceMatcher:
    """
    Matches candidate experience.
    """

    @staticmethod
    def match(
        candidate_experience: dict | None,
        required_years: float | int,
    ) -> dict:

        candidate_years = 0.0

        if candidate_experience:

            candidate_years = float(
                candidate_experience.get(
                    "years",
                    0,
                )
            )

        required_years = float(required_years)

        qualified = (
            candidate_years >= required_years
        )

        score = (
            min(
                round(
                    candidate_years
                    / required_years
                    * 100,
                    2,
                ),
                100,
            )
            if required_years > 0
            else 100
        )

        return {
            "candidate_years": candidate_years,
            "required_years": required_years,
            "qualified": qualified,
            "difference": round(
                candidate_years
                - required_years,
                2,
            ),
            "score": score,
        }