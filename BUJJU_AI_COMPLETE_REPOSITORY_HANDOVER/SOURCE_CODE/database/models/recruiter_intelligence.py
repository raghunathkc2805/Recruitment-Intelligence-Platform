from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, Float

from database.base import Base


class RecruiterIntelligence(Base):

    __tablename__ = "recruiter_intelligence"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    recruiter_id = Column(
        String,
        nullable=False,
        index=True,
    )

    query = Column(
        Text,
    )

    recommendation = Column(
        Text,
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )