from api.repositories.permission_repository import PermissionRepository


class RBACService:

    def __init__(self, db):
        self.repository = PermissionRepository(db)

    def assign_role_to_user(
        self,
        user_id: int,
        role_name: str,
    ):

        role = self.repository.get_role_by_name(role_name)

        if role is None:
            raise ValueError(f"Role '{role_name}' does not exist.")

        self.repository.assign_role_to_user(
            user_id=user_id,
            role_id=role.id,
        )

    def assign_permission_to_role(
        self,
        role_name: str,
        permission_name: str,
    ):

        role = self.repository.get_role_by_name(role_name)

        if role is None:
            raise ValueError(f"Role '{role_name}' does not exist.")

        permission = self.repository.get_permission_by_name(
            permission_name
        )

        if permission is None:
            raise ValueError(
                f"Permission '{permission_name}' does not exist."
            )

        self.repository.assign_permission_to_role(
            role_id=role.id,
            permission_id=permission.id,
        )

    def assign_permissions(
        self,
        role_name: str,
        permissions: list[str],
    ):

        for permission in permissions:
            self.assign_permission_to_role(
                role_name,
                permission,
            )
