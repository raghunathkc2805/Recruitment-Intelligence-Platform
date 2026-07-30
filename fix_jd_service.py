from pathlib import Path

p = Path("api/services/jd_service.py")
t = p.read_text(encoding="utf-8")

old = """            parsed = Parser.parse(
                stored
            )"""

new = """            parser = Parser()

            text = stored.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            parsed = parser.parse(
                text=text,
                jd_file=stored,
                parser_version=cls.PARSER_VERSION,
            )"""

if old not in t:
    raise Exception("Target code block not found")

p.write_text(
    t.replace(old, new),
    encoding="utf-8"
)

print("JD parser service fixed")
