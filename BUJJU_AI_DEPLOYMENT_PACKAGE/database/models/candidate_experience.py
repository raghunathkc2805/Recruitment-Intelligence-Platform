"""
Candidate Experience ORM Model
"""

from __future__ import annotations

import uuid

from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class CandidateExperience(Base):

    __tablename__ = "candidate_experience"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    company_name: Mapped[str] = mapped_column(
        String(255),
    )

    designation: Mapped[str] = mapped_column(
        String(255),
    )

    experience_years: Mapped[float] = mapped_column(
        Float,
        default=0,
    )
