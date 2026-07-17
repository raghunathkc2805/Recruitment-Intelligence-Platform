"""
Recruitment Intelligence Platform
Search Service
"""

from __future__ import annotations

from search_engine.algorithms.keyword_search import KeywordSearch


class SearchService:

    @classmethod
    def search(
        cls,
        query: str,
        candidates: list[dict],
    ) -> list[dict]:

        return KeywordSearch.search(
            query,
            candidates,
        )