"""
Resume ORM Model
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

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
    )

    file_name: Mapped[str] = mapped_column(
        String(300),
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
    )

    parser_version: Mapped[str] = mapped_column(
        String(50),
        default="1.0",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )