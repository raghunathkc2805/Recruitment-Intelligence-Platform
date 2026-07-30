from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class TalentMarketplace(Base):

    __tablename__ = "talent_marketplace"

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

    candidate_type = Column(
        String(100),
        nullable=False,
    )

    availability_status = Column(
        String(100),
        default="Available",
    )

    skill_profile = Column(
        Text,
        default="[]",
    )

    previous_outcome = Column(
        String(100),
    )

    match_score = Column(
        Float,
        default=0,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )