from __future__ import annotations


class JDIntelligenceService:


    @classmethod
    def analyse(
        cls,
        jd: dict,
    ):

        skills = jd.get(
            "skills",
            [],
        )


        return {

            "jd_quality_score":
                100
                if skills
                else 50,

            "identified_skills":
                skills,

            "recommendations":
                [
                    "Validate required competencies",
                    "Review designation alignment",
                    "Confirm experience expectations",
                ],

        }