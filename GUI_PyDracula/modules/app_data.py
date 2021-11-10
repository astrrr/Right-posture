import json
import time
from pypresence import Presence

def load_data():
    try:
        with open("bin/save_setting.json", "r") as read_file:
            loaded_object = json.load(read_file)
        print("Loaded setting from save_setting.json")
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

# Discord Rich Presence
def discordRichPresence(enable):
    if enable:
        rpc = Presence("902601121124728884")
        rpc.connect()
        rpc.update(  # details="Make Life Better.",
            state="Dev GUI",
            large_image="right_posture",
            large_text="อยากรู้ล่ะสิ",
            small_image="verify",
            small_text="Verify by me",
            buttons=[{"label": "Github", "url": "https://github.com/ussnllmn"}],
            party_size=[35, 100],
            start=time.time()
        )
        print("Discord Rich Presence Connected")

def Discord(enable):
    if enable:
        try:
            discordRichPresence(True)
        except:
            print("Pipe Not Found - Is Discord Running?")