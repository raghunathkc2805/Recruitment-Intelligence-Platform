"""
Recruitment Intelligence Platform
Scoring Engine
"""

from __future__ import annotations

from ranking_engine.constants import DEFAULT_WEIGHTS


class ScoringEngine:
    """
    Calculates weighted score.
    """

    @classmethod
    def calculate(
        cls,
        match_result: dict,
        weights: dict | None = None,
    ) -> dict:

        weights = weights or DEFAULT_WEIGHTS

        score = (
            match_result["skill_match"]["score"] * weights["skills"]
            + match_result["experience_match"]["score"] * weights["experience"]
            + match_result["education_match"]["score"] * weights["education"]
            + match_result["designation_match"]["score"] * weights["designation"]
            + match_result["location_match"]["score"] * weights["location"]
            + match_result["certification_match"]["score"] * weights["certification"]
        ) / 100

        return {
            "overall_score": round(score, 2),
            "weights": weights,
        }