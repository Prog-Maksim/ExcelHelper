import customtkinter as ctk
from PIL import Image

from UI_menu_settings import Google_account, Hot_keys, Processing_menu, Program_menu, Security_menu, Theme_menu, Description_menu


class SettingsWindow(ctk.CTkFrame):
    def __init__(self, base, **kwargs):
        super().__init__(**kwargs)

        self.base = base
        self.__start()

    def __start(self):
        self.grid_columnconfigure(0, weight=1)

        #region HeadMenu
        self.grid_rowconfigure(0, weight=0)
        main_label = ctk.CTkLabel(
            master=self,
            text="Настройки",
            text_color=("black", "white"),
            font=("Montserrat", 30, 'bold')
        )
        main_label.grid(row=0, column=0, sticky="n")

        path_image_1 = ctk.CTkImage(
            light_image=Image.open('Image/left-arrow.png'),
            dark_image=Image.open('Image/left-arrow.png'),
            size=(25, 25))

        self.button_frame = ctk.CTkButton(
            master=self,
            width=40, height=40,
            fg_color="transparent",
            text="",
            bg_color="transparent",
            image=path_image_1,
            hover=False,
            command=lambda: self.base.open_base_menu()
        )
        self.button_frame.grid(row=0, rowspan=2, column=0, sticky="w", padx=10, pady=10)

        self.grid_rowconfigure(1, weight=0)
        description_label = ctk.CTkLabel(
            master=self,
            text="Работайте с комфортом",
            text_color="#808080",
            font=("Montserrat", 15, 'bold')
        )
        description_label.grid(row=1, column=0, sticky="n")
        # endregion

        self.grid_rowconfigure(index=2, weight=1)
        scrollview = ctk.CTkScrollableFrame(
            master=self,
            fg_color="transparent",
            scrollbar_button_hover_color=("gray80", "gray30"),
            scrollbar_button_color=("gray90", "gray20"),
        )
        scrollview.grid(row=2, column=0, sticky="nsew", pady=(5, 0))

        menu_1 = Processing_menu.ProcessingMenu(master=scrollview, scrollview=scrollview, position=0)
        menu_1.grid(row=0, column=0, pady=(0, 5))

        menu_2 = Hot_keys.HotKeys(master=scrollview, scrollview=scrollview, position=2)
        menu_2.grid(row=2, column=0, pady=(0, 5))

        menu_3 = Google_account.GoogleAccount(master=scrollview, scrollview=scrollview, position=4)
        menu_3.grid(row=4, column=0, pady=(0, 5))

        menu_4 = Theme_menu.ThemeMenu(master=scrollview, scrollview=scrollview, position=6)
        menu_4.grid(row=6, column=0, pady=(0, 5))

        menu_5 = Security_menu.SecurityMenu(master=scrollview, scrollview=scrollview, position=8)
        menu_5.grid(row=8, column=0, pady=(0, 5))

        menu_6 = Program_menu.ProgramMenu(master=scrollview, scrollview=scrollview, position=10)
        menu_6.grid(row=10, column=0, pady=(0, 5))

        menu_7 = Description_menu.DescriptionMenu(master=scrollview)
        menu_7.grid(row=12, column=0, pady=(0, 5))
