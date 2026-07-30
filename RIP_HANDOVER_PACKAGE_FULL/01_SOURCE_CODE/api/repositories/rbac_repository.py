from sqlalchemy.orm import Session

from api.models.rbac import Permission, Role


class RBACRepository:

    def __init__(self, db: Session):
        self.db = db

    # ---------- Roles ----------

    def get_role(self, role_name: str):
        return (
            self.db.query(Role)
            .filter(Role.name == role_name)
            .first()
        )

    def list_roles(self):
        return (
            self.db.query(Role)
            .order_by(Role.name)
            .all()
        )

    def create_role(self, **kwargs):
        role = Role(**kwargs)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    # ---------- Permissions ----------

    def get_permission(self, permission_name: str):
        return (
            self.db.query(Permission)
            .filter(Permission.name == permission_name)
            .first()
        )

    def list_permissions(self):
        return (
            self.db.query(Permission)
            .order_by(Permission.module, Permission.name)
            .all()
        )

    def create_permission(self, **kwargs):
        permission = Permission(**kwargs)
        self.db.add(permission)
        self.db.commit()
        self.db.refresh(permission)
        return permission
