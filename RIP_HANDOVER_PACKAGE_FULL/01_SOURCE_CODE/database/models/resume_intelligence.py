from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class ResumeIntelligence(Base):

    __tablename__ = "resume_intelligence"

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

    completeness_score = Column(
        Float,
        default=0,
    )

    role_match_score = Column(
        Float,
        default=0,
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    missing_skills = Column(
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