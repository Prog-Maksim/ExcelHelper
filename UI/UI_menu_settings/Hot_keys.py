import math
import tkinter as tk

import customtkinter as ctk
from PIL import Image

from UI.UI_menu_settings.Base_frame import BaseMenu


class KeysMenu(ctk.CTkFrame):
    def __init__(self, name: str, description: str, **kwargs):
        super().__init__(**kwargs)

        self.configure(fg_color="transparent", corner_radius=15, width=180, height=40)
        self.name = name
        self.description = description

        self.__start()

    def __start(self):
        self.grid_columnconfigure(index=0, weight=0)
        image = ctk.CTkImage(
            light_image=Image.open("Image/ctrl-image.png"),
            dark_image=Image.open("Image/ctrl-image.png"),
            size=(35, 35))

        label_image = ctk.CTkLabel(
            master=self,
            text="",
            image=image
        )
        label_image.grid(row=0, column=0, rowspan=2, sticky=tk.NSEW, padx=5, pady=5)

        self.grid_columnconfigure(index=1, weight=0)
        self.grid_rowconfigure(index=0, weight=0)
        label = ctk.CTkLabel(
            master=self,
            height=10,
            text=self.name,
            text_color=("black", "white"),
            font=("Montserrat", 11, "bold")
        )
        label.grid(row=0, column=1, pady=(5, 0), sticky=tk.W, padx=(0, 5))

        self.grid_rowconfigure(index=1, weight=0)
        description = ctk.CTkLabel(
            master=self,
            width=135, height=10,
            text=self.description,
            text_color="#808080",
            anchor=tk.W,
            font=("Montserrat", 10, "bold")
        )
        description.grid(row=1, column=1, pady=(0, 5), sticky=tk.W, padx=(0, 5))


class DropDownMenu(ctk.CTkFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configure(width=380, height=200, corner_radius=15)

        self.__start()

    def __start(self):
        hot_keys = [
            {
                "name": "Ctrl + W",
                "description": "Меню выбора файла"
            },
            {
                "name": "Enter",
                "description": "Запуск обработки файла"
            },
            {
                "name": "Ctrl + Q",
                "description": "Открытие/закрытие настроек"
            },
            {
                "name": "Ctrl + D",
                "description": "Установка темной темы"
            },
            {
                "name": "Ctrl + L",
                "description": "Установка светлой темы"
            },
            {
                "name": "Ctrl + S",
                "description": "Тема как в системе"
            },
            {
                "name": "Ctrl + X",
                "description": "Способ сохранения"
            },
            {
                "name": "Ctrl + F",
                "description": "Формат файла"
            },
            {
                "name": "Ctrl + R",
                "description": "Показать/Скрыть пароль"
            },
        ]

        number = len(hot_keys) / 2
        max_row = math.ceil(number)
        min_row = math.floor(number)
        size_row = max_row
        curr_frame = 0

        for column in range(2):
            for row in range(size_row):
                self.grid_columnconfigure(index=column, weight=0)
                self.grid_rowconfigure(index=column, weight=0)
                menu = KeysMenu(master=self, name=hot_keys[curr_frame].get("name"), description=hot_keys[curr_frame].get("description"))
                menu.grid(row=row, column=column, padx=2, pady=3)
                curr_frame += 1
            size_row = min_row


class HotKeys(BaseMenu):
    def __init__(self, scrollview, position: int, **kwargs):
        super().__init__(path_image='Image/settings-2-image.png', color=("#D1C1FF", "#413959"), **kwargs)

        self.dropdown_menu = False
        self.scrollview = scrollview
        self.position = position

        self.__start()

    def __start(self):
        self.button.configure(command=lambda: self.processing_menu())
        self.main_label.configure(text="Горячие клавиши")
        self.description.configure(text="Весь список горячих клавиш для\nбыстрой работе с программой")

    def processing_menu(self):
        if self.dropdown_menu:
            self.delete_dropdown_menu()
            self.dropdown_menu = False
        else:
            self.create_dropdown_menu()
            self.dropdown_menu = True

    def create_dropdown_menu(self):
        self.drop_down_menu = DropDownMenu(master=self.scrollview, fg_color=("#F3EFFF", "#332F40"))
        self.drop_down_menu.grid(row=self.position+1, column=0, pady=(0, 5))

    def delete_dropdown_menu(self):
        self.drop_down_menu.destroy()