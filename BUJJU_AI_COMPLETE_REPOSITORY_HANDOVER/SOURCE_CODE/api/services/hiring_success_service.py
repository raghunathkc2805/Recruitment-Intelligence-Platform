from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.hiring_success import HiringSuccess


class HiringSuccessService:


    @classmethod
    def record(
        cls,
        db: Session,
        candidate_id: str,
        recruiter_id: str,
        source: str,
        outcome: str,
        acceptance_score: float,
        joining_success: float,
        feedback: str,
    ):

        record = HiringSuccess(
            candidate_id=candidate_id,
            recruiter_id=recruiter_id,
            source=source,
            outcome=outcome,
            acceptance_score=acceptance_score,
            joining_success=joining_success,
            feedback=feedback,
        )


        db.add(record)

        db.commit()

        db.refresh(record)

        return record


    @classmethod
    def analyse_source(
        cls,
        db: Session,
        source: str,
    ):

        records = (
            db.query(HiringSuccess)
            .filter(
                HiringSuccess.source ==
                source
            )
            .all()
        )


        total = len(records)

        joined = len(
            [
                r
                for r in records
                if r.outcome == "Joined"
            ]
        )


        return {
            "source": source,
            "total_candidates": total,
            "joining_rate":
                round(
                    (
                        joined
                        /
                        total
                    )
                    *
                    100,
                    2,
                )
                if total
                else 0,
        }