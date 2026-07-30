"""
Enterprise RBAC Seeder
Seeds:
1. Roles
2. Permissions
3. Role-Permission Mapping
"""

from sqlalchemy.orm import Session

from api.database.seed_rbac import seed_rbac
from api.database.seed_role_permissions import seed_role_permissions


def seed_enterprise_rbac(db: Session):

    seed_rbac(db)
    seed_role_permissions(db)

    db.commit()
