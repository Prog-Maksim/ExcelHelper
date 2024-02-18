# -*- coding: utf-8 -*-

import sys
import json
import os.path
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

from PIL import Image
import customtkinter as ctk
from cryptography.fernet import Fernet

import file_processing as TEST
from ProgramFrame.main_windows import MainWindows

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


class Create_Excel_Card(ctk.CTkScrollableFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_menu = ctk.CTkFrame(self, fg_color=("#b7b7b7", "#3e3e3e"))
        self.frame_menu.grid(row=0, column=0, padx=0)

        self.entries_obj = list()  # храним  id каждого созданного обьекта
        self.entries_image = list()  # храним  id каждого созданного обьекта
        self.entries_text = list()

        self.create_window()

    def create_window(self) -> None:
        """
        Достает данные обработанных excel документов из файла и вызывает функцию для их создания
        :return: None
        """

        self.frame = ctk.CTkFrame(
            master=self.frame_menu,
            width=325, height=300,
            bg_color=("#b7b7b7", "#3e3e3e"),
            fg_color=("#b7b7b7", "#3e3e3e")
        )
        self.frame.grid(row=0, column=0, padx=0, pady=0)

        if os.path.exists('json files/table.json'):
            with open('json files/table.json', 'r', encoding='utf-8') as file:
                data: dict = dict(json.load(file))

                if len(data) <= 0:
                    self.create_enty(row=0, name='Файлы отсутствуют', data=str(datetime.now().date()), path='')
                    return

            for j, i in enumerate(data, start=0):
                self.create_enty(row=j, name=i, data=data[i]['data'], path=data[i]['file_path'])
        else:
            self.create_enty(row=0, name='Файлы отсутствуют', data=str(datetime.now().date()), path='')

    def create_enty(self, row: int, name: str = None, data: str = None, path: str = None) -> None:
        """
        Создает карточки обработанных excel файлов
        :param row: номер строки на которой создать карточку
        :param name: имя обработанной таблицы
        :param data: дата обработки таблицы
        :param path: путь до обработанной таблицы
        :return: None
        """

        self.image = ctk.CTkImage(dark_image=Image.open('Photo_set/Light_table.png'),
                                  light_image=Image.open('Photo_set/Dark_table.png'),
                                  size=(30, 30))
        self.image_delete = ctk.CTkImage(dark_image=Image.open('Photo_set/Red_table_delete.png'),
                                         light_image=Image.open('Photo_set/Red_table_delete.png'),
                                         size=(30, 30))
        self.export_image = ctk.CTkImage(dark_image=Image.open('Photo_set/export_data_dark.png'),
                                         light_image=Image.open('Photo_set/export_data.png'),
                                         size=(20, 20))
        self.export_image_grey = ctk.CTkImage(Image.open('Photo_set/export_data_gray.png'),
                                              size=(20, 20))

        self.frame_1 = ctk.CTkFrame(
            master=self.frame,
            width=325, height=40,
        )
        self.frame_1.grid(row=row, column=0, padx=2, pady=2)

        self.text_1_button = ctk.CTkButton(
            master=self.frame_1,
            width=160, height=30,
            text=name,
            text_color=('black', 'white'),
            anchor='w',
            bg_color='transparent',
            fg_color='transparent',
            hover=False,
            command=lambda: os.system(f'"{path}"') if os.path.exists(path) else ...
        )
        self.text_1_button.place(x=50, y=5)

        self.text_3 = ctk.CTkLabel(
            master=self.frame_1,
            text=data
        )
        self.text_3.place(x=255, y=5)

        def delete_obj():
            self.entries_obj[row].destroy()
            with open('json files/table.json', 'r', encoding='utf-8') as file:
                data = dict(json.load(file))
                os.remove(data[name]['file_path'])
                data.pop(name, None)
            with open('json files/table.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        self.image_arrow_1 = ctk.CTkButton(
            master=self.frame_1,
            text='',
            width=30, height=30,
            fg_color='transparent',
            bg_color='transparent',
            hover=False,
            image=self.image,
            command=delete_obj
        )
        self.image_arrow_1.place(x=3, y=0)

        self.entries_image.append(self.image_arrow_1)
        self.entries_obj.append(self.frame_1)
        self.entries_text.append(self.text_1_button)

        self.entries_image[row].bind("<Enter>",
                                     lambda event: self.entries_image[row].configure(image=self.image_delete))
        self.entries_image[row].bind("<Leave>", lambda event: self.entries_image[row].configure(image=self.image))

        self.entries_text[row].bind("<Enter>",
                                    lambda event: self.entries_text[row].configure(text_color='gray') if os.path.exists(
                                        path) else self.entries_text[row].configure(text_color='red'))
        self.entries_text[row].bind("<Leave>",
                                    lambda event: self.entries_text[row].configure(text_color=('black', 'white')))


class Create_Additional_Menu(ctk.CTkScrollableFrame):
    """
    Дополнительное меню программы
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_position = [False, False, False, False, False, False, False, False]  # Все окна закрыты

        self.frame_menu = ctk.CTkFrame(self, fg_color=("#b7b7b7", "#3e3e3e"))
        self.frame_menu.grid(row=0, column=0, padx=0)
        self.create_window()

    def create_window(self) -> None:
        """
        Создание дополнительного меню и заполнение необходимыми карточками
        :return: None
        """

        self.frame = ctk.CTkFrame(
            master=self.frame_menu,
            width=265, height=430,
            bg_color=("#b7b7b7", "#3e3e3e"),
            fg_color=("#b7b7b7", "#3e3e3e")
        )
        self.frame.grid(row=0, column=0, padx=0, pady=0)

        self.image_down = ctk.CTkImage(light_image=Image.open('Photo_set/Light_down_arrow.png'),
                                       dark_image=Image.open('Photo_set/Dark_down_arrow.png'),
                                       size=(20, 20))

        self.image_up = ctk.CTkImage(light_image=Image.open('Photo_set/Light_up_arrow.png'),
                                     dark_image=Image.open('Photo_set/Dark_up_arrow.png'),
                                     size=(20, 20))

        self.frame_9 = ctk.CTkFrame(
            master=self.frame,
            width=360, height=40,
        )
        self.frame_9.grid(row=8, column=0, padx=2, pady=2)
        self.text_1 = ctk.CTkLabel(
            master=self.frame_9,
            text='Горячие клавищи'
        )
        self.text_1.place(x=5, y=2)
        self.image_arrow_5 = ctk.CTkButton(
            master=self.frame_9,
            text='',
            width=30, height=30,
            fg_color='transparent',
            bg_color='transparent',
            hover=False,
            image=self.image_down,
            command=self.button_menu_click_5
        )
        self.image_arrow_5.place(x=320, y=8)

        self.frame_11 = ctk.CTkFrame(
            master=self.frame,
            width=360, height=40,
        )
        self.frame_11.grid(row=10, column=0, padx=2, pady=2)
        self.text_1 = ctk.CTkLabel(
            master=self.frame_11,
            text='Обработанные файлы'
        )
        self.text_1.place(x=5, y=2)
        self.image_arrow_6 = ctk.CTkButton(
            master=self.frame_11,
            text='',
            width=30, height=30,
            fg_color='transparent',
            bg_color='transparent',
            hover=False,
            image=self.image_down,
            command=self.button_menu_click_6
        )
        self.image_arrow_6.place(x=320, y=8)

        self.frame_20 = ctk.CTkFrame(
            master=self.frame,
            width=360, height=40,
        )
        self.frame_20.grid(row=12, column=0, padx=2, pady=2)
        self.text_1 = ctk.CTkLabel(
            master=self.frame_20,
            text='Защита данных'
        )
        self.text_1.place(x=5, y=2)
        self.image_arrow_8 = ctk.CTkButton(
            master=self.frame_20,
            text='',
            width=30, height=30,
            fg_color='transparent',
            bg_color='transparent',
            hover=False,
            image=self.image_down,
            command=self.button_menu_click_8
        )
        self.image_arrow_8.place(x=320, y=8)

        self.frame_15 = ctk.CTkFrame(
            master=self.frame,
            width=360, height=65,
        )
        self.frame_15.grid(row=14, column=0, padx=2, pady=2)
        self.text_1 = ctk.CTkLabel(
            master=self.frame_15,
            text='Тема приложения'
        )
        self.text_1.place(x=5, y=2)

        with open('json files/program_settings.json', 'r', encoding='utf-8') as file:
            datas = json.load(file)

        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.frame_15,
            width=350, height=30,
            values=[datas['theme'], "Dark", "Light", "System"],
            font=('Arial', 15),
            command=self.change_appearance_mode_event)
        self.appearance_mode_menu.place(x=5, y=27)

        self.frame_16 = ctk.CTkFrame(
            master=self.frame,
            width=360, height=80,
        )
        self.frame_16.grid(row=16, column=0, padx=2, pady=2)
        self.text_1 = ctk.CTkLabel(
            master=self.frame_16,
            text='Тема оформления'
        )
        self.text_1.place(x=5, y=2)

        self.text_1 = ctk.CTkLabel(
            master=self.frame_16,
            font=('Arial', 12),
            text_color='#818181',
            text='*приложение будет перезагружено'
        )
        self.text_1.place(x=5, y=55)

        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.frame_16,
            width=350, height=30,
            values=[datas['color_theme'], "blue", "green", "dark-blue"],
            font=('Arial', 15),
            command=self.change_appearance_mode_event_1)
        self.appearance_mode_menu.place(x=5, y=27)

        self.frame_17 = ctk.CTkFrame(
            master=self.frame,
            width=360, height=40,
        )
        self.frame_17.grid(row=18, column=0, padx=2, pady=2)
        self.text_1 = ctk.CTkLabel(
            master=self.frame_17,
            text='О программе',
            font=('Arial', 15, 'bold')
        )
        self.text_1.place(x=5, y=5)

        self.image_arrow_7 = ctk.CTkButton(
            master=self.frame_17,
            text='',
            width=30, height=30,
            fg_color='transparent',
            bg_color='transparent',
            hover=False,
            image=self.image_down,
            command=self.button_menu_click_7
        )
        self.image_arrow_7.place(x=320, y=8)

    def change_appearance_mode_event(self, new_appearance_mode: str) -> None:
        """
        Данная функция меняет цветовую тему
        :param new_appearance_mode: Строка с названием темы
        :return:
        """
        with open('json files/program_settings.json', 'r', encoding='utf-8') as file:
            datas = json.load(file)
        with open('json files/program_settings.json', 'w', encoding='utf-8') as file:
            data = {'theme': new_appearance_mode, 'color_theme': datas['color_theme'],}
            json.dump(data, file, indent=4, ensure_ascii=False)

        ctk.set_appearance_mode(new_appearance_mode)

    def change_appearance_mode_event_1(self, new_appearance_mode: str) -> None:
        """
        Даннная функция меняет цветовое оформление приложения
        :param new_appearance_mode: Строка с названием цветовой темы
        :return:
        """
        with open('json files/program_settings.json', 'r', encoding='utf-8') as file:
            datas = json.load(file)
        with open('json files/program_settings.json', 'w', encoding='utf-8') as file:
            data = {'theme': datas['theme'], 'color_theme': new_appearance_mode}
            json.dump(data, file, indent=4, ensure_ascii=False)
        os.execl(sys.executable, sys.executable, *sys.argv)  # позволяет перезагрузить приложение

    def delete_menu(self, menu: int) -> None:
        """
        Данная функция "сворачивает" развернутые карточки в дополнительном меню
        :param menu: номер сворачиваемого меню
        :return: None
        """
        match menu:
            case 5:
                self.image_arrow_5.configure(image=self.image_down)
                self.frame_10.destroy()
            case 6:
                self.image_arrow_6.configure(image=self.image_down)
                self.frame_12.destroy()
            case 7:
                self.image_arrow_7.configure(image=self.image_down)
                self.frame_14.destroy()
            case 8:
                self.image_arrow_8.configure(image=self.image_down)
                self.frame_16.destroy()

    def create_password(self, row: int = 1) -> None:
        """
        Данная функция создает карточку для создания нового пароля пользователем
        :param row: строка на которой создать карточку "создания пароля"
        :return: None
        """
        self.text_1 = ctk.CTkLabel(
            master=self.frame_16,
            text="Создайте пароль: ",
            anchor='w'
        )
        self.text_1.grid(row=1, column=0, padx=5, pady=0, sticky='w')

        self.password_entry = ctk.CTkEntry(
            master=self.frame_16,
            width=300, height=30,
            placeholder_text='пароль: ',
            show='•'
        )
        self.password_entry.grid(row=row + 1, column=0, padx=5, pady=5, sticky='w')

        self.image = ctk.CTkImage(
            dark_image=Image.open('Photo_set/open_password_dark.png'),
            light_image=Image.open('Photo_set/open_password_light.png'),
            size=(25, 25)
        )

        def state_password_entry():
            self.image_1 = ctk.CTkImage(
                dark_image=Image.open('Photo_set/close_password_dark.png'),
                light_image=Image.open('Photo_set/close_password_light.png'),
                size=(25, 25)
            )
            if self.state_password == False:
                self.password_entry.configure(show='')
                self.button.configure(image=self.image_1)
                self.state_password = True
            else:
                self.password_entry.configure(show='•')
                self.button.configure(image=self.image)
                self.state_password = False

        self.button = ctk.CTkButton(
            master=self.frame_16,
            image=self.image,
            width=30, height=30,
            bg_color='transparent',
            fg_color='transparent',
            hover=False,
            text='',
            command=state_password_entry
        )
        self.button.grid(row=row + 1, column=1, padx=5, pady=5, sticky='w')

        def save_password():
            if len(self.password_entry.get()) != 0:
                key = "A9bw4erG2-CzbVGE7My4fv6jwVIpEJVdrKqg34ccGkw="
                f = Fernet(key)
                password = str(f.encrypt(self.password_entry.get().encode("utf-8")))

                with open('json files/security_table.json', 'w', encoding='utf-8') as file:
                    data = {
                        "password": password,
                        "state": False,
                        "types_security": {
                            "structure_change": False,
                            "history_change": False,
                            "prohibion_change": False,
                        },
                    }
                    json.dump(data, file, indent=4, ensure_ascii=False)

                self.text_1.destroy()
                self.password_entry.destroy()
                self.button.destroy()
                self.button2.destroy()

        self.button2 = ctk.CTkButton(
            master=self.frame_16,
            width=350, height=30,
            text='Сохранить',
            font=('Centure Gothic', 15, 'bold'),
            command=save_password
        )
        self.button2.grid(row=row + 2, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    def button_menu_click_5(self):
        if not self.frame_position[4]:
            self.image_arrow_5.configure(image=self.image_up)
            self.frame_10 = ctk.CTkFrame(
                master=self.frame,
                width=360, height=330,
            )
            self.frame_10.grid(row=9, column=0, padx=2, pady=2)

            text = """В этом разделе описываются горячие клавиши \nприложения. Горячие клавиши приложения \nподразделяются на три типа: \n1. Системные клавиши: \n- Ctrl + W - открытие меню выбора пути к файлу. \n- Ctrl + E - открытие меню выбора пути для сохранения файла. \n- Ctrl + Enter - запуск обработки файла. \n- Ctrl + Q - открытие информационного табло. \n- Ctrl + R - закрытие информационного табло. \n2. Рабочие клавиши: \n- Ctrl + A - выбор столбцов с данными "5 и 7". \n- Ctrl + F - выбор столбцов с данными "6 и 8". \n- Ctrl + Z - выбор столбцов с данными "другое". \n- Ctrl + X - выбор сохранения файла по умолчанию. \n- Ctrl + C - выбор сохранения файла "заменить исходное". \n3. Палитра: \n- Ctrl + D - устанавливает темную тему. \n- Ctrl + L - устанавливает светлую тему. \n- Ctrl + S - устанавливает тему, как в системе. \n- Ctrl + G - устанавливает зеленое оформление. \n- Ctrl + B - устанавливает синие оформление."""

            self.text_1 = ctk.CTkLabel(
                master=self.frame_10,
                text=text,
                anchor='w'
            )
            self.text_1.place(x=5, y=2)
            self.frame_position[4] = True
        else:
            self.frame_position[4] = False
            self.delete_menu(5)

    def button_menu_click_6(self):
        if self.frame_position[5] == False:
            self.image_arrow_6.configure(image=self.image_up)
            self.frame_12 = ctk.CTkFrame(
                master=self.frame,
                width=360, height=335,
            )
            self.frame_12.grid(row=11, column=0, padx=2, pady=2)

            text = "История обработанных файлов"

            self.text_1 = ctk.CTkLabel(
                master=self.frame_12,
                text=text,
                anchor='w'
            )
            self.text_1.place(x=5, y=2)

            self.text_2 = ctk.CTkLabel(
                master=self.frame_12,
                text='*нажмите на значек "excel" чтобы удалить данный файл\n*нажмите на название таблицы чтобы открыть ее',
                text_color='gray',
                anchor='w'
            )
            self.text_2.place(x=5, y=300)

            self.frame_13 = Create_Excel_Card(
                master=self.frame_12,
                width=330, height=248,
                fg_color=("#b7b7b7", "#3e3e3e")
            )
            self.frame_13.place(x=5, y=35)

            self.frame_position[5] = True
        else:
            self.frame_position[5] = False
            self.delete_menu(6)

    def button_menu_click_7(self):
        if self.frame_position[6] == False:
            self.image_arrow_7.configure(image=self.image_up)
            self.frame_14 = ctk.CTkFrame(
                master=self.frame,
                width=360, height=150,
            )
            self.frame_14.grid(row=19, column=0, padx=2, pady=2)

            self.text_1 = ctk.CTkLabel(
                master=self.frame_14,
                text='Версия: 1.0.0',
                anchor='w'
            )
            self.text_1.place(x=5, y=2)

            self.text_2 = ctk.CTkLabel(
                master=self.frame_14,
                text='Последнее обновление: 25 сентября. 2023г.',
                anchor='w'
            )
            self.text_2.place(x=5, y=22)

            self.button_3 = ctk.CTkButton(
                master=self.frame_14,
                text='Разработчик: Белоглазов Максим',
                text_color=('black', 'white'),
                fg_color='transparent',
                bg_color='transparent',
                hover=False
            )
            self.button_3.place(x=5, y=42)

            self.text_4 = ctk.CTkLabel(
                master=self.frame_14,
                text='Дата выпуска: 25 сентября. 2023г.',
                anchor='w'
            )
            self.text_4.place(x=5, y=62)

            self.text_5 = ctk.CTkLabel(
                master=self.frame_14,
                text='Разрешения для приложения:',
                font=('Arial', 13, 'bold'),
                anchor='w'
            )
            self.text_5.place(x=5, y=82)

            self.text_6 = ctk.CTkLabel(
                master=self.frame_14,
                text='Изменения или удаление содержимого жесткого диска.',
                anchor='w'
            )
            self.text_6.place(x=5, y=102)

            self.text_7 = ctk.CTkLabel(
                master=self.frame_14,
                text='Чтение данных на жестком диске.',
                anchor='w'
            )
            self.text_7.place(x=5, y=122)

            self.frame_position[6] = True
        else:
            self.frame_position[6] = False
            self.delete_menu(7)

    def button_menu_click_8(self):
        if self.frame_position[7] == False:
            self.state_password = False

            self.image_arrow_8.configure(image=self.image_up)
            self.frame_16 = ctk.CTkFrame(
                master=self.frame,
                width=360, height=400,
            )
            self.frame_16.grid(row=13, column=0, padx=2, pady=2)

            self.text_1 = ctk.CTkLabel(
                master=self.frame_16,
                text='Меню настройки защиты данных',
                anchor='w'
            )
            self.text_1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')

            if not os.path.exists('json files/security_table.json'):
                self.create_password()
            else:
                self.create_password_menu()

            self.frame_position[7] = True
        else:
            self.frame_position[7] = False
            self.delete_menu(8)

    def create_password_menu(self) -> None:
        """
        Создание карточки "защита excel файла"
        :return: None
        """

        def update_security():
            with open('json files/security_table.json', 'r', encoding='utf-8') as file:
                datas = dict(json.load(file))
                data = datas['types_security']
                boolean = lambda text: True if text == 'True' else False

                data['structure_change'] = boolean(self.switch_var_1.get())
                data['history_change'] = boolean(self.switch_var_2.get())
                data['prohibion_change'] = boolean(self.switch_var_3.get())
            with open('json files/security_table.json', 'w', encoding='utf-8') as file:
                json.dump(datas, file, indent=4, ensure_ascii=False)

        self.security_text_1 = ctk.CTkLabel(
            master=self.frame_16,
            width=293,
            text='Защита изменения структуры таблицы',
            anchor='w'
        )
        self.security_text_1.grid(row=1, column=0, padx=5, pady=2, sticky='w')

        with open("json files/security_table.json", 'r', encoding='utf-8') as file:
            data = dict(json.load(file))['types_security']

        self.switch_var_1 = ctk.StringVar(value='False')
        self.switch_var_2 = ctk.StringVar(value='False')
        self.switch_var_3 = ctk.StringVar(value='False')

        self.switch_var_1.set(str(data['structure_change']))
        self.switch_var_2.set(str(data['history_change']))
        self.switch_var_3.set(str(data['prohibion_change']))

        self.switch_1 = ctk.CTkSwitch(
            master=self.frame_16,
            width=45, height=35,
            switch_width=40,
            switch_height=20,
            corner_radius=10,
            text="",
            variable=self.switch_var_1,
            onvalue="True", offvalue="False",
            command=update_security
        )
        self.switch_1.grid(row=1, column=1, padx=5, pady=2)

        self.security_text_2 = ctk.CTkLabel(
            master=self.frame_16,
            width=293,
            text='Защита отслеживания истории изменений',
            anchor='w'
        )
        self.security_text_2.grid(row=2, column=0, padx=5, pady=2, sticky='w')

        self.switch_2 = ctk.CTkSwitch(
            master=self.frame_16,
            width=45, height=35,
            switch_width=40,
            switch_height=20,
            corner_radius=10,
            text="",
            variable=self.switch_var_2,
            onvalue="True", offvalue="False",
            command=update_security
        )
        self.switch_2.grid(row=2, column=1, padx=5, pady=2)

        self.security_text_3 = ctk.CTkLabel(
            master=self.frame_16,
            width=293,
            text='Защита листа от изменений',
            anchor='w'
        )
        self.security_text_3.grid(row=3, column=0, padx=5, pady=2, sticky='w')

        self.switch_3 = ctk.CTkSwitch(
            master=self.frame_16,
            width=45, height=35,
            switch_width=40,
            switch_height=20,
            corner_radius=10,
            text="",
            variable=self.switch_var_3,
            onvalue="True", offvalue="False",
            command=update_security
        )
        self.switch_3.grid(row=3, column=1, padx=5, pady=2)

        self.inform_label = ctk.CTkLabel(
            master=self.frame_16,
            width=350,
            text='*чтобы изменить таблицу потребуется ввести пароль',
            text_color='#818181',
            anchor='w'
        )
        self.inform_label.grid(row=4, column=0, columnspan=2, pady=5)

        self.state_password_button = False

        def open_password():
            if self.state_password_button == False:
                with open("json files/security_table.json", 'r', encoding='utf-8') as file:
                    data = dict(json.load(file))
                    key = "A9bw4erG2-CzbVGE7My4fv6jwVIpEJVdrKqg34ccGkw="
                    f = Fernet(key)
                    password = data['password'].replace("b'", "").replace("'", "")
                    password = str(f.decrypt(password.encode("utf-8")))

                self.button5.configure(text='Скрыть пароль')

                self.label = ctk.CTkLabel(
                    master=self.frame_16,
                    text=password[1:].replace("'", '')
                )
                self.label.grid(row=5, column=0, columnspan=2, padx=130, pady=5, sticky='w')
                self.state_password_button = True
            else:
                self.button5.configure(text='Показать пароль')
                self.label.destroy()
                self.state_password_button = False

        self.button5 = ctk.CTkButton(
            master=self.frame_16,
            width=100, height=30,
            text='Показать пароль',
            font=('Centure Gothic', 15),
            command=open_password
        )
        self.button5.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='w')


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.windows_size = (415, 700)
        self.monitor_height = self.winfo_screenheight()
        self.monitor_width = self.winfo_screenwidth()

        x = int((self.monitor_width - self.windows_size[0]) / 2)
        y = int((self.monitor_height - self.windows_size[1]) / 2)

        self.geometry(f'{self.windows_size[0]}x{self.windows_size[1]}+{x}+{y}')
        # self.minsize(self.windows_size[0], self.windows_size[1])
        self.resizable(False, False)
        self.title('ExcelHelper')

        self.start()

    def start(self):
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        self.main_frame = MainWindows(master=self)
        self.main_frame.grid(row=0, column=0, sticky='nsew')

    def create_window(self) -> None:
        self.frame = ctk.CTkFrame(master=self, width=400, height=550)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label1 = ctk.CTkLabel(master=self.frame, text='ExcelHelper', font=('Arial Rounded MT Bold', 25, 'bold'))
        self.label1.place(x=120, y=5)

        self.image = ctk.CTkImage(
            dark_image=Image.open('Photo_set/Dark_menu.png'),
            light_image=Image.open('Photo_set/Light_menu.png'),
            size=(25, 25))

        self.enter_image = ctk.CTkImage(
            dark_image=Image.open('Photo_set/Gray_menu.png'),
            light_image=Image.open('Photo_set/Gray_menu.png'),
            size=(25, 25))

        self.button = ctk.CTkButton(
            master=self.frame,
            image=self.image,
            width=30, height=30,
            bg_color='transparent',
            fg_color='transparent',
            hover=False,
            text='',
            command=self.button_click)
        self.button.place(x=355, y=5)

        self.button.bind("<Enter>", lambda event: self.button.configure(image=self.enter_image))
        self.button.bind("<Leave>", lambda event: self.button.configure(image=self.image))

        self.inform_label1 = ctk.CTkLabel(master=self.frame, text='', text_color='red')
        self.inform_label1.place(x=11, y=50)
        self.name_entry = ctk.CTkEntry(master=self.frame,
                                       placeholder_text='Введите путь к файлу .xlsx',
                                       width=340, height=30)
        self.name_entry.place(x=10, y=75)
        self.path_image_1 = ctk.CTkImage(
            dark_image=Image.open('Photo_set/Dark_path_menu_1.png'),
            light_image=Image.open('Photo_set/Light_path_menu_1.png'),
            size=(20, 20))
        self.button_menu_path_1 = ctk.CTkButton(
            master=self.frame,
            width=30, height=30,
            text='',
            image=self.path_image_1,
            text_color=('gray', 'white'),
            font=('Centure Gothic', 20),
            bg_color='transparent',
            fg_color=('#c1c1c1', '#404040'),
            hover=False,
            command=lambda: self.open_path_menu(menu=1)
        )
        self.button_menu_path_1.place(x=355, y=75)

        self.inform_label2 = ctk.CTkLabel(master=self.frame, text='', text_color='red')
        self.inform_label2.place(x=11, y=105)
        self.name_entry2 = ctk.CTkEntry(master=self.frame,
                                        placeholder_text='Введите путь для сохранения файла .xlsx',
                                        width=340, height=30)
        self.name_entry2.place(x=10, y=130)
        self.path_image_2 = ctk.CTkImage(
            dark_image=Image.open('Photo_set/Dark_path_menu_1.png'),
            light_image=Image.open('Photo_set/Light_path_menu_1.png'),
            size=(20, 20))
        self.button_menu_path_2 = ctk.CTkButton(
            master=self.frame,
            width=30, height=30,
            text='',
            image=self.path_image_2,
            text_color=('gray', 'white'),
            font=('Centure Gothic', 20),
            bg_color='transparent',
            fg_color=('#c1c1c1', '#404040'),
            hover=False,
            command=lambda: self.open_path_menu(menu=2)
        )
        self.button_menu_path_2.place(x=355, y=130)

        self.radio_var_value = tk.IntVar()
        self.inform_label_3 = ctk.CTkLabel(master=self.frame, text='Выберите столбцы с данными')
        self.inform_label_3.place(x=10, y=160)
        self.radiobutton_3 = ctk.CTkRadioButton(
            self.frame, text="5 и 7",
            command=self.radiobutton_event_value,
            variable=self.radio_var_value, value=1)
        self.radiobutton_3.place(x=10, y=190)

        self.radiobutton_4 = ctk.CTkRadioButton(
            self.frame, text="6 и 8",
            command=self.radiobutton_event_value,
            variable=self.radio_var_value, value=2)
        self.radiobutton_4.place(x=80, y=190)

        self.radiobutton_5 = ctk.CTkRadioButton(
            self.frame, text="другое",
            command=self.radiobutton_event_value,
            variable=self.radio_var_value, value=3)
        self.radiobutton_5.place(x=150, y=190)
        self.radio_var_value.set(1)

        self.inform_label_6 = ctk.CTkLabel(master=self.frame, text='Как хотите сохранить файл')
        self.inform_label_6.place(x=10, y=217)
        self.radio_var = tk.IntVar()
        self.radiobutton_1 = ctk.CTkRadioButton(self.frame, text="Сохранить по умолчанию",
                                                command=self.radiobutton_event, variable=self.radio_var, value=1)
        self.radiobutton_1.place(x=10, y=247)

        self.radiobutton_2 = ctk.CTkRadioButton(self.frame, text="Сохранить как новое",
                                                command=self.radiobutton_event, variable=self.radio_var, value=2)
        self.radiobutton_2.place(x=10, y=277)
        self.radio_var.set(2)

        self.inform_label_15 = ctk.CTkLabel(master=self.frame, text='Защита данных')
        self.inform_label_15.place(x=10, y=330)

        self.switch_var = ctk.StringVar(value="off")
        self.switch = ctk.CTkSwitch(
            master=self.frame,
            width=45, height=35,
            switch_width=40,
            switch_height=20,
            corner_radius=10,
            text="Запретить изменение таблицы.",
            command=lambda: self.enabled_security() if os.path.exists("json files/security_table.json") else ...,
            variable=self.switch_var,
            onvalue="on", offvalue="off",
            state="normal" if os.path.exists("json files/security_table.json") else 'disabled'
        )
        self.switch.place(x=10, y=357)

        self.inform_label_5 = ctk.CTkLabel(
            master=self.frame,
            text='',
            width=390, height=30,
            text_color='green'
        )
        self.inform_label_5.place(x=5, y=390)

        self.button2 = ctk.CTkButton(
            master=self.frame,
            width=200, height=30,
            text='Запустить',
            font=('Centure Gothic', 15, 'bold'),
            command=self.check_values_path
        )
        self.button2.place(x=100, y=440)

        text = """При работе с конфиденциальными Excel файлами, необходимо соблюдать \nполитику конфиденциальности. 
        Это включает в себя использование паролей \nдля защиты файлов, установку ограничений доступа, обеспечение 
        \nбезопасности при передаче файлов через сеть, контроль использования \nи управление доступом к файлам."""
        self.inform_label_4 = ctk.CTkLabel(
            master=self.frame,
            text=text,
            text_color='#818181',
            font=('Centure Gothic', 10))
        self.inform_label_4.place(x=5, y=477)

        # Меню горячие клавиши
        self.bind("<Control-w>", lambda a: self.open_path_menu(menu=1))
        self.bind("<Control-e>", lambda a: self.open_path_menu(menu=2))
        self.bind("<Control-Return>", lambda a: self.check_values_path())
        self.bind("<Control-q>", lambda a: self.button_click())
        self.bind("<Control-r>", lambda a: self.button_click_1())
        # Выбор режима работы
        self.bind("<Control-a>", lambda a: self.radiobutton_event_value(value=1))
        self.bind("<Control-f>", lambda a: self.radiobutton_event_value(value=2))
        self.bind("<Control-z>", lambda a: self.radiobutton_event_value(value=3))
        self.bind("<Control-x>", lambda a: self.radiobutton_event(value=1))
        self.bind("<Control-c>", lambda a: self.radiobutton_event(value=2))
        # Цветовая тема
        self.bind("<Control-d>", lambda a: self.change_appearance_mode_event('Dark'))
        self.bind("<Control-l>", lambda a: self.change_appearance_mode_event('Light'))
        self.bind("<Control-s>", lambda a: self.change_appearance_mode_event('System'))
        self.bind("<Control-g>", lambda a: self.change_appearance_mode_event_1('green'))
        self.bind("<Control-b>", lambda a: self.change_appearance_mode_event_1('blue'))

    def enabled_security(self) -> None:
        """
        Функция проверки и сохранение в файл состояния, нужно ли защищать таблицу или нет
        :return: None
        """

        with open("json files/security_table.json", 'r', encoding='utf-8') as file:
            data = dict(json.load(file))

        if self.switch_var.get() == 'off':
            with open("json files/security_table.json", 'w', encoding='utf-8') as file:
                data['state'] = False
                json.dump(data, file, ensure_ascii=False, indent=4)
        else:
            with open("json files/security_table.json", 'w', encoding='utf-8') as file:
                data['state'] = True
                json.dump(data, file, ensure_ascii=False, indent=4)

    def change_appearance_mode_event(self, new_appearance_mode) -> None:
        """
        Данная функция устанавливает цветовую тему приложения
        :param new_appearance_mode: Строка c значением устанавливаемой темы
        :return: None
        """

        with open('json files/program_settings.json', 'r', encoding='utf-8') as file:
            datas = json.load(file)
        with open('json files/program_settings.json', 'w', encoding='utf-8') as file:
            data = {'theme': new_appearance_mode, 'color_theme': datas['color_theme']}
            json.dump(data, file, indent=4, ensure_ascii=False)
        ctk.set_appearance_mode(new_appearance_mode)

    def change_appearance_mode_event_1(self, new_appearance_mode):
        """
        Функция устанавливает цветовое оформление приложения
        :param new_appearance_mode: Строка со значением цветового оформления
        :return:
        """

        with open('json files/program_settings.json', 'r', encoding='utf-8') as file:
            datas = json.load(file)
        with open('json files/program_settings.json', 'w', encoding='utf-8') as file:
            data = {'theme': datas['theme'], 'color_theme': new_appearance_mode}
            json.dump(data, file, indent=4, ensure_ascii=False)

        # Для применения нового цветового оформления требуется перезагрузить приложение
        os.execl(sys.executable, sys.executable, *sys.argv)

    def open_path_menu(self, menu: int) -> None:
        """
        Данная функция запускает диалоговое окно Windows для выбора пути до файла или до места сохранения файла
        :param menu: номер запускаемого диалогового окна
        :return: None
        """
        if menu == 1:
            # Диалоговое меню windows
            root = tk.Tk()
            root.withdraw()
            filename = filedialog.askopenfilename()

            if len(filename) == 0:
                filename = 'Не выбрано'

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, filename)
        else:
            if self.radio_var.get() != 1:
                root = tk.Tk()
                root.withdraw()
                filename = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                        filetypes=[('Excel files', ('.xlsx', '.xls')),
                                                                   ('All files', '*.*')])
                if len(filename) == 0:
                    filename = 'Не выбрано'
                self.name_entry2.delete(0, tk.END)
                self.name_entry2.insert(0, filename)
            else:
                self.inform_label2.configure(text='для этого режима нельзя установить путь')
                self.after(3000, lambda: self.inform_label2.configure(text=''))

    def radiobutton_event_value(self, value: int = None) -> None:
        """
        Данная функция обрабатывает нажатия пользователя по выбору индекса столбцов "Увеличение" и "Уменьшение"
        :param value: Данная переменная служит для смены нажатой кнопки по смене через горячие клавищи
        :return: None
        """
        if value is not None:
            self.radio_var_value.set(value)

        try:
            if self.radio_var_value.get() == 3:
                self.name_entry3 = ctk.CTkEntry(master=self.frame,
                                                placeholder_text='значение (например: 7 9)',
                                                width=170, height=30)
                self.name_entry3.place(x=220, y=185)
            elif self.radio_var_value.get() == 1:
                self.value = [5, 7]
                if self.name_entry3.winfo_exists():
                    self.name_entry3.destroy()
            elif self.radio_var_value.get() == 2:
                self.value = [6, 8]
                if self.name_entry3.winfo_exists():
                    self.name_entry3.destroy()
        except:
            pass

    def button_click_1(self) -> None:
        """
        Данная функция закрывает дополнительное окно программы
        :return: None
        """
        try:
            self.on_menu_bool = True
            self.frame_2.destroy()

            self.geometry(f'415x650')
            self.frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.button.configure(state='normal')
        except: pass

    def button_click(self) -> None:
        """
        Данная функция создает дополнительное меню программы
        :return: None
        """

        if not self.on_menu_bool:
            return
        self.on_menu_bool = False

        self.geometry(f'840x570')
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        self.button.configure(state='disabled')

        self.frame_2 = ctk.CTkFrame(
            master=self,
            width=400, height=550,
        )
        self.frame_2.grid(row=0, column=1, padx=5, pady=10)

        self.label3 = ctk.CTkLabel(
            master=self.frame_2,
            text='Информационное табло',
            font=('Centure Gothic', 20))
        self.label3.place(x=75, y=10)

        self.image_1 = ctk.CTkImage(Image.open('Photo_set/Exit_menu.png'),
                                    size=(25, 25))

        self.label2 = ctk.CTkButton(
            master=self.frame_2,
            image=self.image_1,
            width=20, height=20,
            bg_color='transparent',
            fg_color='transparent',
            hover=False,
            text='',
            command=self.button_click_1)
        self.label2.place(x=350, y=10)

        self.frame_3 = Create_Additional_Menu(
            master=self.frame_2,
            width=365, height=480,
            fg_color=("#b7b7b7", "#3e3e3e")
        )
        self.frame_3.place(x=5, y=50)

    def radiobutton_event(self, value: int = None) -> None:
        """
        Данная функция обрабатывает нажатия кнопок для выбора пути до сохранения файла
        :param value: значение для установки выбранной кнопки через горячие клавищи
        :return: None
        """
        if value is not None:
            self.radio_var.set(value)

        if self.radio_var.get() == 1:
            self.name_entry2.delete(0, tk.END)
            self.name_entry2.configure(placeholder_text='не требуется', placeholder_text_color='red')
            self.name_entry.focus_set()
        elif self.radio_var.get() == 2:
            self.name_entry2.configure(placeholder_text='Введите путь для сохранения файла .xlsx',
                                       placeholder_text_color='gray')

    def check_values(self) -> list:
        """
        Функция проверяет и возвращает выбранное пользователем столбцы "Увеличение" и "Уменьшение"
        :return: возвращает список со значением выбранных столбцов
        """
        if self.radio_var_value.get() == 3:
            values = self.name_entry3.get().split()
            if len(values) != 0 and len(values) == 2:
                self.name_entry3.configure(placeholder_text='значение (например: 7 9)', placeholder_text_color='gray')
                return list(map(int, values))
            else:
                self.name_entry3.configure(placeholder_text='Укажите значение', placeholder_text_color='red')
                self.button2.focus_set()
                return [False]
        return self.value

    def completed_processing(self) -> None:
        """
        Данная функция при успешной обработки файла создает кнопку "открыть" обработанный файл
        :return: None
        """
        self.button2.configure(width=100)
        self.button3 = ctk.CTkButton(
            master=self.frame,
            width=100, height=30,
            text='Открыть',
            command=self.open_file
        )
        self.button3.place(x=205, y=440)
        self.update_time_base_value(time=10)

    def update_time_base_value(self, time: int):
        """
        По истечению 10 секунд запускает функцию удаления кнопки "Открыть" обработанный файл
        :param time: Время работы функции
        :return:
        """
        try:
            if time == 0:
                self.delet_button_file()
                return

            self.button3.configure(text=f'Открыть {time}')
            self.after(1000, lambda: self.update_time_base_value(time - 1))
        except: pass

    def delet_button_file(self):
        """
        Удаляет кнопку "Открыть" обработанный файл
        :return:
        """
        self.button3.destroy()
        self.button2.configure(width=200)

    def open_file(self):
        """
        Данная функция октрывает обработанный файл
        :return:
        """
        self.delet_button_file()
        if self.radio_var.get() == 2:
            os.system(fr'"{self.name_entry2.get()}"')
            self.name_entry.delete(0, tk.END)
            self.name_entry2.delete(0, tk.END)
        else:
            path = os.path.abspath(self.name)
            path = path.replace('\Таблица', '\Обработанные excel файлы\\Таблица')
            os.system(fr'"{path}"')
            self.name_entry.delete(0, tk.END)

    def process_file(self, index: list, source_path: str, download_path: str = None, path: bool = False) -> None:
        """
        Данная функция запускает функции обработки excel файла
        :param index: индексы столбцов "Увеличение" и "Уменьшение"
        :param source_path: путь до обрабатываемого excel файла
        :param download_path: путь до сохранения обрабатываемого excel файла
        :param path: Значение: сохранять файл по умолчанию или по другое пути
        :return: None
        """
        worksheet, workbook = TEST.download_excel_file(source_path)
        TEST.find_dublication(worksheet=worksheet, index=index)
        a, _, _ = TEST.processing_data(worksheet=worksheet, index=index)
        TEST.update_table(worksheet=worksheet, values=a, index=index)
        a, _, _ = TEST.processing_data_1(worksheet=worksheet, index=index)
        TEST.update_table_1(worksheet=worksheet, values=a, index=index)
        if path:
            status, self.name = TEST.save_file_format(workbook=workbook, worksheets=worksheet, path=True)
        else:
            status, self.name = TEST.save_file_format(workbook=workbook, worksheets=worksheet, file_name=download_path,
                                                      path=False)

        if status:
            self.inform_label_5.configure(text="Файл был успешно обработан и сохранен", text_color='green')
            self.switch_var.set('off')
            self.completed_processing()
            self.after(3000, lambda: self.inform_label_5.configure(text=''))
        else:
            self.inform_label_5.configure(text=self.name, text_color='red')
            self.after(3000, lambda: self.inform_label_5.configure(text=''))

    def check_values_path(self):
        """
        Данная функция проверяет корректность введенных пользователем данных и запускает функцию обработки excel файла
        :return:
        """
        source_path = self.name_entry.get()
        download_path = self.name_entry2.get()
        self.value = self.check_values()
        if not self.value[0]:
            return

        def clear_inform_menu(menu: int, text: str, color: str = 'green'):
            if menu == 0:
                self.inform_label1.configure(text=text)
                self.after(3000, lambda: self.inform_label1.configure(text=''))
            elif menu == 1:
                self.inform_label2.configure(text=text)
                self.after(3000, lambda: self.inform_label2.configure(text=''))
            elif menu == 2:
                self.inform_label_5.configure(text=text, text_color=color)
                self.after(3000, lambda: self.inform_label_5.configure(text=''))

        if os.path.exists(source_path):
            if self.radio_var.get() == 2 and len(download_path) == 0:
                clear_inform_menu(menu=1, text='Для этого режима нужно заполнить второе поле')
            elif self.radio_var.get() == 2 and len(download_path) != 0:
                if download_path.split('.')[-1] not in ['xlsx', 'xls']:
                    clear_inform_menu(menu=1, text='Данное расширение файла не поддерживается')
                else:
                    self.process_file(index=self.value, source_path=source_path, download_path=download_path,
                                      path=False)
            elif self.radio_var.get() == 1:
                if source_path.split('.')[-1] not in ['xlsx', 'xls']:
                    clear_inform_menu(menu=0, text='Данное расширение файла не поддерживается')
                    return
                self.process_file(index=self.value, source_path=source_path, path=True)
        elif len(self.name_entry.get()) == 0:
            clear_inform_menu(menu=0, text='Данное поле обязательно для заполнения')
        else:
            clear_inform_menu(menu=0, text='Введеное вами путь к файлу не найден')


if __name__ == '__main__':
    app = Window()
    app.mainloop()
