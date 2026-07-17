"""
Ranking Engine Sorting Utilities
"""

from __future__ import annotations


def sort_candidates(
    candidates: list[dict],
) -> list[dict]:

    return sorted(
        candidates,
        key=lambda x: x.get(
            "overall_score",
            0,
        ),
        reverse=True,
    )