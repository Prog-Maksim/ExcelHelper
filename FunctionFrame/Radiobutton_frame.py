import tkinter as tk
from tkinter import filedialog

import customtkinter as ctk


class RadioButtonFrame(ctk.CTkFrame):
    def __init__(self, title: str, values: list[str], **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.values = values
        self.radio_buttons = []
        self.grid_columnconfigure(0, weight=1)
        self.variable = ctk.IntVar(value=1)
        self.path_name = "ProcessingFile/"

        self.__create_radio_buttons()

    def __create_radio_buttons(self):
        self.title_label = ctk.CTkLabel(
            master=self,
            text=self.title,
            text_color="gray60",
            font=("Montserrat", 12, "bold")
        )
        self.title_label.grid(row=0, column=0, padx=0, sticky="nw")

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=i+1, variable=self.variable,
                                             command=self.__radiobutton_event)
            radiobutton.grid(row=i + 1, column=0, padx=0, pady=(5, 0), sticky="w")
            self.radio_buttons.append(radiobutton)

    def __radiobutton_event(self):
        if self.variable.get() == 2:
            root = tk.Tk()
            root.withdraw()
            filename = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                    filetypes=[('Excel files', ('.xlsx', '.xls', 'csv')),
                                                               ('All files', '*.*')])
            if len(filename) == 0:
                self.set(1)
            else:
                self.path_name = filename

    def get(self) -> tuple:
        return self.variable.get(), self.path_name

    def set(self, value: int):
        self.variable.set(value)
