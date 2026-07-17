"""
Candidate Certification Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate_certification import CandidateCertification

from .base_repository import BaseRepository


class CandidateCertificationRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, **kwargs):

        return self.add(
            CandidateCertification(**kwargs)
        )
