import json
import os

cwd = os.getcwd()

def load_data():
    try:
        with open(f"{cwd}/Right Posture/bin/Data/save_setting.json", "r") as read_file:
            loaded_object = json.load(read_file)
        print(cwd)
        return loaded_object

    except FileNotFoundError:
        new_file = {"Night": 0, "DND": 0, "Discord": 0, "PreCam1": 0}
        with open(f'{cwd}/Right Posturebin/Data/save_setting.json', 'w') as write_file:
            json.dump(new_file, write_file)
        print("File not found we will create a default file")

        with open(f"{cwd}/Right Posture/bin/Data/save_setting.json", "r") as read_file:
            loaded_object = json.load(read_file)
        print("Loaded setting from new file")
        return loaded_object

def save_data(setting, value):
    loaded_object = load_data()
    loaded_object[setting] = value
    with open(f"{cwd}/Right Posture/bin/Data/save_setting.json", 'w') as write_file:
        json.dump(loaded_object, write_file)