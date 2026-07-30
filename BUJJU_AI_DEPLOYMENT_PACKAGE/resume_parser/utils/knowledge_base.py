"""
Recruitment Intelligence Platform
Knowledge Base Loader
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from resume_parser.utils.constants import (
    CERTIFICATION_MASTER,
    COMPANY_MASTER,
    DESIGNATION_MASTER,
    DOMAIN_MASTER,
    EDUCATION_MASTER,
    KEYWORD_SYNONYMS,
    LANGUAGE_MASTER,
    LOCATION_MASTER,
    SKILLS_MASTER,
)


@lru_cache(maxsize=None)
def _load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


SKILLS = _load_json(SKILLS_MASTER)

EDUCATION = _load_json(EDUCATION_MASTER)

CERTIFICATIONS = _load_json(CERTIFICATION_MASTER)

# ---------------------------------------------------------------------
# Domains
# ---------------------------------------------------------------------

_domain_data = _load_json(DOMAIN_MASTER)

if isinstance(_domain_data, list):

    DOMAINS = _domain_data

elif isinstance(_domain_data, dict):

    DOMAINS = []

    for value in _domain_data.values():

        if isinstance(value, list):

            DOMAINS.extend(value)

        elif isinstance(value, str):

            DOMAINS.append(value)

    DOMAINS = sorted(set(DOMAINS))

else:

    DOMAINS = []

LANGUAGES = _load_json(LANGUAGE_MASTER)


# ---------------------------------------------------------------------
# Locations
# ---------------------------------------------------------------------

_location_data = _load_json(LOCATION_MASTER)

if isinstance(_location_data, list):

    LOCATIONS = _location_data

elif isinstance(_location_data, dict):

    LOCATIONS = []

    for value in _location_data.values():

        if isinstance(value, list):

            LOCATIONS.extend(value)

        elif isinstance(value, str):

            LOCATIONS.append(value)

    LOCATIONS = sorted(set(LOCATIONS))

else:

    LOCATIONS = []


# ---------------------------------------------------------------------
# Designations
# ---------------------------------------------------------------------

_designation_data = _load_json(DESIGNATION_MASTER)

if isinstance(_designation_data, dict):

    DESIGNATIONS = _designation_data

else:

    DESIGNATIONS = {"default": _designation_data}

DESIGNATION_ALIASES = {}

for values in DESIGNATIONS.values():

    if not isinstance(values, list):
        continue

    for designation in values:

        DESIGNATION_ALIASES.setdefault(
            designation,
            []
        ).append(designation)


# ---------------------------------------------------------------------
# Companies
# ---------------------------------------------------------------------

_company_data = _load_json(COMPANY_MASTER)

if isinstance(_company_data, dict):

    COMPANY_ALIASES = _company_data

elif isinstance(_company_data, list):

    COMPANY_ALIASES = {
        company: [company]
        for company in _company_data
    }

else:

    COMPANY_ALIASES = {}


KEYWORDS = _load_json(KEYWORD_SYNONYMS)