"""
Recruitment Intelligence Platform
Query Utilities
"""

from __future__ import annotations


class QueryUtils:

    @staticmethod
    def normalize(
        query: str,
    ) -> str:

        return " ".join(
            query.lower().strip().split()
        )

    @staticmethod
    def tokenize(
        query: str,
    ) -> list[str]:

        return [
            token
            for token in QueryUtils.normalize(
                query
            ).split(" ")
            if token
        ]