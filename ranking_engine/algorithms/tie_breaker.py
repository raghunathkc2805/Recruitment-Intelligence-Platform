"""
Recruitment Intelligence Platform
Tie Breaker
"""

from __future__ import annotations


class TieBreaker:

    @staticmethod
    def resolve(
        candidates: list[dict],
    ) -> list[dict]:

        return sorted(
            candidates,
            key=lambda c: (
                c.get("overall_score", 0),
                c.get("experience", {}).get("years", 0),
            ),
            reverse=True,
        )