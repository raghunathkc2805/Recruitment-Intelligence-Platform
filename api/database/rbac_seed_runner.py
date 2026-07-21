"""
Enterprise RBAC Seed Runner
"""

from database.session import SessionLocal
from api.database.seed_rbac import seed_rbac


def main():

    db = SessionLocal()

    try:
        seed_rbac(db)
        print("RBAC seed completed successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    main()

