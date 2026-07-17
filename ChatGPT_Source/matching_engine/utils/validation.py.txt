"""
Validation Utilities
"""

from __future__ import annotations


def validate_candidate(candidate: dict) -> None:

    if not isinstance(candidate, dict):
        raise TypeError(
            "Candidate must be a dictionary."
        )

    if not candidate:
        raise ValueError(
            "Candidate cannot be empty."
        )


def validate_job(job: dict) -> None:

    if not isinstance(job, dict):
        raise TypeError(
            "Job must be a dictionary."
        )

    if not job:
        raise ValueError(
            "Job cannot be empty."
        )