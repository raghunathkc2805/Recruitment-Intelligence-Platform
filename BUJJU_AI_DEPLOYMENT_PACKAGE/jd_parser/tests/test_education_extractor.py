import pytest

from jd_parser.extractors.education_extractor import extract_education


@pytest.mark.parametrize(
    "text,expected",
    [
        ("SSLC", ["SSLC"]),
        ("S.S.L.C", ["SSLC"]),
        ("s s l c", ["SSLC"]),
        ("PUC", ["PUC"]),
        ("Diploma", ["Diploma"]),
        ("ITI", ["ITI"]),
        ("B.E.", ["B.E."]),
        ("BE", ["B.E."]),
        ("B E", ["B.E."]),
        ("BTech", ["B.Tech"]),
        ("B.Tech", ["B.Tech"]),
        ("B Tech", ["B.Tech"]),
        ("BCA", ["BCA"]),
        ("B.Sc", ["B.Sc"]),
        ("BSc", ["B.Sc"]),
        ("B Com", ["B.Com"]),
        ("B.Com", ["B.Com"]),
        ("BA", ["BA"]),
        ("BBA", ["BBA"]),
        ("BBM", ["BBM"]),
        ("MBA", ["MBA"]),
        ("MCA", ["MCA"]),
        ("M.Tech", ["M.Tech"]),
        ("MTech", ["M.Tech"]),
        ("M.E.", ["M.E."]),
        ("ME", ["M.E."]),
        ("M.Com", ["M.Com"]),
        ("MSc", ["M.Sc"]),
        ("M.Sc", ["M.Sc"]),
        ("PhD", ["PhD"]),
        ("Ph.D.", ["PhD"]),
        ("Any Graduate", ["Any Graduate"]),
        ("Any graduate", ["Any Graduate"]),
        ("Graduate", ["Graduate"]),
        ("Post Graduate", ["Post Graduate"]),
        ("UG", ["UG"]),
        ("PG", ["PG"]),
        ("Any Degree", ["Any Degree"]),
        ("Bachelor's Degree", ["Bachelor's Degree"]),
        ("Bachelors Degree", ["Bachelor's Degree"]),
        ("Master's Degree", ["Master's Degree"]),
        ("Masters Degree", ["Master's Degree"]),
        ("BE or equivalent", ["B.E."]),
        ("B.Tech or equivalent", ["B.Tech"]),
        ("Any Graduate or equivalent", ["Any Graduate"]),
        ("M.Sc or equivalent", ["M.Sc"]),
        ("PG or equivalent", ["PG"]),
        ("Graduate or equivalent", ["Graduate"]),
        ("Any Degree or equivalent", ["Any Degree"]),
        (
            "PUC, Diploma, B.Tech, MBA, PG",
            ["PUC", "Diploma", "B.Tech", "MBA", "PG"],
        ),
        (
            "Any Graduate; B.Com; M.Tech; UG; PG",
            ["Any Graduate", "B.Com", "M.Tech", "UG", "PG"],
        ),
        (
            "Graduate and Post Graduate",
            ["Graduate", "Post Graduate"],
        ),
        (
            "UG/PG",
            ["UG", "PG"],
        ),
        (
            "B . T e c h",
            ["B.Tech"],
        ),
        (
            "M . S c",
            ["M.Sc"],
        ),
        (
            "B . E",
            ["B.E."],
        ),
        (
            "Any Degree, Graduate, Post Graduate, Any Graduate",
            ["Any Degree", "Graduate", "Post Graduate", "Any Graduate"],
        ),
        (
            "Graduate, Graduate, G raduate",
            ["Graduate"],
        ),
        (
            "M.Tech, mtech, M . Tech",
            ["M.Tech"],
        ),
        (
            "B.Sc, BSC, b sc",
            ["B.Sc"],
        ),
        (
            "SSLC PUC Diploma ITI B.E. B.Tech BCA B.Sc B.Com BA BBA BBM MBA MCA M.Tech M.E. M.Com M.Sc PhD",
            [
                "SSLC",
                "PUC",
                "Diploma",
                "ITI",
                "B.E.",
                "B.Tech",
                "BCA",
                "B.Sc",
                "B.Com",
                "BA",
                "BBA",
                "BBM",
                "MBA",
                "MCA",
                "M.Tech",
                "M.E.",
                "M.Com",
                "M.Sc",
                "PhD",
            ],
        ),
        (
            "The candidate should be a Graduate with B.Com and MBA.",
            ["Graduate", "B.Com", "MBA"],
        ),
        (
            "Required: Any Graduate, UG, PG, Bachelor's Degree, Master's Degree",
            ["Any Graduate", "UG", "PG", "Bachelor's Degree", "Master's Degree"],
        ),
        (
            "Preferred: PUC or equivalent; Diploma; BCA; M.Sc; Ph.D.",
            ["PUC", "Diploma", "BCA", "M.Sc", "PhD"],
        ),
        (
            "Bachelor's Degree or equivalent in any discipline",
            ["Bachelor's Degree"],
        ),
        (
            "Master's Degree or equivalent in computer science",
            ["Master's Degree"],
        ),
        (
            "UG and PG are both acceptable.",
            ["UG", "PG"],
        ),
        (
            "Freshers with any graduate qualification",
            ["Any Graduate"],
        ),
        (
            "Candidate must have Post Graduate experience.",
            ["Post Graduate"],
        ),
        (
            "Education: SSL C, PUC, and B E.",
            ["SSLC", "PUC", "B.E."],
        ),
        (
            "Education: B TECH, M TECH, M COM, B SC",
            ["B.Tech", "M.Tech", "M.Com", "B.Sc"],
        ),
        (
            "Education Preference: Any Degree or equivalent",
            ["Any Degree"],
        ),
        (
            "Education Preference: Graduate, BBA, BBM",
            ["Graduate", "BBA", "BBM"],
        ),
        (
            "Qualifications: M E, B C A, P U C, D i p l o m a",
            ["M.E.", "BCA", "PUC", "Diploma"],
        ),
        (
            "Wanted: UG; PG; Any Graduate; B.Com; MBA",
            ["UG", "PG", "Any Graduate", "B.Com", "MBA"],
        ),
        (
            "Students with BBA or BBM will be preferred.",
            ["BBA", "BBM"],
        ),
        (
            "Bachelor's Degree, Master's Degree, and PhD",
            ["Bachelor's Degree", "Master's Degree", "PhD"],
        ),
        (
            "Quick test: Diploma diploma DIPLOMA",
            ["Diploma"],
        ),
        (
            "Education includes PUC, SSLC and Any Graduate",
            ["PUC", "SSLC", "Any Graduate"],
        ),
        (
            "M Com and M Sc degrees are required.",
            ["M.Com", "M.Sc"],
        ),
        (
            "Graduation or Post Graduation preferred.",
            ["Graduate", "Post Graduate"],
        ),
    ],
)
def test_extract_education_normalizes_values(text, expected):
    result = extract_education(text)
    assert isinstance(result, list)
    assert result == expected


def test_extract_education_returns_empty_for_none_text():
    assert extract_education(None) == []


def test_extract_education_returns_empty_for_empty_text():
    assert extract_education("") == []


def test_extract_education_handles_or_equivalent_with_degree():
    result = extract_education("B.E. or equivalent and PG")
    assert result == ["B.E.", "PG"]


def test_extract_education_preserves_order_and_uniqueness():
    result = extract_education("PG, B.Tech, PG, B.Tech, MBA, Graduate")
    assert result == ["PG", "B.Tech", "MBA", "Graduate"]
