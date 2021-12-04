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
import sqlite3

from modules import *
from widgets import *

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None
counter = 0

class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        UILoginFunctions.Function_Login_Setup(self)
        UIFunctions.LoginUiDefinitions(self)
        self.ui.title_bar_3.setText("Login V1 Right Posture")

        self.show()

    def buttonClick(self):
        button = self.ui
        btn = self.sender()
        btnName = btn.objectName()
        # print(btnName)

        if btnName == "btn_Login":
            self.check_login()

        if btnName == "btn_Register":
            self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Register_page)

        if btnName == "btn_Fpassword":
            UILoginFunctions.animation_to_Forget(self)
            # self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Forget_page)

        if btnName == "btn_Reg_Back":
            self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Login_page)

        if btnName == "btn_Forget_Back":
            UILoginFunctions.animation_back_to_Login(self)
            # self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Login_page)

    def check_enter(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.check_login()
    # CHECK LOGIN
    # ///////////////////////////////////////////////////////////////
    def check_login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        def open_main():
            self.main = MainWindow()
            self.main.ui.titleRightInfo.setText(f"Welcome {username.capitalize()} to Right Posture")
            self.main.show()
            self.close()

        if len(username) == 0 or len(password) == 0:
            self.ui.user_description.setText("Please input all fields.")
            self.login_fail()
        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()
            query = 'SELECT password FROM login_info WHERE username =\'' + username + "\'"
            cur.execute(query)
            try:
                result_pass = cur.fetchone()[0]
                if result_pass == password:
                    self.ui.user_description.setText(f"Welcome {username} !")
                    self.ui.user_description.setStyleSheet("#user_description { color: #bd93f9 }")
                    self.ui.username.setStyleSheet("#username:focus { border: 3px solid #bd93f9; }")
                    self.ui.password.setStyleSheet("#password:focus { border: 3px solid #bd93f9; }")
                    QTimer.singleShot(1200, lambda: open_main())
                else:
                    self.ui.user_description.setText("Invalid username or password")
                    self.login_fail()
            except:
                self.ui.user_description.setText("Invalid username or password")
                self.login_fail()

    def login_fail(self):
        self.ui.user_description.setStyleSheet("#user_description { color: #ff79c6 }")
        self.ui.username.setStyleSheet("#username:focus { border: 2px solid #ff79c6; }")
        self.ui.password.setStyleSheet("#password:focus { border: 2px solid #ff79c6; }")
        UILoginFunctions.shake_window(self)

    # UPDATE PROGRESS BAR
    # ///////////////////////////////////////////////////////////////
    # def update(self):
    #     global counter
    #
    #     # SET VALUE TO PROGRESS BAR
    #     self.progress.set_value(counter)
    #
    #     # CLOSE SPLASH SCREEN AND OPEN MAIN APP
    #     if counter >= 100:
    #         # STOP TIMER
    #         self.timer.stop()
    #         UILoginFunctions.animation_login(self)
    #     # INCREASE COUNTER
    #     counter += 1

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        UIFunctions.Function_Main_Setup(self)
        AppButtons.defineButtons(self)
        PyToggle.Toggle_Switch(self)
        self.show()

    #     self.Load_Table()
    # def Load_Table(self):
    #     people = [{"test": "james", "text": "idk", "cell": "eiei", "Line": "las"},
    #               {"test": "eak", "text": "idk", "cell": "eiei", "Line": "las"},
    #               {"test": "sun", "text": "idk", "cell": "eiei", "Line": "las"},
    #               {"test": "cry", "text": "idk", "cell": "eiei", "Line": "las"},
    #               {"test": "a", "text": "idk", "cell": "eiei", "Line": "las"},
    #               {"test": "lot", "text": "idk", "cell": "eiei", "Line": "las"}]
    #     table_row = 0
    #     self.ui.Status_Widgets.setRowCount(len(people))
    #     for row in people:
    #         self.ui.Status_Widgets.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row["test"]))
    #         table_row += 1

    # BUTTONS CLICK Add button here and above
    def buttonInterface(self):
        AppButtons.buttonClick(self)

    def Camera_1(self):
        if widgets.pre_cam_1.isChecked():
            Start_Camera.detect(self, True)
            save_data("PreCam1", 1)
            # print("Start Camera_1")
        else:
            Start_Camera.detect(self, False)
            save_data("PreCam1", 0)
            # print("Stop Camera_1")

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

    # windows = MainWindow()
    windows = LoginWindow()

    sys.exit(app.exec())