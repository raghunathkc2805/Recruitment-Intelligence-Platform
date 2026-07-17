"""
Recruitment Intelligence Platform
Ranking Engine
"""

from __future__ import annotations

from ranking_engine.ranking_service import (
    RankingService,
)


class RankingEngine:
    """
    Executes candidate ranking.
    """

    @classmethod
    def execute(
        cls,
        candidates: list[dict],
    ) -> list[dict]:

        return RankingService.rank(
            candidates
        )