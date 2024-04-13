import tkinter as tk

import customtkinter as ctk

from UI.UI_menu_settings.Base_frame import BaseMenu


class DropDownMenu(ctk.CTkFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configure(width=380, height=160, corner_radius=15)

        self.__start()

    def __start(self):
        label = ctk.CTkLabel(
            master=self,
            justify="left",
            font=("Montserrat", 14, 'bold'),
            text_color=("black", "white"),
            text="""Версия: 2.0.0
Дата выпуска: 18.02.2024
Последнее обновление: 18.02.2024
Разработчик: Белоглазов Максим
Разрешения для программы:
1. Изменение содержимого жесткого диска
2. Чтение данных на жестком диске
3. Загрузка данных в интернет"""
        )
        label.place(anchor=tk.CENTER, relx=0.44, rely=0.5)


class ProgramMenu(BaseMenu):
    def __init__(self, scrollview, position: int, **kwargs):
        super().__init__(path_image='Image/settings-6-image.png', color=("#FFCEF7", "#5A3954"), **kwargs)

        self.dropdown_menu = False
        self.scrollview = scrollview
        self.position = position

        self.__start()

    def __start(self):
        self.button.configure(command=lambda: self.processing_menu())
        self.main_label.configure(text="О программе")
        self.description.configure(text="Подробная информация о\nпрограмме")

    def processing_menu(self):
        if self.dropdown_menu:
            self.delete_dropdown_menu()
            self.dropdown_menu = False
        else:
            self.create_dropdown_menu()
            self.dropdown_menu = True

    def create_dropdown_menu(self):
        self.drop_down_menu = DropDownMenu(master=self.scrollview, fg_color=("#FFEEFC", "#3D2E3A"))
        self.drop_down_menu.grid(row=self.position+1, column=0, pady=(0, 5))

    def delete_dropdown_menu(self):
        self.drop_down_menu.destroy()
