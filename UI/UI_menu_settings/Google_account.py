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


class AccountFrame(ctk.CTkFrame):
    def __init__(self, name: str, date: str, id: int, **kwargs):
        super().__init__(**kwargs)
        self.configure(fg_color=("#E2FFD4", "#48663A"), corner_radius=5, width=350, height=30)

        self.frame_checked = False
        self.name = name
        self.date = date,
        self.id = id
        self.__start()

    def __start(self):
        self.grid_rowconfigure(index=0, weight=0)
        button = ctk.CTkButton(
            master=self,
            width=340, height=20,
            fg_color="transparent",
            bg_color="transparent",
            text="",
            hover=False,
            command=lambda: self.click_frame()
        )
        button.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.grid_columnconfigure(index=0, weight=1)
        name_account = ctk.CTkLabel(
            master=self,
            height=10,
            text=self.name,
            text_color=("black", "white"),
            font=("Montserrat", 12, "bold")
        )
        name_account.grid(row=0, column=0, padx=(10, 0), sticky=tk.W)

        self.grid_columnconfigure(index=1, weight=0)
        date_account = ctk.CTkLabel(
            master=self,
            height=10,
            text=self.date,
            text_color=("gray", "#BCBCBC"),
            font=("Montserrat", 8)
        )
        date_account.grid(row=0, column=1, padx=(5, 10), sticky=tk.E)

    def click_frame(self):
        self.frame_checked = not self.frame_checked
        if self.frame_checked:
            self.configure(fg_color=("#FFE4E4", "#824848"))
        else:
            self.configure(fg_color=("#E2FFD4", "#48663A"))

    def get_status(self) -> tuple[bool, int]:
        return self.frame_checked, self.id


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
        size_h = base_size + self.calculating_frame_sizes()
        self.configure(width=380, height=size_h, corner_radius=15)

        self.__start()

    def __start(self):
        num = self.read_number_accounts()
        self.grid_columnconfigure(index=0, weight=0)

        self.grid_rowconfigure(index=0, weight=0)
        label = ctk.CTkLabel(
            master=self,
            text="Пользователи:",
            text_color=("black", "white"),
            font=("Montserrat", 15, "bold")
        )
        label.grid(row=0, column=0, columnspan=2, padx=(15, 0), pady=(10, 5), sticky=tk.W)

        self.create_frame()

        self.grid_columnconfigure(index=0, weight=0)
        self.grid_rowconfigure(index=1, weight=0)
        button = ctk.CTkButton(
            master=self,
            width=300, height=45,
            text="Добавить",
            text_color="white",
            font=("Montserrat", 15, "bold"),
            fg_color=("#1EA362", "#007C3F")
        )
        button.grid(row=num+1, column=0, padx=(15, 5), pady=(10, 0))

        self.grid_columnconfigure(index=1, weight=0)
        self.grid_rowconfigure(index=num+1, weight=0)
        image = ctk.CTkImage(
            light_image=Image.open("Image/basket_2.png"),
            dark_image=Image.open("Image/basket_1.png"),
            size=(15, 15))

        button = ctk.CTkButton(
            master=self,
            width=45, height=45,
            text="",
            image=image,
            hover_color=("#BBF79F", "#61874F"),
            border_width=2,
            border_color=("#1EA362", "#00FF82"),
            fg_color=("#D0FFBA", "#48663A"),
            command=lambda: self.delete_checked_account()
        )
        button.grid(row=num+1, column=1, padx=(0, 15), pady=(10, 0))

        self.grid_rowconfigure(index=num+2, weight=0)
        button = ctk.CTkButton(
            master=self,
            width=350, height=35,
            text="Выйти",
            hover_color=("#BBF79F", "#61874F"),
            text_color=("#1EA362", "#00FF82"),
            border_width=2,
            border_color=("#1EA362", "#00FF82"),
            font=("Montserrat", 15, "bold"),
            fg_color=("#D0FFBA", "#48663A"),
            command=self.exit_on_account
        )
        button.grid(row=num+2, column=0, columnspan=2, padx=15, pady=(5, 15))

    def create_frame(self):
        for item, (name, date, id) in enumerate(self.get_name_account(), start=1):
            self.grid_rowconfigure(index=item, weight=0)
            frame = AccountFrame(master=self, name=name, date=date, id=id)
            frame.grid(row=item, column=0, columnspan=2, pady=(0, 5), padx=15)
            self.list_frame.append(frame)

    def update_list_frame(self):
        [i.destroy() for i in self.list_frame]
        self.create_frame()

    def exit_on_account(self):
        if os.path.exists("PersonData/person_token.json"):
            os.remove("PersonData/person_token.json")

        self.base.update_menu()

        with open("PersonData/person_data.json", "r") as file:
            data = dict(json.load(file))
            data.get("accounts").clear()

        with open("PersonData/person_data.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

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


    @staticmethod
    def get_name_account() -> list[tuple[str, str, int]]:
        if os.path.exists("PersonData/person_data.json"):
            with open("PersonData/person_data.json", 'r', encoding="utf-8") as file:
                data = dict(json.load(file)).get("accounts")
                account_data = list()
                for item in data:
                    account_data.append((item.get("name"), item.get("start_date"), item.get("id")))
                if len(account_data) == 0:
                    account_data.append(("Нет пользователей", str(datetime.now().date()), 1))
                return account_data


    def read_number_accounts(self) -> int:
        list_account = self.get_name_account()
        return len(list_account)

    def calculating_frame_sizes(self) -> int:
        number = self.read_number_accounts()
        size_frame = 30
        distance = 5
        size_list_accounts = number * (size_frame + distance)
        return size_list_accounts


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
