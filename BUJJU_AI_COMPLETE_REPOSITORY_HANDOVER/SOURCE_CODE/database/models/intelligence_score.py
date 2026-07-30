from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class IntelligenceScore(Base):

    __tablename__ = "intelligence_scores"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
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

    overall_score = Column(
        Float,
        default=0,
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    explanation = Column(
        Text,
        default="{}",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )