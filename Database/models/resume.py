"""
Resume ORM Model
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class Resume(Base):

    __tablename__ = "resumes"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
        nullable=False,
    )

    file_name: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    resume_hash: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        index=True,
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        default="",
        nullable=False,
    )

    parser_version: Mapped[str] = mapped_column(
        String(50),
        default="1.0",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
