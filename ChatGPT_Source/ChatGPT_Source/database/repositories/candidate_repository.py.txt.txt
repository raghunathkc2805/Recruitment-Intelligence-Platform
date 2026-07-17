"""
Candidate Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.candidate import Candidate

from .base_repository import BaseRepository


class CandidateRepository(BaseRepository):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

    def create(
        self,
        candidate: Candidate,
    ) -> Candidate:

        return self.add(candidate)

    def get(
        self,
        candidate_id: str,
    ) -> Candidate | None:

        return (
            self.db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )

    def get_by_email(
        self,
        email: str,
    ) -> Candidate | None:

        return (
            self.db.query(Candidate)
            .filter(Candidate.email == email)
            .first()
        )

    def list(
        self,
    ) -> list[Candidate]:

        return (
            self.db.query(Candidate)
            .order_by(Candidate.full_name)
            .all()
        )