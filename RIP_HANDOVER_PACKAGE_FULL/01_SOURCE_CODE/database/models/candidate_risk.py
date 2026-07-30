from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class CandidateRisk(Base):

    __tablename__ = "candidate_risks"

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

    risk_score = Column(
        Float,
        default=0,
    )

    risk_factors = Column(
        Text,
        default="[]",
    )

    recommendation = Column(
        Text,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )