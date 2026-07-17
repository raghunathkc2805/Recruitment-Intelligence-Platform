"""
Recruitment Intelligence Platform
Project Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List


PROJECT_HEADERS = (
    "projects",
    "project experience",
    "professional projects",
)

TECHNOLOGY_PATTERN = re.compile(
    r"""
    \b(
        Python|
        Java|
        C\+\+|
        C#|
        SQL|
        Oracle|
        MySQL|
        PostgreSQL|
        MongoDB|
        AWS|
        Azure|
        GCP|
        Docker|
        Kubernetes|
        VMware|
        Linux|
        Windows|
        Cisco|
        Nokia|
        Ericsson|
        Huawei
    )\b
    """,
    re.IGNORECASE | re.VERBOSE,
)


class ProjectExtractor:
    """
    Extract project details from resume text.
    """

    @classmethod
    def extract(cls, text: str) -> List[Dict]:

        if not text:
            return []

        projects = []

        lines = text.splitlines()

        inside_projects = False

        current = []

        for line in lines:

            value = line.strip()

            if not value:
                continue

            lower = value.lower()

            if lower in PROJECT_HEADERS:

                inside_projects = True

                continue

            if inside_projects:

                if value.isupper() and len(value) < 40:

                    break

                current.append(value)

        if current:

            project_text = "\n".join(current)

            technologies = sorted(
                {
                    match.group(0)
                    for match in TECHNOLOGY_PATTERN.finditer(
                        project_text
                    )
                }
            )

            projects.append(
                {
                    "project_name": None,
                    "client": None,
                    "role": None,
                    "duration": None,
                    "technologies": technologies,
                    "description": project_text,
                }
            )

        return projects