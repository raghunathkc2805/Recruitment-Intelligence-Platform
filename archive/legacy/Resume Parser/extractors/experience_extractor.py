import re


def extract_employment_history(text):
    """
    Extract employment history using simple company/designation pairing.
    """

    history = []

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    company_keywords = [
        "Ltd",
        "Limited",
        "Pvt",
        "Private",
        "Technologies",
        "Solutions",
        "Networks",
        "Systems",
        "Services",
        "Corporation",
        "Inc"
    ]

    for i in range(len(lines) - 1):

        line = lines[i]

        if any(keyword.lower() in line.lower() for keyword in company_keywords):

            designation = lines[i + 1]

            history.append({
                "company": line,
                "designation": designation
            })

    return history


def extract_current_company(history):

    if history:
        return history[0]["company"]

    return ""


def extract_current_designation(history):

    if history:
        return history[0]["designation"]

    return ""


def get_experience_type(history):

    if history:
        return "Experienced"

    return "Fresher"