from UI.UI_menu_settings.Base_frame import BaseMenu, DropDownMenu


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
