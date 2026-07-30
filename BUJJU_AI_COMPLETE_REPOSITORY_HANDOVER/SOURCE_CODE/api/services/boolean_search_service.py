
from __future__ import annotations


import re



class BooleanSearchService:


    @classmethod
    def parse(
        cls,
        query: str,
    ):

        not_terms = re.findall(
            r"NOT\s+([A-Za-z0-9.+#-]+)",
            query,
            flags=re.I,
        )


        cleaned = re.sub(
            r"NOT\s+[A-Za-z0-9.+#-]+",
            "",
            query,
            flags=re.I,
        )


        or_parts = re.split(
            r"\s+OR\s+",
            cleaned,
            flags=re.I,
        )


        or_terms = []


        if len(or_parts) > 1:

            or_terms = [

                item.strip()

                for item in or_parts[1:]

                if item.strip()

            ]


        and_terms = []


        for item in re.split(
            r"\s+AND\s+",
            or_parts[0],
            flags=re.I,
        ):

            value = item.strip()

            if value:

                and_terms.append(
                    value
                )


        phrases = re.findall(
            r'"([^"]+)"',
            query,
        )


        return {

            "and": and_terms,

            "or": or_terms,

            "not": not_terms,

            "phrases": phrases,

            "keywords":
                and_terms + or_terms + phrases,

            "original_query":
                query,

        }



    @classmethod
    def generate(
        cls,
        designation: str,
        skills: list,
        experience: str = "",
    ):

        query = (
            f'("{designation}") '
            f'AND '
            f'({" OR ".join(skills)})'
        )


        if experience:

            query += (
                f' AND "{experience}"'
            )


        return {

            "boolean_query": query,

            "skills_used": skills,

        }
