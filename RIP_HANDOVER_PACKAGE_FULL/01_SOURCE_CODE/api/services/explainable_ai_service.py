from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.intelligence_score import IntelligenceScore


class ExplainableAIService:


    @classmethod
    def generate(
        cls,
        skill_score: float,
        experience_score: float,
        location_score: float,
        organization_score: float = 0,
    ):

        weights = {

            "skills": 0.40,

            "experience": 0.30,

            "location": 0.10,

            "organization": 0.20,

        }


        overall = round(

            (
                skill_score
                *
                weights["skills"]
            )
            +
            (
                experience_score
                *
                weights["experience"]
            )
            +
            (
                location_score
                *
                weights["location"]
            )
            +
            (
                organization_score
                *
                weights["organization"]
            ),

            2,

        )


        recommendation = "Review Candidate"


        if overall >= 80:

            recommendation = "Highly Recommended"

        elif overall >= 60:

            recommendation = "Recommended"


        return {

            "overall_score": overall,

            "confidence_score":
                min(
                    95,
                    overall + 10,
                ),

            "recommendation":
                recommendation,

            "explanation":
                {

                    "skill_match":
                        skill_score,

                    "experience_match":
                        experience_score,

                    "location_match":
                        location_score,

                    "organization_match":
                        organization_score,

                    "reason":
                        (
                            "Recommendation generated "
                            "using explainable weighted scoring"
                        ),

                }

        }



    @classmethod
    def save(
        cls,
        db: Session,
        entity_type: str,
        entity_id: str,
        result: dict,
    ):

        record = IntelligenceScore(

            entity_type=entity_type,

            entity_id=entity_id,

            overall_score=result["overall_score"],

            confidence_score=result["confidence_score"],

            explanation=json.dumps(
                result["explanation"]
            ),

        )


        db.add(record)

        db.commit()

        db.refresh(record)


        return record