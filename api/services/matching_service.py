"""
Enterprise Matching Service
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from api.services.search_service import SearchService
from matching_engine.matching_service import MatchingService as Engine


class MatchingService:

    @classmethod
    def run(
        cls,
        db: Session,
        payload: dict,
    ):

        candidates = SearchService.run(

            db,

            {
                "query": payload["query"],
            },

        )

        matches = []

        for candidate in candidates:

            score = Engine.match(

                candidate,

                payload["job"],

            )

            matches.append(

                {

                    "candidate": candidate,

                    "score": score,

                }

            )

        return matches
