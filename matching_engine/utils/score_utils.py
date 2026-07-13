"""
Score Utilities
"""

from __future__ import annotations


def normalize_score(
    score: float,
    minimum: float = 0.0,
    maximum: float = 100.0,
) -> float:
    """
    Normalize score between minimum and maximum.
    """

    score = float(score)

    if score < minimum:
        return minimum

    if score > maximum:
        return maximum

    return round(score, 2)