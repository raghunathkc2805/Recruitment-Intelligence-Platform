from __future__ import annotations


class RecruiterCopilotService:


    @classmethod
    def assist(
        cls,
        query: str,
        context: dict,
    ):

        skills = context.get(
            "skills",
            [],
        )

        role = context.get(
            "designation",
            "",
        )


        recommendations = []


        if skills:

            recommendations.append(
                {
                    "type": "skill_analysis",
                    "message":
                        f"Candidate search should prioritize {', '.join(skills)}",
                }
            )


        if role:

            recommendations.append(
                {
                    "type": "designation_analysis",
                    "message":
                        f"Focus matching against {role} profiles",
                }
            )


        return {

            "query": query,

            "recommendations":
                recommendations,

            "next_actions":
                [
                    "Review matching candidates",
                    "Validate competency gaps",
                    "Check previous successful hires",
                ],

            "confidence_score":
                85,

        }