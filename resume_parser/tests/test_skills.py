import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from resume_parser.extractors.skills_extractor import extract_skills

sample = """
AWS Azure GCP VMware
Business Development
Sales
Leadership
Communication
"""

print(extract_skills(sample))
