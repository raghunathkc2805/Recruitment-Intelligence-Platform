"""
Recruitment Intelligence Platform
Query Parser
"""

from __future__ import annotations


class QueryParser:

    @classmethod
    def parse(
        cls,
        query: str,
    ) -> dict:

        tokens = [
            token.strip()
            for token in query.split()
            if token.strip()
        ]

        return {
            "original_query": query,
            "tokens": tokens,
            "token_count": len(tokens),
        }