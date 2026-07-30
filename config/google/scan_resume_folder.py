from google.oauth2 import service_account
import os
from pathlib import Path
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly"
]

SERVICE_ACCOUNT_FILE = os.getenv(
    "GOOGLE_SERVICE_ACCOUNT_FILE",
    str(Path(__file__).parent / "service_account.json"),
)

ROOT_FOLDER_ID = "1xWuPeJY_gxYmQZccUUhvHm5y7Rk8j1Gj"


creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build(
    "drive",
    "v3",
    credentials=creds
)


resume_count = 0


def scan_folder(folder_id, level=0):

    global resume_count

    query = "'" + folder_id + "' in parents and trashed=false"

    result = service.files().list(
        q=query,
        fields="files(name,id,mimeType)"
    ).execute()

    files = result.get("files", [])

    for file in files:

        name = file["name"]
        mime = file["mimeType"]

        if mime == "application/vnd.google-apps.folder":

            print("  " * level + "[FOLDER] " + name)

            scan_folder(
                file["id"],
                level + 1
            )

        elif mime in [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ]:

            resume_count += 1

            print(
                "  " * level +
                "[RESUME] " +
                name
            )


scan_folder(ROOT_FOLDER_ID)


print("")
print("==============================")
print("TOTAL RESUMES FOUND:", resume_count)
print("==============================")
print("RECURSIVE RESUME SCAN COMPLETE")
