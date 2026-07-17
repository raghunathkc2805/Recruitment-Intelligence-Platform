"""
Candidate ORM Model
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class Candidate(Base):

    __tablename__ = "candidates"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        index=True,
    )

    mobile: Mapped[str] = mapped_column(
        String(30),
    )

    location: Mapped[str] = mapped_column(
        String(150),
        default="",
    )

    experience_years: Mapped[float] = mapped_column(
        default=0.0,
    )

    current_designation: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )