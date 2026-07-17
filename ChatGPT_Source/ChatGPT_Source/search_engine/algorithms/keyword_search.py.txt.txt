"""
Recruitment Intelligence Platform
Keyword Search
"""

from __future__ import annotations


class KeywordSearch:

    @classmethod
    def search(
        cls,
        query: str,
        candidates: list[dict],
    ) -> list[dict]:

        query = query.lower().strip()

        results = []

        for candidate in candidates:

            searchable = " ".join(
                str(value)
                for value in candidate.values()
            ).lower()

            if query in searchable:

                candidate = candidate.copy()

                candidate["search_score"] = 100

                results.append(candidate)

        return results