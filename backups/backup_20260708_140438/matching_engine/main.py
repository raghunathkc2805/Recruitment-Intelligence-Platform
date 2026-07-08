from services.matching_service import MatchingService


def main():

    print("=" * 60)
    print("Recruitment Matching Engine")
    print("=" * 60)

    print()

    # -------------------------------------------------
    # Skills
    # -------------------------------------------------

    candidate_skills = [
        "Python",
        "Linux",
        "AWS",
        "Docker",
        "VMware",
        "Git"
    ]

    jd_skills = [
        "Python",
        "Linux",
        "AWS",
        "Terraform",
        "Docker"
    ]

    skills = MatchingService.match_skills(
        candidate_skills,
        jd_skills
    )

    # -------------------------------------------------
    # Experience
    # -------------------------------------------------

    experience = MatchingService.match_experience(
        candidate_experience=4.5,
        minimum_required=3,
        maximum_required=6
    )

    # -------------------------------------------------

    print(f"Skill Score        : {skills['skills_score']}%")

    print(
        f"Experience Score   : "
        f"{experience['experience_score']}%"
    )

    print(
        f"Qualified          : "
        f"{experience['qualified']}"
    )

    print(
        f"Experience Gap     : "
        f"{experience['experience_gap']} Years"
    )


if __name__ == "__main__":
    main()