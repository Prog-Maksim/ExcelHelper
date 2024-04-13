import tkinter as tk

from PIL import Image
import customtkinter as ctk


class ExcelHelperFrame(ctk.CTkFrame):
    def __init__(self, data: dict, **kwargs):
        super().__init__(**kwargs)

        self.data = data
        self.configure(height=80, fg_color=("#D2EDFF", "#44686B"), corner_radius=15)
        self.__start()

    def __start(self):
        self.grid_rowconfigure(index=0, weight=0)

        self.grid_columnconfigure(index=0, weight=0)
        image = ctk.CTkImage(
            dark_image=Image.open('Image/file-image.png'),
            light_image=Image.open('Image/file-image.png'),
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
            height=10,
            font=("Montserrat", 12),
            text="Наименование",
            text_color="#808080"
        )
        self.label_1.grid(row=0, column=1, sticky=tk.NW, pady=(13, 0))

        self.label_2 = ctk.CTkLabel(
            master=self,
            height=5,
            font=("Montserrat", 17, "bold"),
            text=self.data["ExcelHelper"]["Name"],
            text_color=("black", "white")
        )
        self.label_2.grid(row=0, column=1, sticky=tk.NW, pady=(25, 0))

        self.label_3 = ctk.CTkLabel(
            master=self,
            height=10,
            font=("Montserrat", 12),
            text=self.data["ExcelHelper"]["Datetime"].strftime("%d %B %Y года"),
            text_color="#808080"
        )
        self.label_3.grid(row=0, column=1, sticky=tk.SE, padx=(0, 5), pady=(0, 8))

        self.label_3 = ctk.CTkLabel(
            master=self,
            height=10,
            font=("Montserrat", 12),
            text=f"Размер: {self.data['ExcelHelper']['Weight']} кб",
            text_color="#808080"
        )
        self.label_3.grid(row=0, column=1, sticky=tk.SW, pady=(0, 8))
