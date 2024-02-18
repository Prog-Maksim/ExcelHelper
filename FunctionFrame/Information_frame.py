import tkinter as tk

import customtkinter as ctk


class InformationFrame(ctk.CTkFrame):
    def __init__(self, error: bool, message: str, **kwargs):
        super().__init__(**kwargs)
        self.error = error
        self.message = message

        self.__start()

    def __start(self):
        if self.error:
            self.__install_error_frame()
        else:
            self.__install_complete_frame()

        inform_message = ctk.CTkLabel(
            master=self,
            text=self.message,
            text_color="#EF0000" if self.error else ("#508F00", "#86EF00"),
        )
        inform_message.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.after(3000, lambda: self.destroy())

    def __install_error_frame(self):
        self.configure(fg_color=("#FFDED7", "#5D3535"))

    def __install_complete_frame(self):
        self.configure(fg_color=("#C4FFBA", "#365D35"))
