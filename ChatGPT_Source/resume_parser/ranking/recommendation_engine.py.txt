"""
Recruitment Intelligence Platform
Recommendation Engine
"""

from __future__ import annotations


class RecommendationEngine:
    """
    Converts ranking scores into hiring recommendations.
    """

    RECOMMENDED = 85.0
    CONSIDER = 70.0
    REVIEW = 50.0

    @classmethod
    def recommend(
        cls,
        score: float,
    ) -> dict:

        if score >= cls.RECOMMENDED:

            recommendation = "Highly Recommended"

            priority = "High"

        elif score >= cls.CONSIDER:

            recommendation = "Recommended"

            priority = "Medium"

        elif score >= cls.REVIEW:

            recommendation = "Consider"

            priority = "Low"

        else:

            recommendation = "Not Recommended"

            priority = "Reject"

        return {
            "score": round(score, 2),
            "recommendation": recommendation,
            "priority": priority,
        }