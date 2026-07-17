"""
Recruitment Intelligence Platform
Ranking Engine
"""

from __future__ import annotations

from resume_parser.ranking.scoring_engine import (
    ScoringEngine,
)


class RankingEngine:
    """
    Ranks candidates based on calculated scores.
    """

    @classmethod
    def rank(
        cls,
        candidates: list[dict],
    ) -> list[dict]:

        ranked = []

        for candidate in candidates:

            match_result = candidate.get("match_result", {})

            score = ScoringEngine.calculate(
                match_result
            )

            candidate["ranking_score"] = score["overall_score"]

            ranked.append(candidate)

        ranked.sort(
            key=lambda item: item["ranking_score"],
            reverse=True,
        )

        for rank, candidate in enumerate(
            ranked,
            start=1,
        ):

            candidate["rank"] = rank

        return ranked