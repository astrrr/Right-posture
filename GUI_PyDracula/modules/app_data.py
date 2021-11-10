import json

def load_data():
    try:
        with open("bin/save_setting.json", "r") as read_file:
            loaded_object = json.load(read_file)
        # print("Loaded setting from save_setting.json")
        return loaded_object

    except FileNotFoundError:
        new_file = {"Night": 0, "Close": 0, "Sound": 0, "Discord": 0}
        with open('bin/save_setting.json', 'w') as write_file:
            json.dump(new_file, write_file)
        print("File not found we will create a default file")

        with open("bin/save_setting.json", "r") as read_file:
            loaded_object = json.load(read_file)
        print("Loaded setting from new file")
        return loaded_object

def save_data(setting, value):
    loaded_object = load_data()
    loaded_object[setting] = value
    with open('bin/save_setting.json', 'w') as write_file:
        json.dump(loaded_object, write_file)