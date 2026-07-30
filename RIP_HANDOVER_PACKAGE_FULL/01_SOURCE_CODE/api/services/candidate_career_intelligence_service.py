from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.candidate_career_intelligence import CandidateCareerIntelligence


class CandidateCareerIntelligenceService:


    @classmethod
    def analyse(
        cls,
        db: Session,
        candidate_id: str,
        experience: list,
        designation_history: list,
    ):

        company_count = len(
            experience
        )

        stability_score = max(
            0,
            100 - (
                max(
                    company_count - 3,
                    0
                )
                *
                10
            )
        )


        growth_score = min(
            100,
            len(
                designation_history
            )
            *
            20,
        )


        predicted_level = "Senior Professional"


        if growth_score >= 80:
            predicted_level = "Leadership Role"


        record = CandidateCareerIntelligence(
            candidate_id=candidate_id,
            stability_score=stability_score,
            growth_score=growth_score,
            predicted_next_level=predicted_level,
            career_summary=json.dumps(
                {
                    "companies": company_count,
                    "designation_changes": len(designation_history),
                }
            ),
        )


        db.add(record)

        db.commit()

        db.refresh(record)

        return record