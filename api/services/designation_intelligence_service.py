from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.knowledge_graph_node import KnowledgeGraphNode


class DesignationIntelligenceService:


    @classmethod
    def register_designation(
        cls,
        db: Session,
        designation: str,
        domain: str = "General",
    ):

        existing = (
            db.query(KnowledgeGraphNode)
            .filter(
                KnowledgeGraphNode.node_type ==
                "DESIGNATION",
                KnowledgeGraphNode.name ==
                designation,
            )
            .first()
        )

        if existing:
            return existing


        node = KnowledgeGraphNode(
            node_type="DESIGNATION",
            name=designation,
            metadata_json=(
                '{"domain":"' +
                domain +
                '"}'
            ),
        )

        db.add(node)
        db.commit()
        db.refresh(node)

        return node


    @classmethod
    def search_designation(
        cls,
        db: Session,
        designation: str,
    ):

        return (
            db.query(KnowledgeGraphNode)
            .filter(
                KnowledgeGraphNode.node_type ==
                "DESIGNATION",
                KnowledgeGraphNode.name.ilike(
                    f"%{designation}%"
                ),
            )
            .all()
        )


    @classmethod
    def find_related_roles(
        cls,
        db: Session,
        designation: str,
    ):

        roles = []

        nodes = cls.search_designation(
            db,
            designation,
        )

        for node in nodes:
            roles.append(
                {
                    "designation": node.name,
                    "metadata": node.metadata_json,
                }
            )

        return roles