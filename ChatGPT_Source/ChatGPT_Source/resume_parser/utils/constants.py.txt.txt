"""
Recruitment Intelligence Platform
Resume Parser - Global Constants

Author: Recruitment Intelligence Platform
"""

from pathlib import Path

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RESUME_PARSER_ROOT = PROJECT_ROOT / "resume_parser"

SHARED_KNOWLEDGE_BASE = PROJECT_ROOT / "shared" / "knowledge_base"

OUTPUT_ROOT = RESUME_PARSER_ROOT / "output"

CSV_OUTPUT = OUTPUT_ROOT / "csv"
EXCEL_OUTPUT = OUTPUT_ROOT / "excel"
JSON_OUTPUT = OUTPUT_ROOT / "json"
REPORT_OUTPUT = OUTPUT_ROOT / "reports"

LOG_DIRECTORY = RESUME_PARSER_ROOT / "logs"

KNOWLEDGE_BASE = SHARED_KNOWLEDGE_BASE

SAMPLE_RESUMES = RESUME_PARSER_ROOT / "sample_resumes"

# --------------------------------------------------
# Supported File Types
# --------------------------------------------------

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt"
}

SUPPORTED_MIME_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "text/plain"
}

# --------------------------------------------------
# File Limits
# --------------------------------------------------

MAX_FILE_SIZE_MB = 20

MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

MIN_TEXT_LENGTH = 30

DEFAULT_ENCODING = "utf-8"

# --------------------------------------------------
# Resume Parser
# --------------------------------------------------

DEFAULT_LANGUAGE = "en"

DEFAULT_SCORE = 0

DEFAULT_CONFIDENCE = 0.0

DEFAULT_PAGE_COUNT = 0

# --------------------------------------------------
# Parsing Status
# --------------------------------------------------

STATUS_SUCCESS = "success"

STATUS_FAILED = "failed"

STATUS_WARNING = "warning"

# --------------------------------------------------
# Export Formats
# --------------------------------------------------

EXPORT_JSON = "json"

EXPORT_CSV = "csv"

EXPORT_EXCEL = "excel"

EXPORT_PDF = "pdf"

SUPPORTED_EXPORTS = {
    EXPORT_JSON,
    EXPORT_CSV,
    EXPORT_EXCEL,
    EXPORT_PDF
}

# --------------------------------------------------
# Knowledge Base Files
# --------------------------------------------------

SKILLS_MASTER = KNOWLEDGE_BASE / "skills_master.json"

CERTIFICATION_MASTER = KNOWLEDGE_BASE / "certification_master.json"

COMPANY_MASTER = KNOWLEDGE_BASE / "company_master.json"

DESIGNATION_MASTER = KNOWLEDGE_BASE / "designation_master.json"

EDUCATION_MASTER = KNOWLEDGE_BASE / "education_master.json"

DOMAIN_MASTER = KNOWLEDGE_BASE / "domain_master.json"

LOCATION_MASTER = KNOWLEDGE_BASE / "location_master.json"

LANGUAGE_MASTER = KNOWLEDGE_BASE / "language_master.json"

KEYWORD_SYNONYMS = KNOWLEDGE_BASE / "keyword_synonyms.json"

# --------------------------------------------------
# Parser Names
# --------------------------------------------------

TXT_PARSER = "txt"

DOCX_PARSER = "docx"

PDF_PARSER = "pdf"

# --------------------------------------------------
# Logging
# --------------------------------------------------

LOG_LEVEL = "INFO"

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)

# --------------------------------------------------
# Common Response Keys
# --------------------------------------------------

KEY_SUCCESS = "success"

KEY_STATUS = "status"

KEY_ERRORS = "errors"

KEY_TEXT = "text"

KEY_FILE_NAME = "file_name"

KEY_FILE_TYPE = "file_type"

KEY_FILE_SIZE = "file_size"

KEY_PAGE_COUNT = "pages"

KEY_METADATA = "metadata"

KEY_ENCODING = "encoding"

# --------------------------------------------------
# Miscellaneous
# --------------------------------------------------

EMPTY_STRING = ""

UNKNOWN = "Unknown"

NOT_AVAILABLE = "N/A"
