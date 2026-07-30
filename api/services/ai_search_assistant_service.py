from __future__ import annotations


class AISearchAssistantService:


    @classmethod
    def search_intent(
        cls,
        query: str,
    ):

        keywords = []


        known_terms = [

            "python",

            "java",

            "cisco",

            "nokia",

            "ciena",

            "dwdm",

            "telecom",

            "datacenter",

        ]


        text = query.lower()


        for term in known_terms:

            if term in text:

                keywords.append(
                    term
                )


        return {

            "original_query":
                query,

            "identified_keywords":
                keywords,

            "search_strategy":
                "Skill + Designation + Experience based matching",

            "confidence_score":
                80,

        }