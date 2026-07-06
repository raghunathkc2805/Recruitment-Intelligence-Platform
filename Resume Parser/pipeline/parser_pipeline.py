from jd_parser.extractors.contact_extractor import (
    extract_name,
    extract_email,
    extract_mobile
)

.experience_extractor import (
    extract_employment_history,
    extract_current_company,
    extract_current_designation,
    get_experience_type
)

from jd_parser.extractors.skills_extractor import extract_skills
from jd_parser.extractors.keyword_extractor import extract_search_keywords
from jd_parser.extractors.domain_extractor import extract_domains
from jd_parser.extractors.education_extractor import (
    extract_education,
    highest_qualification
)
from jd_parser.extractors.certification_extractor import (
    extract_certifications
)
from jd_parser.extractors.company_extractor import (
    normalize_company,
    normalize_company_list
)
from jd_parser.extractors.designation_extractor import (
    normalize_designation
)
from jd_parser.extractors.location_extractor import (
    extract_locations
)

from scorers.resume_scorer import calculate_resume_score

from jd_parser.models.candidate import Candidate


def build_candidate(text, resume_file, parser_version):
    """
    Build Candidate object from resume text.
    """

    # Contact
    name = extract_name(text)
    email = extract_email(text)
    mobile = extract_mobile(text)

    # Experience
    history = extract_employment_history(text)

    experience_type = get_experience_type(history)

    current_company = normalize_company(
        extract_current_company(history)
    )

    current_designation = normalize_designation(
        extract_current_designation(history)
    )

    companies = normalize_company_list(
        [item["company"] for item in history]
    )

    # Skills
    skills = extract_skills(text)

    # Domains
    primary_domain, secondary_domain = extract_domains(text)

    # Education
    education = extract_education(text)
    highest = highest_qualification(education)
    education_confidence = 100 if education else 0

    # Certifications
    certifications = extract_certifications(text)

    # Locations
    locations = extract_locations(text)

    # Candidate
    candidate = Candidate(
        name=name,
        email=email,
        mobile=mobile,

        experience_type=experience_type,
        current_company=current_company,
        current_designation=current_designation,

        companies=companies,
        employment_history=history,

        technical_skills=skills["technical_skills"],
        functional_skills=skills["functional_skills"],
        soft_skills=skills["soft_skills"],

        primary_domain=primary_domain,
        secondary_domain=secondary_domain,

        education=education,
        highest_qualification=highest,
        education_confidence=education_confidence,

        certifications=certifications,

        primary_city=locations["primary_city"],
        primary_state=locations["primary_state"],
        cities=locations["cities"],
        states=locations["states"],

        resume_file=resume_file,
        parser_version=parser_version
    )

    candidate.search_keywords = extract_search_keywords(candidate)

    # Resume Score
    candidate.resume_score = calculate_resume_score(candidate)

    if candidate.resume_score >= 90:
        candidate.resume_grade = "A+"
    elif candidate.resume_score >= 80:
        candidate.resume_grade = "A"
    elif candidate.resume_score >= 70:
        candidate.resume_grade = "B"
    elif candidate.resume_score >= 60:
        candidate.resume_grade = "C"
    else:
        candidate.resume_grade = "D"

    return candidate