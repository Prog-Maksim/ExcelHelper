import tkinter as tk

import customtkinter as ctk

from UI.UI_menu_settings.Base_frame import BaseMenu, DropDownMenu


class ProcessingMenu(BaseMenu):
    def __init__(self, scrollview, position: int, **kwargs):
        super().__init__(path_image='Image/settings-1-image.png', color=("#DCE4FF", "#384264"), **kwargs)

        self.dropdown_menu = False
        self.scrollview = scrollview
        self.position = position

        self.__start()

    def __start(self):
        self.button.configure(command=lambda: self.processing_menu())
        self.main_label.configure(text="Обработанные файлы")
        self.description.configure(text="История обработанных вами файлов")

    def processing_menu(self):
        if self.dropdown_menu:
            self.delete_dropdown_menu()
            self.dropdown_menu = False
        else:
            self.create_dropdown_menu()
            self.dropdown_menu = True

    def create_dropdown_menu(self):
        self.drop_down_menu = DropDownMenu(master=self.scrollview, fg_color=("#ECF1FF", "#2C3140"))
        self.drop_down_menu.grid(row=self.position+1, column=0, pady=(0, 5))

    def delete_dropdown_menu(self):
        self.drop_down_menu.destroy()
