import re

from jd_parser.utils.knowledge_base import DOMAINS


def extract_domains(text):
    """
    Extract primary and secondary domains from a Job Description.
    """

    text_lower = text.lower()
    scores = {}

    for domain, keywords in DOMAINS.items():

        score = 0

        for keyword in keywords:

            pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

            if re.search(pattern, text_lower):
                score += 1

        if score:
            scores[domain] = score

    if not scores:
        return "", ""

    ranked = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    primary = ranked[0][0]
    secondary = ranked[1][0] if len(ranked) > 1 else ""

    return primary, secondary