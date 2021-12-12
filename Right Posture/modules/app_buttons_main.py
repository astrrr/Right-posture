from main import MainWindow
from modules import UIFunctions, AppFunctions, load_data
from modules.app_checkbox import Main_checkbox
import traceback
import sys
class Main_buttons(MainWindow):

    def defineButtons(self):
        button = self.ui
        loaded_object = load_data()
        button.btn_Home.clicked.connect(self.Main_button_Interface)
        button.btn_Status.clicked.connect(self.Main_button_Interface)
        button.btn_Posture.clicked.connect(self.Main_button_Interface)
        button.btn_Tutorial.clicked.connect(self.Main_button_Interface)
        button.btn_Camera.clicked.connect(self.Main_button_Interface)
        button.btn_Notification.clicked.connect(self.Main_button_Interface)
        button.btn_Logout.clicked.connect(self.Main_button_Interface)
        button.btn_saveNotify.clicked.connect(self.Main_button_Interface)
        button.btn_print.clicked.connect(self.Main_button_Interface)
        button.btn_clear_log.clicked.connect(self.Main_button_Interface)

        # button.Test_radioButton_1.clicked.connect(self.Main_button_Interface)

        # Preview Detail
        button.show_detail.setChecked(loaded_object["PreDetail"])
        button.show_detail.clicked.connect(self.Main_button_Interface)

        # Preview Detect log
        button.show_log.setChecked(loaded_object["PreLog"])
        button.show_log.clicked.connect(self.Main_button_Interface)

        # Preview Camera 1
        button.pre_cam_1.setChecked(loaded_object["PreCam1"])
        button.pre_cam_1.clicked.connect(self.Camera_1)
        self.Camera_1()

        # Discord Rich Presence
        AppFunctions.discordRichPresence(loaded_object["Discord"])

    def buttonClick(self):
        button = self.ui
        btn = self.sender()
        btnName = btn.objectName()

        # ////////// CHECK BOX ZONE //////////
        if btnName == "show_log":
            Main_checkbox.Detect_Log(self)

        if btnName == "show_detail":
            Main_checkbox.Show_Detail(self)
        # ////////////////////////////////////

        if btnName == "btn_Logout":
            self.Logout()

        if btnName == "btn_clear_log":
            self.ui.Detect_LOG.clear()

        if btnName == "btn_Home":
            button.stackedWidget.setCurrentWidget(button.Home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_Status":
            button.stackedWidget.setCurrentWidget(button.Status)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_Posture":
            button.stackedWidget.setCurrentWidget(button.Posture)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_Tutorial":
            button.stackedWidget.setCurrentWidget(button.Tutorial)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_Notification":
            button.stackedWidget.setCurrentWidget(button.Notification)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED

        if btnName == "btn_saveNotify":
            print(button.notifyword.text())
            AppFunctions.notifyMe("ไปนอนซะ", button.notifyword.text())

        if btnName == "btn_print":
            try:
                AppFunctions.notifyMe(self, "Debug", "Notification")
            except:
                traceback.print_exc()
                excType, value = sys.exc_info()[:2]
                self.ui.Detail_text.append = f"\nException error\n{excType}\n{value}\n{traceback.format_exc()}"
        # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')