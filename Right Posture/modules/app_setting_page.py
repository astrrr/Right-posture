from main import MainWindow
from modules.app_detect import Camera_detail
from modules.app_checkbox import Main_checkbox
from modules.Version_control import Setting_func
from widgets import PyToggle
from modules.app_functions import AppFunctions
import os
import sqlite3
cwd = os.getcwd()
user_now = ""

class Main_setting(MainWindow):

    def save_setting(self):
        setting = self.ui
        try:
            conn = sqlite3.connect(f"{cwd}/bin/Data/Accounts.db")
            cur = conn.cursor()
            period = setting.combo_period.currentIndex()
            sensitive = setting.combo_sensitive.currentIndex()
            sitting = setting.combo_sitting.currentIndex()
            dnd = Setting_func.DND
            discord = Setting_func.Discord
            query = f"UPDATE login_info set period={period}, sensitive={sensitive}, sitting={sitting}, " \
                    f"dnd={dnd}, discord={discord} WHERE username = \'{user_now}\'"
            cur.execute(query)
            cur.execute(query)
            conn.commit()
            conn.close()
            Main_setting.apply_setting(self)
            setting.Setting_log.append("Save complete !")
        except Exception as e:
            print(e)

    def load_setting(self, user_setting):
        global user_now
        user_now = user_setting
        setting = self.ui
        conn = sqlite3.connect(f"{cwd}/bin/Data/Accounts.db")
        cur = conn.cursor()
        query = f"SELECT period,sensitive,sitting,dnd,discord " \
                f"FROM login_info WHERE username = \'{user_setting}\'"
        cur.execute(query)
        try:
            result = cur.fetchall()
            # print(result)
            set_Index = result[0]
            setting.combo_period.setCurrentIndex(set_Index[0])
            setting.combo_sensitive.setCurrentIndex(set_Index[1])
            setting.combo_sitting.setCurrentIndex(set_Index[2])
            Setting_func.DND = set_Index[3]
            Setting_func.Discord = set_Index[4]
            PyToggle.Toggle_Switch(self)
            Main_setting.apply_setting(self)
        except Exception as e:
            print(e)

    def apply_setting(self):
        setting = self.ui
        show_setting = "Apply setting\n"

        period_raw = setting.combo_period.currentText()
        period_time = [int(s) for s in period_raw.split() if s.isdigit()]
        if setting.combo_period.currentIndex() <= 3:
            Camera_detail.period = period_time[0]
            period_text = f"Period = {setting.combo_period.currentText()} = {Camera_detail.period} Second\n"
            show_setting = show_setting + period_text
            # print(f"Period = {period_time[0]} = {Camera_detail.period} Second")
        else:
            Camera_detail.period = period_time[0] * 60
            period_text = f"Period = {setting.combo_period.currentText()} = {Camera_detail.period} Second\n"
            show_setting = show_setting + period_text
            # print(f"Period = {period_time[0]} = {Camera_detail.period} Second")

        sensitive_raw = setting.combo_sensitive.currentText()
        sensitive_time = [int(s) for s in sensitive_raw.split() if s.isdigit()]
        Camera_detail.sensitive = sensitive_time[0]
        sensitive_text = f"Sensitive = {setting.combo_sensitive.currentText()} = {Camera_detail.sensitive} Second\n"
        show_setting = show_setting + sensitive_text
        # print(f"Sensitive = {sensitive_time[0]} = {Camera_detail.sensitive} Second")

        sitting_raw = setting.combo_sitting.currentText()
        sitting_time = [int(s) for s in sitting_raw.split() if s.isdigit()]
        if setting.combo_sitting.currentIndex() <= 1:
            Camera_detail.sitting = sitting_time[0]
            sitting_text = f"Sitting = {setting.combo_sitting.currentText()} = {Camera_detail.sitting} Minute\n"
            show_setting = show_setting + sitting_text
            # print(f"Sitting = {sitting_time[0]} = {Camera_detail.sitting} Minute")
        else:
            Camera_detail.sitting = sitting_time[0] * 60
            sitting_text = f"Sitting = {setting.combo_sitting.currentText()} = {Camera_detail.sitting} Minute\n"
            show_setting = show_setting + sitting_text
            # print(f"Sitting = {sitting_time[0]} = {Camera_detail.sitting} Minute")

        Main_checkbox.Show_Detail(self)
        setting.Setting_log.setText(show_setting)
        # Discord Rich Presence
        AppFunctions.discordRichPresence(self, Setting_func.Discord)