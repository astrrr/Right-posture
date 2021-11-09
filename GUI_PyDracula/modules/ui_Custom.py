from main import *




class ui_Custom:

    def load(self):
        with open("bin/save_setting.json", "r") as read_file:
            loaded_object = json.load(read_file)
        return loaded_object

    def setup_gui(self):
        widgets = self.ui



