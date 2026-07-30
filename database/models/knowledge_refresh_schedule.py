from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Boolean

from database.base import Base


class KnowledgeRefreshSchedule(Base):

    __tablename__ = "knowledge_refresh_schedule"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    domain = Column(
        String(100),
        nullable=False,
    )

    frequency = Column(
        String(50),
        nullable=False,
    )

    last_refresh = Column(
        DateTime,
    )

    next_refresh = Column(
        DateTime,
    )

    active = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )