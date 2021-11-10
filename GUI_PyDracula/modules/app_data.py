import json

def load_data():
    with open("bin/save_setting.json", "r") as read_file:
        loaded_object = json.load(read_file)
    return loaded_object

def save_data(setting, value):
    loaded_object = load_data()
    loaded_object[setting] = value
    with open('bin/save_setting.json', 'w') as write_file:
        json.dump(loaded_object, write_file)