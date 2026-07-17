"""
Recruitment Intelligence Platform
Matching Service
"""

from __future__ import annotations

from matching_engine.exceptions import (
    InvalidCandidateError,
    InvalidJobError,
)
from matching_engine.matchers.overall_matcher import OverallMatcher


class MatchingService:
    """
    Executes the complete matching workflow.
    """

    @classmethod
    def match(
        cls,
        candidate: dict,
        job: dict,
    ) -> dict:

        if not isinstance(candidate, dict):
            raise InvalidCandidateError(
                "Candidate must be a dictionary."
            )

        if not isinstance(job, dict):
            raise InvalidJobError(
                "Job must be a dictionary."
            )

        result = OverallMatcher.match(
            candidate,
            job,
        )

        score = result["overall_score"]

        if score >= 90:
            recommendation = "Highly Recommended"
            priority = "High"
        elif score >= 75:
            recommendation = "Recommended"
            priority = "Medium"
        elif score >= 60:
            recommendation = "Consider"
            priority = "Low"
        else:
            recommendation = "Not Recommended"
            priority = "Reject"

        return {
            "candidate": candidate,
            "job": job,
            "match_result": result,
            "overall_score": score,
            "weights": {},
            "recommendation": recommendation,
            "priority": priority,
        }