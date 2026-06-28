from dataclasses import dataclass, field


@dataclass
class Candidate:

    # Contact
    name: str = ""
    email: str = ""
    mobile: str = ""

    # Experience
    experience_type: str = ""
    current_company: str = ""
    current_designation: str = ""

    companies: list = field(default_factory=list)
    employment_history: list = field(default_factory=list)

    # Skills
    technical_skills: list = field(default_factory=list)
    functional_skills: list = field(default_factory=list)
    soft_skills: list = field(default_factory=list)

    # Search
    search_keywords: list = field(default_factory=list)

    # Domains
    primary_domain: str = ""
    secondary_domain: str = ""

    # Education
    education: list = field(default_factory=list)
    highest_qualification: str = ""
    education_confidence: int = 0

    # Certifications
    certifications: list = field(default_factory=list)

    # Files
    resume_file: str = ""
    parser_version: str = ""