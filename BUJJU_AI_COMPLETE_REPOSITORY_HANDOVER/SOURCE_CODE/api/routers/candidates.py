"""
Candidate Router
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import status

from api.auth.permission_constants import Permission
from api.auth.permission_dependency import require_permission
from api.dependencies import DatabaseSession
from api.schemas.candidate import (
    CandidateCreateRequest,
    CandidateUpdateRequest,
)
from api.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"],
)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
def create_candidate(
    payload: CandidateCreateRequest,
    db: DatabaseSession,
    _=Depends(
        require_permission(
            Permission.CANDIDATE_CREATE,
        ),
    ),
):
    return CandidateService.create(
        db,
        payload.model_dump(),
    )


@router.get("")
def list_candidates(
    db: DatabaseSession,
    _=Depends(
        require_permission(
            Permission.CANDIDATE_VIEW,
        ),
    ),
):
    return CandidateService.list(db)


@router.get("/{candidate_id}")
def get_candidate(
    candidate_id: str,
    db: DatabaseSession,
    _=Depends(
        require_permission(
            Permission.CANDIDATE_VIEW,
        ),
    ),
):
    candidate = CandidateService.get(
        db,
        candidate_id,
    )

    if candidate is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found.",
        )

    return candidate


@router.put("/{candidate_id}")
def update_candidate(
    candidate_id: str,
    payload: CandidateUpdateRequest,
    db: DatabaseSession,
    _=Depends(
        require_permission(
            Permission.CANDIDATE_UPDATE,
        ),
    ),
):
    candidate = CandidateService.update(
        db,
        candidate_id,
        payload.model_dump(),
    )

    if candidate is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found.",
        )

    return candidate


@router.delete(
    "/{candidate_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_candidate(
    candidate_id: str,
    db: DatabaseSession,
    _=Depends(
        require_permission(
            Permission.CANDIDATE_DELETE,
        ),
    ),
):
    deleted = CandidateService.delete(
        db,
        candidate_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found.",
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
