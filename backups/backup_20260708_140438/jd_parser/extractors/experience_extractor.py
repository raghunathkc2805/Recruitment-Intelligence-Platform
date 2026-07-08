import re


def extract_experience(text):
    """
    Extract minimum and maximum experience from a Job Description.
    """

    if not text:
        return (0, 0)

    cleaned = re.sub(r"\s+", " ", text.strip().lower())

    patterns = [
        # Freshers
        (r"\bfreshers?(?:\s+can\s+apply)?\b", (0, 0)),

        # Range variants
        (r"\b(\d+)\s*[-–]\s*(\d+)\s*(?:years?|yrs?|yoe)\b", None),
        (r"\b(\d+)\s*to\s*(\d+)\s*(?:years?|yrs?|yoe)\b", None),

        # Minimum / At least
        (r"\bminimum\s*(\d+)\s*(?:years?|yrs?|yoe)\b", None),
        (r"\bat\s+least\s*(\d+)\s*(?:years?|yrs?|yoe)\b", None),

        # More than / greater than
        (r"\bmore\s+than\s+(\d+)\s*(?:years?|yrs?|yoe)\b", None),

        # Plus variants
        (r"\b(\d+)\s*\+\s*(?:years?|yrs?|yoe)\b", None),

        # Months to days mapping
        (r"\b1\s*months?\b", (30, 30)),
        (r"\b2\s*months?\b", (60, 60)),
        (r"\b3\s*months?\b", (90, 90)),

        # Explicit single values
        (r"\b(\d+)\s*years?\b", None),
        (r"\b(\d+)\s*yrs?\b", None),
        (r"\b(\d+)\s*yoe\b", None),
    ]

    for pattern, fixed in patterns:
        match = re.search(pattern, cleaned)

        if not match:
            continue

        if fixed is not None:
            return fixed

        groups = match.groups()

        if len(groups) == 2 and groups[1] is not None:
            return (int(groups[0]), int(groups[1]))

        value = int(groups[0])
        matched = match.group(0)

        if "more than" in matched:
            return (value + 1, 99)

        if "+" in matched:
            return (value, 99)

        if "minimum" in matched or "at least" in matched:
            return (value, 99)

        return (value, value)

    return (0, 0)