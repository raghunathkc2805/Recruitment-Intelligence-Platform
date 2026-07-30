"""
Recruitment Intelligence Platform
Console Printer
"""

from __future__ import annotations

from typing import Any


class ConsolePrinter:
    """
    Pretty prints parsed resume information.
    """

    @staticmethod
    def print(data: dict[str, Any]) -> None:

        candidate = data.get("candidate", {})

        print("=" * 80)
        print("Resume Information")
        print("=" * 80)

        print(f"File           : {data.get('file_name')}")
        print(f"Type           : {data.get('file_type')}")
        print(f"Pages          : {data.get('pages')}")

        print("-" * 80)

        print(f"Name           : {candidate.get('name')}")
        print(f"Email          : {candidate.get('email')}")
        print(f"Phone          : {candidate.get('phone')}")

        print()

        print("Summary")
        print("-" * 80)
        print(candidate.get("summary") or "")

        print()

        print("Experience")
        print("-" * 80)
        print(candidate.get("experience"))

        print()

        print("Education")
        print("-" * 80)
        for item in candidate.get("education", []):
            print(item)

        print()

        print("Skills")
        print("-" * 80)
        skills = candidate.get("skills", {})
        print("Technical :", ", ".join(skills.get("technical_skills", [])))
        print("Functional:", ", ".join(skills.get("functional_skills", [])))
        print("Soft      :", ", ".join(skills.get("soft_skills", [])))

        print()

        print("Employers")
        print("-" * 80)
        for item in candidate.get("employers", []):
            print(item)

        print()

        print("Projects")
        print("-" * 80)
        for item in candidate.get("projects", []):
            print(item)

        print()

        print("Certifications")
        print("-" * 80)
        for item in candidate.get("certifications", []):
            print(item)

        print()

        print("Languages")
        print("-" * 80)
        for item in candidate.get("languages", []):
            print(item)

        print()

        print("Locations")
        print("-" * 80)
        for item in candidate.get("locations", []):
            print(item)

        print("=" * 80)