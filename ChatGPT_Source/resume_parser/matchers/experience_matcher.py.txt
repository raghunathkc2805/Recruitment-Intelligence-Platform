"""
Recruitment Intelligence Platform
Experience Matcher
"""

from __future__ import annotations


class ExperienceMatcher:
    """
    Compare candidate experience against required experience.
    """

    @staticmethod
    def match(
        candidate_experience: dict | None,
        required_years: float | int,
    ) -> dict:

        if not candidate_experience:

            return {
                "candidate_years": 0.0,
                "required_years": float(required_years),
                "qualified": False,
                "score": 0.0,
            }

        candidate_years = float(
            candidate_experience.get("years", 0)
        )

        required_years = float(required_years)

        qualified = candidate_years >= required_years

        score = min(
            100.0,
            round(
                (candidate_years / required_years) * 100,
                2,
            ) if required_years else 100.0,
        )

        return {
            "candidate_years": candidate_years,
            "required_years": required_years,
            "qualified": qualified,
            "score": score,
        }