"""
Recruitment Intelligence Platform
Matching Engine
"""

from __future__ import annotations

from matching_engine.matching_service import (
    MatchingService,
)


class MatchingEngine:
    """
    High-level matching engine.
    """

    @classmethod
    def execute(
        cls,
        candidate: dict,
        job: dict,
    ) -> dict:

        return MatchingService.match(
            candidate,
            job,
        )

    @classmethod
    def batch_execute(
        cls,
        candidates: list[dict],
        job: dict,
    ) -> list[dict]:

        results = []

        for candidate in candidates:

            results.append(
                cls.execute(
                    candidate,
                    job,
                )
            )

        results.sort(
            key=lambda x: x["overall_score"],
            reverse=True,
        )

        return results