import re


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


def extract_mobile(text):

    pattern = r"(?:\+91)?[6-9]\d{9}"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


def extract_name(text):
    """
    Candidate name is normally the first non-empty line.
    """

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        if "@" in line:
            continue

        if "email" in line.lower():
            continue

        if "mobile" in line.lower():
            continue

        if "address" in line.lower():
            continue

        if re.search(r"\d{5,}", line):
            continue

        words = line.split()

        if 2 <= len(words) <= 5:
            return line

    return ""