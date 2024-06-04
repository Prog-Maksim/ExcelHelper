import asyncio
from datetime import datetime
import json
import os
import tkinter as tk

import customtkinter as ctk
from PIL import Image
import win32api
import win32con

from UI.UI_menu_settings.Base_frame import BaseMenu
from logic.GoogleDrive import GoogleDriveClass


class DropDownMenu_1(ctk.CTkFrame):
    def __init__(self, base, **kwargs):
        super().__init__(**kwargs)
        self.configure(width=380, height=120, corner_radius=15)

        self.base = base
        self.__start()

    def __start(self):
        self.grid_columnconfigure(index=0, weight=0)

        self.grid_rowconfigure(index=0, weight=0)
        image = ctk.CTkImage(
            light_image=Image.open("Image/settings-3-image.png"),
            dark_image=Image.open("Image/settings-3-image.png"),
            size=(30, 30))
        label = ctk.CTkLabel(
            master=self,
            text="Чтобы загружать и сохранять файлы Excel на Google\nДиске, авторизуйтесь в Google Drive.",
            text_color=("black", "white"),
            font=("Montserrat", 11, "bold"),
            compound="left",
            justify=ctk.LEFT,
            anchor=tk.W,
            image=image
        )
        label.grid(row=0, column=0, pady=10)

        self.grid_rowconfigure(index=1, weight=0)
        button = ctk.CTkButton(
            master=self,
            width=350, height=50,
            text="Авторизоваться",
            corner_radius=10,
            font=("Montserrat", 17, "bold"),
            text_color="white",
            fg_color="#1EA362",
            command=self.auth_person
        )
        button.grid(row=1, column=0, padx=15, pady=(5, 2))

        self.grid_rowconfigure(index=2, weight=0)
        label_description = ctk.CTkLabel(
            master=self,
            text="*Вы будете перенаправлены на сайт https://accounts.google.com/",
            text_color="gray",
            height=5,
            justify=tk.LEFT,
            font=("Montserrat", 10, "bold"),
        )
        label_description.grid(row=3, column=0, padx=15, pady=(0, 5), sticky=tk.W)

    def auth_person(self):
        result = GoogleDriveClass().authorization()

        if result:
            self.base.update_menu()
            win32api.MessageBox(win32con.NULL, 'Вы успешно авторизовались!', 'Excel Helper', win32con.MB_OK)
        else:
            win32api.MessageBox(win32con.NULL, 'Вы не авторизовались!\nПовторите попытку позже...', 'Excel Helper', win32con.MB_OK)


class DropDownMenu_2(ctk.CTkFrame):
    def __init__(self, base, **kwargs):
        super().__init__(**kwargs)

        base_size = 150
        self.base = base
        self.list_frame = list()
        size_h = base_size + 35
        self.configure(width=380, height=size_h, corner_radius=15)

        self.__start()

    def __start(self):
        button = ctk.CTkButton(
            master=self,
            width=350, height=45,
            text="Выйти",
            text_color="white",
            font=("Montserrat", 15, "bold"),
            fg_color=("#1EA362", "#007C3F"),
            command=self.exit_on_account
        )
        button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

    def exit_on_account(self):
        if os.path.exists("PersonData/person_token.json"):
            os.remove("PersonData/person_token.json")

        self.base.update_menu()

    def delete_checked_account(self):
        for frame in self.list_frame:
            result = frame.get_status()
            if result[0]:
                frame.destroy()
                self.delete_account(id=result[1])

    def delete_account(self, id: int):
        with open("PersonData/person_data.json", 'r', encoding="utf-8") as file:
            data = dict(json.load(file))

        for num, item in enumerate(data.get("accounts")):
            if item.get("id") == id:
                del(data.get("accounts")[num])


        with open("PersonData/person_data.json", 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)



class GoogleAccount(BaseMenu):
    def __init__(self, scrollview, position: int, **kwargs):
        super().__init__(path_image='Image/settings-3-image.png', color=("#DCFFCB", "#48663A"), **kwargs)

        self.dropdown_menu = False
        self.scrollview = scrollview
        self.position = position

        self.__start()

    def __start(self):
        self.button.configure(command=lambda: self.processing_menu())
        self.main_label.configure(text="Google Drive")
        self.description.configure(text="Авторизационные данные для\nдоступа к таблице")

    def processing_menu(self):
        if self.dropdown_menu:
            self.delete_dropdown_menu()
            self.dropdown_menu = False
        else:
            self.create_dropdown_menu()
            self.dropdown_menu = True

    def create_dropdown_menu(self):
        if os.path.exists("PersonData/person_token.json"):
            self.drop_down_menu = DropDownMenu_2(master=self.scrollview, fg_color=("#F2FFEC", "#353F31"), base=self)
        else:
            self.drop_down_menu = DropDownMenu_1(master=self.scrollview, fg_color=("#F2FFEC", "#353F31"), base=self)
        self.drop_down_menu.grid(row=self.position+1, column=0, pady=(0, 5))

    def delete_dropdown_menu(self):
        self.drop_down_menu.destroy()

    def update_menu(self):
        self.delete_dropdown_menu()
        self.create_dropdown_menu()
