from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, Float, DateTime, Boolean

from database.base import Base


class MarketIntelligence(Base):

    __tablename__ = "market_intelligence"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    domain = Column(
        String(100),
        nullable=False,
        index=True,
    )

    intelligence_type = Column(
        String(100),
        nullable=False,
    )

    title = Column(
        String(255),
    )

    information = Column(
        Text,
        default="{}",
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    approved = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )