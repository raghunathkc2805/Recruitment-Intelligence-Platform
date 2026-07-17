"""
Enterprise Ranking Service
"""

from __future__ import annotations


class RankingService:

    @classmethod
    def run(
        cls,
        payload: dict,
    ):

        return sorted(

            payload,

            key=lambda x: x["score"],

            reverse=True,

        )
