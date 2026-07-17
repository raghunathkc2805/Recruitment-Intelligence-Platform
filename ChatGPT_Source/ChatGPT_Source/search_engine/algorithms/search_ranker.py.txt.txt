"""
Recruitment Intelligence Platform
Search Ranker
"""

from __future__ import annotations


class SearchRanker:

    @classmethod
    def rank(
        cls,
        candidates: list[dict],
    ) -> list[dict]:

        return sorted(
            candidates,
            key=lambda x: x.get(
                "search_score",
                0,
            ),
            reverse=True,
        )