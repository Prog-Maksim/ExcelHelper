import io
import os.path
import re
from urllib.parse import urlparse

from pathlib import Path

import oauthlib.oauth2.rfc6749.errors
import win32api
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


def check_url(url: str) -> tuple[bool, str]:
    parsed_url = urlparse(url)
    if parsed_url.scheme == "https" and "google.com" in parsed_url.netloc and "spreadsheets" in parsed_url.path:
        id_match = re.search(r'/d/([^/]+)/', url)
        if id_match:
            document_id = id_match.group(1)
            return True, document_id
        else:
            return False, "Идентификатор ссылки не найден"
    else:
        return False, "Данная ссылка не обслуживается"


class GoogleDriveClass:
    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/drive"]
        self.creds = None

    def check_auth(self):
        if os.path.exists("PersonData/person_token.json"):
            self.creds = Credentials.from_authorized_user_file("PersonData/person_token.json", self.SCOPES)
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            return True
        else:
            result = win32api.MessageBox(0, 'Чтобы скачать файл с Google drive требуется авторизоваться.\n'
                                            'Хотите авторизоваться?', 'ExcelHepler - авторизация', 4)

            if result == 6:
                res = self.authorization()
                if res:
                    self.check_auth()
                else:
                    return False
            else:
                return False

    def authorization(self) -> bool:
        """
        Авторизуем пользователя
        :return: результат авторизации
        """
        try:
            flow = InstalledAppFlow.from_client_secrets_file("PersonData/Credentials.json", self.SCOPES)
            self.creds = flow.run_local_server(port=0)
            with open("PersonData/person_token.json", "w") as token:
                token.write(self.creds.to_json())
            return True
        except oauthlib.oauth2.rfc6749.errors.AccessDeniedError:
            return False

    def create_folder(self, folder_name: str) -> str:
        """
        Создает папку на облачном хранилище в Google drive
        :param folder_name: название создаваемой папки
        :return: идентификатор созданной папки
        """
        try:
            service = build("drive", "v3", credentials=self.creds)
            file_metadata = {
                "name": folder_name,
                "mimeType": "application/vnd.google-apps.folder",
            }
            file = service.files().create(body=file_metadata, fields="id").execute()
            return file.get("id")

        except HttpError as error:
            print(f"An error occurred: {error}")
            return ""

    def check_exists_folder(self, folder_name: str = "ExcelHelperFolder") -> str:
        """
        Проверяет наличие папки на облачном хранилище Google drive и возвращает идентификатор данной папки
        :param folder_name: название папки
        :return: идентификатор папки
        """
        try:
            service = build("drive", "v3", credentials=self.creds)
            while True:
                response = (
                    service.files()
                    .list(
                        q=f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}'",
                        spaces="drive",
                        fields="files(id, name)",
                    )
                    .execute()
                )

                if not response.get("files", []):
                    return self.create_folder(folder_name)

                for file in response.get("files", []):
                    return file.get("id")

        except HttpError as error:
            print(f"An error occurred: {error}")

    def create_file_folder(self, file_name: Path, folder_id: str) -> str:
        """
        Загружает файл на облачное хранилище Google Drive
        :param file_name: путь до файла
        :param folder_id: идентификатор папки на google drive
        :return: ссылка на созданный файл.
        """

        suffix_file = {
            "xls": 'application/vnd.ms-excel',
            "xlsx": 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        }

        try:
            service = build("drive", "v3", credentials=self.creds)

            file_metadata = {"name": file_name.stem, "parents": [folder_id]}
            media = MediaFileUpload(file_name, mimetype=suffix_file.get(file_name.suffix), resumable=True)
            file = (
                service.files()
                .create(body=file_metadata, media_body=media, fields="id")
                .execute()
            )
            return f"https://docs.google.com/spreadsheets/d/{file.get('id')}/"

        except HttpError:
            return None

    def __get_file_name(self, file_id: str) -> Path:
        """
        Получение имени файла по идентификатору файла с облачного хранилища Google Drive
        :param file_id: идентификатор файла
        :return: название файла.
        """
        try:
            drive_service = build('drive', 'v3', credentials=self.creds)
            file_metadata = drive_service.files().get(fileId=file_id).execute()
            return Path("ProcessingFiles/" + file_metadata.get('name'))
        except HttpError as error:
            return str(error)

    def download_file(self, file_id: str) -> tuple[bool, str]:
        """
        Скачивание файла с облачного хранилища google drive
        :param file_id: идентификатор файла
        :return: статус выполнения, сообщение.
        """
        file_name = self.__get_file_name(file_id)
        try:
            drive_service = build('drive', 'v3', credentials=self.creds)

            request = drive_service.files().get_media(fileId=file_id)
            fh = io.FileIO(file_name, mode='wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()

            return True, str(file_name)
        except HttpError as error:
            return False, str(error)
        except PermissionError:
            if os.path.exists(file_name.name):
                os.remove(file_name.name)
            self.download_file(file_id)
