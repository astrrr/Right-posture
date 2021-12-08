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

from modules.app_detect import VideoThread
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None
counter = 0
CircularProgress_timer = 300
model_status = "Not loaded"

class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        UILoginFunctions.Function_Login_Setup(self)
        UIFunctions.LoginUiDefinitions(self)
        self.ui.title_bar_3.setText("Login V1 Right Posture")
        self.ui.Login_Status.setText("Login")
        self.ui.Reg_Status.setText("Register")
        self.show()

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_Login":
            self.check_login()

        if btnName == "btn_Register":
            self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Register_page)

        if btnName == "btn_Fpassword":
            UILoginFunctions.animation_to_Forget(self)

        if btnName == "btn_Reg_Back":
            self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Login_page)

        if btnName == "btn_Forget_Back":
            UILoginFunctions.animation_back_to_Login(self)

        if btnName == "btn_Com_Register":
            self.check_register()

    def check_register(self):
        username = self.ui.Reg_username.text()
        password = self.ui.Reg_password.text()
        con_Password = self.ui.Reg_password_2.text()
        email = self.ui.Reg_email.text()

        if len(username) == 0 or len(password) == 0 or len(con_Password) == 0 or len(email) == 0:
            self.ui.Reg_Status.setText("Please fill in all inputs.")
            self.regis_fail()
        elif password != con_Password:
            self.ui.Reg_Status.setText("Passwords do not match.")
            self.regis_fail()
        else:
            conn = sqlite3.connect("bin/Data/Accounts.db")
            cur = conn.cursor()
            user_info = [username, password, email]
            try:
                cur.execute('INSERT INTO login_info (username, password, email) VALUES (?,?,?)', user_info)
                conn.commit()
                conn.close()
                self.ui.Reg_username.clear()
                self.ui.Reg_password.clear()
                self.ui.Reg_password_2.clear()
                self.ui.Reg_email.clear()
                self.ui.Reg_Status.setStyleSheet("#Reg_Status { color: #50fa7b }")
                self.ui.Reg_username.setStyleSheet("#Reg_username:focus { border: 2px solid rgb(91, 101, 124); }")
                self.ui.Reg_password.setStyleSheet("#Reg_password:focus { border: 2px solid rgb(91, 101, 124); }")
                self.ui.Reg_password_2.setStyleSheet("#Reg_password_2:focus { border: 2px solid rgb(91, 101, 124); }")
                self.ui.Reg_email.setStyleSheet("#Reg_email:focus { border: 2px solid rgb(91, 101, 124); }")
                self.ui.Reg_Status.setText("Register Complete !")
            except:
                self.ui.Reg_Status.setText("This username is already registered in the database.")
                self.regis_fail()

    def check_login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        def open_main():
            self.main = MainWindow()
            self.main.ui.titleRightInfo.setText(f"Welcome {username.capitalize()} to Right Posture")
            self.main.show()
            self.close()

        if len(username) == 0 or len(password) == 0:
            self.ui.Login_Status.setText("Please input all fields.")
            self.login_fail()
        else:
            conn = sqlite3.connect("bin/Data/Accounts.db")
            cur = conn.cursor()
            query = 'SELECT password FROM login_info WHERE username =\'' + username + "\'"
            cur.execute(query)
            try:
                result_pass = cur.fetchone()[0]
                if result_pass == password:
                    self.ui.Login_Status.setText(f"Welcome {username} !")
                    self.ui.Login_Status.setStyleSheet("#Login_Status { color: #50fa7b }")
                    self.ui.username.setStyleSheet("#username:focus { border: 3px solid #50fa7b; }")
                    self.ui.password.setStyleSheet("#password:focus { border: 3px solid #50fa7b; }")
                    QTimer.singleShot(1200, lambda: open_main())
                else:
                    self.ui.Login_Status.setText("Invalid username or password")
                    self.login_fail()
            except:
                self.ui.Login_Status.setText("Invalid username or password")
                self.login_fail()

    def regis_fail(self):
        self.ui.Reg_Status.setStyleSheet("#Reg_Status { color: #ff5555 }")
        self.ui.Reg_username.setStyleSheet("#Reg_username:focus { border: 2px solid #ff5555; }")
        self.ui.Reg_password.setStyleSheet("#Reg_password:focus { border: 2px solid #ff5555; }")
        self.ui.Reg_password_2.setStyleSheet("#Reg_password_2:focus { border: 2px solid #ff5555; }")
        self.ui.Reg_email.setStyleSheet("#Reg_email:focus { border: 2px solid #ff5555; }")
        UILoginFunctions.shake_window(self)

    def login_fail(self):
        self.ui.Login_Status.setStyleSheet("#Login_Status { color: #ff5555 }")
        self.ui.username.setStyleSheet("#username:focus { border: 2px solid #ff5555; }")
        self.ui.password.setStyleSheet("#password:focus { border: 2px solid #ff5555; }")
        UILoginFunctions.shake_window(self)

    def enter_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.check_login()

    def enter_regis(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.check_register()

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

    def Show_Detail(self):
        if self.ui.show_detail.isChecked():
            self.ui.Detail_text.setText(f"Camera: 1 (VideoCapture(0))\n"
                                        f"Model: MNv2_V3 ({model_status})")
            save_data("PreDetail", 1)
            # print("Start Detail")
        else:
            self.ui.Detail_text.clear()
            save_data("PreDetail", 0)
            # print("Stop Detail")

    def Detect_Log(self):
        if self.ui.show_log.isChecked():
            self.ui.Detect_LOG.append(Camera.log)
            save_data("PreLog", 1)
            # print("Start Logging")
        else:
            save_data("PreLog", 0)
            # print("Stop Logging")

    # UPDATE PROGRESS BAR
    def update(self):
        global counter
        global model_status
        self.progress.set_value(counter)
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            Camera.First_load_model = False
            Camera.start_cam = True
            Camera.detect(self, False)
            Camera.detect(self, True)
            self.progress.setParent(None)
            self.progress.close()
            model_status = "Loaded"
            self.Show_Detail()
            self.ui.Camera_Frame_1_Layout.removeWidget(self.ui.Camera1_label)
            self.ui.pre_cam_1.setEnabled(True)
        counter += 1

    def Camera_1(self):
        if Camera.First_load_model:
            self.ui.Camera1_label.setText("The model hasn't loaded yet.")
        else:
            self.ui.Camera1_label.setText("The model is loaded.")

        if self.ui.pre_cam_1.isChecked():
            if Camera.First_load_model:
                self.ui.pre_cam_1.setEnabled(False)
                self.ui.Camera1_label.setText(" ")
                self.timer = QTimer()
                self.timer.timeout.connect(self.update)
                self.timer.start(CircularProgress_timer)
                self.progress.setParent(self.ui.Camera_Frame_1)
                self.progress.show()
            self.ui.Camera_Frame_1_Layout.removeWidget(self.ui.Camera1_label)
            Camera.detect(self, True)
            save_data("PreCam1", 1)
            # print("Start Camera_1")
        else:
            self.ui.Camera_Frame_1_Layout.addWidget(self.ui.Camera1_label)
            self.ui.Camera1_label.setAlignment(Qt.AlignCenter)
            Camera.detect(self, False)
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
            self.Detect_Log()
        except:
            pass

    # BUTTONS CLICK Add button here and above
    def buttonInterface(self):
        AppButtons.buttonClick(self)

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    # windows = MainWindow()
    windows = LoginWindow()

    sys.exit(app.exec())