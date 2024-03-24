import tkinter as tk

import customtkinter as ctk
from PIL import Image

from FunctionFrame import Checkbox_frame, Entry_frame, Information_frame, Radiobutton_frame
from logic import CheckData


class MainWindows(ctk.CTkFrame):
    def __init__(self, base, **kwargs):
        super().__init__(**kwargs)

        self.base = base
        self.__start()

    def create_information(self, error: bool, message: str, error_frame: Entry_frame = None):
        self.grid_rowconfigure(1, weight=0)
        frame = Information_frame.InformationFrame(error=error, message=message, error_frame=error_frame, master=self, height=30)
        frame.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=(0, 5))

    def __start(self):
        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)
        #region MainTitle
        title_frame = ctk.CTkFrame(
            master=self,
            height=100,
            fg_color="transparent"
        )
        title_frame.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)

        version_title = ctk.CTkLabel(
            master=title_frame,
            text_color="gray40",
            text="V 2.0.0",
            font=("Montserrat", 10, "bold")
        )
        version_title.place(x=278, y=20, anchor=tk.CENTER)

        path_image_1 = ctk.CTkImage(
            light_image=Image.open('Image/settings-image_black.png'),
            dark_image=Image.open('Image/settings-image_white.png'),
            size=(25, 25))

        self.button_frame = ctk.CTkButton(
            master=self,
            width=40, height=40,
            fg_color="transparent",
            text="",
            bg_color="transparent",
            image=path_image_1,
            hover=False,
            command=lambda: self.base.open_settings()
        )
        self.button_frame.place(anchor=tk.NW, rely=0.05, relx=0.85)

        title_font = ctk.CTkFont(family="Montserrat", size=30, weight="bold")
        title_label = ctk.CTkLabel(
            master=title_frame,
            text_color=("black", "white"),
            bg_color="transparent",
            text="ExcelHelper",
            font=title_font
        )
        title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        description_title = ctk.CTkLabel(
            master=title_frame,
            text_color="gray40",
            text="мгновенно обрабатывайте файлы",
            font=("Montserrat", 15, "bold")
        )
        description_title.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        #endregion

        self.grid_rowconfigure(2, weight=0)
        #region PathEntry
        self.entry_frame_1 = Entry_frame.EntryFrame(
            title="Путь к обрабатываемому файлу",
            base=self,
            placeholder_text="C:/ или https://",
            master=self,
            height=60,
            fg_color="transparent"
        )
        self.entry_frame_1.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=10)
        #endregion

        self.grid_rowconfigure(3, weight=0)
        #region FileEntry
        self.entry_frame_2 = Entry_frame.EntryFrame(
            title="Новое имя файла",
            base=self,
            placeholder_text="file_processing_result",
            file=True,
            master=self,
            height=60,
            fg_color="transparent"
        )
        self.entry_frame_2.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=10)
        #endregion

        self.grid_rowconfigure(4, weight=0)
        # region RadioButtonFrame
        self.radiobutton_frame = Radiobutton_frame.RadioButtonFrame(
            title="Способ сохранения",
            values=["Сохранить по умолчанию", "Сохранить как новое", "Сохранить на google sheets"],
            master=self,
            file_path=self.entry_frame_2,
            height=350,
            fg_color="transparent"
        )
        self.radiobutton_frame.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=10)
        # endregion

        self.grid_rowconfigure(5, weight=0)
        # region CheckboxFrame
        self.checkbox_frame = Checkbox_frame.CheckBoxFrame(
            title="Защита данных",
            values=["Защита изменения структуры таблицы", "Защита отслеживания истории изменения", "Защита листа от изменения"],
            master=self,
            height=350,
            fg_color="transparent"
        )
        self.checkbox_frame.grid(row=5, column=0, sticky="nsew", pady=(0, 5), padx=10)
        # endregion

        self.grid_rowconfigure(6, weight=0)
        # region PasswordEntry
        self.entry_frame_3 = Entry_frame.EntryFrame(
            title="Пароль для защиты таблицы",
            base=self,
            placeholder_text="aA-zZ 0-9 итд",
            password=True,
            master=self,
            height=60,
            fg_color="transparent"
        )
        self.entry_frame_3.grid(row=6, column=0, sticky="nsew", pady=(0, 5), padx=10)
        # endregion

        self.grid_rowconfigure(7, weight=1)
        # region MainButton
        self.main_button = ctk.CTkButton(
            master=self,
            width=300, height=60,
            text="Обработать",
            text_color=("black", "white"),
            font=("Montserrat", 20, "bold"),
            corner_radius=15,
            command=lambda: CheckData.check_data(main_data=self)
        )
        self.main_button.grid(row=7, column=0, padx=57, sticky="w")
        # endregion
