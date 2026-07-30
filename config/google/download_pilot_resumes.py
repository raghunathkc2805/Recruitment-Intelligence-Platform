from google.oauth2 import service_account
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

import io
from pathlib import Path


SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly"
]

SERVICE_ACCOUNT_FILE = os.getenv(
    "GOOGLE_SERVICE_ACCOUNT_FILE",
    str(Path(__file__).parent / "service_account.json"),
)

OUTPUT_FOLDER = Path("talent_import/pilot_resumes")

OUTPUT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)


creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build(
    "drive",
    "v3",
    credentials=creds
)


resume_files = []


def scan_folder(folder_id):

    query = "'" + folder_id + "' in parents and trashed=false"

    result = service.files().list(
        q=query,
        fields="files(name,id,mimeType)"
    ).execute()

    for file in result.get("files", []):

        if file["mimeType"] == "application/vnd.google-apps.folder":

            scan_folder(file["id"])

        elif file["mimeType"] in [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ]:

            resume_files.append(file)


scan_folder(
    "1xWuPeJY_gxYmQZccUUhvHm5y7Rk8j1Gj"
)


print("Total resumes found:", len(resume_files))

pilot_files = resume_files[:100]


for index, file in enumerate(pilot_files, start=1):

    request = service.files().get_media(
        fileId=file["id"]
    )

    filename = OUTPUT_FOLDER / file["name"]

    with io.FileIO(
        filename,
        "wb"
    ) as fh:

        downloader = MediaIoBaseDownload(
            fh,
            request
        )

        done = False

        while not done:
            status, done = downloader.next_chunk()


    print(
        index,
        "Downloaded:",
        file["name"]
    )


print("PILOT DOWNLOAD COMPLETE")
