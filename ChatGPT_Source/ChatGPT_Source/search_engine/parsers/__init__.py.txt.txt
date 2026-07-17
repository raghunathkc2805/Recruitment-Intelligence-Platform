"""
Recruitment Intelligence Platform
Search Result Model
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SearchResult:

    results: list[dict] = field(
        default_factory=list
    )

    total_results: int = 0

    execution_time_ms: float = 0.0

    search_type: str = ""

    def to_dict(self) -> dict:

        return {
            "results": self.results,
            "total_results": self.total_results,
            "execution_time_ms": self.execution_time_ms,
            "search_type": self.search_type,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "SearchResult":

        return cls(
            results=data.get(
                "results",
                [],
            ),
            total_results=int(
                data.get(
                    "total_results",
                    0,
                )
            ),
            execution_time_ms=float(
                data.get(
                    "execution_time_ms",
                    0,
                )
            ),
            search_type=data.get(
                "search_type",
                "",
            ),
        )