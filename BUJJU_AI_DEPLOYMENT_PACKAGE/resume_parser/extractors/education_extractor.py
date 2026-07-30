"""
Recruitment Intelligence Platform
Education Extractor
"""

from __future__ import annotations

import re
from typing import Dict, List

from resume_parser.utils.knowledge_base import EDUCATION

DEGREES = EDUCATION

YEAR_PATTERN = re.compile(r"\b(?:19|20)\d{2}\b")

PERCENT_PATTERN = re.compile(r"\b\d{2,3}(?:\.\d+)?\s*%")

CGPA_PATTERN = re.compile(r"\b\d(?:\.\d+)?\s*/\s*10\b")


class EducationExtractor:

    @classmethod
    def extract(cls, text: str) -> List[Dict]:

        if not text:
            return []

        records = []

        lines = text.splitlines()

        for line in lines:

            degree = None

            for item in DEGREES:

                if item.lower() in line.lower():

                    degree = item

                    break

            if not degree:
                continue

            years = [match.group(0) for match in YEAR_PATTERN.finditer(line)]

            percentage = PERCENT_PATTERN.search(line)

            cgpa = CGPA_PATTERN.search(line)

            records.append(

                {

                    "degree": degree,

                    "text": line.strip(),

                    "year": years[-1] if years else None,

                    "percentage": percentage.group(0) if percentage else None,

                    "cgpa": cgpa.group(0) if cgpa else None,

                }

            )

        return records
