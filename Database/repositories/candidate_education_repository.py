"""
Candidate Education Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate_education import CandidateEducation

from .base_repository import BaseRepository


class CandidateEducationRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, **kwargs):

        return self.add(
            CandidateEducation(**kwargs)
        )
