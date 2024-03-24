import tkinter as tk
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk
from PIL import Image

from logic.GoogleDrive import check_url
from UI import main_windows


class EntryFrame(ctk.CTkFrame):
    def __init__(self, base: main_windows, title: str, placeholder_text: str, password: bool = False, file: bool = False, **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.placeholder_text = placeholder_text
        self.password = password
        self.file = file

        self.text = ""
        self.url = False
        self.base_windows = base

        self.create_frame()

    def create_frame(self):
        self.title_label = ctk.CTkLabel(
            master=self,
            text=self.title,
            text_color="gray60",
            font=("Montserrat", 12, "bold")
        )
        self.title_label.place(anchor=tk.NW, rely=0.1)

        self.entry = ctk.CTkEntry(
            master=self,
            height=30, width=340,
            font=("Montserrat", 15),
            placeholder_text=self.placeholder_text
        )
        self.entry.place(anchor=tk.NW, rely=0.5)

        if not self.password and not self.file:
            self.after(50, self.__search_url)

        if self.password:
            self.__password_button()
        else:
            if self.file:
                self.__extension_file()
            else:
                self.__path_button()

    def __search_url(self):
        if self.text != self.entry.get():
            self.text = self.entry.get()
            if self.text[:8] == "https://" and len(self.text) >= 15:
                result = check_url(self.text)
                self.url = result[0]
                self.access_url(result)
            else:
                self.base_windows.main_button.configure(state="normal")
                self.entry.configure(fg_color=("#DBDBDB", "#404040"))

        self.after(50, self.__search_url)

    def access_url(self, result: tuple[bool, str]):
        if result[0]:
            self.base_windows.main_button.configure(state="normal")
            self.entry.configure(fg_color=("#D2FFCB", "#365D35"))
        else:
            self.base_windows.main_button.configure(state="disabled")
            self.base_windows.create_information(error=True, message=result[1], error_frame=self)
            self.entry.configure(fg_color=("#FFC9C9", "#5D3535"))

    def __path_button(self):
        path_image_1 = ctk.CTkImage(
            dark_image=Image.open('Image/Dark_path_menu_1.png'),
            light_image=Image.open('Image/Light_path_menu_1.png'),
            size=(20, 20))

        self.button_frame = ctk.CTkButton(
            master=self,
            width=40, height=30,
            fg_color=("#DBDBDB", "#404040"),
            text="",
            bg_color="transparent",
            image=path_image_1,
            hover_color=("#BEBEBE", "#4C4C4C"),
            command=self.__click_path
        )
        self.button_frame.place(anchor=tk.NW, rely=0.5, relx=0.9)

    def __click_path(self):
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename()

        if len(filename) == 0:
            filename = 'Не выбрано'

        self.entry.delete(0, tk.END)
        self.entry.insert(0, filename)

    def __password_button(self):
        self.entry.configure(show='•')

        path_image_2 = ctk.CTkImage(
            dark_image=Image.open('Image/open_password_dark.png'),
            light_image=Image.open('Image/open_password_light.png'),
            size=(20, 20))

        self.button_frame = ctk.CTkButton(
            master=self,
            width=40, height=30,
            fg_color=("#DBDBDB", "#404040"),
            text="",
            bg_color="transparent",
            image=path_image_2,
            hover_color=("#BEBEBE", "#4C4C4C"),
            command=self.__click_password
        )
        self.button_frame.place(anchor=tk.NW, rely=0.5, relx=0.9)

    def __click_password(self):
        path_image_3 = ctk.CTkImage(
            dark_image=Image.open('Image/open_password_dark.png'),
            light_image=Image.open('Image/open_password_light.png'),
            size=(20, 20))
        path_image_4 = ctk.CTkImage(
            light_image=Image.open('Image/close-eye-dark.png'),
            dark_image=Image.open('Image/close-eye-light.png'),
            size=(20, 20))

        if self.entry.cget("show") == "•":
            self.button_frame.configure(image=path_image_4)
            self.entry.configure(show='')
        else:
            self.button_frame.configure(image=path_image_3)
            self.entry.configure(show='•')

    def __extension_file(self):
        self.button_frame = ctk.CTkButton(
            master=self,
            width=40, height=30,
            fg_color=("#DBDBDB", "#404040"),
            text=".xlsx",
            text_color="#808080",
            bg_color="transparent",
            hover_color=("#BEBEBE", "#4C4C4C"),
            command=self.__click_file
        )
        self.button_frame.place(anchor=tk.NW, rely=0.5, relx=0.9)

    def __click_file(self):
        if self.button_frame.cget("text") == ".xlsx":
            self.button_frame.configure(text=".xls")
        elif self.button_frame.cget("text") == ".xls":
            self.button_frame.configure(text=".xlsx")

    def error(self):
        self.entry.configure(border_color=("#D56161", "#943030"))
        self.after(3000, lambda: self.entry.configure(border_color=("#A29797", "#565B5E")))

    def get_text(self) -> Path:
        if self.url:
            return self.entry.get()
        if self.password:
            return self.entry.get()
        if self.file:
            if str(self.entry.get()) == "":
                return Path("file_processing_result" + self.button_frame.cget("text"))
            return Path(self.entry.get() + self.button_frame.cget("text"))
        else:
            return Path(self.entry.get())
