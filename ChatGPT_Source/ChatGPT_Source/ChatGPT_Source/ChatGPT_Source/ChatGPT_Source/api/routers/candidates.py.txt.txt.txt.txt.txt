"""
Candidate Router
"""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.dependencies import get_database
from api.schemas.candidate import CandidateCreateRequest
from api.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"],
)


@router.post("")
def create_candidate(
    payload: CandidateCreateRequest,
    db: Session = Depends(get_database),
):
    return CandidateService.create(
        db,
        payload.model_dump(),
    )


@router.get("")
def list_candidates(
    db: Session = Depends(get_database),
):
    return CandidateService.list(db)