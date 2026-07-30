from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class CandidateCareerIntelligence(Base):

    __tablename__ = "candidate_career_intelligence"

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

    stability_score = Column(
        Float,
        default=0,
    )

    growth_score = Column(
        Float,
        default=0,
    )

    predicted_next_level = Column(
        String(200),
    )

    career_summary = Column(
        Text,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )