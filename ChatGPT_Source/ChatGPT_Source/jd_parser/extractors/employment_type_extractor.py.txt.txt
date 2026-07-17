import re


# Employment Type Patterns
EMPLOYMENT_TYPE_PATTERNS = {
    "Contract to Hire": [
        r"\bcontract\s+to\s+hire\b",
        r"\bc2h\b"
    ],
    "Full Time": [
        r"\bfull\s+time\b",
        r"\bfull-time\b",
        r"\bfulltime\b"
    ],
    "Permanent": [
        r"\bpermanent\b",
        r"\bperm\b"
    ],
    "Contract": [
        r"\bcontract\b",
        r"\bcontractual\b"
    ],
    "Internship": [
        r"\binternship\b",
        r"\bintern(?:s)?\b"
    ],
    "Freelance": [
        r"\bfreelance\b",
        r"\bfreelancer(?:s)?\b"
    ],
    "Temporary": [
        r"\btemporary\b",
        r"\btemp\b"
    ],
    "Part Time": [
        r"\bpart\s+time\b",
        r"\bpart-time\b",
        r"\bparttime\b"
    ],
    "Apprenticeship": [
        r"\bapprenticeship\b",
        r"\bapprentice(?:s)?\b"
    ]
}

# Work Mode Patterns
WORK_MODE_PATTERNS = {
    "Remote": [
        r"\bremote\b",
        r"\bwork\s+from\s+home\b",
        r"\bwfh\b"
    ],
    "Hybrid": [
        r"\bhybrid\b"
    ],
    "Onsite": [
        r"\bonsite\b",
        r"\bon-site\b",
        r"\boffice\s+based\b",
        r"\bwork\s+from\s+office\b",
        r"\bwfo\b"
    ]
}


def extract_employment_type(text):
    """
    Extract employment type and work mode from Job Description.

    Returns:
        dict: {
            "employment_type": str,
            "work_mode": str
        }
    """

    if not text:
        return {
            "employment_type": "",
            "work_mode": ""
        }

    text_lower = text.lower()

    employment_type = ""
    work_mode = ""

    # Extract Employment Type
    for emp_type, patterns in EMPLOYMENT_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text_lower):
                employment_type = emp_type
                break
        if employment_type:
            break

    # Extract Work Mode
    for mode, patterns in WORK_MODE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text_lower):
                work_mode = mode
                break
        if work_mode:
            break

    return {
        "employment_type": employment_type,
        "work_mode": work_mode
    }
