"""
Candidate Project ORM Model
"""

from __future__ import annotations

import uuid

from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class CandidateProject(Base):

    __tablename__ = "candidate_projects"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    project_name: Mapped[str] = mapped_column(
        String(255),
    )

    description: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    technologies: Mapped[str] = mapped_column(
        Text,
        default="",
    )
