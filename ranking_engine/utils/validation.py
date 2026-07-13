"""
Ranking Engine Validation Utilities
"""

from __future__ import annotations


def validate_candidates(
    candidates: list[dict],
) -> None:

    if not isinstance(
        candidates,
        list,
    ):
        raise TypeError(
            "Candidates must be a list."
        )

    if not candidates:
        raise ValueError(
            "Candidate list cannot be empty."
        )