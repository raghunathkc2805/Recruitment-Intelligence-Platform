"""
Enterprise Search Repository
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from database.models.search_history import SearchHistory

from .base_repository import BaseRepository


class SearchRepository(BaseRepository):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

    def save_search(
        self,
        *,
        user_id: str,
        query: str,
        search_type: str = "GENERAL",
    ) -> SearchHistory:

        history = SearchHistory(

            user_id=user_id,

            search_query=query,

            search_type=search_type,

        )

        return self.add(history)

    def recent(
        self,
        limit: int = 20,
    ):

        return (

            self.db.query(SearchHistory)

            .order_by(

                SearchHistory.created_at.desc()

            )

            .limit(limit)

            .all()

        )
