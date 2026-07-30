from prometheus_client import Counter
from prometheus_client import Histogram
from prometheus_client import Gauge

REQUEST_COUNT = Counter(
    "bujju_http_requests_total",
    "Total HTTP Requests",
    ["method","endpoint","status"]
)

REQUEST_DURATION = Histogram(
    "bujju_http_request_duration_seconds",
    "HTTP Request Duration",
    ["method","endpoint"]
)

ACTIVE_REQUESTS = Gauge(
    "bujju_http_active_requests",
    "Current Active Requests"
)

RESUME_PARSED = Counter(
    "bujju_resume_parsed_total",
    "Parsed Resumes"
)

JD_PARSED = Counter(
    "bujju_jd_parsed_total",
    "Parsed Job Descriptions"
)

AI_REQUESTS = Counter(
    "bujju_ai_requests_total",
    "Bujju AI Requests"
)

MATCH_REQUESTS = Counter(
    "bujju_candidate_matching_total",
    "Candidate Matching Requests"
)
