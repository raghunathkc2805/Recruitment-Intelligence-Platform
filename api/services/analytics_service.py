from __future__ import annotations

import json

from sqlalchemy import func

from sqlalchemy.orm import Session

from database.models.analytics_event import AnalyticsEvent


class AnalyticsService:


    @classmethod
    def record(
        cls,
        db: Session,
        event_type: str,
        entity_type: str,
        entity_id: str,
        metric_value: float,
        metadata: dict,
    ):

        event = AnalyticsEvent(
            event_type=event_type,
            entity_type=entity_type,
            entity_id=entity_id,
            metric_value=metric_value,
            metadata_json=json.dumps(
                metadata
            ),
        )


        db.add(event)

        db.commit()

        db.refresh(event)

        return event



    @classmethod
    def dashboard(
        cls,
        db: Session,
    ):

        total_events = (
            db.query(
                func.count(
                    AnalyticsEvent.id
                )
            )
            .scalar()
        )


        avg_metric = (
            db.query(
                func.avg(
                    AnalyticsEvent.metric_value
                )
            )
            .scalar()
        )


        event_summary = (
            db.query(
                AnalyticsEvent.event_type,
                func.count(
                    AnalyticsEvent.id
                ),
            )
            .group_by(
                AnalyticsEvent.event_type
            )
            .all()
        )


        return {
            "total_events": total_events or 0,
            "average_metric":
                round(
                    avg_metric or 0,
                    2,
                ),
            "event_summary": [
                {
                    "event": row[0],
                    "count": row[1],
                }
                for row in event_summary
            ],
        }