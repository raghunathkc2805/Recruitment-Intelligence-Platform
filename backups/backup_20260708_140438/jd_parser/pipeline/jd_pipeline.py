from jd_parser.extractors.title_extractor import extract_job_title
from jd_parser.extractors.company_extractor import extract_company
from jd_parser.extractors.location_extractor import extract_location
from jd_parser.extractors.experience_extractor import extract_experience
from jd_parser.extractors.openings_extractor import extract_openings
from jd_parser.extractors.education_extractor import extract_education
from jd_parser.extractors.skills_extractor import extract_skills
from jd_parser.extractors.domain_extractor import extract_domains
from jd_parser.extractors.certification_extractor import extract_certifications
from jd_parser.extractors.search_keywords_extractor import extract_search_keywords

from jd_parser.extractors.boolean_search_extractor import extract_boolean_search
from jd_parser.extractors.resume_search_extractor import extract_resume_search
from jd_parser.extractors.recruiter_query_extractor import extract_recruiter_query
from jd_parser.extractors.candidate_match_extractor import extract_candidate_match
from jd_parser.extractors.candidate_ranking_extractor import extract_candidate_ranking
from jd_parser.extractors.ai_recommendation_extractor import extract_ai_recommendation

from jd_parser.models.job_description import JobDescription


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
    # Search Intelligence
    # ----------------------------------------------------------

    search_keywords = extract_search_keywords(text)
    boolean_search = extract_boolean_search(text)
    resume_search = extract_resume_search(text)
    recruiter_query = extract_recruiter_query(text)

    # ----------------------------------------------------------
    # Candidate Intelligence
    # ----------------------------------------------------------

    candidate_match = extract_candidate_match(text)
    candidate_ranking = extract_candidate_ranking(text)
    ai_recommendation = extract_ai_recommendation(text)

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

        search_keywords=search_keywords,

        jd_file=jd_file,
        parser_version=parser_version
    )

    # Attach Intelligence (without breaking existing model)

    job.boolean_search = boolean_search
    job.resume_search = resume_search
    job.recruiter_query = recruiter_query

    job.candidate_match = candidate_match
    job.candidate_ranking = candidate_ranking
    job.ai_recommendation = ai_recommendation

    return job