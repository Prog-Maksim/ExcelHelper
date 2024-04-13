import tkinter as tk
from UI.UI_menu_settings.Base_frame import BaseMenu


class DescriptionMenu(BaseMenu):
    def __init__(self, **kwargs):
        super().__init__(path_image='', color="transparent", **kwargs)
        self.configure(height=100)
        self.__start()

    def __start(self):
        self.description.configure(text="""При работе с конфиденциальными Excel файлами, 
необходимо соблюдать политику конфиденциальности.
Это включает в себя использование паролей для защиты 
файлов, установку ограничений доступа, обеспечение 
безопасности при передаче файлов через сеть, контроль 
использования и управление доступом к файлам.""")
        self.description.place(anchor=tk.CENTER, relx=0.5)
