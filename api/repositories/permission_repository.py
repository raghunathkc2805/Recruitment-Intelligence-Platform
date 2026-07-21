from sqlalchemy.orm import Session

from api.models.rbac import (
    Permission,
    Role,
    role_permissions,
    user_roles,
)


class PermissionRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_role_by_name(self, role_name: str):
        return (
            self.db.query(Role)
            .filter(Role.name == role_name)
            .first()
        )

    def get_permission_by_name(self, permission_name: str):
        return (
            self.db.query(Permission)
            .filter(Permission.name == permission_name)
            .first()
        )

    def assign_permission_to_role(
        self,
        role_id: int,
        permission_id: int,
    ):

        exists = self.db.execute(
            role_permissions.select().where(
                (role_permissions.c.role_id == role_id) &
                (role_permissions.c.permission_id == permission_id)
            )
        ).first()

        if exists:
            return

        self.db.execute(
            role_permissions.insert().values(
                role_id=role_id,
                permission_id=permission_id,
            )
        )

        self.db.commit()

    def assign_role_to_user(
        self,
        user_id: int,
        role_id: int,
    ):

        exists = self.db.execute(
            user_roles.select().where(
                (user_roles.c.user_id == user_id) &
                (user_roles.c.role_id == role_id)
            )
        ).first()

        if exists:
            return

        self.db.execute(
            user_roles.insert().values(
                user_id=user_id,
                role_id=role_id,
            )
        )

        self.db.commit()
