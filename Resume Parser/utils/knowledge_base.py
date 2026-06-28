import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KB_DIR = BASE_DIR / "knowledge_base"


def load_json(filename):
    with open(KB_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


# Skills
SKILLS = load_json("skills_master.json")
TECHNICAL_SKILLS = SKILLS["technical_skills"]
FUNCTIONAL_SKILLS = SKILLS["functional_skills"]
SOFT_SKILLS = SKILLS["soft_skills"]

# Designations
DESIGNATIONS = load_json("designation_master.json")

# Keyword Synonyms
KEYWORD_SYNONYMS = load_json("keyword_synonyms.json")

# Domains
DOMAINS = load_json("domain_master.json")

# Universities
UNIVERSITIES = load_json("universities.json")

# Certifications
CERTIFICATIONS = load_json("certification_master.json")

# Companies
COMPANIES = load_json("companies_master.json")