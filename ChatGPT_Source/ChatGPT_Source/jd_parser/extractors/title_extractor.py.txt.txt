import re

from jd_parser.utils.knowledge_base import DESIGNATIONS


FIELD_PATTERNS = [
    r"Position\s+Name\s*:?\s*(.+)",
    r"Job\s+Title\s*:?\s*(.+)",
    r"Designation\s*:?\s*(.+)",
    r"Position\s*:?\s*(.+)",
    r"Role\s*:?\s*(.+)",
    r"Requirement\s*:?\s*(.+)",
    r"Opening\s+For\s*:?\s*(.+)"
]


IGNORE_WORDS = {
    "manager",
    "reporting manager",
    "hiring manager",
    "project manager",
    "approved by",
    "requested by"
}


def clean_title(title):
    """
    Clean extracted title.
    """

    title = title.strip()

    title = re.sub(r"\s+", " ", title)

    title = title.replace(":", "")

    return title


def extract_job_title(text):
    """
    Extract Job Title from Teleindia GRC and standard JDs.
    """

    # -----------------------------------------
    # Step 1
    # Structured field extraction
    # -----------------------------------------

    for pattern in FIELD_PATTERNS:

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        if match:

            title = clean_title(match.group(1))

            if title.lower() not in IGNORE_WORDS:
                return title

    # -----------------------------------------
    # Step 2
    # Search only Job Description section
    # -----------------------------------------

    jd_match = re.search(
        r"JOB DESCRIPTION(.*)",
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    if jd_match:

        jd_text = jd_match.group(1)

        for designation in sorted(
            DESIGNATIONS,
            key=len,
            reverse=True
        ):

            if designation.lower() in jd_text.lower():

                if designation.lower() not in IGNORE_WORDS:
                    return designation

    return ""