import os
import json
import customtkinter as ctk


def update_theme(new_theme: str):
    ctk.set_appearance_mode(new_theme)

    if os.path.exists("PersonData/person_data.json"):
        with open("PersonData/person_data.json", "r", encoding="utf-8") as file:
            data = dict(json.load(file))
            data["theme"] = new_theme

        with open("PersonData/person_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
