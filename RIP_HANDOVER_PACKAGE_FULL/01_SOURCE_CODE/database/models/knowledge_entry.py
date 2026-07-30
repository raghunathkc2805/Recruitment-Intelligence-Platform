from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Float, Boolean, DateTime, Text

from database.base import Base


class KnowledgeEntry(Base):

    __tablename__ = "knowledge_entries"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    domain = Column(
        String(100),
        nullable=False,
    )

    category = Column(
        String(100),
        nullable=False,
    )

    key = Column(
        String(255),
        nullable=False,
        index=True,
    )

    value = Column(
        Text,
        nullable=False,
    )

    source = Column(
        String(255),
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    version = Column(
        String(50),
        default="1.0",
    )

    approved = Column(
        Boolean,
        default=False,
    )

    active = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )