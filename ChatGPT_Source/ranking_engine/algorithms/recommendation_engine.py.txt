"""
Recruitment Intelligence Platform
Recommendation Engine
"""

from __future__ import annotations


class RecommendationEngine:

    @staticmethod
    def recommend(
        score: float,
    ) -> dict:

        if score >= 90:
            return {
                "recommendation": "Highly Recommended",
                "priority": "High",
            }

        if score >= 75:
            return {
                "recommendation": "Recommended",
                "priority": "Medium",
            }

        if score >= 60:
            return {
                "recommendation": "Consider",
                "priority": "Low",
            }

        return {
            "recommendation": "Not Recommended",
            "priority": "Reject",
        }