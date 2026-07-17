from shared.knowledge_base.loader import load_json


# Skills
SKILLS = load_json("skills_master.json")
TECHNICAL_SKILLS = SKILLS["technical_skills"]
FUNCTIONAL_SKILLS = SKILLS["functional_skills"]
SOFT_SKILLS = SKILLS["soft_skills"]

# Designations
DESIGNATIONS = load_json("designation_master.json")
DESIGNATION_ALIASES = load_json("designation_aliases.json")

# Keyword Synonyms
KEYWORD_SYNONYMS = load_json("keyword_synonyms.json")

# Domains
DOMAINS = load_json("domain_master.json")

# Universities
UNIVERSITIES = load_json("universities.json")

# Certifications
CERTIFICATIONS = load_json("certification_master.json")

# Companies
COMPANIES = load_json("company_master.json")

# Locations
LOCATIONS = load_json("location_master.json")
INDIA_STATES = LOCATIONS["states"]
INDIA_CITIES = LOCATIONS["cities"]
