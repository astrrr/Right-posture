from main import *
from widgets.py_toggle import PyToggle

class ui_Custom:
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def addWidget(self):
        widgets = self.ui
        widgets.tableWidget.setColumnWidth(0, 20)

        Toggle_NightMode = PyToggle()
        widgets.Toggle_Night_Layout.addWidget(Toggle_NightMode)

        Toggle_Close = PyToggle()
        widgets.Toggle_Close_Layout.addWidget(Toggle_Close)

        Toggle_Sound = PyToggle()
        widgets.Toggle_Sound_Layout.addWidget(Toggle_Sound)

    def setup_gui(self):
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        # APP NAME
        title = "Right Posture"
        description = "Right Posture - Make life better."

        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

