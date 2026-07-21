from api.repositories.rbac_repository import RBACRepository


class PermissionService:

    def __init__(self, db):
        self.repository = RBACRepository(db)

    def get_roles(self):
        return self.repository.list_roles()

    def get_permissions(self):
        return self.repository.list_permissions()

    def role_exists(self, role_name: str) -> bool:
        return self.repository.get_role(role_name) is not None

    def permission_exists(self, permission_name: str) -> bool:
        return self.repository.get_permission(permission_name) is not None

    def create_role(
        self,
        name: str,
        description: str = "",
        is_active: bool = True,
    ):
        role = self.repository.get_role(name)
        if role:
            return role

        return self.repository.create_role(
            name=name,
            description=description,
            is_active=is_active,
        )

    def create_permission(
        self,
        name: str,
        module: str,
        description: str = "",
        is_active: bool = True,
    ):
        permission = self.repository.get_permission(name)
        if permission:
            return permission

        return self.repository.create_permission(
            name=name,
            module=module,
            description=description,
            is_active=is_active,
        )
