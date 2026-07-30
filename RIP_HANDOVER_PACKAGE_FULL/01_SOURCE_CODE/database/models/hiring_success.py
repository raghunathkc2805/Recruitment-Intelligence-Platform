from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Text, DateTime

from database.base import Base


class HiringSuccess(Base):

    __tablename__ = "hiring_success"

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

    source = Column(
        String(200),
    )

    recruiter_id = Column(
        String(200),
    )

    outcome = Column(
        String(100),
    )

    acceptance_score = Column(
        Float,
        default=0,
    )

    joining_success = Column(
        Float,
        default=0,
    )

    feedback = Column(
        Text,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )