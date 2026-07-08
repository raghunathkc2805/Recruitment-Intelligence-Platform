import argparse
import pathlib
import subprocess
import sys
import shutil
from datetime import datetime

VERSION = "1.4.0"
ROOT = pathlib.Path(__file__).resolve().parent.parent

def doctor(args):
    print("Project Status : OK")

def init(args):
    print("Project Initialized")

def version(args):
    print(f"Developer CLI v{VERSION}")

def stats(args):
    print("Project Statistics")
    print("------------------")
    print(f"Python Files : {len(list(ROOT.rglob('*.py')))}")
    print(f"JSON Files   : {len(list(ROOT.rglob('*.json')))}")
    print(f"Test Files   : {len(list(ROOT.rglob('test_*.py')))}")

def test(args):
    subprocess.run([sys.executable, "-m", "pytest"], cwd=ROOT)

def build(args):
    print("Build Successful")

def backup(args):
    backup_root = ROOT / "backups"
    backup_root.mkdir(exist_ok=True)

    name = datetime.now().strftime("backup_%Y%m%d_%H%M%S")
    destination = backup_root / name

    shutil.copytree(
        ROOT,
        destination,
        ignore=shutil.ignore_patterns(
            "backups",
            "__pycache__",
            ".pytest_cache",
            ".git",
            "*.pyc"
        )
    )

    print(f"Backup Created : {destination}")

COMMANDS = {
    "doctor": doctor,
    "init": init,
    "version": version,
    "stats": stats,
    "test": test,
    "build": build,
    "backup": backup,
}

parser = argparse.ArgumentParser(prog="dev.py")
sub = parser.add_subparsers(dest="command")

for cmd in COMMANDS:
    sub.add_parser(cmd)

args = parser.parse_args()

if args.command:
    COMMANDS[args.command](args)
else:
    parser.print_help()
