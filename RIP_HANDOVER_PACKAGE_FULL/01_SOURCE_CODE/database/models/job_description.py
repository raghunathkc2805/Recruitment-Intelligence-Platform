"""
Job Description ORM Model
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from database.base import Base


class JobDescription(Base):

    __tablename__ = "job_descriptions"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    job_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )

    designation: Mapped[str] = mapped_column(
        String(255),
    )

    location: Mapped[str] = mapped_column(
        String(150),
        default="",
    )

    experience_required: Mapped[float] = mapped_column(
        default=0.0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )