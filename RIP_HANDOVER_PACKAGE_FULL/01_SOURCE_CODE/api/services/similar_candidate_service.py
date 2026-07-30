from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.candidate_recommendation import CandidateRecommendation


class SimilarCandidateService:


    @classmethod
    def recommend(
        cls,
        db: Session,
        candidate_id: str,
        candidates: list,
    ):

        recommendations = []


        source_skills = set(
            candidates[0].get(
                "skills",
                [],
            )
        )


        for candidate in candidates:

            if candidate.get(
                "id"
            ) == candidate_id:

                continue


            candidate_skills = set(
                candidate.get(
                    "skills",
                    [],
                )
            )


            intersection = (
                source_skills
                &
                candidate_skills
            )


            score = 0

            if source_skills:

                score = round(
                    (
                        len(intersection)
                        /
                        len(source_skills)
                    )
                    *
                    100,
                    2,
                )


            if score:

                record = CandidateRecommendation(
                    source_candidate_id=candidate_id,
                    recommended_candidate_id=candidate["id"],
                    recommendation_type="SIMILAR_CANDIDATE",
                    similarity_score=score,
                    explanation=json.dumps(
                        {
                            "common_skills":
                                list(intersection)
                        }
                    ),
                )


                db.add(record)

                recommendations.append(
                    record
                )


        db.commit()

        return recommendations