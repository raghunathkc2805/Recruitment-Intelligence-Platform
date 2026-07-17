"""
Recruitment Intelligence Platform
Score Utilities
"""

from __future__ import annotations


class ScoreUtils:

    @staticmethod
    def calculate_keyword_score(
        query: str,
        text: str,
    ) -> float:

        query_tokens = {
            token.lower()
            for token in query.split()
        }

        text_tokens = {
            token.lower()
            for token in text.split()
        }

        if not query_tokens:
            return 0.0

        matches = len(
            query_tokens.intersection(
                text_tokens
            )
        )

        return round(
            (matches / len(query_tokens))
            * 100,
            2,
        )