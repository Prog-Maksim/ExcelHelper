import tkinter as tk

import customtkinter as ctk
from PIL import Image


class BaseMenu(ctk.CTkFrame):
    def __init__(self, path_image: str, color: tuple | str, **kwargs):
        super().__init__(**kwargs)

        self.path_image = path_image
        self.configure(width=390, height=80, corner_radius=15, fg_color=color)
        self.__start()

    def __start(self):
        self.button = ctk.CTkButton(
            master=self,
            width=380, height=70,
            corner_radius=15,
            fg_color="transparent",
            hover=False,
            text="",
        )
        self.button.place(x=5, y=5)

        try:
            self.image = ctk.CTkImage(
                light_image=Image.open(self.path_image),
                dark_image=Image.open(self.path_image),
                size=(50, 50))

            image_label = ctk.CTkLabel(
                master=self,
                width=50, height=50,
                image=self.image,
                text=""
            )
            image_label.place(anchor=tk.NW, rely=0.2, relx=0.85)
        except AttributeError:
            pass

        self.main_label = ctk.CTkLabel(
            master=self,
            text="",
            justify="left",
            text_color=("black", "white"),
            font=("Montserrat", 20, 'bold')
        )
        self.main_label.place(anchor=tk.NW, rely=0.2, relx=0.02)

        self.description = ctk.CTkLabel(
            master=self,
            height=10,
            justify="left",
            text="",
            text_color="#808080",
            font=("Montserrat", 11, 'bold')
        )
        self.description.place(anchor=tk.NW, rely=0.5, relx=0.02)


class DropDownMenu(ctk.CTkFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configure(width=380, height=200, corner_radius=15)
