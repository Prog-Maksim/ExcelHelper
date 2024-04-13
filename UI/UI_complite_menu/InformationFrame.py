import tkinter as tk

from PIL import Image
import customtkinter as ctk


class InformationFrame(ctk.CTkFrame):
    def __init__(self, data: dict, **kwargs):
        super().__init__(**kwargs)

        self.data = data
        self.configure(height=80, fg_color=("#FFF1DA", "#50442F"), corner_radius=15)
        self.__start()

    def __start(self):
        self.grid_rowconfigure(index=0, weight=0)

        self.grid_columnconfigure(index=0, weight=0)
        image = ctk.CTkImage(
            dark_image=Image.open('Image/information-image.png'),
            light_image=Image.open('Image/information-image.png'),
            size=(65, 65))

        self.icon_label = ctk.CTkLabel(
            master=self,
            image=image,
            text=""
        )
        self.icon_label.grid(row=0, column=0, sticky=tk.N, padx=5, pady=5)

        self.grid_columnconfigure(index=1, weight=0)
        self.grid_rowconfigure(index=0, weight=1)
        self.label_1 = ctk.CTkLabel(
            master=self,
            font=("Montserrat", 15, "bold"),
            text=f"Найдено и обработано: {self.data['Information']['all-processing']} элементов",
            text_color=("black", "white")
        )
        self.label_1.grid(row=0, column=1, sticky=tk.NW, pady=(15, 0))

        self.label_1 = ctk.CTkLabel(
            master=self,
            height=10,
            font=("Montserrat", 12, "bold"),
            text=f"из них {self.data['Information']['same-values']} одинаковых значений",
            text_color="#808080"
        )
        self.label_1.grid(row=0, column=1, sticky=tk.SW, pady=(0, 23))
