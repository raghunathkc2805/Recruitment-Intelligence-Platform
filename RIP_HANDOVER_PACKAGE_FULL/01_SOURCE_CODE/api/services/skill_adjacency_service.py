from __future__ import annotations


class SkillAdjacencyService:


    SKILL_MAP = {

        "mpls": [
            "EVPN",
            "VXLAN",
            "Segment Routing",
            "SRv6",
        ],

        "python": [
            "Django",
            "FastAPI",
            "Machine Learning",
        ],

        "cisco": [
            "Routing",
            "Switching",
            "Firewall",
        ],

        "dwdm": [
            "OTN",
            "Optical Transport",
            "Ciena",
        ],

    }


    @classmethod
    def recommend(
        cls,
        skills: list[str],
    ):

        recommendations = set()


        for skill in skills:

            related = cls.SKILL_MAP.get(
                skill.lower(),
                [],
            )

            recommendations.update(
                related
            )


        return {
            "existing_skills": skills,
            "recommended_skills": sorted(
                recommendations
            ),
            "confidence_score": 80,
        }