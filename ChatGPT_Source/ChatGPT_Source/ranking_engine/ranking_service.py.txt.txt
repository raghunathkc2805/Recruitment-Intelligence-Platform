"""
Recruitment Intelligence Platform
Ranking Service
"""

from __future__ import annotations

from ranking_engine.algorithms.weighted_ranker import (
    WeightedRanker,
)


class RankingService:
    """
    Candidate ranking service.
    """

    @classmethod
    def rank(
        cls,
        candidates: list[dict],
    ) -> list[dict]:

        return WeightedRanker.rank(
            candidates
        )