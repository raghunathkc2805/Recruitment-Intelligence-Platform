from extractors.contact_extractor import (
    extract_name,
    extract_email,
    extract_mobile
)

from extractors.experience_extractor import (
    extract_employment_history,
    extract_current_company,
    extract_current_designation,
    get_experience_type
)

from extractors.skills_extractor import extract_skills
from extractors.keyword_extractor import extract_search_keywords
from extractors.domain_extractor import extract_domains

from extractors.education_extractor import (
    extract_education,
    highest_qualification
)

from extractors.certification_extractor import (
    extract_certifications
)

from models.candidate import Candidate


def build_candidate(text, resume_file, parser_version):
    """
    Build Candidate object from resume text.
    """

    # ---------------------------------
    # Contact
    # ---------------------------------

    name = extract_name(text)
    email = extract_email(text)
    mobile = extract_mobile(text)

    # ---------------------------------
    # Experience
    # ---------------------------------

    history = extract_employment_history(text)

    experience_type = get_experience_type(history)

    current_company = extract_current_company(history)

    current_designation = extract_current_designation(history)

    companies = [item["company"] for item in history]

    # ---------------------------------
    # Skills
    # ---------------------------------

    skills = extract_skills(text)

    # ---------------------------------
    # Domains
    # ---------------------------------

    primary_domain, secondary_domain = extract_domains(text)

    # ---------------------------------
    # Education
    # ---------------------------------

    education = extract_education(text)

    highest = highest_qualification(education)

    education_confidence = 100 if education else 0

    # ---------------------------------
    # Certifications
    # ---------------------------------

    certifications = extract_certifications(text)

    # ---------------------------------
    # Candidate Object
    # ---------------------------------

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

        resume_file=resume_file,
        parser_version=parser_version
    )

    # ---------------------------------
    # Search Keywords
    # ---------------------------------

    candidate.search_keywords = extract_search_keywords(candidate)

    return candidate