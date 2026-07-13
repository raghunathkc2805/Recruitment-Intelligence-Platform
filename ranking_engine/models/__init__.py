"""
Recruitment Intelligence Platform
Weighted Ranker
"""

from __future__ import annotations

from ranking_engine.algorithms.tie_breaker import (
    TieBreaker,
)


class WeightedRanker:

    @classmethod
    def rank(
        cls,
        candidates: list[dict],
    ) -> list[dict]:

        ranked = sorted(
            candidates,
            key=lambda c: c.get(
                "overall_score",
                0,
            ),
            reverse=True,
        )

        return TieBreaker.resolve(
            ranked
        )