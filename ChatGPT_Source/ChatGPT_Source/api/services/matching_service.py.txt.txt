"""
Recruitment Intelligence Platform
Matching Service
"""

from __future__ import annotations

from matching_engine.matching_service import (
    MatchingService as Engine,
)


class MatchingService:

    @classmethod
    def run(
        cls,
        payload: dict,
    ) -> dict:

        return Engine.match(
            payload["candidate"],
            payload["job"],
        )