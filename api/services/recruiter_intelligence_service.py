from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.recruiter_performance import RecruiterPerformance


class RecruiterIntelligenceService:


    @classmethod
    def analyse(
        cls,
        db: Session,
        recruiter_id: str,
        hires: list,
        domains: list,
    ):

        successful = len(
            [
                item
                for item in hires
                if item.get(
                    "status"
                ) == "Joined"
            ]
        )


        effectiveness = 0

        if hires:

            effectiveness = round(
                (
                    successful
                    /
                    len(hires)
                )
                *
                100,
                2,
            )


        record = RecruiterPerformance(
            recruiter_id=recruiter_id,
            specialization=", ".join(
                domains
            ),
            successful_hires=successful,
            effectiveness_score=effectiveness,
            intelligence_summary=json.dumps(
                {
                    "strengths": domains,
                    "hire_count": len(hires),
                }
            ),
        )


        db.add(record)

        db.commit()

        db.refresh(record)

        return record