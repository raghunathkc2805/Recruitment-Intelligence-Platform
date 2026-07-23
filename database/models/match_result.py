"""
Match Result ORM Model
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from database.base import Base


class MatchResult(Base):

    __tablename__ = "match_results"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    job_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    recommendation: Mapped[str] = mapped_column(
        String(100),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )