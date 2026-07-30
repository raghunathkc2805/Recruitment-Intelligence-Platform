from fastapi import APIRouter

from api.dependencies import DatabaseSession

from api.services.candidate_relationship_service import CandidateRelationshipService


router = APIRouter(
    prefix="/candidate-relationship",
    tags=["Candidate Relationship Intelligence"],
)


@router.post("/record")
def record(
    payload: dict,
    db: DatabaseSession,
):

    return CandidateRelationshipService.record(
        db,
        payload["candidate_id"],
        payload["interaction_type"],
        payload.get(
            "message",
            "",
        ),
    )


@router.get("/{candidate_id}")
def history(
    candidate_id: str,
    db: DatabaseSession,
):

    return CandidateRelationshipService.history(
        db,
        candidate_id,
    )