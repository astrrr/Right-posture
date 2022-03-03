from main import *

class UILoginFunctions:
    def Function_Login_Setup(self):
        self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Login_page)

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

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

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_to_Auth_key(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 60, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -600, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def animation_back_to_Forget(self):
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