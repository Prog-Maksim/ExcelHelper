import customtkinter as ctk

from UI.main_windows import MainWindows
from UI.settings_windows import SettingsWindow

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("PersonData/green.json")


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.windows_size = (415, 700)
        self.monitor_height = self.winfo_screenheight()
        self.monitor_width = self.winfo_screenwidth()

        x = int((self.monitor_width - self.windows_size[0]) / 2)
        y = int((self.monitor_height - self.windows_size[1]) / 2)

        self.geometry(f'{self.windows_size[0]}x{self.windows_size[1]}+{x}+{y}')
        self.resizable(False, False)
        self.title('ExcelHelper')

        self.start()

    def start(self):
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        self.open_base_menu()

    def open_base_menu(self):
        if hasattr(self, 'settings_frame'):
            self.settings_frame.destroy()

        self.main_frame = MainWindows(master=self, base=self)
        self.main_frame.grid(row=0, column=0, sticky='nsew')

    def open_settings(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()

        self.settings_frame = SettingsWindow(master=self, base=self)
        self.settings_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == '__main__':
    app = Window()
    app.mainloop()
