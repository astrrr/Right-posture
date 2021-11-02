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
import platform
import time
from modules import *
from widgets import *
from modules.setup_main_window import SetupMainWindow
from widgets.py_toggle import PyToggle
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        # APP NAME
        title = "Right Posture"
        description = "Right Posture - Make life better."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)
        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        autoClose = True  # Toggle Auto Close Left Box when click.
        if autoClose:
            widgets.btn_Camera.clicked.connect(openCloseLeftBox)
            widgets.btn_Notification.clicked.connect(openCloseLeftBox)
            widgets.btn_Logout.clicked.connect(openCloseLeftBox)
        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        # SHOW APP
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

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.Home)
        widgets.btn_Home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_Home.styleSheet()))

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
        SetupMainWindow.addWidget(self)

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

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
        #AppFunctions.notifyMe("ไปนอนซะ","eiei")

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
    window = MainWindow()
    # TOGGLE Discord Rich Presence
    # *** Not recommended if discord doesn't running in background ***
    AppFunctions.discordRichPresence(False)
    sys.exit(app.exec())