"""
Resume Parser Constants
"""

from pathlib import Path

# ---------------------------------------------------------
# Project Paths
# ---------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[2]

RESUME_PARSER_DIR = ROOT_DIR / "resume_parser"

KNOWLEDGE_BASE_DIR = RESUME_PARSER_DIR / "knowledge_base"

OUTPUT_DIR = RESUME_PARSER_DIR / "output"

LOG_DIR = RESUME_PARSER_DIR / "logs"

SAMPLE_RESUME_DIR = RESUME_PARSER_DIR / "sample_resumes"

# ---------------------------------------------------------
# Supported File Types
# ---------------------------------------------------------

SUPPORTED_FILE_TYPES = {
    ".pdf",
    ".docx",
    ".txt",
}

# ---------------------------------------------------------
# Text Limits
# ---------------------------------------------------------

MIN_TEXT_LENGTH = 20

MAX_TEXT_LENGTH = 2_000_000

# ---------------------------------------------------------
# Resume Scoring
# ---------------------------------------------------------

MAX_SCORE = 100

DEFAULT_SCORE = 0

# ---------------------------------------------------------
# Ranking Thresholds
# ---------------------------------------------------------

OUTSTANDING_SCORE = 95

EXCELLENT_SCORE = 90

VERY_GOOD_SCORE = 80

GOOD_SCORE = 70

AVERAGE_SCORE = 50

# ---------------------------------------------------------
# Default Encoding
# ---------------------------------------------------------

DEFAULT_ENCODING = "utf-8"

# ---------------------------------------------------------
# Regex Flags
# ---------------------------------------------------------

REGEX_FLAGS = 0

# ---------------------------------------------------------
# Output Formats
# ---------------------------------------------------------

OUTPUT_JSON = "json"

OUTPUT_CSV = "csv"

OUTPUT_CONSOLE = "console"

# ---------------------------------------------------------
# Knowledge Base Files
# ---------------------------------------------------------

SKILLS_MASTER = KNOWLEDGE_BASE_DIR / "skills_master.json"

DESIGNATION_MASTER = KNOWLEDGE_BASE_DIR / "designation_master.json"

COMPANY_MASTER = KNOWLEDGE_BASE_DIR / "company_master.json"

DOMAIN_MASTER = KNOWLEDGE_BASE_DIR / "domain_master.json"

LOCATION_MASTER = KNOWLEDGE_BASE_DIR / "location_master.json"

EDUCATION_MASTER = KNOWLEDGE_BASE_DIR / "education_master.json"

CERTIFICATION_MASTER = KNOWLEDGE_BASE_DIR / "certification_master.json"

LANGUAGE_MASTER = KNOWLEDGE_BASE_DIR / "language_master.json"

KEYWORD_SYNONYMS = KNOWLEDGE_BASE_DIR / "keyword_synonyms.json"