from main import MainWindow
from modules.app_detect import Camera_detail
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
            query = f"UPDATE login_info set period={period}, sensitive={sensitive}, sitting={sitting} WHERE username = \'{user_now}\'"
            cur.execute(query)
            cur.execute(query)
            conn.commit()
            conn.close()
            Main_setting.apply_setting(self)
            print("save complete")
        except Exception as e:
            print(e)

    def load_setting(self, user_setting):
        global user_now
        user_now = user_setting
        setting = self.ui
        conn = sqlite3.connect(f"{cwd}/bin/Data/Accounts.db")
        cur = conn.cursor()
        query = f"SELECT period,sensitive,sitting FROM login_info WHERE username = \'{user_setting}\'"
        cur.execute(query)
        try:
            result = cur.fetchall()
            # print(result)
            set_Index = result[0]
            setting.combo_period.setCurrentIndex(set_Index[0])
            setting.combo_sensitive.setCurrentIndex(set_Index[1])
            setting.combo_sitting.setCurrentIndex(set_Index[2])
            Main_setting.apply_setting(self)

        except Exception as e:
            print(e)

    def apply_setting(self):
        setting = self.ui
        period_raw = setting.combo_period.currentText()
        period_time = [int(s) for s in period_raw.split() if s.isdigit()]
        if setting.combo_period.currentIndex() == 0:
            Camera_detail.period = 30
        else:
            Camera_detail.period = period_time[0] * 60
        print(f"Period = {Camera_detail.period}")

        sensitive_raw = setting.combo_sensitive.currentText()
        sensitive_time = [int(s) for s in sensitive_raw.split() if s.isdigit()]
        Camera_detail.sensitive = sensitive_time[0]
        print(f"Sensitive = {Camera_detail.sensitive}")

        sitting_raw = setting.combo_sitting.currentText()
        sitting_time = [int(s) for s in sitting_raw.split() if s.isdigit()]
        Camera_detail.sitting = sitting_time[0]
        print(f"Sitting = {Camera_detail.sitting}")