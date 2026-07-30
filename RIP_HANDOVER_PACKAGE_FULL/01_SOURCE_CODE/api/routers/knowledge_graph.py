from fastapi import APIRouter

from api.dependencies import DatabaseSession
from api.services.knowledge_graph_service import KnowledgeGraphService


router = APIRouter(
    prefix="/knowledge-graph",
    tags=["Knowledge Graph"],
)


@router.post("/node")
def create_node(
    payload: dict,
    db: DatabaseSession,
):

    return KnowledgeGraphService.create_node(
        db,
        payload["node_type"],
        payload["name"],
        payload.get("metadata"),
    )


@router.post("/relation")
def create_relation(
    payload: dict,
    db: DatabaseSession,
):

    return KnowledgeGraphService.create_relation(
        db,
        payload["source_node_id"],
        payload["target_node_id"],
        payload["relation_type"],
        payload.get(
            "confidence_score",
            0,
        ),
    )


@router.post("/search")
def search(
    payload: dict,
    db: DatabaseSession,
):

    return KnowledgeGraphService.search_nodes(
        db,
        payload["node_type"],
        payload["name"],
    )