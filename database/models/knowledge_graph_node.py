from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Text

from database.base import Base


class KnowledgeGraphNode(Base):

    __tablename__ = "knowledge_graph_nodes"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    node_type = Column(
        String(100),
        nullable=False,
        index=True,
    )

    name = Column(
        String(255),
        nullable=False,
        index=True,
    )

    metadata_json = Column(
        Text,
        default="{}",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )