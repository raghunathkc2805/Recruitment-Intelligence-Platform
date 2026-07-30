from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, Float, DateTime, Boolean

from database.base import Base


class ContinuousLearningEvent(Base):

    __tablename__ = "continuous_learning_events"

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
        nullable=False,
    )

    entity_id = Column(
        String,
        nullable=False,
        index=True,
    )

    data = Column(
        Text,
        default="{}",
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    approved = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )