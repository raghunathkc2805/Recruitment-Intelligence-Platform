"""
Weight Utilities
"""

from __future__ import annotations

from matching_engine.constants import (
    DEFAULT_WEIGHTS,
)


def calculate_weighted_score(
    scores: dict,
    weights: dict | None = None,
) -> float:
    """
    Calculate weighted matching score.
    """

    weights = weights or DEFAULT_WEIGHTS

    total = 0.0

    total += (
        scores["skill_match"]["score"]
        * weights["skills"]
    )

    total += (
        scores["experience_match"]["score"]
        * weights["experience"]
    )

    total += (
        scores["education_match"]["score"]
        * weights["education"]
    )

    total += (
        scores["designation_match"]["score"]
        * weights["designation"]
    )

    total += (
        scores["location_match"]["score"]
        * weights["location"]
    )

    total += (
        scores["certification_match"]["score"]
        * weights["certification"]
    )

    return round(total / 100, 2)