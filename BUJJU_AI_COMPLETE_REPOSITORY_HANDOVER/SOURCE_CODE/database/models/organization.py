"""
Organization ORM Model
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class Organization(Base):

    __tablename__ = "organizations"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    organization_name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
    )

    organization_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )

    contact_email: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )