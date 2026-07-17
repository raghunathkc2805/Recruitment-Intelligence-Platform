"""
Recruitment Intelligence Platform
Search Engine
"""

from __future__ import annotations

from search_engine.search_service import SearchService


class SearchEngine:

    @classmethod
    def search(
        cls,
        query: str,
        candidates: list[dict],
    ) -> list[dict]:

        return SearchService.search(
            query,
            candidates,
        )