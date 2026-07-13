"""
Ranking Engine Score Utilities
"""

from __future__ import annotations


def normalize_score(
    score: float,
) -> float:

    score = float(score)

    if score < 0:
        return 0.0

    if score > 100:
        return 100.0

    return round(score, 2)