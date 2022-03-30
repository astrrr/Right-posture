from main import MainWindow
from modules import UIFunctions, AppFunctions
from modules.app_data import Main_data

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
            AppFunctions.send_Email(self, text=f"This is test e-mail", to_emails=['inwpbmak@gmail.com'])
            AppFunctions.notifyMe(self, "Test E-mail", "E-mail has been sent")

        if btnName == "btn_test_notify":
            AppFunctions.notifyMe(self, "Test notify", "Notification work correctly")

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