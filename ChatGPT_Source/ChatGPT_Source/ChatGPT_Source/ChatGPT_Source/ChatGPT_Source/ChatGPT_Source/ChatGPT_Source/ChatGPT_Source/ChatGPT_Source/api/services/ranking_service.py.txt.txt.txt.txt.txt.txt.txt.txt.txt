"""
Recruitment Intelligence Platform
Ranking Service
"""

from __future__ import annotations

from ranking_engine.ranking_service import (
    RankingService as Engine,
)


class RankingService:

    @classmethod
    def run(
        cls,
        payload: dict,
    ) -> list[dict]:

        return Engine.rank(
            payload["candidates"]
        )