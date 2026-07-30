from __future__ import annotations


class ResumeIntelligenceService:


    @classmethod
    def analyse(
        cls,
        resume: dict,
        job: dict,
    ):

        skills = set(
            resume.get(
                "skills",
                [],
            )
        )


        required = set(
            job.get(
                "skills",
                [],
            )
        )


        missing = sorted(
            required - skills
        )


        completeness = 100


        if not resume.get(
            "experience"
        ):

            completeness -= 20


        if not resume.get(
            "education"
        ):

            completeness -= 20


        return {

            "resume_completeness_score":
                max(
                    completeness,
                    0,
                ),

            "role_match_score":
                round(
                    (
                        len(
                            skills
                            &
                            required
                        )
                        /
                        max(
                            len(required),
                            1,
                        )
                    )
                    *
                    100,
                    2,
                ),

            "missing_skills":
                missing,

            "improvement_suggestions":
                [
                    "Add missing competencies",
                    "Highlight measurable achievements",
                ],

        }