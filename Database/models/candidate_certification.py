"""
Candidate Certification ORM Model
"""

from __future__ import annotations

import uuid

from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class CandidateCertification(Base):

    __tablename__ = "candidate_certifications"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    certification_name: Mapped[str] = mapped_column(
        String(255),
    )

    issuing_organization: Mapped[str] = mapped_column(
        String(255),
        default="",
    )
