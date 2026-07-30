from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.knowledge_governance_service import KnowledgeGovernanceService


router = APIRouter(
    prefix="/knowledge-governance",
    tags=["Knowledge Governance"],
)


@router.post("/version")
def create_version(
    payload: dict,
    db: DatabaseSession,
):

    return KnowledgeGovernanceService.create_version(
        db,
        payload["knowledge_id"],
        payload.get(
            "old_value",
            "",
        ),
        payload["new_value"],
        payload.get(
            "confidence_score",
            0,
        ),
    )


@router.post("/approve/{version_id}")
def approve(
    version_id: str,
    db: DatabaseSession,
):

    return KnowledgeGovernanceService.approve_version(
        db,
        version_id,
    )


@router.get("/audit/{knowledge_id}")
def audit(
    knowledge_id: str,
    db: DatabaseSession,
):

    return KnowledgeGovernanceService.audit_history(
        db,
        knowledge_id,
    )