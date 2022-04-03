import os
import sqlite3
from main import MainWindow
from modules import UIFunctions, AppFunctions
from modules.app_data import Main_data
from modules.app_temp import superuser

cwd = os.getcwd()
cwd = cwd+'/Right Posture'
acc_path = f"{cwd}/bin/Data/Accounts.db"

class Main_buttons(MainWindow):

    def defineButtons(self):
        button = self.ui
        button.btn_Home.clicked.connect(self.Main_button_Interface)
        button.btn_Log.clicked.connect(self.Main_button_Interface)
        button.btn_Setting.clicked.connect(self.Main_button_Interface)
        button.btn_Logout.clicked.connect(self.Main_button_Interface)
        button.btn_clear_log.clicked.connect(self.Main_button_Interface)
        button.btn_save_setting.clicked.connect(self.Main_button_Interface)
        button.btn_reload.clicked.connect(self.Main_button_Interface)
        button.btn_test_notify.clicked.connect(self.Main_button_Interface)
        button.btn_test_email.clicked.connect(self.Main_button_Interface)
        # Show Camera
        button.show_camera.clicked.connect(self.Camera_1)
        # Show Detail
        button.show_detail.clicked.connect(self.Main_button_Interface)

    def buttonClick(self):
        button = self.ui
        btn = self.sender()
        btnName = btn.objectName()

        # ////////// CHECK BOX ZONE //////////
        if btnName == "show_detail":
            Main_data.Show_Detail(self)
        # ////////////////////////////////////

        if btnName == "btn_Logout":
            self.Logout()

        if btnName == "btn_clear_log":
            self.ui.Detect_LOG.clear()

        if btnName == "btn_Home":
            button.stackedWidget.setCurrentWidget(button.Home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_Log":
            button.stackedWidget.setCurrentWidget(button.Log)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_Setting":
            button.stackedWidget.setCurrentWidget(button.Setting)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_test_email":
            conn = sqlite3.connect(acc_path)
            cur = conn.cursor()
            query = f"SELECT email FROM login_info WHERE username = \'{superuser.user}\'"
            cur.execute(query)
            try:
                email = cur.fetchone()[0]
                # print(email)
                AppFunctions.send_Email(self, text=f"This is test e-mail", to_emails=[email])
                self.ui.Setting_log.append(f"E-mail has been send to {email}")
            except Exception as e:
                print(e)
                self.ui.Setting_log.append(f"Fail to send e-mail please check your internet connection.\n{str(e)}")

        if btnName == "btn_test_notify":
            try:
                AppFunctions.notifyMe(self, "Test notify", "Notification work correctly")
                self.ui.Setting_log.append(f"Notification work correctly")
            except Exception as e:
                print(e)
                self.ui.Setting_log.append(f"Fail to notify unknown error.\n{str(e)}")

        if btnName == "btn_reload":
            Main_data.Load_table(self)
            print("Reloaded")

        if btnName == "btn_save_setting":
            Main_data.save_setting(self)

        # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')

    def set_custom_theme(self, enable):
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = enable
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.btn_Home.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_Home.styleSheet()))