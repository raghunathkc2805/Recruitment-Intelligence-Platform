import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from sqlalchemy import inspect

try:
    from database.session import engine
except Exception:
    from database.session import SessionLocal
    engine = SessionLocal().get_bind()

insp = inspect(engine)

print("=" * 100)
print("PROJECT ROOT:", PROJECT_ROOT)
print("=" * 100)

print("\nDATABASE TABLES\n")
tables = sorted(insp.get_table_names())

for table in tables:
    print(table)

if "audit_logs" not in tables:
    print("\nERROR: audit_logs table does not exist.")
    raise SystemExit(1)

print("\n" + "=" * 100)
print("AUDIT_LOGS COLUMNS")
print("=" * 100)

for c in insp.get_columns("audit_logs"):
    print(f"{c['name']:<35} {c['type']}")

print("\n" + "=" * 100)
print("PRIMARY KEY")
print("=" * 100)

print(insp.get_pk_constraint("audit_logs"))

print("\n" + "=" * 100)
print("INDEXES")
print("=" * 100)

for idx in insp.get_indexes("audit_logs"):
    print(idx)

print("\nCompleted successfully.")
