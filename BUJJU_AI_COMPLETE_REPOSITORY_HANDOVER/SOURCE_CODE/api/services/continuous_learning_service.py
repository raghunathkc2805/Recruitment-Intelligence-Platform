from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.continuous_learning_event import ContinuousLearningEvent


class ContinuousLearningService:


    @classmethod
    def capture(
        cls,
        db: Session,
        event_type: str,
        entity_type: str,
        entity_id: str,
        data: dict,
        confidence_score: float = 0,
    ):

        event = ContinuousLearningEvent(
            event_type=event_type,
            entity_type=entity_type,
            entity_id=entity_id,
            data=json.dumps(data),
            confidence_score=confidence_score,
        )

        db.add(event)

        db.commit()

        db.refresh(event)

        return event


    @classmethod
    def history(
        cls,
        db: Session,
        entity_type: str,
        entity_id: str,
    ):

        return (
            db.query(ContinuousLearningEvent)
            .filter(
                ContinuousLearningEvent.entity_type ==
                entity_type,
                ContinuousLearningEvent.entity_id ==
                entity_id,
            )
            .order_by(
                ContinuousLearningEvent.created_at.desc()
            )
            .all()
        )


    @classmethod
    def approve(
        cls,
        db: Session,
        event_id: str,
    ):

        event = (
            db.query(ContinuousLearningEvent)
            .filter(
                ContinuousLearningEvent.id ==
                event_id
            )
            .first()
        )

        if not event:
            return None


        event.approved = True

        db.commit()

        db.refresh(event)

        return event