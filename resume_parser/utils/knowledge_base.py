"""Resume Parser accessors for the shared knowledge base."""

from shared.knowledge_base.loader import load_json


SKILLS = load_json("skills_master.json")
CERTIFICATIONS = load_json("certification_master.json")
COMPANY_ALIASES = load_json("company_master.json")
COMPANIES = list(COMPANY_ALIASES)
EDUCATION = load_json("education_master.json")
LANGUAGES = load_json("language_master.json")
LOCATIONS = load_json("location_master.json")["cities"]
DESIGNATIONS = load_json("designation_master.json")
UNIVERSITIES = load_json("universities.json")
KEYWORD_SYNONYMS = load_json("keyword_synonyms.json")
