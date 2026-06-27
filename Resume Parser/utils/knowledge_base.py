import json
from pathlib import Path

# Project Root
ROOT = Path(__file__).resolve().parent.parent

# Knowledge Base Folder
KB_FOLDER = ROOT / "knowledge_base"


def load_json(filename):
    """
    Load a JSON file from the Knowledge Base folder.
    """
    file_path = KB_FOLDER / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# Load Knowledge Base Files
SKILLS = load_json("skills_master.json")
DESIGNATIONS = load_json("designation_master.json")
KEYWORD_SYNONYMS = load_json("keyword_synonyms.json")
DOMAINS = load_json("domain_master.json")