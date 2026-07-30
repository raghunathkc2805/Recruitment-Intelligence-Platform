from pathlib import Path

p = Path("api/auth/auth_service.py")
t = p.read_text(encoding="utf-8")

t = t.replace(
'''        claims = {
            "sub": str(user.id),
            "username": user.username,
            "email": user.email,
            "role": user.role,
        }''',
'''        from api.models.rbac import Role, Permission, role_permissions

        role = db.query(Role).filter(Role.name == user.role).first()

        permissions = []

        if role:
            permissions = [
                permission.name
                for permission in (
                    db.query(Permission)
                    .join(
                        role_permissions,
                        Permission.id == role_permissions.c.permission_id
                    )
                    .filter(role_permissions.c.role_id == role.id)
                    .all()
                )
            ]

        claims = {
            "sub": str(user.id),
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "permissions": permissions,
        }'''
)

p.write_text(t, encoding="utf-8")
print("JWT permission claim patch applied")
