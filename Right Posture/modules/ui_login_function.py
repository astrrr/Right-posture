from main import *

class UILoginFunctions:
    def Function_Login_Setup(self):
        self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Login_page)
        # ADD BUTTON
        # ///////////////////////////////////////////////////////////////
        self.ui.btn_Login.clicked.connect(self.buttonClick)
        self.ui.btn_Register.clicked.connect(self.buttonClick)
        self.ui.btn_Fpassword.clicked.connect(self.buttonClick)

        self.ui.btn_Com_Register.clicked.connect(self.buttonClick)
        self.ui.btn_Reg_Back.clicked.connect(self.buttonClick)

        # self.ui.btn_Forget_Email.clicked.connect(self.buttonClick)
        # self.ui.btn_Forget_Back.clicked.connect(self.buttonClick)

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        # ///////////////////////////////////////////////////////////////
        # self.progress = CircularProgress()
        # self.progress.width = 240
        # self.progress.height = 240
        # self.progress.value = 0
        # self.progress.setFixedSize(self.progress.width, self.progress.height)
        # self.progress.font_size = 20
        # self.progress.add_shadow(True)
        # self.progress.progress_width = 4
        # self.progress.progress_color = QColor("#ff79c6")
        # self.progress.text_color = QColor("#E6E6E6")
        # self.progress.bg_color = QColor("#222222")
        # self.progress.setParent(self.ui.preloader)
        # self.progress.show()

        # ADD DROP SHADOW
        # ///////////////////////////////////////////////////////////////
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.bg.setGraphicsEffect(self.shadow)

        # QTIMER
        # ///////////////////////////////////////////////////////////////
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        self.ui.username.keyReleaseEvent = self.check_enter
        self.ui.password.keyReleaseEvent = self.check_enter

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_to_Forget(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 60, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -600, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def animation_back_to_Login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, -600, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, 60, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def shake_window(self):
        # SHAKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))