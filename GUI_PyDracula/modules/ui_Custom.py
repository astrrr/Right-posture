from widgets.py_toggle import PyToggle

class ui_Custom:

    def addWidget(self):
        self.toggle = PyToggle()
        self.ui.Toggle_Night_Layout.addWidget(self.toggle)