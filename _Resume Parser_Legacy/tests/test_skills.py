import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from extractors.skills_extractor import extract_skills

sample = """
AWS Azure GCP VMware
Business Development
Sales
Leadership
Communication
"""

skills = extract_skills(sample)

print(skills)