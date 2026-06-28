import re

from utils.knowledge_base import UNIVERSITIES


DEGREES = [
    "PhD",
    "Doctor of Philosophy",
    "M.Tech",
    "ME",
    "M.E",
    "MBA",
    "MCA",
    "M.Sc",
    "M.Com",
    "MA",
    "MS",

    "B.Tech",
    "BE",
    "B.E",
    "BCA",
    "BBA",
    "B.Sc",
    "B.Com",
    "BA",

    "Diploma",
    "Polytechnic",
    "ITI",

    "PUC",
    "12th",
    "Intermediate",

    "SSLC",
    "10th"
]


def extract_education(text):

    education = []

    years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)

    for degree in DEGREES:

        if degree.lower() in text.lower():

            university = ""

            for item in UNIVERSITIES:

                if item.lower() in text.lower():
                    university = item
                    break

            year = ""

            if years:
                year = years[0]

            education.append(
                {
                    "degree": degree,
                    "university": university,
                    "year": year
                }
            )

    return education


def highest_qualification(education):

    priority = [
        "PhD",
        "Doctor of Philosophy",

        "M.Tech",
        "ME",
        "M.E",
        "MBA",
        "MCA",
        "M.Sc",
        "M.Com",
        "MA",
        "MS",

        "B.Tech",
        "BE",
        "B.E",
        "BCA",
        "BBA",
        "B.Sc",
        "B.Com",
        "BA",

        "Diploma",
        "ITI",

        "PUC",
        "12th",

        "SSLC",
        "10th"
    ]

    for degree in priority:

        for item in education:

            if item["degree"] == degree:
                return degree

    return ""