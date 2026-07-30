from __future__ import annotations

from matching_engine.matchers.overall_matcher import OverallMatcher
from api.services.explainable_ai_service import ExplainableAIService


class AICandidateRankingService:


    @classmethod
    def rank(
        cls,
        candidates: list,
        job: dict,
    ):

        ranked = []


        for candidate in candidates:

            match_result = OverallMatcher.match(
                candidate,
                job,
            )


            explanation = ExplainableAIService.generate(
                match_result["skill_match"]["score"],
                match_result["experience_match"]["score"],
                match_result["location_match"]["score"],
                match_result.get(
                    "organization_match",
                    {}
                ).get(
                    "score",
                    0,
                ),
            )


            ranked.append(
                {
                    "candidate": candidate,
                    "match_result": match_result,
                    "ai_score": explanation["overall_score"],
                    "confidence_score": explanation["confidence_score"],
                    "recommendation": explanation["recommendation"],
                    "explanation": explanation["explanation"],
                }
            )


        return sorted(
            ranked,
            key=lambda x: x["ai_score"],
            reverse=True,
        )