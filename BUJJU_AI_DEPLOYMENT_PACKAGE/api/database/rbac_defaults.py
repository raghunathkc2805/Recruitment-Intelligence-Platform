"""
Enterprise RBAC Default Roles & Permissions
"""

from api.auth.permission_constants import Permission


DEFAULT_ROLE_PERMISSIONS = {

    "Super Admin": [
        Permission.SYSTEM_ADMIN,
        "*",
    ],

    "Admin": [
        Permission.USER_CREATE,
        Permission.USER_VIEW,
        Permission.USER_UPDATE,
        Permission.USER_DELETE,
        Permission.ROLE_CREATE,
        Permission.ROLE_VIEW,
        Permission.ROLE_UPDATE,
        Permission.ROLE_DELETE,
        Permission.PERMISSION_CREATE,
        Permission.PERMISSION_VIEW,
        Permission.PERMISSION_UPDATE,
        Permission.PERMISSION_DELETE,
        Permission.CANDIDATE_CREATE,
        Permission.CANDIDATE_VIEW,
        Permission.CANDIDATE_UPDATE,
        Permission.CANDIDATE_DELETE,
        Permission.RESUME_UPLOAD,
        Permission.RESUME_VIEW,
        Permission.JD_CREATE,
        Permission.JD_VIEW,
        Permission.MATCHING_RUN,
        Permission.RANKING_RUN,
        Permission.SEARCH_EXECUTE,
        Permission.RECOMMENDATION_RUN,
    ],

    "Recruitment Manager": [
        Permission.CANDIDATE_CREATE,
        Permission.CANDIDATE_VIEW,
        Permission.CANDIDATE_UPDATE,
        Permission.RESUME_UPLOAD,
        Permission.RESUME_VIEW,
        Permission.JD_CREATE,
        Permission.JD_VIEW,
        Permission.MATCHING_RUN,
        Permission.RANKING_RUN,
        Permission.SEARCH_EXECUTE,
        Permission.RECOMMENDATION_RUN,
    ],

    "Recruiter": [
        Permission.CANDIDATE_CREATE,
        Permission.CANDIDATE_VIEW,
        Permission.RESUME_UPLOAD,
        Permission.RESUME_VIEW,
        Permission.JD_VIEW,
        Permission.MATCHING_RUN,
        Permission.RANKING_RUN,
        Permission.SEARCH_EXECUTE,
    ],

    "Hiring Manager": [
        Permission.CANDIDATE_VIEW,
        Permission.RESUME_VIEW,
        Permission.JD_VIEW,
        Permission.MATCHING_RUN,
        Permission.RANKING_RUN,
    ],

    "Interviewer": [
        Permission.CANDIDATE_VIEW,
        Permission.RESUME_VIEW,
    ],

    "Read Only": [
        Permission.CANDIDATE_VIEW,
        Permission.RESUME_VIEW,
        Permission.JD_VIEW,
    ],
}
