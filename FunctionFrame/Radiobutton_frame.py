import tkinter as tk
from tkinter import filedialog
from pathlib import Path

import customtkinter as ctk

from FunctionFrame.Entry_frame import EntryFrame


class RadioButtonFrame(ctk.CTkFrame):
    def __init__(self, title: str, values: list[str], file_path: EntryFrame, **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.values = values
        self.radio_buttons = []
        self.grid_columnconfigure(0, weight=1)
        self.variable = ctk.IntVar(value=1)
        self.file_path: EntryFrame = file_path
        self.path_name: Path
        self.base_folder = "ProcessingFiles"

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

    def new_state_radio_button(self):
        if self.variable.get() == 1:
            self.variable.set(2)
            self.__radiobutton_event()
        elif self.variable.get() == 2:
            self.variable.set(3)
        elif self.variable.get() == 3:
            self.variable.set(1)

    def __radiobutton_event(self):
        if self.variable.get() == 2:
            filename = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                    filetypes=[('Excel files', ('.xlsx', '.xls', 'csv')),
                                                               ('All files', '*.*')])
            if len(filename) == 0:
                self.set(1)
            else:
                self.path_name = Path(filename)

    def get(self) -> tuple[int, Path]:
        if self.variable.get() == 1:
            return 1, Path(f"{self.base_folder}/{self.file_path.get_text()}")
        elif self.variable.get() == 2:
            return self.variable.get(), self.path_name
        else:
            return 3, Path(self.file_path.get_text())

    def set(self, value: int):
        self.variable.set(value)
