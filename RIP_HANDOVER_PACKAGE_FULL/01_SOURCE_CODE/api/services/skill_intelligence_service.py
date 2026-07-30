from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.knowledge_graph_node import KnowledgeGraphNode
from database.models.knowledge_graph_relation import KnowledgeGraphRelation


class SkillIntelligenceService:


    @classmethod
    def register_skill(
        cls,
        db: Session,
        skill_name: str,
        category: str = "General",
        confidence: float = 0,
    ):

        existing = (
            db.query(KnowledgeGraphNode)
            .filter(
                KnowledgeGraphNode.name ==
                skill_name,
                KnowledgeGraphNode.node_type ==
                "SKILL",
            )
            .first()
        )

        if existing:
            return existing


        node = KnowledgeGraphNode(
            node_type="SKILL",
            name=skill_name,
            metadata_json=f'{{"category":"{category}"}}',
        )

        db.add(node)
        db.commit()
        db.refresh(node)

        return node


    @classmethod
    def relate_skill(
        cls,
        db: Session,
        skill_id: str,
        related_skill_id: str,
        relation="RELATED_TO",
        confidence=0,
    ):

        graph = KnowledgeGraphRelation(
            source_node_id=skill_id,
            target_node_id=related_skill_id,
            relation_type=relation,
            confidence_score=confidence,
        )

        db.add(graph)
        db.commit()
        db.refresh(graph)

        return graph


    @classmethod
    def search_skill(
        cls,
        db: Session,
        skill_name: str,
    ):

        return (
            db.query(KnowledgeGraphNode)
            .filter(
                KnowledgeGraphNode.node_type ==
                "SKILL",
                KnowledgeGraphNode.name.ilike(
                    f"%{skill_name}%"
                ),
            )
            .all()
        )