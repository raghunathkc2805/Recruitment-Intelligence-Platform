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

FOLDER_ID = "1xWuPeJY_gxYmQZccUUhvHm5y7Rk8j1Gj"


creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build(
    "drive",
    "v3",
    credentials=creds
)


query = "'" + FOLDER_ID + "' in parents"

response = service.files().list(
    q=query,
    fields="files(name,id,mimeType)"
).execute()


files = response.get("files", [])

print("Folder: Consolidated Resumes")
print("Files Found:", len(files))

for file in files[:10]:
    print(
        file["name"],
        "-",
        file["mimeType"]
    )

print("GOOGLE DRIVE CONNECTION SUCCESS")
