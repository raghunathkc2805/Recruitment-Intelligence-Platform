from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class CandidateIntelligence(Base):

    __tablename__ = "candidate_intelligence"

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

    intelligence_type = Column(
        String(100),
        nullable=False,
    )

    score = Column(
        Float,
        default=0,
    )

    explanation = Column(
        Text,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )