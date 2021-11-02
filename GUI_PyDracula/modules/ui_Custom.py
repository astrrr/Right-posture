from widgets.py_toggle import PyToggle

class ui_Custom:

    def addWidget(self):
        Toggle_NightMode = PyToggle()
        self.ui.Toggle_Night_Layout.addWidget(Toggle_NightMode)
        Toggle_Close = PyToggle()
        self.ui.Toggle_Close_Layout.addWidget(Toggle_Close)
        Toggle_Sound = PyToggle()
        self.ui.Toggle_Sound_Layout.addWidget(Toggle_Sound)