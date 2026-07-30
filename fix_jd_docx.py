from pathlib import Path

p = Path("api/services/jd_service.py")
t = p.read_text(encoding="utf-8")

t = t.replace(
"from jd_parser.services.jd_service import JDService as Parser",
"from jd_parser.services.jd_service import JDService as Parser\nfrom jd_parser.core.docx_reader import extract_docx_text\n"
)

old = """            text = stored.read_text(
                encoding="utf-8",
                errors="ignore",
            )"""

new = """            if stored.suffix.lower() == ".docx":
                text = extract_docx_text(stored)
            else:
                text = stored.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )"""

if old in t:
    t = t.replace(old, new)

p.write_text(t, encoding="utf-8")

print("JD DOCX extractor patch applied")
