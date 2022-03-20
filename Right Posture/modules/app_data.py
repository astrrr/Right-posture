import json
import os
from modules.Version_control import Debug_path
cwd = os.getcwd()

def load_data():
    try:
        with open(f"{cwd}{Debug_path.path}/bin/Data/save_setting.json", "r") as read_file:
            loaded_object = json.load(read_file)
        return loaded_object

    except FileNotFoundError:
        new_file = {"Light": 0, "DND": 0, "Discord": 0, "PreCam1": 0, "PreDetail": 0, "PreLog": 0}
        with open(f"{cwd}{Debug_path.path}/bin/Data/save_setting.json", 'w') as write_file:
            json.dump(new_file, write_file)
        print("File not found we will create a default file")

        with open(f"{cwd}{Debug_path.path}/bin/Data/save_setting.json", "r") as read_file:
            loaded_object = json.load(read_file)
        print("Loaded setting from new file")
        return loaded_object

def load_password():
    with open(f"{cwd}{Debug_path.path}/bin/Data/password.txt", "r") as read_file:
        loaded_object = read_file.readline()
    return loaded_object

def save_data(setting, value):
    loaded_object = load_data()
    loaded_object[setting] = value
    with open(f"{cwd}{Debug_path.path}/bin/Data/save_setting.json", 'w') as write_file:
        json.dump(loaded_object, write_file)