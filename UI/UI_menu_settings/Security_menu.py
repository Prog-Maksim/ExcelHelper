import tkinter as tk

import customtkinter as ctk

from UI.UI_menu_settings.Base_frame import BaseMenu


class DropDownMenu(ctk.CTkFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configure(width=380, height=140, corner_radius=15)

        self.__start()

    def __start(self):
        self.grid_columnconfigure(index=0, weight=0)

        self.grid_rowconfigure(index=0, weight=0)
        label = ctk.CTkLabel(
            master=self,
            justify="left",
            text="""Защита изменения структуры таблицы - запрещает 
создавать, переименовывать, удалять листы итд

Защита отслеживания истории изменения - скрывает 
историю показа изменения таблицы

Защита листа от изменения - запрещает изменять 
ячейки в таблице""",
            text_color=("black", "white"),
            font=("Montserrat", 13, "bold")
        )
        label.place(x=5, y=5)


class SecurityMenu(BaseMenu):
    def __init__(self, scrollview, position: int, **kwargs):
        super().__init__(path_image='Image/settings-5-image.png', color=("#FFCECE", "#5D3434"), **kwargs)

        self.dropdown_menu = False
        self.scrollview = scrollview
        self.position = position

        self.__start()

    def __start(self):
        self.button.configure(command=lambda: self.processing_menu())
        self.main_label.configure(text="Безопасность")
        self.description.configure(text="Информация о том как обезопасить\nконфидициальные данные")

    def processing_menu(self):
        if self.dropdown_menu:
            self.delete_dropdown_menu()
            self.dropdown_menu = False
        else:
            self.create_dropdown_menu()
            self.dropdown_menu = True

    def create_dropdown_menu(self):
        self.drop_down_menu = DropDownMenu(master=self.scrollview, fg_color=("#FFF0F0", "#3E2C2C"))
        self.drop_down_menu.grid(row=self.position+1, column=0, pady=(0, 5))

    def delete_dropdown_menu(self):
        self.drop_down_menu.destroy()
