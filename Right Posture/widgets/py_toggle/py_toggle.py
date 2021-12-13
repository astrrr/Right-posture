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

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from main import Ui_MainWindow
from modules.app_data import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

Toggle1 = None
Toggle2 = None
Toggle3 = None
Toggle4 = None
loaded_object = load_data()

class PyToggle(QCheckBox):
    def __init__(
        self,
        width = 50,
        bg_color = "#343B48",
        circle_color = "#DDD",
        active_color = "#BD93F9",
        animation_curve = QEasingCurve.OutBounce
    ):
        QCheckBox.__init__(self)
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        # COLORS
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color
        self._position = 3
        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)
        self.ui = Ui_MainWindow()
        global Toggle1, Toggle2, Toggle3, Toggle4
        Toggle1 = self.setup_animation_1
        Toggle2 = self.setup_animation_2
        Toggle3 = self.setup_animation_3
        Toggle4 = self.setup_animation_4

    def Toggle_Switch(self):
        Toggle = self.ui

        Toggle_LightMode = PyToggle()
        Toggle.Toggle_Light_Layout.addWidget(Toggle_LightMode)
        Toggle_LightMode.stateChanged.connect(Toggle1)
        Light = loaded_object["Light"]
        Toggle_LightMode.setChecked(Light)

        Toggle_Close = PyToggle()
        Toggle.Toggle_Close_Layout.addWidget(Toggle_Close)
        Toggle_Close.stateChanged.connect(Toggle2)
        Close = loaded_object["Close"]
        Toggle_Close.setChecked(Close)

        Toggle_Sound = PyToggle()
        Toggle.Toggle_Sound_Layout.addWidget(Toggle_Sound)
        Toggle_Sound.stateChanged.connect(Toggle3)
        Sound = loaded_object["Sound"]
        Toggle_Sound.setChecked(Sound)

        Toggle_Discord = PyToggle()
        Toggle.Toggle_Discord_Layout.addWidget(Toggle_Discord)
        Toggle_Discord.stateChanged.connect(Toggle4)
        Discord = loaded_object["Discord"]
        Toggle_Discord.setChecked(Discord)

    def setup_animation_1(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
            print("Status : ON Light Mode")
            save_data("Light", 1)
        else:
            self.animation.setEndValue(4)
            print("Status : OFF Light Mode")
            save_data("Light", 0)
        self.animation.start()

    def setup_animation_2(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
            print("Status : ON Auto Close")
            save_data("Close", 1)
        else:
            self.animation.setEndValue(4)
            print("Status : OFF Close")
            save_data("Close", 0)
        self.animation.start()

    def setup_animation_3(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
            print("Status : ON Sound")
            save_data("Sound", 1)
        else:
            self.animation.setEndValue(4)
            print("Status : OFF Sound")
            save_data("Sound", 0)
        self.animation.start()

    def setup_animation_4(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
            print("Status : ON Discord")
            save_data("Discord", 1)
        else:
            self.animation.setEndValue(4)
            print("Status : OFF Discord")
            save_data("Discord", 0)
        self.animation.start()

    @Property(float)
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
        self.update()

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setFont(QFont("Segoe UI", 9))

        # SET PEN
        p.setPen(Qt.NoPen)

        # DRAW RECT
        rect = QRect(0, 0, self.width(), self.height())        

        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0,0,rect.width(), 28, 14, 14)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._position, 3, 22, 22)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0,0,rect.width(), 28, 14, 14)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._position, 3, 22, 22)

        p.end()