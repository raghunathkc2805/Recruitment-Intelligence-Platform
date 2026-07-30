"""
Candidate Project Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate_project import CandidateProject

from .base_repository import BaseRepository


class CandidateProjectRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, **kwargs):

        return self.add(
            CandidateProject(**kwargs)
        )
