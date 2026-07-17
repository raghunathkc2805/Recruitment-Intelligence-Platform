"""
Recruitment Intelligence Platform
Scoring Engine
"""

from __future__ import annotations


class ScoringEngine:
    """
    Calculates weighted candidate scores.
    """

    DEFAULT_WEIGHTS = {
        "skills": 0.35,
        "experience": 0.25,
        "education": 0.15,
        "designation": 0.10,
        "location": 0.05,
        "certification": 0.10,
    }

    @classmethod
    def calculate(
        cls,
        match_result: dict,
        weights: dict | None = None,
    ) -> dict:

        weights = weights or cls.DEFAULT_WEIGHTS

        weighted_score = (
            match_result["skill_match"]["score"] * weights["skills"]
            + match_result["experience_match"]["score"] * weights["experience"]
            + match_result["education_match"]["score"] * weights["education"]
            + match_result["designation_match"]["score"] * weights["designation"]
            + match_result["location_match"]["score"] * weights["location"]
            + match_result["certification_match"]["score"] * weights["certification"]
        )

        return {
            "overall_score": round(weighted_score, 2),
            "weights": weights,
        }