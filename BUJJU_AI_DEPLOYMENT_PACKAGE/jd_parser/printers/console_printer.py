def print_job_description(job):
    """
    Print Job Description Summary.
    """

    print(f"Job Title              : {job.title}")
    print(f"Company                : {job.company}")
    print(f"Location               : {job.location}")
    print(f"Open Positions         : {job.openings}")

    print(f"Minimum Experience     : {job.minimum_experience}")
    print(f"Maximum Experience     : {job.maximum_experience}")

    print(f"Education              : {len(job.education)}")
    if job.education:
        print(f"Education List         : {', '.join(job.education)}")

    print(f"Technical Skills       : {len(job.technical_skills)}")
    if job.technical_skills:
        print(f"Technical List         : {', '.join(job.technical_skills)}")

    print(f"Functional Skills      : {len(job.functional_skills)}")
    if job.functional_skills:
        print(f"Functional List        : {', '.join(job.functional_skills)}")

    print(f"Soft Skills            : {len(job.soft_skills)}")
    if job.soft_skills:
        print(f"Soft Skills List       : {', '.join(job.soft_skills)}")

    print(f"Certifications         : {len(job.certifications)}")
    if job.certifications:
        print(
            f"Certification List     : "
            f"{', '.join(job.certifications)}"
        )

    print(f"Primary Domain         : {job.primary_domain}")
    print(f"Secondary Domain       : {job.secondary_domain}")

    print(f"Employment Type        : {job.employment_type}")
    print(f"Notice Period          : {job.notice_period}")
    print(f"Salary                 : {job.salary}")

    print(f"Search Keywords        : {len(job.search_keywords)}")