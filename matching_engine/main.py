from models.match_result import MatchResult
from scorers.overall_scorer import calculate_overall_score


def main():

    result = MatchResult()

    result.skills_score = 0.95
    result.experience_score = 1.00
    result.education_score = 1.00
    result.certification_score = 0.70
    result.domain_score = 1.00
    result.location_score = 0.90

    result = calculate_overall_score(result)

    print("=" * 60)
    print("Recruitment Matching Engine")
    print("=" * 60)

    print(f"Overall Score : {result.overall_score}%")
    print(f"Grade         : {result.grade}")


if __name__ == "__main__":
    main()