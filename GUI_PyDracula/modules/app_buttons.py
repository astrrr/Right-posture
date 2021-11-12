from main import MainWindow
from modules import UIFunctions, AppFunctions, load_data

class AppButtons(MainWindow):

    def defineButtons(self):
        button = self.ui
        loaded_object = load_data()
        button.btn_Home.clicked.connect(self.buttonInterface)
        button.btn_Status.clicked.connect(self.buttonInterface)
        button.btn_Posture.clicked.connect(self.buttonInterface)
        button.btn_Tutorial.clicked.connect(self.buttonInterface)
        button.btn_Widgets.clicked.connect(self.buttonInterface)
        button.btn_Camera.clicked.connect(self.buttonInterface)
        button.btn_Notification.clicked.connect(self.buttonInterface)
        button.btn_Logout.clicked.connect(self.buttonInterface)
        button.btn_saveNotify.clicked.connect(self.buttonInterface)
        button.btn_print.clicked.connect(self.buttonInterface)

        # button.Test_radioButton_1.clicked.connect(self.buttonInterface)

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

        if btnName == "btn_Widgets":
            button.stackedWidget.setCurrentWidget(button.Widgets)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_Notification":
            button.stackedWidget.setCurrentWidget(button.Notification)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED

        if btnName == "btn_saveNotify":
            print(button.notifyword.text())
            AppFunctions.notifyMe("ไปนอนซะ", button.notifyword.text())

        if btnName == "btn_print":
            print(button.notifyword.text())
            AppFunctions.notifyMe("Debug", "Notification")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')