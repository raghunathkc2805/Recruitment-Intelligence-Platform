from jd_parser.utils.knowledge_base import DOMAINS


def extract_domains(text):
    """
    Detect primary and secondary domains from resume text.
    """

    text = text.lower()

    scores = {}

    for domain, keywords in DOMAINS.items():

        score = 0

        for keyword in keywords:

            if keyword.lower() in text:
                score += 1

        if score > 0:
            scores[domain] = score

    if not scores:
        return "", ""

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    primary = ranked[0][0]

    secondary = ""

    if len(ranked) > 1:
        secondary = ranked[1][0]

    return primary, secondary