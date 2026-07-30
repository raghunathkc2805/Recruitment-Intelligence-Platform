"""
Match Result Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.match_result import MatchResult

from .base_repository import BaseRepository


class MatchResultRepository(BaseRepository):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

    def create(
        self,
        result: MatchResult,
    ) -> MatchResult:

        return self.add(result)

    def get(
        self,
        result_id: str,
    ) -> MatchResult | None:

        return (
            self.db.query(MatchResult)
            .filter(
                MatchResult.id == result_id
            )
            .first()
        )

    def list_by_job(
        self,
        job_id: str,
    ) -> list[MatchResult]:

        return (
            self.db.query(MatchResult)
            .filter(
                MatchResult.job_id == job_id
            )
            .order_by(
                MatchResult.score.desc()
            )
            .all()
        )

    def list_by_candidate(
        self,
        candidate_id: str,
    ) -> list[MatchResult]:

        return (
            self.db.query(MatchResult)
            .filter(
                MatchResult.candidate_id == candidate_id
            )
            .order_by(
                MatchResult.created_at.desc()
            )
            .all()
        )
