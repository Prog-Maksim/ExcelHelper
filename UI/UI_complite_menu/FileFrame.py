import os
import subprocess
import tkinter as tk
import webbrowser

from PIL import Image
import customtkinter as ctk


class FileFrame(ctk.CTkFrame):
    def __init__(self, data: dict, **kwargs):
        super().__init__(**kwargs)

        self.data = data
        self.save = "GoogleDrive" in data.keys()
        self.configure(height=80, fg_color=("#D5E8FE", "#465362"), corner_radius=15)
        self.__start()

    def __start(self):
        self.grid_rowconfigure(index=0, weight=0)

        self.grid_columnconfigure(index=0, weight=0)
        image = ctk.CTkImage(
            dark_image=Image.open('Image/folder-image.png'),
            light_image=Image.open('Image/folder-image.png'),
            size=(65, 65))

        self.icon_label = ctk.CTkLabel(
            master=self,
            image=image,
            text=""
        )
        self.icon_label.grid(row=0, column=0, sticky=tk.N, padx=5, pady=5)

        self.grid_columnconfigure(index=1, weight=1)
        self.grid_rowconfigure(index=0, weight=1)
        self.label_1 = ctk.CTkLabel(
            master=self,
            font=("Montserrat", 12, "bold"),
            text=self.data["Files"]["Path"] if not self.save else self.data["GoogleDrive"]["folder_id"],
            anchor=tk.W,
            text_color=("black", "white")
        )
        self.label_1.grid(row=0, column=1, sticky=tk.NW, pady=(25, 0))

        self.label_1 = ctk.CTkLabel(
            master=self,
            height=10,
            font=("Montserrat", 10, "bold"),
            text="Нахождение",
            text_color="#808080"
        )
        self.label_1.grid(row=0, column=1, sticky=tk.NW, pady=(17, 0))

        self.grid_columnconfigure(index=2, weight=0)
        image1 = ctk.CTkImage(
            dark_image=Image.open('Image/right-arrow.png'),
            light_image=Image.open('Image/right-arrow.png'),
            size=(20, 20))

        self.icon_label = ctk.CTkButton(
            master=self,
            bg_color="transparent",
            fg_color="transparent",
            hover=False,
            width=20, height=60,
            image=image1,
            text="",
            command=self.click
        )
        self.icon_label.grid(row=0, column=2, sticky=tk.E, padx=(0, 2))

    def click(self):
        if not self.save:
            if os.path.exists(self.data["Files"]["Path"]):
                subprocess.Popen(r'explorer /select,"{}"'.format(self.data["Files"]["Path"]))
        else:
            webbrowser.open(self.data["GoogleDrive"]["folder_id"])
