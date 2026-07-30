from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.knowledge_graph_node import KnowledgeGraphNode
from database.models.knowledge_graph_relation import KnowledgeGraphRelation


class KnowledgeGraphService:


    @classmethod
    def create_node(
        cls,
        db: Session,
        node_type: str,
        name: str,
        metadata=None,
    ):

        node = KnowledgeGraphNode(
            node_type=node_type,
            name=name,
            metadata_json=json.dumps(
                metadata or {}
            ),
        )

        db.add(node)
        db.commit()
        db.refresh(node)

        return node


    @classmethod
    def create_relation(
        cls,
        db: Session,
        source_node_id: str,
        target_node_id: str,
        relation_type: str,
        confidence_score: float = 0,
    ):

        relation = KnowledgeGraphRelation(
            source_node_id=source_node_id,
            target_node_id=target_node_id,
            relation_type=relation_type,
            confidence_score=confidence_score,
        )

        db.add(relation)
        db.commit()
        db.refresh(relation)

        return relation


    @classmethod
    def search_nodes(
        cls,
        db: Session,
        node_type: str,
        name: str,
    ):

        return (
            db.query(KnowledgeGraphNode)
            .filter(
                KnowledgeGraphNode.node_type ==
                node_type,
                KnowledgeGraphNode.name.ilike(
                    f"%{name}%"
                )
            )
            .all()
        )