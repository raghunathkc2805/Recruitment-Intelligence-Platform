"""
Enterprise Boolean Search Service
"""

from __future__ import annotations

import re


class BooleanSearchService:

    @classmethod
    def parse(
        cls,
        query: str,
    ) -> dict:

        result = {

            "and": [],

            "or": [],

            "not": [],

            "phrases": [],

        }

        phrases = re.findall(
            r'"([^"]+)"',
            query,
        )

        result["phrases"] = phrases

        query = re.sub(
            r'"[^"]+"',
            "",
            query,
        )

        tokens = query.split()

        mode = "and"

        for token in tokens:

            upper = token.upper()

            if upper == "AND":

                mode = "and"

                continue

            if upper == "OR":

                mode = "or"

                continue

            if upper == "NOT":

                mode = "not"

                continue

            result[mode].append(
                token.strip()
            )

        return result
