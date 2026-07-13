def print_candidate(candidate):
    """
    Print Candidate Summary.
    """

    print(f"Name                   : {candidate.name}")
    print(f"Email                  : {candidate.email}")
    print(f"Mobile                 : {candidate.mobile}")

    print(f"Experience Type        : {candidate.experience_type}")
    print(f"Current Company        : {candidate.current_company}")
    print(f"Current Designation    : {candidate.current_designation}")

    print(f"Primary Domain         : {candidate.primary_domain}")
    print(f"Secondary Domain       : {candidate.secondary_domain}")

    print(f"Highest Qualification  : {candidate.highest_qualification}")
    print(f"Education Records      : {len(candidate.education)}")
    print(f"Education Confidence   : {candidate.education_confidence}%")

    print(f"Certifications         : {len(candidate.certifications)}")

    print(f"Primary City           : {candidate.primary_city}")
    print(f"Primary State          : {candidate.primary_state}")
    print(f"Cities Found           : {len(candidate.cities)}")
    print(f"States Found           : {len(candidate.states)}")

    print(f"Companies Found        : {len(candidate.companies)}")

    print(f"Technical Skills       : {len(candidate.technical_skills)}")
    print(f"Functional Skills      : {len(candidate.functional_skills)}")
    print(f"Soft Skills            : {len(candidate.soft_skills)}")

    print(f"Search Keywords        : {len(candidate.search_keywords)}")

    print("-" * 60)

    print(f"Resume Score           : {candidate.resume_score}/100")
    print(f"Resume Grade           : {candidate.resume_grade}")