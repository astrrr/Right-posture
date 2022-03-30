import os
from modules.Version_control import Debug_path
cwd = os.getcwd()

def load_password():
    with open(f"{cwd}{Debug_path.path}/bin/Data/password.txt", "r") as read_file:
        loaded_object = read_file.readline()
        # print("Password_loaded")
    return loaded_object