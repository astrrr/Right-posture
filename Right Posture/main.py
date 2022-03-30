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

from PySide6 import QtCore, QtGui, QtCharts
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from modules.Version_control import version, Debug_path

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# main "1" = MainWindow , main "0" = AuthWindow
main = 1
version.thisVersion = "1.1.6.9"
# /////////////////////////////////////////////
counter = 0
CircularProgress_timer = 300
# /////////////////////////////////////////////
class AuthWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        UILoginFunctions.Function_Login_Setup(self)
        UIFunctions.LoginUiDefinitions(self)
        Auth_buttons.defineButtons(self)
        self.ui.Login_Status.setText("Login")
        self.ui.Reg_Status.setText("Register")
        self.show()

    def open_main(self):
        username = self.ui.username.text()
        self.main = MainWindow()
        if username == "":
            username = "Guest"
        Camera_detail.user = username
        Main_setting.load_setting(self.main, username)
        self.main.ui.titleRightInfo.setText(f"Welcome {username.capitalize()} to Right Posture")
        self.main.show()
        self.close()

    # ENTER EVENT
    # ///////////////////////////////////////////////////////////////
    def enter_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            Auth_system.check_login(self, False)

    def enter_regis(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            Auth_system.check_register(self)

    def enter_forget(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            Auth_system.check_email(self)

    def enter_auth(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            Auth_system.change_password(self)

    # BUTTONS INTERFACE TO app_button_login
    def Login_button_Interface(self):
        Auth_buttons.buttonClick(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UIFunctions.Function_Main_Setup(self)
        Main_buttons.defineButtons(self)
        self.show()
        Main_buttons.set_custom_theme(self, False)
        Main_table.Load_table(self, 'a')
        # Main_table.Load_Table(self)

        self.Donut_charts()
        self.ui.Donut_Frame_Layout.addWidget(self.chartview)

        self.ui.Line_Frame_Layout.addWidget(Line_charts())

    def Donut_charts(self):
        data = {
            "Correct 70%": (70, QtGui.QColor("#bd93f9")),
            "Incorrect 30%": (30, QtGui.QColor("#ff79c6")),
        }

        series = QtCharts.QPieSeries()
        series.setHoleSize(0.4)
        for name, (value, color) in data.items():
            _slice = series.append(name, value)
            _slice.setBrush(color)

        chart = QtCharts.QChart()
        chart.setContentsMargins(-10, -10, -10, -10)
        chart.addSeries(series)
        chart.setTitle("Test donut chart")
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)
        chart.legend().setFont(QtGui.QFont("Arial", 10))

        self.chartview = QtCharts.QChartView(chart)
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)

    # UPDATE PROGRESS BAR
    def update(self):
        global counter
        self.progress.set_value(counter)
        if counter >= 100:
            # STOP TIMER
            if Camera_detail.Finish_load_model:
                self.timer.stop()
                Camera_detail.First_load_model = False
                Camera_detail.start_cam = True
                Camera.detect(self, False)
                Camera.detect(self, True)
                self.progress.setParent(None)
                self.progress.close()
                Main_checkbox.Show_Detail(self)
                self.ui.Camera_Frame_1_Layout.removeWidget(self.ui.Camera1_label)
                self.ui.pre_cam_1.setEnabled(True)
            else:
                Camera_detail.model_status = "Waiting for model."
                Main_checkbox.Show_Detail(self)
        else:
            if Camera_detail.Finish_load_model:
                if counter < 50:
                    QTimer.singleShot(500, lambda: set_counter(65))
                elif counter < 68:
                    QTimer.singleShot(500, lambda: set_counter(87))
                elif counter < 88:
                    counter = 95

            if Camera_detail.Error_load_model:
                self.timer.stop()
                Main_checkbox.Show_Detail(self)
                self.ui.pre_cam_1.setEnabled(True)
            counter += 1

    def Camera_1(self):
        global counter
        if Camera_detail.First_load_model:
            self.ui.Camera1_label.setText("The model hasn't loaded yet.")
        else:
            self.ui.Camera1_label.setText("The model is loaded.")

        if self.ui.pre_cam_1.isChecked():
            if Camera_detail.First_load_model:
                counter = 0
                Camera_detail.model_status = "Loading model"
                Main_checkbox.Show_Detail(self)
                self.ui.pre_cam_1.setEnabled(False)
                self.ui.Camera1_label.setText(" ")
                self.timer = QTimer()
                self.timer.timeout.connect(self.update)
                self.timer.start(CircularProgress_timer)
                self.progress.setParent(self.ui.Camera_Frame_1)
                self.progress.show()
            Main_checkbox.camera_status = "ON"
            Main_checkbox.Show_Detail(self)
            self.ui.Camera_Frame_1_Layout.removeWidget(self.ui.Camera1_label)
            Camera.detect(self, True)
            save_data("PreCam1", 1)
            # print("Start Camera_1")
        else:
            counter = 0
            Main_checkbox.camera_status = "OFF"
            Main_checkbox.Show_Detail(self)
            self.ui.Camera_Frame_1_Layout.addWidget(self.ui.Camera1_label)
            self.ui.Camera1_label.setAlignment(Qt.AlignCenter)
            self.progress.setParent(None)
            self.progress.close()
            Camera_detail.Error_load_model = False
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
            qImg = QtGui.QImage(cv_img.data, cv_img.shape[1], cv_img.shape[0], cv_img.strides[0],
                                QtGui.QImage.Format.Format_BGR888)
            qPix = QPixmap.fromImage(qImg)
            self.image_label.setPixmap(qPix)
            if Camera_detail.Update_log:
                Main_checkbox.Detect_Log(self)
            if Camera_detail.Error_load_model:
                Main_checkbox.Show_Detail(self)
        except:
            pass

    # BUTTONS INTERFACE TO app_button_main
    def Main_button_Interface(self):
        Main_buttons.buttonClick(self)

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()
        
    def Logout(self):
        QTimer.singleShot(500, lambda: open_Login())
        def open_Login():
            self.Login = AuthWindow()
            self.Login.show()
            self.close()

def set_counter(value):
    global counter
    counter = value

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    if main:
        windows = MainWindow()
    else:
        windows = AuthWindow()

    sys.exit(app.exec())