"""
Recruitment Intelligence Platform
Semantic Search
"""

from __future__ import annotations


class SemanticSearch:
    """
    Lightweight semantic search.
    Matches candidates when ANY query token appears
    anywhere in the candidate profile.
    """

    @classmethod
    def search(
        cls,
        query: str,
        candidates: list[dict],
    ) -> list[dict]:

        query_tokens = {
            token.lower()
            for token in query.split()
            if token.strip()
        }

        results = []

        for candidate in candidates:

            searchable_text = " ".join(
                str(value)
                for value in candidate.values()
            ).lower()

            matched = 0

            for token in query_tokens:

                if token in searchable_text:
                    matched += 1

            if matched:

                item = candidate.copy()

                item["search_score"] = round(
                    matched / len(query_tokens) * 100,
                    2,
                )

                results.append(item)

        results.sort(
            key=lambda x: x["search_score"],
            reverse=True,
        )

        return results