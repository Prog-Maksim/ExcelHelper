import customtkinter as ctk


class CheckBoxFrame(ctk.CTkFrame):
    def __init__(self, title: str, values: list[str],  **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.values = values
        self.checkboxes = []

        self.__create_checkbox()

    def __create_checkbox(self):
        self.title_label = ctk.CTkLabel(
            master=self,
            text=self.title,
            text_color="gray60",
            font=("Montserrat", 12, "bold")
        )
        self.title_label.grid(row=0, column=0, padx=0, sticky="nw")

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=0, pady=(5, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self) -> list:
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
