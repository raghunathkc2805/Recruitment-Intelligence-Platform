from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime

from database.base import Base


class WhatsAppOutreach(Base):

    __tablename__ = "whatsapp_outreach"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    candidate_id = Column(
        String,
        nullable=False,
        index=True,
    )

    template_name = Column(
        String(200),
    )

    message = Column(
        Text,
    )

    status = Column(
        String(100),
        default="Created",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )