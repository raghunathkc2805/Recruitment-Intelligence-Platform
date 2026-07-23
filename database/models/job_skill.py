"""
Job Skill ORM Model
"""

from __future__ import annotations

import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class JobSkill(Base):

    __tablename__ = "job_skills"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    job_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    skill_name: Mapped[str] = mapped_column(
        String(150),
        index=True,
    )

    skill_category: Mapped[str] = mapped_column(
        String(100),
        default="General",
    )
