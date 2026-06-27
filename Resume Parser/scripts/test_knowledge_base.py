import sys
from pathlib import Path

# Add project root to Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from utils.knowledge_base import (
    SKILLS,
    DESIGNATIONS,
    KEYWORD_SYNONYMS,
    DOMAINS
)

print("=" * 60)
print("Knowledge Base Test")
print("=" * 60)

print()

print("Technical Skills :", len(SKILLS["technical_skills"]))
print("Functional Skills:", len(SKILLS["functional_skills"]))
print("Soft Skills      :", len(SKILLS["soft_skills"]))

print()

print("Designation Groups :", len(DESIGNATIONS))
print("Keyword Synonyms   :", len(KEYWORD_SYNONYMS))
print("Domains            :", len(DOMAINS))

print()
print("Knowledge Base Loaded Successfully.")