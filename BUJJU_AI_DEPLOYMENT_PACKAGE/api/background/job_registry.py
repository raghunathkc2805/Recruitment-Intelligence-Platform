"""
Background Job Registry
"""

from api.background.jobs.resume_parser_job import process_resume
from api.background.jobs.jd_parser_job import process_job_description
from api.background.jobs.candidate_matching_job import process_candidate_matching
from api.background.jobs.recommendation_job import process_recommendation
from api.background.jobs.report_generation_job import generate_report
from api.background.jobs.email_notification_job import send_email_notification

JOB_REGISTRY = {
    "resume_parser": process_resume,`r`n    "jd_parser": process_job_description,`r`n    "candidate_matching": process_candidate_matching,`r`n    "recommendation": process_recommendation,`r`n    "report_generation": generate_report,`r`n    "email_notification": send_email_notification,
}





