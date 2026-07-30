from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class JDIntelligence(Base):

    __tablename__ = "jd_intelligence"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    job_id = Column(
        String,
        nullable=False,
        index=True,
    )

    quality_score = Column(
        Float,
        default=0,
    )

    skill_coverage_score = Column(
        Float,
        default=0,
    )

    missing_information = Column(
        Text,
        default="[]",
    )

    recommendations = Column(
        Text,
        default="[]",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )