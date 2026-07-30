"""
Recruitment Intelligence Platform
CSV Printer
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


class CSVPrinter:
    """
    Export parsed resume data to CSV.
    """

    HEADERS = [
        "name",
        "email",
        "phone",
        "experience",
        "technical_skills",
        "functional_skills",
        "soft_skills",
        "education",
        "employers",
        "certifications",
        "languages",
        "locations",
    ]

    @classmethod
    def save(
        cls,
        data: dict[str, Any],
        output_file: str | Path,
    ) -> Path:

        output_path = Path(output_file)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        candidate = data.get("candidate", {})
        skills = candidate.get("skills", {})

        row = {
            "name": candidate.get("name"),
            "email": candidate.get("email"),
            "phone": candidate.get("phone"),
            "experience": candidate.get("experience"),
            "technical_skills": ", ".join(
                skills.get("technical_skills", [])
            ),
            "functional_skills": ", ".join(
                skills.get("functional_skills", [])
            ),
            "soft_skills": ", ".join(
                skills.get("soft_skills", [])
            ),
            "education": "; ".join(
                item.get("degree", "")
                for item in candidate.get("education", [])
            ),
            "employers": "; ".join(
                item.get("company", "")
                for item in candidate.get("employers", [])
            ),
            "certifications": "; ".join(
                item.get("certification", "")
                for item in candidate.get("certifications", [])
            ),
            "languages": "; ".join(
                item.get("language", "")
                for item in candidate.get("languages", [])
            ),
            "locations": "; ".join(
                item.get("location", "")
                for item in candidate.get("locations", [])
            ),
        }

        with open(
            output_path,
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=cls.HEADERS,
            )

            writer.writeheader()
            writer.writerow(row)

        return output_path