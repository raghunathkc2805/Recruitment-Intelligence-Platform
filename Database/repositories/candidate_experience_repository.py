"""
Candidate Experience Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate_experience import CandidateExperience

from .base_repository import BaseRepository


class CandidateExperienceRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, **kwargs):

        return self.add(
            CandidateExperience(**kwargs)
        )
