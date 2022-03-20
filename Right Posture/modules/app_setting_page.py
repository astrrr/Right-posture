from main import MainWindow
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
            setting.labelBoxBlenderInstalation_19.setText("save_complete")
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
        except Exception as e:
            print(e)