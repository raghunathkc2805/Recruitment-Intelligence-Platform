from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime

from database.base import Base


class KnowledgeAudit(Base):

    __tablename__ = "knowledge_audits"

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

    action = Column(
        String(100),
        nullable=False,
    )

    performed_by = Column(
        String(100),
        default="system",
    )

    details = Column(
        Text,
        default="{}",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )