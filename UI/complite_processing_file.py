import os.path
import tkinter as tk
import asyncio
import subprocess
import webbrowser

import customtkinter as ctk
from PIL import Image

from UI.UI_complite_menu import InformationFrame, SecurityFrame, ExcelHelperFrame, FileFrame


class CompliteProcessingFile(ctk.CTkFrame):
    def __init__(self, func, data: dict, **kwargs):
        super().__init__(**kwargs)

        self.data = data["data"]
        self.func = func

        self.__start()

    def __start(self):
        self.grid_columnconfigure(index=0, weight=1)

        self.grid_rowconfigure(index=0, weight=0)
        # region MainTitle
        title_frame = ctk.CTkFrame(
            master=self,
            height=150,
            fg_color="transparent"
        )
        title_frame.grid(row=0, column=0, sticky=tk.NSEW, pady=5, padx=5)

        image = ctk.CTkImage(
            dark_image=Image.open('Image/left-arrow.png'),
            light_image=Image.open('Image/left-arrow.png'),
            size=(20, 20))
        button = ctk.CTkButton(
            master=title_frame,
            width=30, height=30,
            text="",
            image=image,
            hover=False,
            fg_color="transparent",
            command=lambda: self.func()
        )
        button.place(relx=0.05, rely=0.2, anchor=tk.CENTER)

        title_font = ctk.CTkFont(family="Montserrat", size=30, weight="bold")
        title_label = ctk.CTkLabel(
            master=title_frame,
            text_color=("black", "white"),
            bg_color="transparent",
            text="ExcelHelper",
            font=title_font
        )
        title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        description_title = ctk.CTkLabel(
            master=title_frame,
            text_color="#2DAD00",
            text="файл успешно обработан",
            font=("Montserrat", 20, "bold")
        )
        description_title.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        description_text = ctk.CTkLabel(
            master=title_frame,
            text_color="#808080",
            text="Мы также поддерживаем следующие форматы: \n.xlsx,  .xls, google sheet",
            font=("Montserrat", 10, "bold")
        )
        description_text.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        line = ctk.CTkFrame(
            master=title_frame,
            height=2,
            width=300,
            corner_radius=30,
            fg_color=("#E2E2E2", "#454545")
        )
        line.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        # endregion

        self.grid_rowconfigure(index=1, weight=0)
        self.label_text_1 = ctk.CTkLabel(
            master=self,
            text="Информация",
            text_color="#808080",
            font=("Montserrat", 15, 'bold')
        )
        self.label_text_1.grid(row=1, column=0, sticky=tk.W, padx=20, pady=0)

        self.grid_rowconfigure(index=2, weight=0)
        self.menu_1 = InformationFrame.InformationFrame(master=self, data=self.data)
        self.menu_1.grid(row=2, column=0, sticky=tk.NSEW, padx=10, pady=(0, 5))

        self.grid_rowconfigure(index=3, weight=0)
        self.label_text_1 = ctk.CTkLabel(
            master=self,
            text="Безопасность",
            text_color="#808080",
            font=("Montserrat", 15, 'bold')
        )
        self.label_text_1.grid(row=3, column=0, sticky=tk.W, padx=20, pady=0)

        self.grid_rowconfigure(index=4, weight=0)
        self.menu_1 = SecurityFrame.SecurityFrame(master=self, status=self.data["Security"])
        self.menu_1.grid(row=4, column=0, sticky=tk.NSEW, padx=10, pady=(0, 5))

        self.grid_rowconfigure(index=5, weight=0)
        self.label_text_1 = ctk.CTkLabel(
            master=self,
            text="ExcelHelper",
            text_color="#808080",
            font=("Montserrat", 15, 'bold')
        )
        self.label_text_1.grid(row=5, column=0, sticky=tk.W, padx=20, pady=0)

        self.grid_rowconfigure(index=6, weight=0)
        self.menu_1 = ExcelHelperFrame.ExcelHelperFrame(master=self, data=self.data)
        self.menu_1.grid(row=6, column=0, sticky=tk.NSEW, padx=10, pady=(0, 5))

        self.grid_rowconfigure(index=7, weight=0)
        self.label_text_1 = ctk.CTkLabel(
            master=self,
            text="Файл",
            text_color="#808080",
            font=("Montserrat", 15, 'bold')
        )
        self.label_text_1.grid(row=7, column=0, sticky=tk.W, padx=20, pady=0)

        self.grid_rowconfigure(index=8, weight=0)
        self.menu_1 = FileFrame.FileFrame(master=self, data=self.data)
        self.menu_1.grid(row=8, column=0, sticky=tk.NSEW, padx=10, pady=(0, 5))

        self.grid_rowconfigure(index=9, weight=1)
        self.button = ctk.CTkButton(
            master=self,
            width=300, height=60,
            fg_color=("#29C682", "#00AD62"),
            text="Открыть",
            text_color="black",
            corner_radius=15,
            font=("Montserrat", 20, 'bold'),
            command=lambda: asyncio.run(self.open_file())
        )
        self.button.grid(row=9, column=0)

    async def open_file(self):
        if "GoogleDrive" not in self.data.keys():
            if os.path.exists(self.data["Files"]["Path"]):
                subprocess.run([self.data["Files"]["Path"]], shell=True)
        else:
            webbrowser.open(self.data["GoogleDrive"]["file_url"])
