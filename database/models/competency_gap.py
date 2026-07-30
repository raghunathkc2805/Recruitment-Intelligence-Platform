from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, Float, DateTime

from database.base import Base


class CompetencyGap(Base):

    __tablename__ = "competency_gaps"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_id = Column(
        String,
        nullable=False,
        index=True,
    )

    job_id = Column(
        String,
        nullable=False,
        index=True,
    )

    missing_competencies = Column(
        Text,
        default="[]",
    )

    verification_priority = Column(
        Float,
        default=0,
    )

    recommendation = Column(
        Text,
        default="",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )