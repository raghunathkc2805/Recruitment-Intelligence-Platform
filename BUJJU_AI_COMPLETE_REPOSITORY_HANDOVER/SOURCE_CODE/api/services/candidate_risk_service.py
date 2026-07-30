from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.candidate_risk import CandidateRisk


class CandidateRiskService:


    @classmethod
    def analyse(
        cls,
        db: Session,
        candidate_id: str,
        employment_history: list,
        resume_data: dict,
    ):

        risks = []

        risk_score = 0


        if len(employment_history) >= 5:

            risks.append(
                "Frequent job changes"
            )

            risk_score += 30


        if resume_data.get(
            "employment_gap",
            False,
        ):

            risks.append(
                "Employment gap detected"
            )

            risk_score += 25


        if resume_data.get(
            "salary_difference",
            False,
        ):

            risks.append(
                "Salary anomaly detected"
            )

            risk_score += 20


        record = CandidateRisk(
            candidate_id=candidate_id,
            risk_score=risk_score,
            risk_factors=json.dumps(
                risks
            ),
            recommendation=(
                "Verify flagged items during recruiter screening"
            ),
        )


        db.add(record)

        db.commit()

        db.refresh(record)

        return record