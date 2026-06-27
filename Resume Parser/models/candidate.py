from dataclasses import dataclass, field


@dataclass
class Candidate:
    # Contact Details
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

    # Future Modules
    search_keywords: list = field(default_factory=list)

    primary_domain: str = ""
    secondary_domain: str = ""

    education: list = field(default_factory=list)
    certifications: list = field(default_factory=list)

    # File Information
    resume_file: str = ""
    parser_version: str = ""