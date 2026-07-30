from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class RecruiterPerformance(Base):

    __tablename__ = "recruiter_performance"

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

    specialization = Column(
        String(200),
    )

    successful_hires = Column(
        Float,
        default=0,
    )

    average_time_to_hire = Column(
        Float,
        default=0,
    )

    effectiveness_score = Column(
        Float,
        default=0,
    )

    intelligence_summary = Column(
        Text,
        default="{}",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )