from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class AnalyticsEvent(Base):

    __tablename__ = "analytics_events"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    event_type = Column(
        String(100),
        nullable=False,
        index=True,
    )

    entity_type = Column(
        String(100),
    )

    entity_id = Column(
        String,
    )

    metric_value = Column(
        Float,
        default=0,
    )

    metadata_json = Column(
        Text,
        default="{}",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )