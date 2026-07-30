from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Float

from database.base import Base


class KnowledgeGraphRelation(Base):

    __tablename__ = "knowledge_graph_relations"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    source_node_id = Column(
        String,
        nullable=False,
        index=True,
    )

    target_node_id = Column(
        String,
        nullable=False,
        index=True,
    )

    relation_type = Column(
        String(100),
        nullable=False,
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )