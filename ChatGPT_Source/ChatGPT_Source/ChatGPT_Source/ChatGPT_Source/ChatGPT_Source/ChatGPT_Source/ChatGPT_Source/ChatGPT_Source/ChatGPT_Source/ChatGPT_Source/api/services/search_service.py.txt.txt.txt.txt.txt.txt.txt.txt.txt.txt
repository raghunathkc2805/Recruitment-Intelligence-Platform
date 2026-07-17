"""
Recruitment Intelligence Platform
Search Service
"""

from __future__ import annotations

from search_engine.search_service import (
    SearchService as Engine,
)


class SearchService:

    @classmethod
    def run(
        cls,
        payload: dict,
    ) -> list[dict]:

        return Engine.search(
            payload["query"],
            payload["candidates"],
        )