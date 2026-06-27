from dataclasses import dataclass, field


@dataclass
class Candidate:

    # Contact
    name: str = ""
    email: str = ""
    mobile: str = ""

    # Experience
    experience_type: str = ""
    total_experience: str = ""

    current_company: str = ""
    current_designation: str = ""

    companies: list = field(default_factory=list)

    employment_history: list = field(default_factory=list)

    # Skills
    technical_skills: list = field(default_factory=list)
    functional_skills: list = field(default_factory=list)
    soft_skills: list = field(default_factory=list)

    # Search
    keywords: list = field(default_factory=list)
    search_keywords: list = field(default_factory=list)

    # Metadata
    resume_file: str = ""
    parser_version: str = ""