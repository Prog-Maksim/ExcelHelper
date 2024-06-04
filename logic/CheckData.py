import os.path

from UI import main_windows
from logic import ProcessingFile

from pathlib import Path

from logic.GoogleDrive import GoogleDriveClass, check_url


class check_data:
    def __init__(self, main_data: main_windows):
        self.main_data = main_data
        self.__start()

    def __start(self):
        file_path: Path = self.main_data.entry_frame_1.get_text()
        self.method: tuple[int, Path] = self.main_data.radiobutton_frame.get()
        print(self.method, file_path)

        if str(file_path) == ".":
            self.main_data.create_information(
                error=True,
                message="Данное поле обязательно к заполнению",
                error_frame=self.main_data.entry_frame_1
            )
            return
        elif str(file_path)[:5] == "https":
            drive = GoogleDriveClass()
            result = drive.check_auth()

            if not result:
                self.main_data.create_information(
                    error=True,
                    message='Невозможно скачать данный файл',
                    error_frame=self.main_data.entry_frame_1
                )
                return

            id = str(check_url(str(file_path))[1])
            res = drive.download_file(file_id=id)
            if res[0]:
                file_path = Path(res[1])
            else:
                self.main_data.create_information(
                    error=True,
                    message=res[1],
                    error_frame=self.main_data.entry_frame_1
                )
                return

        if file_path.exists():
            self.security = self.main_data.checkbox_frame.get()
            self.password = self.main_data.entry_frame_3.get_text()

            if self.security and self.password == "":
                self.main_data.create_information(
                    error=True,
                    message="Поле пароль не заполнено",
                    error_frame=self.main_data.entry_frame_3
                )
                return

            if self.method[0] != 3:
                self.__start_processing_file_local(save_path=self.method[1], file_path=file_path)
            else:
                self.__start_processing_file(save_path=self.method[1], file_path=file_path)
        else:
            self.main_data.create_information(
                error=True,
                message="Выбранный вами файл не найден",
                error_frame=self.main_data.entry_frame_1
            )

    def __start_processing_file(self, file_path: Path, save_path: Path) -> None:
        result_save = ProcessingFile.processing_file(
            file_path=file_path,
            save_path=save_path,
            security=self.security,
            password=self.password
        ).start()

        if result_save["success"]:
            drive = GoogleDriveClass()
            result = drive.check_auth()

            if not result:
                self.main_data.create_information(
                    error=True,
                    message='Невозможно сохранить обработанный файл',
                    error_frame=self.main_data.entry_frame_1
                )
                return

            folder_id = drive.check_exists_folder()
            file_id = drive.create_file_folder(file_name=save_path, folder_id=folder_id)
            result_save["data"]["GoogleDrive"] = {"folder_id": f"https://drive.google.com/drive/u/0/folders/{folder_id}", "file_url": file_id}

            self.main_data.base.open_complete_menu(data=result_save)

            if save_path.exists():
                os.remove(save_path)
        else:
            self.main_data.create_information(
                error=True,
                message=result_save["Error"],
            )

        if os.path.exists(save_path):
            os.remove(save_path)

    def __start_processing_file_local(self, save_path: Path, file_path: Path):
        result = ProcessingFile.processing_file(
            file_path=file_path,
            save_path=save_path,
            security=self.security,
            password=self.password
        ).start()

        if result["success"]:
            self.main_data.base.open_complete_menu(data=result)
        else:
            self.main_data.create_information(
                error=True,
                message=result["Error"],
            )
