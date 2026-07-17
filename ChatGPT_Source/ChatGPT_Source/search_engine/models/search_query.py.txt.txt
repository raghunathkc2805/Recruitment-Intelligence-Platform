"""
Recruitment Intelligence Platform
Search Query Model
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SearchQuery:

    query: str = ""

    search_type: str = "keyword"

    limit: int = 25

    filters: dict = field(
        default_factory=dict
    )

    def to_dict(self) -> dict:

        return {
            "query": self.query,
            "search_type": self.search_type,
            "limit": self.limit,
            "filters": self.filters,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "SearchQuery":

        return cls(
            query=data.get(
                "query",
                "",
            ),
            search_type=data.get(
                "search_type",
                "keyword",
            ),
            limit=int(
                data.get(
                    "limit",
                    25,
                )
            ),
            filters=data.get(
                "filters",
                {},
            ),
        )