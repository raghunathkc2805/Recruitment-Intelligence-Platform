from dataclasses import dataclass, field


@dataclass
class MatchResult:
    """
    Result of comparing one Candidate against one Job Description.
    """

    # ------------------------------------------------------------------
    # Overall
    # ------------------------------------------------------------------

    overall_score: float = 0.0
    grade: str = ""

    # ------------------------------------------------------------------
    # Individual Scores
    # ------------------------------------------------------------------

    skills_score: float = 0.0
    experience_score: float = 0.0
    education_score: float = 0.0
    certification_score: float = 0.0
    domain_score: float = 0.0
    location_score: float = 0.0

    # ------------------------------------------------------------------
    # Skills Analysis
    # ------------------------------------------------------------------

    matched_skills: list = field(default_factory=list)
    missing_skills: list = field(default_factory=list)
    additional_skills: list = field(default_factory=list)

    # ------------------------------------------------------------------
    # Certifications
    # ------------------------------------------------------------------

    matched_certifications: list = field(default_factory=list)
    missing_certifications: list = field(default_factory=list)

    # ------------------------------------------------------------------
    # Education
    # ------------------------------------------------------------------

    education_match: bool = False

    # ------------------------------------------------------------------
    # Experience
    # ------------------------------------------------------------------

    experience_gap: float = 0.0

    # ------------------------------------------------------------------
    # Location
    # ------------------------------------------------------------------

    location_match: bool = False

    # ------------------------------------------------------------------
    # Domain
    # ------------------------------------------------------------------

    primary_domain_match: bool = False
    secondary_domain_match: bool = False

    # ------------------------------------------------------------------
    # Recommendation
    # ------------------------------------------------------------------

    recommendation: str = ""