from pathlib import Path

APP_NAME = "Recruitment Intelligence Engine"
VERSION = "4.8.0"

ROOT = Path(__file__).resolve().parent.parent

INPUT_FOLDER = ROOT / "input"
OUTPUT_FOLDER = ROOT / "output"
LOG_FOLDER = ROOT / "logs"
JSON_FOLDER = ROOT / "output"

SUPPORTED_FILES = [".pdf", ".docx"]