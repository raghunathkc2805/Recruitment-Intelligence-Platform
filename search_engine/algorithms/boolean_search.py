"""
Recruitment Intelligence Platform
Boolean Search
"""

from __future__ import annotations


class BooleanSearch:

    @classmethod
    def search(
        cls,
        query: str,
        candidates: list[dict],
    ) -> list[dict]:

        tokens = [
            token.lower()
            for token in query.split()
            if token.upper()
            not in (
                "AND",
                "OR",
                "NOT",
            )
        ]

        results = []

        for candidate in candidates:

            text = " ".join(
                str(v)
                for v in candidate.values()
            ).lower()

            if all(
                token in text
                for token in tokens
            ):

                item = candidate.copy()

                item["search_score"] = 100

                results.append(item)

        return results