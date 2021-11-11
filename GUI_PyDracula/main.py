# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import numpy as np

from modules import *
from widgets import *

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None
Camera = None
counter = 0

loaded_object = None

class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_login.py"
        # Load widgets inside LoginWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        UILoginFunctions.Function_Login_Setup(self)
        UIFunctions.LoginUiDefinitions(self)
        self.show()

    # CHECK LOGIN
    # ///////////////////////////////////////////////////////////////
    def check_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()

            def open_main():
                # SHOW MAIN WINDOW
                self.main = MainWindow()
                self.main.ui.titleRightInfo.setText(f"Welcome {username.capitalize()} to Right Posture")
                self.main.show()
                self.close()

            if username and password == "123456":
                self.ui.user_description.setText(f"Welcome {username} !")
                self.ui.user_description.setStyleSheet("#user_description { color: #bd93f9 }")
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid #bd93f9; }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid #bd93f9; }")
                QTimer.singleShot(1200, lambda: open_main())
            else:
                # SET STYLESHEET
                self.ui.username.setStyleSheet("#username:focus { border: 2px solid #ff79c6; }")
                self.ui.password.setStyleSheet("#password:focus { border: 2px solid #ff79c6; }")
                self.shacke_window()

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    # UPDATE PROGRESS BAR
    # ///////////////////////////////////////////////////////////////
    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            self.animation_login()

        # INCREASE COUNTER
        counter += 1

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets, Camera, loaded_object
        widgets = self.ui
        UIFunctions.Function_Main_Setup(self)
        PyToggle.Toggle_Switch(self)

        loaded_object = load_data()

        self.show()
        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"
        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)


    #     self.loaddata()
    # def loaddata(self):
    #     people = [{"test": "jjames", "text": "idk", "cell": "eiei", "Line": "las"},
    #               {"test": "qwrdsfsdf", "text": "idk", "cell": "eiei", "Line": "las"},
    #               {"test": "48151262", "text": "idk", "cell": "eiei", "Line": "las"}]
    #     tablerow = 0
    #     self.ui.tableWidget.setRowCount(len(people))
    #     for row in people:
    #         self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row["test"]))
    #         tablerow += 1

        # BUTTONS CLICK Don't forget to add button here
        widgets.btn_Home.clicked.connect(self.buttonClick)
        widgets.btn_Status.clicked.connect(self.buttonClick)
        widgets.btn_Posture.clicked.connect(self.buttonClick)
        widgets.btn_Tutorial.clicked.connect(self.buttonClick)
        widgets.btn_Widgets.clicked.connect(self.buttonClick)
        widgets.btn_Camera.clicked.connect(self.buttonClick)
        widgets.btn_Notification.clicked.connect(self.buttonClick)
        widgets.btn_Logout.clicked.connect(self.buttonClick)
        widgets.btn_saveNotify.clicked.connect(self.buttonClick)
        widgets.btn_print.clicked.connect(self.buttonClick)

        # Preview Camera 1
        widgets.pre_cam_1.setChecked(loaded_object["PreCam1"])
        widgets.pre_cam_1.clicked.connect(self.Camera_1)
        self.Camera_1()

        # Discord Rich Presence
        AppFunctions.discordRichPresence(loaded_object["Discord"])

    # BUTTONS CLICK Add button here and above
    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_Home":
            widgets.stackedWidget.setCurrentWidget(widgets.Home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_Status":
            widgets.stackedWidget.setCurrentWidget(widgets.Status)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_Posture":
            widgets.stackedWidget.setCurrentWidget(widgets.Posture) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_Tutorial":
            widgets.stackedWidget.setCurrentWidget(widgets.Tutorial) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_Widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.Widgets)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_Notification":
            widgets.stackedWidget.setCurrentWidget(widgets.Notification)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
        if btnName == "btn_saveNotify":
            print(widgets.notifyword.text())
            AppFunctions.notifyMe("ไปนอนซะ", widgets.notifyword.text())
        if btnName == "btn_print":
            print(widgets.notifyword.text())
            AppFunctions.notifyMe("Debug", "Notification")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def Camera_1(self):
        if widgets.pre_cam_1.isChecked():
            Start_Camera.detect(self, True)
            save_data("PreCam1", 1)
            print("Start Camera")
        else:
            Start_Camera.detect(self, False)
            save_data("PreCam1", 0)
            print("Stop Camera")

    def closeEvent(self, event):
        try:
            self.thread.stop()
            event.accept()
        except:
            pass

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        try:
            # img = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
            # QT側でチャネル順BGRを指定
            qimg = QtGui.QImage(cv_img.data, cv_img.shape[1], cv_img.shape[0], cv_img.strides[0],
                                QtGui.QImage.Format.Format_BGR888)
            qpix = QPixmap.fromImage(qimg)
            self.image_label.setPixmap(qpix)
        except:
            pass

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    windows = MainWindow()
    # windows = LoginWindow()

    sys.exit(app.exec())