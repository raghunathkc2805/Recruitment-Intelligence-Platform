import re


def _acronym_pattern(token):
    """Build a regex for OCR-tolerant acronym matching."""

    escaped = [re.escape(char) for char in token]
    return r"\b" + r"\s*\.?\s*".join(escaped) + r"\b"


def _normalize_education(text):
    """Detect qualification terms and normalize to standard labels."""

    if not text:
        return []

    patterns = [
        ("Any Graduate", r"\bany\s+graduate\b(?:\s+or\s+equivalent\b)?"),
        ("Post Graduate", r"\bpost\s+(?:graduate|graduation)\b(?:\s+or\s+equivalent\b)?"),
        (
            "Graduate",
            r"(?<!\bany\s)(?<!\bpost\s)\bgraduat(?:e|ion)\b(?:\s+or\s+equivalent\b)?",
        ),
        ("Any Degree", r"\bany\s+degree\b(?:\s+or\s+equivalent\b)?"),
        (
            "Bachelor's Degree",
            r"\b(bachelor|bachelors)(?:'s)?\s+degree\b(?:\s+or\s+equivalent\b)?",
        ),
        (
            "Master's Degree",
            r"\b(master|masters)(?:'s)?\s+degree\b(?:\s+or\s+equivalent\b)?",
        ),
        ("UG", _acronym_pattern("UG")),
        ("PG", _acronym_pattern("PG")),
        ("SSLC", _acronym_pattern("SSLC")),
        ("PUC", _acronym_pattern("PUC")),
        ("Diploma", _acronym_pattern("Diploma")),
        ("ITI", _acronym_pattern("ITI")),
        ("B.E.", _acronym_pattern("BE")),
        ("B.Tech", r"\bB\s*\.?\s*T\s*\.?\s*E\s*\.?\s*C\s*\.?\s*H\b"),
        ("BCA", _acronym_pattern("BCA")),
        ("B.Sc", r"\bB\s*\.?\s*S\s*\.?\s*C\b"),
        ("B.Com", r"\bB\s*\.?\s*C\s*\.?\s*O\s*\.?\s*M\b"),
        ("BA", _acronym_pattern("BA")),
        ("BBA", _acronym_pattern("BBA")),
        ("BBM", _acronym_pattern("BBM")),
        ("MBA", _acronym_pattern("MBA")),
        ("MCA", _acronym_pattern("MCA")),
        ("M.Tech", r"\bM\s*\.?\s*T\s*\.?\s*E\s*\.?\s*C\s*\.?\s*H\b"),
        ("M.E.", _acronym_pattern("ME")),
        ("M.Com", r"\bM\s*\.?\s*C\s*\.?\s*O\s*\.?\s*M\b"),
        ("M.Sc", r"\bM\s*\.?\s*S\s*\.?\s*C\b"),
        ("PhD", r"\bP\s*\.?\s*H\s*\.?\s*D\b"),
    ]

    def _match_is_valid(label, match_text):
        if label in {"B.E.", "M.E."}:
            stripped = re.sub(r"[\.\s]", "", match_text)
            if stripped.lower() in {"be", "me"}:
                return match_text.isupper() or bool(re.search(r"[\.\s]", match_text))
        return True

    matches = []
    for index, (label, pattern) in enumerate(patterns):
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            if _match_is_valid(label, match.group(0)):
                matches.append((match.start(), index, label))

    matches.sort(key=lambda item: (item[0], item[1]))

    normalized = []
    seen = set()
    for _, _, label in matches:
        if label not in seen:
            normalized.append(label)
            seen.add(label)

    return normalized


def extract_education(text):
    """Extract education requirements."""

    if not text:
        return []

    return _normalize_education(text)
