import json
import os
import tkinter as tk

import customtkinter as ctk
from PIL import Image

from logic import UpdateTheme
from UI.UI_menu_settings.Base_frame import BaseMenu


class ButtonMenu(ctk.CTkButton):
    def __init__(self, image: list, button_click, pos: int, **kwargs):
        super().__init__(**kwargs)

        image = ctk.CTkImage(
            light_image=Image.open(image[0]),
            dark_image=Image.open(image[1]),
            size=(25, 25))

        self.configure(
            width=370, height=50,
            corner_radius=10,
            compound="left",
            image=image,
            anchor=tk.W,
            text_color=("black", "white"),
            fg_color="transparent",
            hover_color=("#FEFFC6", "#656643"),
            command=lambda: button_click(pos)
        )
        self.__start()

    def __start(self):
        pass


class DropDownMenu(ctk.CTkFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configure(width=380, height=200, corner_radius=15)

        self.__start()

    def __start(self):
        self.data_image = {
            "Всегда светлый": ["Image/light.png", "Image/light_1.png", 0],
            "Всегда темный": ["Image/dark.png", "Image/dark_1.png", 1],
            "Как в системе": ["Image/system.png", "Image/system_1.png", 2]
        }

        for num, item in enumerate(["Всегда светлый", "Всегда темный", "Как в системе"], start=0):
            self.grid_rowconfigure(index=num, weight=0)
            button_1 = ButtonMenu(master=self, text=item, image=self.data_image.get(item), button_click=self.button_click, pos=num)
            button_1.grid(row=num, column=0, pady=5, padx=5)

        self.loading_theme()

    def loading_theme(self):
        if os.path.exists("PersonData/person_data.json"):
            with open("PersonData/person_data.json", "r", encoding="utf-8") as file:
                data = dict(json.load(file)).get("theme")
                data_pos = {"light": 0, "dark": 1, "system": 2}
                self.button_click(index=data_pos.get(data))

    def button_click(self, index: int):
        if hasattr(self, "label"):
            self.label.destroy()

        image = ctk.CTkImage(
            light_image=Image.open('Image/check_black.png'),
            dark_image=Image.open('Image/check_white.png'),
            size=(25, 25))

        self.grid_rowconfigure(index=index, weight=0)
        self.label = ctk.CTkLabel(
            master=self,
            image=image,
            bg_color="transparent",
            fg_color="transparent",
            text=""
        )
        self.label.grid(row=index, column=0, sticky="e", padx=(0, 15))

        data_pos = {0: "light", 1: "dark", 2: "system"}
        UpdateTheme.update_theme(data_pos.get(index))


class ThemeMenu(BaseMenu):
    def __init__(self, scrollview, position: int, **kwargs):
        super().__init__(path_image='Image/settings-4-image.png', color=("#FEFFC6", "#656643"), **kwargs)

        self.dropdown_menu = False
        self.scrollview = scrollview
        self.position = position

        self.__start()

    def __start(self):
        self.button.configure(command=lambda: self.processing_menu())
        self.main_label.configure(text="Тема программы")
        self.description.configure(text="Сделайте программу более удобной")

    def processing_menu(self):
        if self.dropdown_menu:
            self.delete_dropdown_menu()
            self.dropdown_menu = False
        else:
            self.create_dropdown_menu()
            self.dropdown_menu = True

    def create_dropdown_menu(self):
        self.drop_down_menu = DropDownMenu(master=self.scrollview, fg_color=("#FEFFE4", "#3C3C2E"))
        self.drop_down_menu.grid(row=self.position+1, column=0, pady=(0, 5))

    def delete_dropdown_menu(self):
        self.drop_down_menu.destroy()
