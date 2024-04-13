import tkinter as tk

from PIL import Image
import customtkinter as ctk


class SecurityFrame(ctk.CTkFrame):
    def __init__(self, status: bool, **kwargs):
        super().__init__(**kwargs)

        self.status = status
        self.configure(height=80, fg_color=("#DDFFE6", "#4D5C48") if self.status else ("#FFDBD4", "#5C3F3F"), corner_radius=15)
        self.__start()

    def __start(self):
        self.grid_rowconfigure(index=0, weight=0)

        self.grid_columnconfigure(index=0, weight=0)
        image_1 = ctk.CTkImage(
            dark_image=Image.open('Image/security-image.png'),
            light_image=Image.open('Image/security-image.png'),
            size=(65, 65))

        image_2 = ctk.CTkImage(
            dark_image=Image.open('Image/red-secure-image.png'),
            light_image=Image.open('Image/red-secure-image.png'),
            size=(65, 65))

        self.icon_label = ctk.CTkLabel(
            master=self,
            image=image_1 if self.status else image_2,
            text=""
        )
        self.icon_label.grid(row=0, column=0, sticky=tk.N, padx=5, pady=5)

        self.grid_columnconfigure(index=1, weight=0)
        self.grid_rowconfigure(index=0, weight=1)
        self.label_1 = ctk.CTkLabel(
            master=self,
            font=("Montserrat", 15, "bold"),
            text="Файл защищен" if self.status else "Файл не защищен",
            text_color="#159700" if self.status else "#E61522"
        )
        self.label_1.grid(row=0, column=1, sticky=tk.NW, pady=(15, 0))

        self.label_1 = ctk.CTkLabel(
            master=self,
            height=10,
            font=("Montserrat", 12, "bold"),
            text="дополнительная защита не требуется" if self.status else "конфидициальные данные под угрозой!",
            text_color="#808080"
        )
        self.label_1.grid(row=0, column=1, sticky=tk.SW, pady=(0, 23))
