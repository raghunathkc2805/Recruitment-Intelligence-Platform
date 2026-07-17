"""
Recruitment Intelligence Platform
Hybrid Search
"""

from __future__ import annotations

from search_engine.algorithms.boolean_search import (
    BooleanSearch,
)
from search_engine.algorithms.semantic_search import (
    SemanticSearch,
)


class HybridSearch:

    @classmethod
    def search(
        cls,
        query: str,
        candidates: list[dict],
    ) -> list[dict]:

        results = {}

        for item in BooleanSearch.search(
            query,
            candidates,
        ):

            results[id(item)] = item

        for item in SemanticSearch.search(
            query,
            candidates,
        ):

            results[id(item)] = item

        return list(results.values())