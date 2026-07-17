"""
Enterprise Recommendation Engine
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RecommendationResult:

    candidate_id: str

    score: float

    matched_skills: int

    total_skills: int

    experience_score: float

    designation_score: float

    certification_score: float

    location_score: float

    final_score: float


class RecommendationEngine:

    SKILL_WEIGHT = 50.0
    EXPERIENCE_WEIGHT = 20.0
    DESIGNATION_WEIGHT = 15.0
    CERTIFICATION_WEIGHT = 10.0
    LOCATION_WEIGHT = 5.0

    @classmethod
    def calculate(

        cls,

        *,

        matched_skills: int,

        total_required_skills: int,

        experience_match: float,

        designation_match: bool,

        certification_match: float,

        location_match: bool,

    ) -> RecommendationResult:

        if total_required_skills == 0:

            skill_score = cls.SKILL_WEIGHT

        else:

            skill_score = (

                matched_skills

                / total_required_skills

            ) * cls.SKILL_WEIGHT

        experience_score = (

            experience_match

            * cls.EXPERIENCE_WEIGHT

        )

        designation_score = (

            cls.DESIGNATION_WEIGHT

            if designation_match

            else 0.0

        )

        certification_score = (

            certification_match

            * cls.CERTIFICATION_WEIGHT

        )

        location_score = (

            cls.LOCATION_WEIGHT

            if location_match

            else 0.0

        )

        final_score = round(

            skill_score
            + experience_score
            + designation_score
            + certification_score
            + location_score,

            2,

        )

        return RecommendationResult(

            candidate_id="",

            score=final_score,

            matched_skills=matched_skills,

            total_skills=total_required_skills,

            experience_score=round(
                experience_score,
                2,
            ),

            designation_score=round(
                designation_score,
                2,
            ),

            certification_score=round(
                certification_score,
                2,
            ),

            location_score=round(
                location_score,
                2,
            ),

            final_score=final_score,

        )
