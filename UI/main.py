import json
import os.path

import customtkinter as ctk

from logic import UpdateTheme, CheckData
from UI.main_windows import MainWindows
from UI.settings_windows import SettingsWindow
from complite_processing_file import CompliteProcessingFile

ctk.set_default_color_theme("PersonData/green.json")


def check_person_file_data():
    if os.path.exists("PersonData/person_data.json"):
        with open("PersonData/person_data.json", "r", encoding="utf-8") as file:
            data = dict(json.load(file)).get("theme")
            ctk.set_appearance_mode(data)
    else:
        with open("PersonData/person_data.json", "w", encoding="utf-8") as file:
            date = {
                "theme": "system",
                "processing_files": [],
                "accounts": []
            }
            json.dump(date, file, ensure_ascii=False, indent=4)

    if not os.path.exists("ProcessingFiles"):
        os.mkdir("ProcessingFiles")


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.windows_size = (415, 700)
        self.monitor_height = self.winfo_screenheight()
        self.monitor_width = self.winfo_screenwidth()

        x = int((self.monitor_width - self.windows_size[0]) / 2)
        y = int((self.monitor_height - self.windows_size[1]) / 2)

        self.geometry(f'{self.windows_size[0]}x{self.windows_size[1]}+{x}+{y}')
        self.resizable(False, False)
        self.title('ExcelHelper')

        check_person_file_data()
        self.start()

    def start(self):
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        # настройка цветовой темы
        self.bind("<Control-d>", lambda a: UpdateTheme.update_theme("dark"))
        self.bind("<Control-l>", lambda a: UpdateTheme.update_theme("light"))
        self.bind("<Control-s>", lambda a: UpdateTheme.update_theme("system"))

        # открытие/закрытие настроек
        self.bind("<Control-q>", lambda a: self.open_menu_keys())


        self.open_base_menu()

    def open_menu_keys(self):
        if hasattr(self, 'settings_frame'):
            self.settings_frame.destroy()
            del self.settings_frame
            self.open_base_menu()
        elif hasattr(self, 'main_frame'):
            self.main_frame.destroy()
            del self.main_frame
            self.open_settings()


    def open_base_menu(self):
        if hasattr(self, 'settings_frame'):
            self.settings_frame.destroy()
            del self.settings_frame
        elif hasattr(self, 'frame'):
            try:
                self.frame.destroy()
            except AttributeError:
                pass

        self.main_frame = MainWindows(master=self, base=self)
        self.main_frame.grid(row=0, column=0, sticky='nsew')

        self.bind("<Return>", lambda a: CheckData.check_data(self.main_frame))
        self.bind("<Control-r>", lambda a: self.main_frame.entry_frame_3.click_password())
        self.bind("<Control-f>", lambda a: self.main_frame.entry_frame_2.click_file())
        self.bind("<Control-x>", lambda a: self.main_frame.radiobutton_frame.new_state_radio_button())
        self.bind("<Control-w>", lambda a: self.main_frame.entry_frame_1.click_path())

    def open_settings(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()
            del self.main_frame

        self.settings_frame = SettingsWindow(master=self, base=self)
        self.settings_frame.grid(row=0, column=0, sticky="nsew")

    def open_complete_menu(self, data):
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()

        self.frame = CompliteProcessingFile(master=self, data=data, func=self.open_base_menu)
        self.frame.grid(row=0, column=0, sticky="nsew")


if __name__ == '__main__':
    app = Window()
    app.mainloop()
