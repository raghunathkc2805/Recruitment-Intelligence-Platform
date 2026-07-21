from sqlalchemy.orm import Session

from api.database.rbac_defaults import DEFAULT_ROLE_PERMISSIONS
from api.services.rbac_service import RBACService


def seed_role_permissions(db: Session):

    service = RBACService(db)

    for role_name, permissions in DEFAULT_ROLE_PERMISSIONS.items():
        service.assign_permissions(
            role_name=role_name,
            permissions=permissions,
        )

    db.commit()
