"""
Recruitment Intelligence Platform
Validation Utilities
"""

from __future__ import annotations


class Validation:

    @staticmethod
    def validate_query(
        query: str,
    ) -> None:

        if not isinstance(
            query,
            str,
        ):

            raise TypeError(
                "Query must be a string."
            )

        if not query.strip():

            raise ValueError(
                "Query cannot be empty."
            )

    @staticmethod
    def validate_candidates(
        candidates: list,
    ) -> None:

        if not isinstance(
            candidates,
            list,
        ):

            raise TypeError(
                "Candidates must be a list."
            )