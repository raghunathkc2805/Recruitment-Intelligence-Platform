import json
import os
import re


def _load_certifications():
    """
    Load certification master.
    """

    kb_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "knowledge_base",
        "certification_master.json"
    )

    with open(kb_path, "r", encoding="utf-8") as file:
        return json.load(file)


CERTIFICATIONS = _load_certifications()


def extract_certifications(text):
    """
    Extract certifications from Job Description.
    """

    if not text:
        return []

    text = text.lower()

    found = []

    for certification in CERTIFICATIONS:

        pattern = r"\b" + re.escape(certification.lower()) + r"\b"

        if re.search(pattern, text):

            found.append(certification)

    return sorted(set(found))