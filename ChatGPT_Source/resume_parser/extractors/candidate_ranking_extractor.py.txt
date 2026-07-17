"""
Recruitment Intelligence Platform
Candidate Ranking Extractor
"""

from __future__ import annotations

from resume_parser.ranking.ranking_engine import RankingEngine


class CandidateRankingExtractor:
    """
    Rank matched candidates.
    """

    @classmethod
    def extract(
        cls,
        candidates: list[dict],
    ) -> dict:

        ranked_candidates = RankingEngine.rank(
            candidates
        )

        return {
            "total_candidates": len(ranked_candidates),
            "ranked_candidates": ranked_candidates,
        }