from fastapi import APIRouter

from api.dependencies import DatabaseSession
from api.services.knowledge_service import KnowledgeService


router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge Intelligence"],
)


@router.post("/{knowledge_id}/approve")
def approve(
    knowledge_id: str,
    db: DatabaseSession,
):
    return KnowledgeService.approve(
        db,
        knowledge_id,
    )


@router.put("/{knowledge_id}/update")
def update(
    knowledge_id: str,
    payload: dict,
    db: DatabaseSession,
):
    return KnowledgeService.update(
        db,
        knowledge_id,
        payload["value"],
    )


@router.get("/{knowledge_id}/history")
def history(
    knowledge_id: str,
    db: DatabaseSession,
):
    return KnowledgeService.history(
        db,
        knowledge_id,
    )


@router.post("/{knowledge_id}/rollback")
def rollback(
    knowledge_id: str,
    payload: dict,
    db: DatabaseSession,
):
    return KnowledgeService.rollback(
        db,
        knowledge_id,
        payload["version"],
    )