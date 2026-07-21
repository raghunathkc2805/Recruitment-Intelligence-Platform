from sqlalchemy.orm import Session

from api.services.permission_service import PermissionService


DEFAULT_ROLES = [
    ("Super Admin", "System Super Administrator"),
    ("Admin", "Application Administrator"),
    ("Recruitment Manager", "Recruitment Manager"),
    ("Recruiter", "Recruiter"),
    ("Hiring Manager", "Hiring Manager"),
    ("Interviewer", "Interviewer"),
    ("Read Only", "Read Only User"),
]


DEFAULT_PERMISSIONS = [

    ("candidate.create", "candidate", "Create Candidate"),
    ("candidate.view", "candidate", "View Candidate"),
    ("candidate.update", "candidate", "Update Candidate"),
    ("candidate.delete", "candidate", "Delete Candidate"),

    ("resume.upload", "resume", "Upload Resume"),
    ("resume.view", "resume", "View Resume"),

    ("jd.create", "jd", "Create JD"),
    ("jd.view", "jd", "View JD"),

    ("matching.run", "matching", "Run Matching"),
    ("ranking.run", "ranking", "Run Ranking"),

    ("search.execute", "search", "Execute Search"),

    ("user.manage", "admin", "Manage Users"),
    ("role.manage", "admin", "Manage Roles"),
    ("permission.manage", "admin", "Manage Permissions"),
]


def seed_rbac(db: Session):

    service = PermissionService(db)

    for role_name, description in DEFAULT_ROLES:
        service.create_role(
            name=role_name,
            description=description,
        )

    for permission_name, module, description in DEFAULT_PERMISSIONS:
        service.create_permission(
            name=permission_name,
            module=module,
            description=description,
        )

    db.commit()
