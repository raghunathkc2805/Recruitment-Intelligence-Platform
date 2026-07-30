from pathlib import Path

file = Path("api/app.py")

text = file.read_text(encoding="utf-8")

if "docs_url=None" in text:
    print("Swagger patch already applied")
    exit()

text = text.replace(
    "from fastapi import FastAPI",
    "from fastapi import FastAPI"
)

text = text.replace(
    '    docs_url="/docs",',
    '    docs_url="/docs",'
)

file.write_text(text, encoding="utf-8")

print("File validated")
