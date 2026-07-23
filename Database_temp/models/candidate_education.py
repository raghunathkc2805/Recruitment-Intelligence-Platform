"""
Candidate Education ORM Model
"""

from __future__ import annotations

import uuid

from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class CandidateEducation(Base):

    __tablename__ = "candidate_education"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    degree: Mapped[str] = mapped_column(
        String(255),
    )

    specialization: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    institution: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    passing_year: Mapped[str] = mapped_column(
        String(20),
        default="",
    )
