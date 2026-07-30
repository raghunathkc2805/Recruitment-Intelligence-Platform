from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate_relationship import CandidateRelationship


class CandidateRelationshipService:


    @classmethod
    def record(
        cls,
        db: Session,
        candidate_id: str,
        interaction_type: str,
        message: str,
    ):

        record = CandidateRelationship(
            candidate_id=candidate_id,
            interaction_type=interaction_type,
            message=message,
        )

        db.add(record)

        db.commit()

        db.refresh(record)

        return record


    @classmethod
    def history(
        cls,
        db: Session,
        candidate_id: str,
    ):

        return (
            db.query(CandidateRelationship)
            .filter(
                CandidateRelationship.candidate_id ==
                candidate_id
            )
            .order_by(
                CandidateRelationship.created_at.desc()
            )
            .all()
        )