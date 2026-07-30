from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.competency_gap import CompetencyGap


class CompetencyGapService:


    @classmethod
    def analyse(
        cls,
        db: Session,
        candidate_id: str,
        job_id: str,
        candidate_skills: list,
        required_skills: list,
    ):

        candidate = {
            x.lower()
            for x in candidate_skills
        }


        required = {
            x.lower()
            for x in required_skills
        }


        missing = sorted(
            required - candidate
        )


        priority = (
            len(missing)
            /
            max(
                len(required),
                1
            )
        ) * 100


        gap = CompetencyGap(
            candidate_id=candidate_id,
            job_id=job_id,
            missing_competencies=json.dumps(
                missing
            ),
            verification_priority=round(
                priority,
                2,
            ),
            recommendation=(
                "Verify missing competencies during recruiter screening"
            ),
        )


        db.add(gap)

        db.commit()

        db.refresh(gap)


        return gap