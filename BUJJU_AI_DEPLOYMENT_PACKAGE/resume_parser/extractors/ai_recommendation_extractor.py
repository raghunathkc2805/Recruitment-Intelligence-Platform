"""
Recruitment Intelligence Platform
AI Recommendation Extractor
"""

from __future__ import annotations

from resume_parser.ranking.recommendation_engine import (
    RecommendationEngine,
)
from resume_parser.ranking.scoring_engine import (
    ScoringEngine,
)


class AIRecommendationExtractor:
    """
    Generates an AI hiring recommendation based on
    candidate matching results.
    """

    @classmethod
    def extract(
        cls,
        match_result: dict,
    ) -> dict:

        scoring = ScoringEngine.calculate(
            match_result
        )

        recommendation = (
            RecommendationEngine.recommend(
                scoring["overall_score"]
            )
        )

        return {
            "overall_score": scoring["overall_score"],
            "weights": scoring["weights"],
            "recommendation": recommendation[
                "recommendation"
            ],
            "priority": recommendation[
                "priority"
            ],
        }