from calculators.skill_matcher import calculate_skill_match


def main():

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

    result = calculate_skill_match(

        candidate_skills,
        jd_skills

    )

    print("=" * 60)
    print("Recruitment Matching Engine")
    print("=" * 60)

    print()

    print(f"Skill Score : {result['skills_score']}%")

    print()

    print("Matched Skills")

    for skill in result["matched_skills"]:
        print(f"  ✓ {skill}")

    print()

    print("Missing Skills")

    for skill in result["missing_skills"]:
        print(f"  ✗ {skill}")

    print()

    print("Additional Skills")

    for skill in result["additional_skills"]:
        print(f"  + {skill}")


if __name__ == "__main__":
    main()