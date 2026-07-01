import re


def extract_experience(text):
    """
    Extract minimum and maximum experience from a Job Description.
    """

    patterns = [

        r"(\d+)\s*[-–]\s*(\d+)\s*Years",

        r"(\d+)\s*to\s*(\d+)\s*Years",

        r"Minimum\s*(\d+)\s*Years",

        r"(\d+)\+\s*Years",

        r"(\d+)\s*Years"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        if not match:
            continue

        if len(match.groups()) == 2:

            return (
                float(match.group(1)),
                float(match.group(2))
            )

        value = float(match.group(1))

        if "+" in match.group(0):
            return (value, 99)

        if "minimum" in match.group(0).lower():
            return (value, 99)

        return (value, value)

    return (0, 0)