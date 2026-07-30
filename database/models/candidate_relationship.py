from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime, Integer

from database.base import Base


class CandidateRelationship(Base):

    __tablename__ = "candidate_relationships"

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

    interaction_type = Column(
        String(100),
        nullable=False,
    )

    message = Column(
        Text,
    )

    response_status = Column(
        String(100),
        default="Pending",
    )

    interaction_count = Column(
        Integer,
        default=1,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )