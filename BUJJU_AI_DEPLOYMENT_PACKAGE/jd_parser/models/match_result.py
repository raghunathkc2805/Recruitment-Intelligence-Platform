from dataclasses import dataclass, field


@dataclass
class MatchResult:

    # Overall
    overall_score: float = 0

    # Individual Scores
    skills_score: float = 0
    experience_score: float = 0
    education_score: float = 0
    certification_score: float = 0
    domain_score: float = 0
    location_score: float = 0

    # Details
    matched_skills: list = field(default_factory=list)
    missing_skills: list = field(default_factory=list)

    matched_certifications: list = field(default_factory=list)
    missing_certifications: list = field(default_factory=list)

    recommendation: str = ""