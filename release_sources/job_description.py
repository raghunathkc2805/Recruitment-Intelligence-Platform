from dataclasses import dataclass, field


@dataclass
class JobDescription:

    # Basic Details
    title: str = ""
    company: str = ""
    location: str = ""

    # Hiring Details
    openings: int = 0

    # Experience
    minimum_experience: float = 0
    maximum_experience: float = 0

    # Education
    education: list = field(default_factory=list)

    # Skills
    technical_skills: list = field(default_factory=list)
    functional_skills: list = field(default_factory=list)
    soft_skills: list = field(default_factory=list)

    # Certifications
    certifications: list = field(default_factory=list)

    # Domains
    primary_domain: str = ""
    secondary_domain: str = ""

    # Employment
    employment_type: str = ""
    notice_period: str = ""
    salary: str = ""

    # Search
    search_keywords: list = field(default_factory=list)

    # Metadata
    jd_file: str = ""
    parser_version: str = ""