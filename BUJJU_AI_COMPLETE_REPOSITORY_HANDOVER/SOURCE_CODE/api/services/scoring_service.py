"""
Enterprise Candidate Scoring Service
"""

from __future__ import annotations


class ScoringService:

    SKILL_WEIGHT = 50
    EXPERIENCE_WEIGHT = 20
    DESIGNATION_WEIGHT = 15
    LOCATION_WEIGHT = 10
    CERTIFICATION_WEIGHT = 5

    @classmethod
    def calculate(

        cls,

        *,

        matched_skills: int,

        total_skills: int,

        candidate_experience: float,

        required_experience: float,

        candidate_designation: str,

        required_designation: str,

        candidate_location: str,

        required_location: str,

        certification_score: float = 0,

    ):

        score = 0

        if total_skills:

            score += (

                matched_skills

                / total_skills

            ) * cls.SKILL_WEIGHT

        if candidate_experience >= required_experience:

            score += cls.EXPERIENCE_WEIGHT

        elif required_experience > 0:

            score += (

                candidate_experience

                / required_experience

            ) * cls.EXPERIENCE_WEIGHT

        if (

            candidate_designation.lower()

            == required_designation.lower()

        ):

            score += cls.DESIGNATION_WEIGHT

        if (

            candidate_location.lower()

            == required_location.lower()

        ):

            score += cls.LOCATION_WEIGHT

        score += min(

            certification_score,

            cls.CERTIFICATION_WEIGHT,

        )

        return round(

            score,

            2,

        )
