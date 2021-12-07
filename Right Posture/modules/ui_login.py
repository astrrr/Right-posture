# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginFSKCYB.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
from .resources_rc import *

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(900, 710)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QSize(900, 710))
        Login.setMaximumSize(QSize(900, 1000))
        Login.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bg {	\n"
"	background-color: rgb(4"
                        "0, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#top_bar{	\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"/* Top Buttons */\n"
"#top_btns_3 .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#top_btns_3 .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#top_btns_3 .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5p"
                        "x;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(1000, 1200))
        self.centralwidget.setStyleSheet(u"#stackedWidget{\n"
"	background: transparent;\n"
"		border: 1px solid red;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setMaximumSize(QSize(1000, 1200))
        self.bg.setFrameShape(QFrame.NoFrame)
        self.bg.setFrameShadow(QFrame.Raised)
        self.frame_widgets = QFrame(self.bg)
        self.frame_widgets.setObjectName(u"frame_widgets")
        self.frame_widgets.setGeometry(QRect(0, 60, 878, 811))
        self.frame_widgets.setMinimumSize(QSize(280, 720))
        self.frame_widgets.setMouseTracking(False)
        self.frame_widgets.setFrameShape(QFrame.NoFrame)
        self.frame_widgets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_widgets)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 0, 20, 10)
        self.Login_stackedWidget = QStackedWidget(self.frame_widgets)
        self.Login_stackedWidget.setObjectName(u"Login_stackedWidget")
        self.Login_stackedWidget.setStyleSheet(u"/*background: transparent;*/")
        self.Login_page = QWidget()
        self.Login_page.setObjectName(u"Login_page")
        self._2 = QVBoxLayout(self.Login_page)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(-1, -1, 9, -1)
        self.logo = QFrame(self.Login_page)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 400))
        self.logo.setMaximumSize(QSize(16777215, 400))
        self.logo.setStyleSheet(u"#logo {\n"
"	background-image: url(:/images/images/images/Logo_Big (8).png);\n"
"	/*background-image: url(:/images/images/images/PyDracula_vertical.png);*/\n"
"	border-radius: 10px;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"    /*border: 1px solid #73AD21;*/\n"
"}")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)

        self._2.addWidget(self.logo)

        self.Login_Status = QLabel(self.Login_page)
        self.Login_Status.setObjectName(u"Login_Status")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Login_Status.sizePolicy().hasHeightForWidth())
        self.Login_Status.setSizePolicy(sizePolicy1)
        self.Login_Status.setMaximumSize(QSize(16777215, 20))

        self._2.addWidget(self.Login_Status)

        self.username = QLineEdit(self.Login_page)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self._2.addWidget(self.username)

        self.password = QLineEdit(self.Login_page)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.password.setEchoMode(QLineEdit.Password)

        self._2.addWidget(self.password)

        self.btn_Login = QPushButton(self.Login_page)
        self.btn_Login.setObjectName(u"btn_Login")
        self.btn_Login.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.btn_Login.setFont(font)
        self.btn_Login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Login.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon = QIcon()
        icon.addFile(u"Backup/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Login.setIcon(icon)

        self._2.addWidget(self.btn_Login)

        self.btn_Register = QPushButton(self.Login_page)
        self.btn_Register.setObjectName(u"btn_Register")
        self.btn_Register.setMinimumSize(QSize(150, 30))
        self.btn_Register.setFont(font)
        self.btn_Register.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Register.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Register.setIcon(icon)

        self._2.addWidget(self.btn_Register)

        self.btn_Fpassword = QPushButton(self.Login_page)
        self.btn_Fpassword.setObjectName(u"btn_Fpassword")
        self.btn_Fpassword.setMinimumSize(QSize(150, 30))
        self.btn_Fpassword.setFont(font)
        self.btn_Fpassword.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Fpassword.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Fpassword.setIcon(icon)

        self._2.addWidget(self.btn_Fpassword)

        self.Login_stackedWidget.addWidget(self.Login_page)
        self.Register_page = QWidget()
        self.Register_page.setObjectName(u"Register_page")
        self.gridLayout = QGridLayout(self.Register_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_Com_Register = QPushButton(self.Register_page)
        self.btn_Com_Register.setObjectName(u"btn_Com_Register")
        self.btn_Com_Register.setMinimumSize(QSize(150, 30))
        self.btn_Com_Register.setFont(font)
        self.btn_Com_Register.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Com_Register.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Com_Register.setIcon(icon)

        self.gridLayout.addWidget(self.btn_Com_Register, 13, 0, 1, 2)

        self.btn_Reg_Back = QPushButton(self.Register_page)
        self.btn_Reg_Back.setObjectName(u"btn_Reg_Back")
        self.btn_Reg_Back.setMinimumSize(QSize(150, 30))
        self.btn_Reg_Back.setFont(font)
        self.btn_Reg_Back.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Reg_Back.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Reg_Back.setIcon(icon)

        self.gridLayout.addWidget(self.btn_Reg_Back, 14, 0, 1, 2)

        self.Reg_password_2 = QLineEdit(self.Register_page)
        self.Reg_password_2.setObjectName(u"Reg_password_2")
        self.Reg_password_2.setMinimumSize(QSize(0, 30))
        self.Reg_password_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.Reg_password_2.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.Reg_password_2, 8, 1, 1, 1)

        self.Reg_password = QLineEdit(self.Register_page)
        self.Reg_password.setObjectName(u"Reg_password")
        self.Reg_password.setMinimumSize(QSize(0, 30))
        self.Reg_password.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.Reg_password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.Reg_password, 8, 0, 1, 1)

        self.Reg_email = QLineEdit(self.Register_page)
        self.Reg_email.setObjectName(u"Reg_email")
        self.Reg_email.setMinimumSize(QSize(0, 30))
        self.Reg_email.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.Reg_email, 9, 0, 1, 2)

        self.Reg_username = QLineEdit(self.Register_page)
        self.Reg_username.setObjectName(u"Reg_username")
        self.Reg_username.setMinimumSize(QSize(0, 30))
        self.Reg_username.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.Reg_username, 7, 0, 1, 2)

        self.Reg_Status = QLabel(self.Register_page)
        self.Reg_Status.setObjectName(u"Reg_Status")
        sizePolicy1.setHeightForWidth(self.Reg_Status.sizePolicy().hasHeightForWidth())
        self.Reg_Status.setSizePolicy(sizePolicy1)
        self.Reg_Status.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.Reg_Status, 2, 0, 1, 1)

        self.logo_2 = QFrame(self.Register_page)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setMinimumSize(QSize(0, 400))
        self.logo_2.setMaximumSize(QSize(16777215, 400))
        self.logo_2.setStyleSheet(u"#logo_2{\n"
"	background-image: url(:/images/images/images/Logo_Big (8).png);\n"
"	/*background-image: url(:/images/images/images/PyDracula_vertical.png);*/\n"
"	border-radius: 10px;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"    /*border: 1px solid #73AD21;*/\n"
"}")
        self.logo_2.setFrameShape(QFrame.NoFrame)
        self.logo_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.logo_2, 1, 0, 1, 2)

        self.Login_stackedWidget.addWidget(self.Register_page)

        self.verticalLayout_2.addWidget(self.Login_stackedWidget)

        self.verticalSpacer = QSpacerItem(838, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame = QFrame(self.frame_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Forget_Email = QLineEdit(self.frame)
        self.Forget_Email.setObjectName(u"Forget_Email")
        self.Forget_Email.setMinimumSize(QSize(0, 30))
        self.Forget_Email.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.Forget_Email, 1, 0, 1, 1)

        self.btn_Forget_Email = QPushButton(self.frame)
        self.btn_Forget_Email.setObjectName(u"btn_Forget_Email")
        self.btn_Forget_Email.setMinimumSize(QSize(150, 30))
        self.btn_Forget_Email.setFont(font)
        self.btn_Forget_Email.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Forget_Email.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Forget_Email.setIcon(icon)

        self.gridLayout_4.addWidget(self.btn_Forget_Email, 2, 0, 1, 1)

        self.user_description_15 = QLabel(self.frame)
        self.user_description_15.setObjectName(u"user_description_15")
        sizePolicy1.setHeightForWidth(self.user_description_15.sizePolicy().hasHeightForWidth())
        self.user_description_15.setSizePolicy(sizePolicy1)
        self.user_description_15.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.user_description_15, 0, 0, 1, 1)

        self.btn_Forget_Back = QPushButton(self.frame)
        self.btn_Forget_Back.setObjectName(u"btn_Forget_Back")
        self.btn_Forget_Back.setMinimumSize(QSize(150, 30))
        self.btn_Forget_Back.setFont(font)
        self.btn_Forget_Back.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Forget_Back.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_Forget_Back.setIcon(icon)

        self.gridLayout_4.addWidget(self.btn_Forget_Back, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.top_bar = QFrame(self.bg)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 881, 50))
        self.top_bar.setMinimumSize(QSize(0, 50))
        self.top_bar.setMaximumSize(QSize(16777215, 45))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(33, 37, 43, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 120, 215, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(240, 240, 240, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.top_bar.setPalette(palette)
        self.top_bar.setStyleSheet(u"")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.top_bar.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.topLogo = QFrame(self.top_bar)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"background-image: url(:/images/images/images/Logo_Small (5).png);\n"
"/*background-image: url(:/images/images/images/PyDracula.png);*/\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.topLogo)

        self.title_bar_3 = QLabel(self.top_bar)
        self.title_bar_3.setObjectName(u"title_bar_3")
        self.title_bar_3.setFrameShape(QFrame.NoFrame)
        self.title_bar_3.setLineWidth(0)
        self.title_bar_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.title_bar_3.setMargin(20)

        self.horizontalLayout_3.addWidget(self.title_bar_3)

        self.top_btns_3 = QFrame(self.top_bar)
        self.top_btns_3.setObjectName(u"top_btns_3")
        self.top_btns_3.setMaximumSize(QSize(100, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.top_btns_3.setPalette(palette1)
        self.top_btns_3.setStyleSheet(u"")
        self.top_btns_3.setFrameShape(QFrame.NoFrame)
        self.top_btns_3.setFrameShadow(QFrame.Raised)
        self.top_btns_3.setLineWidth(0)
        self.top_btn_layout_3 = QHBoxLayout(self.top_btns_3)
        self.top_btn_layout_3.setSpacing(5)
        self.top_btn_layout_3.setObjectName(u"top_btn_layout_3")
        self.top_btn_layout_3.setContentsMargins(0, 0, 0, 0)
        self.maximizeRestoreAppBtn = QPushButton(self.top_btns_3)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setEnabled(False)
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.top_btn_layout_3.addWidget(self.maximizeRestoreAppBtn)

        self.minimizeAppBtn = QPushButton(self.top_btns_3)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setEnabled(True)
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.top_btn_layout_3.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.top_btns_3)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.top_btn_layout_3.addWidget(self.closeAppBtn)


        self.horizontalLayout_3.addWidget(self.top_btns_3)


        self.verticalLayout.addWidget(self.bg)

        Login.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.username, self.password)
        QWidget.setTabOrder(self.password, self.btn_Login)
        QWidget.setTabOrder(self.btn_Login, self.btn_Register)
        QWidget.setTabOrder(self.btn_Register, self.btn_Fpassword)
        QWidget.setTabOrder(self.btn_Fpassword, self.Forget_Email)
        QWidget.setTabOrder(self.Forget_Email, self.btn_Forget_Email)
        QWidget.setTabOrder(self.btn_Forget_Email, self.btn_Forget_Back)
        QWidget.setTabOrder(self.btn_Forget_Back, self.Reg_username)
        QWidget.setTabOrder(self.Reg_username, self.Reg_password)
        QWidget.setTabOrder(self.Reg_password, self.Reg_password_2)
        QWidget.setTabOrder(self.Reg_password_2, self.Reg_email)
        QWidget.setTabOrder(self.Reg_email, self.btn_Com_Register)
        QWidget.setTabOrder(self.btn_Com_Register, self.btn_Reg_Back)
        QWidget.setTabOrder(self.btn_Reg_Back, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.minimizeAppBtn)
        QWidget.setTabOrder(self.minimizeAppBtn, self.closeAppBtn)

        self.retranslateUi(Login)

        self.Login_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login. PyBlackBOX", None))
        self.Login_Status.setText(QCoreApplication.translate("Login", u"Login (Pass: 123456)", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Login", u"Username", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.btn_Login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.btn_Register.setText(QCoreApplication.translate("Login", u"Register", None))
        self.btn_Fpassword.setText(QCoreApplication.translate("Login", u"Forget password", None))
        self.btn_Com_Register.setText(QCoreApplication.translate("Login", u"Register", None))
        self.btn_Reg_Back.setText(QCoreApplication.translate("Login", u"Back", None))
        self.Reg_password_2.setText("")
        self.Reg_password_2.setPlaceholderText(QCoreApplication.translate("Login", u"Verify Password ", None))
        self.Reg_password.setText("")
        self.Reg_password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.Reg_email.setText("")
        self.Reg_email.setPlaceholderText(QCoreApplication.translate("Login", u"E-mail", None))
        self.Reg_username.setText("")
        self.Reg_username.setPlaceholderText(QCoreApplication.translate("Login", u"Username", None))
        self.Reg_Status.setText(QCoreApplication.translate("Login", u"Status", None))
        self.Forget_Email.setText("")
        self.Forget_Email.setPlaceholderText(QCoreApplication.translate("Login", u"E-mail", None))
        self.btn_Forget_Email.setText(QCoreApplication.translate("Login", u"Send E-mail", None))
        self.user_description_15.setText(QCoreApplication.translate("Login", u"E-mail", None))
        self.btn_Forget_Back.setText(QCoreApplication.translate("Login", u"Back", None))
        self.title_bar_3.setText(QCoreApplication.translate("Login", u"Login V1 PyDracula", None))
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("Login", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("Login", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("Login", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
    # retranslateUi

