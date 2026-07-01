from extractors.title_extractor import extract_job_title
from extractors.company_extractor import extract_company
from extractors.location_extractor import extract_location
from extractors.experience_extractor import extract_experience
from extractors.openings_extractor import extract_openings
from extractors.education_extractor import extract_education
from extractors.skills_extractor import extract_skills
from extractors.domain_extractor import extract_domains
from extractors.certification_extractor import extract_certifications

from models.job_description import JobDescription


def build_job_description(text, jd_file, parser_version):
    """
    Build JobDescription object.
    """

    # ----------------------------------------------------------
    # Basic Information
    # ----------------------------------------------------------

    title = extract_job_title(text)
    company = extract_company(text)
    location = extract_location(text)

    # ----------------------------------------------------------
    # Hiring Details
    # ----------------------------------------------------------

    openings = extract_openings(text)
    minimum_experience, maximum_experience = extract_experience(text)

    # ----------------------------------------------------------
    # Education
    # ----------------------------------------------------------

    education = extract_education(text)

    # ----------------------------------------------------------
    # Skills
    # ----------------------------------------------------------

    skills = extract_skills(text)

    # ----------------------------------------------------------
    # Certifications
    # ----------------------------------------------------------

    certifications = extract_certifications(text)

    # ----------------------------------------------------------
    # Domains
    # ----------------------------------------------------------

    primary_domain, secondary_domain = extract_domains(text)

    # ----------------------------------------------------------
    # Create Job Description
    # ----------------------------------------------------------

    job = JobDescription(

        title=title,
        company=company,
        location=location,

        openings=openings,

        minimum_experience=minimum_experience,
        maximum_experience=maximum_experience,

        education=education,

        technical_skills=skills["technical_skills"],
        functional_skills=skills["functional_skills"],
        soft_skills=skills["soft_skills"],

        certifications=certifications,

        primary_domain=primary_domain,
        secondary_domain=secondary_domain,

        employment_type="",
        notice_period="",
        salary="",

        search_keywords=[],

        jd_file=jd_file,
        parser_version=parser_version
    )

    return job