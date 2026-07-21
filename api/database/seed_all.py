"""
Master Enterprise Seeder

Execution Order

1. Roles
2. Permissions
3. Role-Permission Mapping
"""

from database.session import SessionLocal
from api.database.seed_enterprise_rbac import seed_enterprise_rbac


def main():

    db = SessionLocal()

    try:

        seed_enterprise_rbac(db)

        print("=" * 60)
        print("Enterprise RBAC Seed Completed Successfully")
        print("=" * 60)

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    main()

