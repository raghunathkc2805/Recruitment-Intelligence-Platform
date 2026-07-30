from __future__ import annotations

from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from database.models.knowledge_refresh_schedule import KnowledgeRefreshSchedule


class KnowledgeRefreshService:


    @classmethod
    def create_schedule(
        cls,
        db: Session,
        domain: str,
        frequency: str,
    ):

        days = {

            "daily": 1,

            "weekly": 7,

            "monthly": 30,

        }.get(
            frequency.lower(),
            30,
        )


        schedule = KnowledgeRefreshSchedule(
            domain=domain,
            frequency=frequency,
            last_refresh=None,
            next_refresh=datetime.utcnow()
            +
            timedelta(
                days=days
            ),
        )


        db.add(schedule)

        db.commit()

        db.refresh(schedule)

        return schedule


    @classmethod
    def pending_refreshes(
        cls,
        db: Session,
    ):

        return (
            db.query(
                KnowledgeRefreshSchedule
            )
            .filter(
                KnowledgeRefreshSchedule.next_refresh
                <=
                datetime.utcnow()
            )
            .all()
        )