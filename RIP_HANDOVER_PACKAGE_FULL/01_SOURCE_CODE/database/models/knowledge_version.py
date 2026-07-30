from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, Float, DateTime, Boolean

from database.base import Base


class KnowledgeVersion(Base):

    __tablename__ = "knowledge_versions"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    knowledge_id = Column(
        String,
        nullable=False,
        index=True,
    )

    version = Column(
        String(50),
        nullable=False,
    )

    previous_value = Column(
        Text,
    )

    new_value = Column(
        Text,
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    approved = Column(
        Boolean,
        default=False,
    )

    created_by = Column(
        String(100),
        default="system",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )